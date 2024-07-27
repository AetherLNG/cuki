from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        print("Download completed successfully.")
    except:
        print("An error occurred while downloading the video.")

link = input("Enter the YouTube video URL: ")
Download(link)
