from xml.etree import ElementTree as ET
import os


def check_objects(filepath):
    doc = ET.parse(filepath).getroot()
    names = []
    for object in doc.findall('object'):
        for name in object.findall('name'):
            names.append(name.text)
    return list(set(names))  # use set() to avoid duplicate names


def main():
    dir_path = 'VOC2012/Annotations/'
    for filename in os.listdir(dir_path):
        objects = check_objects(dir_path + filename)
        for object in objects:
            f = open('VOC2012/ImageByObjectContained/' + object + '.txt', 'a')
            f.write(filename[:-4] + '\n')  # get the filename without the suffix
            f.close()


if __name__ == '__main__':
    main()
