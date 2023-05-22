try:

    from pytube import YouTube
    import os

    yt = YouTube( str(input("Enter the URL of the youtube video you want downloaded : \n")))

    video = yt.streams.filter(only_audio=True).first()

    destination =  "."

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Successfully downloaded')
except:
    print("error")