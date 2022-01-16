import discord

from urllib.parse import quote_plus

def generate_query(query: str):
    # we need to quote the query string to make a valid url. Discord will raise an error if it isn't valid.
    query = quote_plus(query)
    return f"https://www.google.com/search?q={query}"

# Define a simple View that gives us a google link button.
# We take in `query` as the query that the command author requests for
class Google(discord.ui.View):
    
    def __init__(self, query: str):
        super().__init__()

        # Link buttons cannot be made with the decorator
        # Therefore we have to manually create one.
        # We add the quoted url to the button, and add the button to the view.
        self.add_item(discord.ui.Button(label="Click Here", url=generate_query(query)))
