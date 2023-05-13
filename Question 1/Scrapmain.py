from bs4 import BeautifulSoup as bs				        #1 Importing BeautifulSoup4
import requests as req							#2 Importing requests library
from csv import writer


def north_east_west_south():
	html_text = req.get('https://www.sportskeeda.com/').text

	soup = bs(html_text, 'lxml')
	#print(soup.prettify())

	news = soup.find_all('section', class_='sports-latest-news-section')
	#print(news)

	categories = ['Cricket', 'IPL 2023', 'WWE', 'Football', 'NBA', 'NFL', 'MMA', 'Tennis', 'Golf', 'MLB', 'AEW', 'Fortnite', 'Gaming', 'Minecraft']

	print('Here are some few news...\n\tLoading...\n')
	for i, category in enumerate(news):
		print(f'{i+1}. {categories[i]} NEWS')
		headlines = category.find_all('div', 'news-detail')
		for index, headline in enumerate(headlines):
			lines = headline.text.replace('[',"").replace(']',"")
			print(f'   {index+1}. {lines}')

			#Saving
			save=[i+1, categories[i], index+1, lines]
			with open('news.csv', 'a') as data:
				writer_object = writer(data)
				writer_object.writerow(save)
				data.close()

		print("\n")

def i_dont_watch_ipl():
	print(f"You won't miss this, Right?\n\tLoading...\n")
	html_text = req.get('https://sportskeeda.com/go/ipl/results').text

	soup = bs(html_text, 'lxml')
	#print(soup.prettify())

	cricket = soup.find_all('a', class_='keeda_cricket_event_match post')
	#print(matches)

	for match in cricket:

		date 			= match.find('div', class_ = 'keeda_cricket_event_date').text.replace("\n"," ").strip().replace('\n','')
		location_stadium = match.find("div", class_ = 'match-description').text.split(',')[1].strip().replace('\n','')
		location_city 	= match.find("div", class_ = 'match-description').text.split(',')[-1].strip().replace('\n','')
		teams 			= match.find_all('span', class_ = 'keeda_cricket_team_name')
		scores			= match.find_all('span', class_ = 'keeda_cricket_score')
		#print(scores)
		team1			= teams[0].text.strip().replace('\n','')
		score1			= scores[0].text.strip().replace('\n','')
		team2			= teams[1].text.strip().replace('\n','')
		score2			= scores[1].text.strip().replace('\n','')
		match_number	= match.find("div", class_ = 'match-description').text.split(',')[0].strip().replace('\n','')
		result 			= match.find('div', class_ = 'keeda_cricket_result').text.strip()
		#print(teams[1])
		print(f'Match Number : {match_number}')
		print(f'Teams        : {team1} vs {team2}')
		print(f'Scores       : {score1} vs {score2}')
		print(f'Scheduled on : {date}')
		print(f'Location     : {location_stadium}, {location_city}')
		print(f'Result       : {result}')

		#Saving
		save=[match_number, team1, score1, team2, score2, date, location_stadium, location_city, result]
		with open('postiplmatches.csv', 'a') as data:
			writer_object = writer(data)
			writer_object.writerow(save)
			data.close()
		print('\n')
	print("Saved to postiplmatches.csv !\n")

def i_wont_be_be_able_to_watch_these_except_for_finals():
	print("IPL Matches that were organised in 2023\n\tLoading...\n")

	html_text = req.get('https://www.sportskeeda.com/go/ipl/schedule').text

	soup = bs(html_text, 'lxml')
	#print(soup.prettify())

	cricket = soup.find_all('a', class_='keeda_cricket_event_match pre')
	#print(matches)

	for match in cricket:
		date 			= match.find('div', class_ = 'keeda_cricket_event_date').text.replace("\n"," ").strip()
		location_stadium = match.find("div", class_ = 'keeda_cricket_venue').text.split(',')[1].strip()
		location_city 	= match.find("div", class_ = 'keeda_cricket_venue').text.split(',')[-1].strip()
		teams 			= match.find_all('div', class_ = 'keeda_cricket_team')
		team1			= teams[0].text.strip()
		team2			= teams[1].text.strip()
		match_number	= match.find("div", class_ = 'keeda_cricket_venue').text.split(',')[0].strip()
		#print(teams[1])
		print(f'Match Number : {match_number}')
		print(f'Teams playing: {team1} vs {team2}')
		print(f'On {date} at {location_stadium}, {location_city}')

		#Saving
		save=[match_number, team1, team2, date, location_stadium, location_city]
		with open('upcomingiplmatches.csv', 'a') as data:
			writer_object = writer(data)
			writer_object.writerow(save)
			data.close()
		print('\n')
	print("Saved to upcomingiplmatches.csv !\n")


if __name__ == "__main__":
	
	val = 1
	while val != 0:
		print(
'''I can retrieve these for you
PRESS 1 for Some NEWS
PRESS 2 for Upcoming IPL Matches
PRESS 3 for Post IPL Matches
PRESS 0 to Quit
''')
		response = int(input("> "))
		if response == 1:
			north_east_west_south()
		elif response == 2:
			i_dont_watch_ipl()
		elif response == 3:
			i_wont_be_be_able_to_watch_these_except_for_finals()
		print('Should I Continue ? [PRESS 0 to Stop]')
		val = int(input('> '))
