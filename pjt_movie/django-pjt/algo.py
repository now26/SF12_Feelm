# 추천 알고리즘
import pandas as pd
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

movies_df = load_movie_data(r"C:\Users\lyw\Desktop\SF12_Feelm\pjt_movie\django-pjt\movies\fixtures\movietop1.json")

# 추천 알고리즘
def calculate_combined_weighted_similarity(movies_df, field1, field2, field3, field4, field5, weight1, weight2, weight3, weight4, weight5):
    # 장르와 키워드를 결합
    
    combined_features = movies_df.apply(
        lambda row: "{} ".format(' '.join([row[field1]] * int(weight1) if row[field1]!="" else '-')) + 
        "{} ".format(' '.join([row[field2]] * int(weight2) if row[field2]!="" else '-')) +
        "{} ".format(' '.join([row[field3]] * int(weight3) if row[field3]!="" else '-')) +
        "{} ".format(' '.join([row[field4]] * int(weight4) if row[field4]!="" else '-')) +
        "{}".format(' '.join([row[field5]] * int(weight5) if row[field5]!="" else '-')), axis=1)
    
    count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
    combined_mat = count_vect.fit_transform(combined_features)
    
    # 코사인 유사도 계산
    combined_sim = cosine_similarity(combined_mat, combined_mat)
    return combined_sim

def find_sim_movie_combined(df, sorted_ind, title_name, top_n=10):
    # 입력된 영화의 인덱스 찾기
    title_movie = df[df['title'] == title_name]
    if title_movie.empty:
        return "영화를 찾을 수 없습니다."
    
    title_index = title_movie.index.values
    
    # 유사도 높은 영화 인덱스 추출
    similar_indexes = sorted_ind[title_index, :(top_n*2)]
    similar_indexes = similar_indexes.reshape(-1)
    
    # 입력 영화 제외
    similar_indexes = similar_indexes[similar_indexes != title_index]
    
    # 유사도 순으로 정렬, 슬라이싱
    result = df.iloc[similar_indexes][:top_n]
    # return result[['title', 'genre', 'vote_avg', 'overview', 'keyword']]
    return list(result[['tmdb_id'][0]])


def movie_recommendation_system_combined(json_file_path, title_name, key1, key2, key3, key4, key5, weight1, weight2, weight3, weight4, weight5, top_n=10):
    # 데이터 로드
    movies_df = load_movie_data(json_file_path)
    # print(movies_df)
    
    # 유사도 계산
    combined_sim = calculate_combined_weighted_similarity(movies_df, key1, key2, key3, key4, key5, weight1, weight2, weight3, weight4, weight5)
    
    # 유사도 정렬
    combined_sim_sorted_ind = combined_sim.argsort()[:, ::-1]
    
    # 추천 영화 찾기
    recommendations = find_sim_movie_combined(movies_df, combined_sim_sorted_ind, title_name, top_n)

    
    return recommendations

# ============================================
# 북마크 기반 추천
# def calculate_combined_weighted_similarity_bookmark(movies_df, bookmark, field1, field2, field3, field4, field5, weight1, weight2, weight3, weight4, weight5):
#     bookmark = pd.DataFrame(bookmark)
    
#     combined_bookmark = bookmark.apply(
#         lambda row: "{} ".format(' '.join([row[field1]] * int(weight1))) + 
#         "{} ".format(' '.join([row[field2]] * int(weight2))) +
#         "{} ".format(' '.join([row[field3]] * int(weight3))) +
#         "{} ".format(' '.join([row[field4]] * int(weight4))) +
#         "{}".format(' '.join([row[field5]] * int(weight5))), axis=1
#     )
#     # print(combined_bookmark)
#     combined_bookmark = pd.Series([' '.join(combined_bookmark.values)])
#     print(combined_bookmark)
#     # 장르와 키워드를 결합
#     combined_features = movies_df.apply(
#         lambda row: "{} ".format(' '.join([row[field1]] * int(weight1))) + 
#         "{} ".format(' '.join([row[field2]] * int(weight2))) +
#         "{} ".format(' '.join([row[field3]] * int(weight3))) +
#         "{} ".format(' '.join([row[field4]] * int(weight4))) +
#         "{}".format(' '.join([row[field5]] * int(weight5))), axis=1)
#     combined_features = pd.concat([combined_features, combined_bookmark], ignore_index=True)
#     print(combined_features)
    
#     count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
#     combined_mat = count_vect.fit_transform(combined_features)
    
#     # 코사인 유사도 계산
#     combined_sim = cosine_similarity(combined_mat, combined_mat)
#     # print(combined_sim)
#     # print('==========')
#     return combined_sim

def calculate_combined_weighted_similarity_bookmark(movies_df, bookmark, field1, field2, field3, field4, field5, weight1, weight2, weight3, weight4, weight5):
    bookmark = pd.DataFrame(bookmark)
    
    # 북마크된 영화들의 특성을 결합
    combined_bookmark = bookmark.apply(
        lambda row: "{} ".format(' '.join([str(row[field1]) if pd.notna(row[field1]) and row[field1] != '' else '-'] * int(weight1))) + 
        "{} ".format(' '.join([str(row[field2]) if pd.notna(row[field2]) and row[field2] != '' else '-'] * int(weight2))) +
        "{} ".format(' '.join([str(row[field3]) if pd.notna(row[field3]) and row[field3] != '' else '-'] * int(weight3))) +
        "{} ".format(' '.join([str(row[field4]) if pd.notna(row[field4]) and row[field4] != '' else '-'] * int(weight4))) +
        "{}".format(' '.join([str(row[field5]) if pd.notna(row[field5]) and row[field5] != '' else '-'] * int(weight5))), axis=1
    )
    
    # 북마크된 모든 영화의 특성을 하나로 결합
    combined_bookmark = pd.Series([' '.join(combined_bookmark.values)])
    
    # 전체 영화 데이터의 특성을 결합
    combined_features = movies_df.apply(
        lambda row: "{} ".format(' '.join([str(row[field1]) if pd.notna(row[field1]) and row[field1] != '' else '-'] * int(weight1))) + 
        "{} ".format(' '.join([str(row[field2]) if pd.notna(row[field2]) and row[field2] != '' else '-'] * int(weight2))) +
        "{} ".format(' '.join([str(row[field3]) if pd.notna(row[field3]) and row[field3] != '' else '-'] * int(weight3))) +
        "{} ".format(' '.join([str(row[field4]) if pd.notna(row[field4]) and row[field4] != '' else '-'] * int(weight4))) +
        "{}".format(' '.join([str(row[field5]) if pd.notna(row[field5]) and row[field5] != '' else '-'] * int(weight5))), axis=1
    )
    
    # 북마크 특성을 전체 특성에 추가
    combined_features = pd.concat([combined_features, combined_bookmark], ignore_index=True)
    
    # 벡터화 및 유사도 계산
    count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
    combined_mat = count_vect.fit_transform(combined_features)
    combined_sim = cosine_similarity(combined_mat, combined_mat)
    # print(combined_sim)
    return combined_sim

import numpy as np
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