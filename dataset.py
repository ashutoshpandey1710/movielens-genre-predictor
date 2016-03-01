import csv, config

movies = {}
with open(config.DATASET_HOME + '/movies.dat') as csvfile:
	for line in csvfile:
		row = line.strip().split('::')
		movie_id = int(row[0])
		movie_title = row[1]
		genres = row[2].split('|')

		movies[movie_id] = {'title':movie_title, 'genres':genres}

movie_user_tags = {}
with open(config.DATASET_HOME + '/tags.dat') as csvfile:
	for line in csvfile:
		row = line.strip().split('::')
		user_id = int(row[0])
		movie_id = int(row[1])
		tag = row[2]
		if movie_id in movies:
			if movie_id in movie_user_tags:
				movie_user_tags[movie_id].append({'user':user_id, 'tag':tag})
			else:
				movie_user_tags[movie_id] = [{'user':user_id, 'tag':tag}]
		else:
			print "Movie id {0} not found.".format(movie_id)


#Vectorize tag dataset 

def show_movie_and_tags(movie_id):
	if movie_id in movies:
		print "Title: {0}\nTags: {1}".format(movies[movie_id], movie_user_tags[movie_id])