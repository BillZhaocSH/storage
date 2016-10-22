import http.client
import json


class FootballDataAPI():
    'api.football-data.org网站的api'

    X_Auth_Token= '1dd69cfa649645e9acf41f20b52eada5'

    #List all available competitions.
    def competitions(self,season ):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token': FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if season=="":
            connection.request('GET', '/v1/competitions/?season='+season, None, headers )
        else:
            connection.request('GET', '/v1/competitions', None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #List all teams for a certain competition.
    def allTeam(self,id):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/competitions/'+id+'/teams', None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #Show League Table / current standing.
    def leagueTable(self,id,matchday):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if matchday=="":
            connection.request('GET', '/v1/competitions/'+id+'/leagueTable/?matchday='+matchday, None, headers )
        else:
            connection.request('GET', '/v1/competitions/'+id+'/leagueTable', None, headers )

        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #List all fixtures for a certain competition.
    def fixtureForCertainCompetition(self,id,timeFrame,matchday):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if  matchday!="" and  timeFrame!="" :
            connection.request('GET', '/v1/competitions/'+id+'/fixtures', None, headers )
        else:
            if matchday=="" and timeFrame=="":
                connection.request('GET', '/v1/competitions/'+id+'/fixtures/?matchday='+matchday+'&timeFrame='+timeFrame, None, headers )
            else:
                if matchday=="":
                    connection.request('GET', '/v1/competitions/'+id+'/fixtures/?matchday='+matchday, None, headers )
                if timeFrame=="":
                    connection.request('GET', '/v1/competitions/'+id+'/fixtures/?timeFrame='+timeFrame, None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #List fixtures across a set of competitions.
    def fixtureForSetCompetition(self,timeFrame,league):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if timeFrame!="" and league!="" :
            connection.request('GET', '/v1/fixtures/', None, headers )
        else:
            if league=="" and timeFrame=="":
                connection.request('GET', '/v1/fixtures/?league='+league+'&timeFrame='+timeFrame, None, headers )
            else:
                if league=="":
                    connection.request('GET', '/v1/fixtures/?league='+league, None, headers )
                if timeFrame=="":
                    connection.request('GET', '/v1/fixtures/?timeFrame='+timeFrame, None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #Show one fixture.
    def fixtureForOne(self,id,head2head):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if head2head=="":
            connection.request('GET', '/v1/fixtures/'+id+'/?head2head='+head2head, None, headers )
        else:
            connection.request('GET', '/v1/fixtures/'+id, None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #Show all fixtures for a certain team.
    def fixtureForOneTeam(self,id,season,timeFrame,venue):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        if timeFrame!="" and season!="" and venue!="":
            connection.request('GET', '/v1/teams/'+id+'/fixtures/', None, headers )
        else:
            if timeFrame=="" and season=="" and venue=="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?season='+season+'&timeFrame='+timeFrame+'&venue='+venue, None, headers )
            if timeFrame!="" and season=="" and venue=="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?season='+season+'&venue='+venue, None, headers )
            if timeFrame=="" and season!="" and venue=="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?timeFrame='+timeFrame+'&venue='+venue, None, headers )
            if timeFrame=="" and season=="" and venue!="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?season='+season+'&timeFrame='+timeFrame, None, headers )
            if timeFrame!="" and season!="" and venue=="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?venue='+venue, None, headers )
            if timeFrame=="" and season!="" and venue!="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?timeFrame='+timeFrame, None, headers )
            if timeFrame!="" and season=="" and venue!="":
                connection.request('GET', '/v1/teams/'+id+'/fixtures/?season='+season, None, headers )

        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #Show one team.
    def team(self,id):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/teams/'+id, None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response

    #Show all players for a certain team.
    def players(self,id):
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token':FootballDataAPI.X_Auth_Token, 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/teams/'+id+'/players', None, headers )
        response = json.loads(connection.getresponse().read().decode())
        print (response)
        return response