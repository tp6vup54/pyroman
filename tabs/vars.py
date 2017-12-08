json_name = 'pyroman.json'
pixiv_username = "globaluser"
pixiv_password = "password"
default_source_path = r'D:\odrive\Google Drive\temp'
default_magazine_source_path = ''
# windows
default_manga_dest_path = r'D:\odrive\Google Drive\Private\JoystickDriver\Manga'
default_image_dest_path = r'D:\odrive\Google Drive\Private\ImageSet'
default_magazine_dest_path = r'C:\Users\Thinker\Desktop\tmp'
# mac
#default_source_path = '/Users/tp6vup54/Documents/'
#default_dest_path = '/Users/tp6vup54/Desktop/dest/'
source_path_dict = {
    0: default_source_path,
    1: default_source_path,
    2: default_magazine_source_path
}
dest_path_dict = {
    0: default_manga_dest_path,
    1: default_image_dest_path,
    2: default_magazine_dest_path
}

image_valid_extension = ('.jpg', '.png', '.gif')
split = '\\'
