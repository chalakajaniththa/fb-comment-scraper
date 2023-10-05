import requests

def get_facebook_comments(post_id, access_token):
    base_url = "http://graph.facebook.com"
    endpoint = f"/{post_id}/comments"
    params = {
        "access_token": access_token
    }

    try:
        response = requests.get(base_url + endpoint, params=params)
        if response.status_code == 200:
            comments_data = response.json()
            return comments_data.get('data', [])
        else:
            print(f"Error: {response.status_code}, {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Specify the post ID and access token
post_id = "10152297032458306"  # Replace with the actual post ID
access_token = "EAAX21kIZAa4wBOZBEJYafPy9q8Rnx6FCgTFRUE5NuGyVgKI1OdzFkKTFnO9Mg7CamFJi8GRMZBaBBBLtEfoJlogTeuGQQKikPtfCZCCa3yqqfXZBanv5otbevyKAPmfBpljnZAGyBZBlViv5WrNa3FxgE7XD5R0nhtalHzanTrRL7GwaD8PZBIJ5Si4mZAK1ZARoM65CSBpZBQKy2ZAZBxm62NYIIIzJvoUdzOXmIc1ZBWqB45ZC1fSQy9BX9NewNIEV9nsNbNSJHSY4K9Ko3cZD"  # Replace with your access token

# Get comments for the specified post
comments = get_facebook_comments(post_id, access_token)

if comments:
    # Print the comments
    for comment in comments:
        print(comment.get('message'))
else:
    print("No comments found.")
