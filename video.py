import moviepy.editor

# Show info
print('Данная программа вырезает из видео файла звук.\n')

# Main loop
flag = True
while flag == True:
    # User input
    name_video = input('Введите название ВИДЕО в формате: "C:\путь к файлу.mp4",\
    \nесли файл находится со скриптом в одной дериктории \nто введите просто\
    имя файла в формате "video.mp4".   ВАШ ВВОД: ')
    print('\n')
    name_mp3 = input('Введите название АУДИО в формате: "C:\путь к файлу.mp3",\
    \nесли файл находится со скриптом в одной дериктории \nто введите просто\
    имя файла в формате "audio.mp3".   ВАШ ВВОД: ')
    print('\n')

    # Programm logic
    video = moviepy.editor.VideoFileClip(name_video)
    audio = video.audio
    audio.write_audiofile(name_mp3)

    # Restart loop
    print('\nВаш файл успешно записан.')
    restart = input(' Записать еще файл? y/n:  ')
    re_flag = True
    while re_flag == True:
        if restart == 'y':
            flag = True
            re_flag = False
        elif restart == 'n':
            print('\nСпасибо что воспользовались данной программой. До свидания.')
            flag = False
            re_flag = False
        else:
            print('Не корректный ввод!')
            restart = input(' Записать еще файл? y/n:  ')
