headers = {'Accept-Language': 'en-US,en;q=0.8'}

# initialize empty lists to store the variables scraped
titles = []
years = []
ratings = []
genres = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
metascores = []
votes = []

for page in pages:

    # get request for sci-fi
    response = get(
        "https://www.imdb.com/title/tt9389998/?ref_=fn_al_tt_0", headers=headers)

    sleep(randint(8, 15))

    # throw warning for status codes that are not 200
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(
            requests, response.status_code))

    # parse the content of current iteration of request
    page_html = BeautifulSoup(response.text, 'html.parser')

    movie_containers = page_html.find_all(
        'div', class_='lister-item mode-advanced')

    # extract the 50 movies for that page
    for container in movie_containers:

        # conditional for all with metascore
        if container.find('div', class_='ratings-metascore') is not None:

            # title
            title = container.h3.a.text
            titles.append(title)

            if container.h3.find('span', class_='lister-item-year text-muted unbold') is not None:

                # year released
                # remove the parentheses around the year and make it an integer
                year = container.h3.find(
                    'span', class_='lister-item-year text-muted unbold').text
                years.append(year)

            else:
                # each of the additional if clauses are to handle type None data, replacing it with an empty string so the arrays are of the same length at the end of the scraping
                years.append(None)

            if container.p.find('span', class_='certificate') is not None:

                # rating
                rating = container.p.find('span', class_='certificate').text
                ratings.append(rating)

            else:
                ratings.append("")

            if container.p.find('span', class_='genre') is not None:

                # genre
                genre = container.p.find('span', class_='genre').text.replace("\n", "").rstrip().split(
                    ',')  # remove the whitespace character, strip, and split to create an array of genres
                genres.append(genre)

            else:
                genres.append("")

            if container.p.find('span', class_='runtime') is not None:

                # runtime
                # remove the minute word from the runtime and make it an integer
                time = int(container.p.find(
                    'span', class_='runtime').text.replace(" min", ""))
                runtimes.append(time)

            else:
                runtimes.append(None)

            if float(container.strong.text) is not None:

                # IMDB ratings
                # non-standardized variable
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

            else:
                imdb_ratings.append(None)

            if container.find('span', class_='metascore').text is not None:
                m_score = int(container.find('span', class_='metascore').text)
                metascores.append(m_score)

            else:
                metascores.append(None)

            if container.find('span', attrs={'name': 'nv'})['data-value'] is not None:
                vote = int(container.find(
                    'span', attrs={'name': 'nv'})['data-value'])
                votes.append(vote)

            else:
                votes.append(None)

            else:
                votes.append(None)
print(titles[0])
print(years[0])
