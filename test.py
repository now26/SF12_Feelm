# 추천 알고리즘
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# JSON 파일 로드
def load_movie_data(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # fields 부분만 추출하여 DataFrame 생성
    movies_df = pd.DataFrame([item['fields'] for item in data])
    return movies_df

movies_df = load_movie_data("C:/Users/SSAFY/Desktop/새 폴더 (4)/SF12_Feelm/pjt_movie/django-pjt/movies/fixtures/movietop1.json")

def apply_review_weight(movie_id, user_reviews, review_weight=4):
    if movie_id in user_reviews:    # user_reviews에 dict 형태로 movie_id : rating 들어가야함
        review_score = user_reviews[movie_id]
        # 평점이 높을수록 더 높은 가중치 부여
        weight = int(review_score * review_weight)
        return weight
    return 1
df = pd.DataFrame()
# df.loc(len(df))=[208, 4.0]
# 여러 행을 한번에 추가
new_data = pd.DataFrame({
    'movie_id': [912649, 82702, 634649],
    'rating': [4.5, 3.0, 5.0]
})
df = pd.concat([df, new_data], ignore_index=True)
print(df[['movie_id']])


def calculate_combined_similarity_rating(movies_df, rating_df, field1, field2, field3, field4, field5, weight1, weight2, weight3, weight4, weight5):
    # rating_df : 이미 데이터 프레임
    # movie_id, rating을 col으로 가지고 있음
    apply_review_weight
    
    # 전체 영화 데이터의 특성을 결합
    combined_features = movies_df.apply(
        lambda row: "{} ".format(' '.join([str(row[field1]) if pd.notna(row[field1]) and row[field1] != '' else '-'] * int(weight1))) + 
        "{} ".format(' '.join([str(row[field2]) if pd.notna(row[field2]) and row[field2] != '' else '-'] * int(weight2))) +
        "{} ".format(' '.join([str(row[field3]) if pd.notna(row[field3]) and row[field3] != '' else '-'] * int(weight3))) +
        "{} ".format(' '.join([str(row[field4]) if pd.notna(row[field4]) and row[field4] != '' else '-'] * int(weight4))) +
        "{}".format(' '.join([str(row[field5]) if pd.notna(row[field5]) and row[field5] != '' else '-'] * int(weight5))), axis=1
    )
    weighted_features = movies_df.apply(
        lambda row:
            combined_features[row.name] * apply_review_weight(row['movie_id'], rating_df, 4), axis=1
    )
    
    # 벡터화 및 유사도 계산
    count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
    combined_mat = count_vect.fit_transform(weighted_features)
    combined_sim = cosine_similarity(combined_mat, combined_mat)
    # print(combined_sim)
    return combined_sim


def find_sim_movie_combined_bookmark(df, sorted_ind, bookmark, top_n=10):
    # 입력된 영화의 인덱스 찾기
    movie = pd.DataFrame(bookmark)
    title_movie = pd.DataFrame()
    title_indexes = []
    for title in movie['title']:
        matched_movie = df[df['title']==title]
        title_movie = pd.concat([title_movie, matched_movie], ignore_index=True)
        title_indexes.extend(df[df['title']==title].index.tolist())
    # print(title_movie)
    # title_index = len(df)
    title_index = title_movie.index.values
    
    # 유사도 높은 영화 인덱스 추출
    # print(sorted_ind)
    similar_indexes = sorted_ind[200, :(top_n*2)]
    similar_indexes = similar_indexes.reshape(-1)
    # print(similar_indexes)
    
    # 입력 영화 제외
    # for i in title_movie:
    #     similar_indexes = similar_indexes[similar_indexes != i]
    similar_indexes = similar_indexes[~np.isin(similar_indexes, title_indexes)]
    similar_indexes = similar_indexes[similar_indexes < len(df)]
    # print(similar_indexes)
    # 유사도 순으로 정렬, 슬라이싱
    result = df.iloc[similar_indexes][:top_n]
    # print(result)
    # return result[['title', 'genre', 'vote_avg', 'overview', 'keyword']]
    return list(result[['tmdb_id'][0]])

def movie_recommendation_system_combined_bookmark(json_file_path, bookmark, key1, key2, key3, key4, key5, weight1, weight2, weight3, weight4, weight5, top_n=10):
    # 데이터 로드
    movies_df = load_movie_data(json_file_path)
    # print(movies_df)
    
    # 유사도 계산
    combined_sim = calculate_combined_weighted_similarity_bookmark(movies_df, bookmark, key1, key2, key3, key4, key5, weight1, weight2, weight3, weight4, weight5)
    
    # 유사도 정렬
    combined_sim_sorted_ind = combined_sim.argsort()[:, ::-1]
    
    # 추천 영화 찾기
    recommendations = find_sim_movie_combined_bookmark(movies_df, combined_sim_sorted_ind, bookmark, top_n)

    
    return recommendations

# =============================================