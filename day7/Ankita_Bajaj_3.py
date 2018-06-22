#Access token = EAACEdEose0cBAKFD9Yn0E7JFcPc3gJXRj8sXB1gWzfZCYYo2IXDJptCqF9bJpz2vpw4Xi31qJ2SUsjh15xyOBFeCq9wijGQWzeDB0zsyO2lyqZA9WLeI35CYjUJAQpBAOZBZAnthJiLzp4njWLGpZC7XDA4by4WjzJUJw0YGso1dNBsEd90prS7SfwHLWtH6xpW88WLrmgwZDZD
import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBAJJ2SRYV4pyn2vntmxBvTbVbKt6gRQeFzy54ZCq67TBOQpfMB0eV7Uj7hX2yXcPXVNk2sDp0ePMiHIxoKHBcjuDUdNeHHM9ElnGqC5xk555LkZA0usZBIEcYaloYlfZAUIyei3UUc4zUCZAUpCYrI3ZCwqbQWqZB0ti5zB9VqLjuNZC8UPJdmhbIqJ8FY0b7CQZDZD"
# Message to post as status on Facebook
# Authenticating
graph = fb.GraphAPI(access_token)

status= "testing with api"
post_id = graph.put_wall_post(status)
post_pic=graph.put_photo(image=open("cloud.jpg",'rb').read(), message="Here's my image")
print(post_pic)