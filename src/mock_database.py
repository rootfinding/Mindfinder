pinecone_example = {"usuario_A":
                                 {"name":"John Sullivan",
                                  "age":25,
                                  "location":"New York, NY",
                                  "tastes": "sports, music, movies, travel, food, and fitness",
                                  "description":
                                      "Hey there! I'm an athletic and sports-loving guy who's passionate about staying active and living a healthy lifestyle. I find great joy in the thrill of sports, whether it's playing soccer, hitting the basketball court, or going for a long run in nature. I'm looking to connect with someone who shares my enthusiasm for sports and adventure. Whether you're an athlete yourself or simply enjoy being active, I believe that shared passions can be the foundation of a strong connection. When I'm not on the field or in the gym, I enjoy exploring new hiking trails, catching live sporting events, and even trying out different cuisines to fuel my active lifestyle. I value spontaneity, laughter, and deep conversations that go beyond the surface. If you're up for a fun and adventurous journey, both on and off the sports field, let's connect and see where our shared interests and chemistry take us. Let's cheer each other on and create unforgettable memories together!Swipe right if you're ready to dive into a world of sports, laughter, and shared passions. Let's embark on a thrilling match that goes beyond the ordinary!"},
                                "usuario_B":
                                    {"name":"Mary Smith",
                                     "age":23,
                                     "location":"New York, NY",
                                     "tastes": "books, movies, music",
                                     "description":
                                     "Hello there! I'm a woman with a deep passion for books and the captivating worlds they hold. As an avid reader, I find solace and inspiration within the pages of a good book. Whether it's losing myself in a thrilling mystery, exploring fantastical realms, or delving into thought-provoking literature, reading is my ultimate escape.I'm on a quest to find someone who shares my love for literature and intellectual conversations. I believe that the magic of books can spark connections and ignite meaningful discussions. If you're someone who appreciates the power of words and enjoys getting lost in literary adventures, we might just have a fantastic story to write together.When I'm not engrossed in a novel, you can find me exploring cozy bookstores, attending book club meetings, or simply curled up with a cup of tea, savoring the quiet moments of literary bliss. I cherish the art of storytelling and believe that it opens doors to empathy, growth, and endless possibilities.If you're ready to embark on a literary journey filled with engaging conversations, shared book recommendations, and moments of enchantment, then let's connect and create our own chapter of romance. Swipe right if you're ready to dive into the world of books with me, where every page turned can lead to a beautiful connection. Let's write our own love story, one chapter at a time."}
                             ,

"usuario_C":
                                 {"name":"Raquel Ameri",
                                  "age":25,
                                  "location":"Buenos Aires, Ar",
                                  "tastes": "art, music, photography, nature, and traveling",
                                  "description": "Hello, I'm Raquel, a lover of art and music. I spend my days exploring art galleries, attending concerts and enjoying the beauty of nature. Photography is another of my passions, I love capturing special moments and finding the beauty in details. I also enjoy traveling and immersing myself in different cultures. I believe that sharing similar interests is essential to building a strong connection. I am looking for someone with whom I can share deep conversations and moments filled with joy and fun. If you are passionate about art, music and exploration, I'd love to meet you. Swipe right if you're ready to discover a world full of creativity and connection."
                                  },

"usuario_D":
                                    {"name":"Franco Franza",
                                     "age":31,
                                     "location":"Buenos Aires, Ar",
                                     "tastes": "technology, gaming, movies, cooking, and fitness",
                                     "description": "Hi, I'm Franco, I'm passionate about technology and gaming. I love keeping up with the latest technology and spending time playing video games both solo and online with friends. I also enjoy watching movies of various genres and exploring cooking, experimenting with new recipes and flavors I also care about staying fit and exercising regularly I am looking for someone to share my enthusiasm for technology, games, cooking and fitness I think we have common interests it's important to building a strong and meaningful relationship. If you're ready to dive into a world of technology, fun and adventure, swipe right and let's start this exciting connection together."
                                     }
                    }

def similarity_search(example_dict):
    users_with_same_location = []

    locations = {}

    # Iterate over the user keys in the dictionary
    for user_key in example_dict.keys():
        user = example_dict[user_key]
        location = user["location"]

        # Check if the location has been encountered before
        if location in locations:
            # If the location is already in the dictionary, append both users to the list
            users_with_same_location.append(locations[location])
            users_with_same_location.append(user)
            break  # Exit the loop since we have found a pair

        # If the location is encountered for the first time, store the user as the value in the dictionary
        locations[location] = user

    return tuple(users_with_same_location)


