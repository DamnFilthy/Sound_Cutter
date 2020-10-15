import moviepy.editor

# Show info
print('This program cuts audio from the video.\n')

# Main loop
flag = True
while flag == True:
    # User input
    name_video = input('Enter the  title video in the format: \
    "C:\path\your_video.mp4",\nif your file is located in the same folder \
    with the script \nthen just enter the file name like - "video.mp4".  \
    VIDEO title:  ')
    print('\n')
    name_mp3 = input('Enter the  title sound in the format: \
    "C:\path\your_sound.mp3",\nif your file is located in the same folder \
    with the script \nthen just enter the file name like - "sound.mp3".  \
    SOUND title:  ')
    print('\n')

    # Programm logic
    video = moviepy.editor.VideoFileClip(name_video)
    audio = video.audio
    audio.write_audiofile(name_mp3)

    # Restart loop
    print('\nYour file is written.')
    restart = input(' Cut one more? y/n:  ')
    re_flag = True
    while re_flag == True:
        if restart == 'y':
            flag = True
            re_flag = False
        elif restart == 'n':
            print('\nThank you for using this program. Bye.')
            flag = False
            re_flag = False
        else:
            print('Invalid input!')
            restart = input(' Cut one more? y/n:  ')
