from pytube import Search

def get_first_youtube_result(query):
    search = Search(query)
    return f"https://www.youtube.com/watch?v={search.results[0].video_id}" if search.results else None
