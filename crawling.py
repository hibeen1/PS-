import json, os, shutil, time, requests
from bs4 import BeautifulSoup

def thumb_png_get(pic):
    # pic_url = pic.find_all("img")[0]["src"]
    pic_url = pic.find("div").find_all("img")[0]["src"]
    href_path = pic.find("div").a["href"]
    if "_m.jpg" in pic_url:
        print(pic_url, href_path)
        create_picture(pic_url)
        create_json(href_path)
    else:
        print("Not Thumb_png")
        pass
    # create_picture(pic_url)
    # create_json(href_path)

def create_json(href_path):
    dir_json = 'data/json/'
    if os.path.exists(dir_json):
        with open('data/json/%s.json' % (keyword), 'a', encoding="utf-8") as out_file:
            url_deep = "https://www.10000recipe.com/recipe/view.html?seq=%s" % str(href_path).split("/")[2]
            # print(url_deep)
            data = BeautifulSoup(requests.get(url_deep).text, "lxml")
            if data.select_one("#contents_area > div.view_cont > div") != None:
                # print("cont_ingre")
                # print(data.select_one("#contents_area > div.view_cont > div").find("dd").text)
                pass
            elif data.select_one("#contents_area > div.cont_ingre2") != None:
                # print("cont_ingre2")
                # print([{str(x.get_text()).split("                                                ")[0] : x.span.text} for x in data.select_one("#divConfirmedMaterialArea > ul:nth-child(1)").find_all("li")])
                out_file.write(json.dumps({num: [
                    str(x.get_text()).split("                                                ")[0] for x in
                    data.select_one("#divConfirmedMaterialArea > ul:nth-child(1)").find_all("li")]},
                    ensure_ascii=False) + "\n")
            else:
                # print("?????")
                pass
    else:
        os.makedirs(dir_json)


def create_picture(pic_url):
    response = requests.get(pic_url, stream=True)
    dir_pic = 'data/picture/%s' % keyword
    if os.path.exists(dir_pic):
        with open('data/picture/%s/%s.png' % (keyword, str(num).zfill(5)), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        # del response
    else:
        os.makedirs(dir_pic)

if __name__ == '__main__':
    keywords = ["김치찌개"]
    for keyword in keywords:
        page = 1
        num = 1
        while True:
            try:
                url = "https://www.10000recipe.com/recipe/list.html?q=%s&order=reco&page=%s" % (keyword, page)
                print(url)
                time.sleep(0.1)
                text = requests.get(url).text
                soup = BeautifulSoup(text, "lxml")
                # total_pic = soup.select_one("#contents_area_full > ul > ul")
                # list_pic = total_pic.findChildren("div", recursive=False)
                total_pic = soup.select_one("#contents_area_full > ul > ul")
                list_pic = total_pic.findChildren("li")
                if len(list_pic) == 0:
                    break
                for i, pic in enumerate(list_pic):
                    try:
                        thumb_png_get(pic)
                    except Exception:
                        # print(Exception.args)
                        pass
                    num += 1
                page += 1
            except:
                print("키워드 검색 끝")
                break
