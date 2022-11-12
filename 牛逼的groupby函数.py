df = pd.DataFrame([['Odin','电影','男'],
                   ['Odin','旅游','男'],
                   ['Odin','音乐','男'],
                   ['Lee','篮球','女'],
                   ['Lee','插花','女'],
                   ['Lee','瑜伽','女'],
                   ['Andy','足球','男'],
                   ['Andy','乒乓球','男'],
                   ['Summer','阅读','女'],
                   ['Summer','音乐','女'],
                  ],columns=['name','hobby','gender'])


def concat_func(row):
    return pd.Series({
        'hobby':','.join(row['hobby'].unique()),
        'gender':','.join(row['gender'].unique())
    })
  
df.groupby(df['name']).apply(lambda row:concat_func(row)).reset_index()

df.groupby('name')['gender'].apply(list)

df.groupby('name')['hobby'].apply(list)



