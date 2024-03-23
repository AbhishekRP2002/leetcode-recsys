import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# GraphQL query
query = """
query getUserProfile($username: String!) {
    allQuestionsCount {
        difficulty
        count
    }
    matchedUser(username: $username) {
        contributions {
            points
        }
        profile {
            reputation
            ranking
        }
        submissionCalendar
        submitStats {
            acSubmissionNum {
                difficulty
                count
                submissions
            }
            totalSubmissionNum {
                difficulty
                count
                submissions
            }
        }
    }
    recentSubmissionList(username: $username) {
        title
        titleSlug
        timestamp
        statusDisplay
        lang
        __typename
    }
    matchedUserStats: matchedUser(username: $username) {
        submitStats: submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
                submissions
                __typename
            }
            totalSubmissionNum {
                difficulty
                count
                submissions
                __typename
            }
            __typename
        }
    }
}
"""

# Function to format the data
def format_data(data):
    result_data = {
        "totalSolved": data["matchedUser"]["submitStats"]["acSubmissionNum"][0]["count"],
        "totalSubmissions": data["matchedUser"]["submitStats"]["totalSubmissionNum"],
        "totalQuestions": data["allQuestionsCount"][0]["count"],
        "easySolved": data["matchedUser"]["submitStats"]["acSubmissionNum"][1]["count"],
        "totalEasy": data["allQuestionsCount"][1]["count"],
        "mediumSolved": data["matchedUser"]["submitStats"]["acSubmissionNum"][2]["count"],
        "totalMedium": data["allQuestionsCount"][2]["count"],
        "hardSolved": data["matchedUser"]["submitStats"]["acSubmissionNum"][3]["count"],
        "totalHard": data["allQuestionsCount"][3]["count"],
        "ranking": data["matchedUser"]["profile"]["ranking"],
        "contributionPoint": data["matchedUser"]["contributions"]["points"],
        "reputation": data["matchedUser"]["profile"]["reputation"],
        "recentSubmissions": data["recentSubmissionList"],
        "matchedUserStats": data["matchedUserStats"]["submitStats"]
    }
    return result_data

def leetcode(user):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode.com'
    }
    variables = {'username': user}
    data = {'query': query, 'variables': variables}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        data = response.json()

        if 'errors' in data:
            return data['errors']
        else:
            return format_data(data['data'])
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return e

if __name__ == '__main__':
    username = 'aviranjan444'
    logger.info(leetcode(username))