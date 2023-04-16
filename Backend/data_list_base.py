#import bs4
from bs4 import BeautifulSoup
# import redis
# import json
# black_list = redis.Redis(host='localhost', port=6379, db=0)
# white_list = redis.Redis(host='localhost', port=6379, db=1) 
# with open("/home/xuananle/Documents/URL_net/Backend/data/whitelist.txt", mode = 'r') as f:
#     rows = f.readlines()
# for row in rows:
#         white_list.sadd("white_list", row)
# with open("/home/xuananle/Documents/URL_net/Backend/data/blacklist.txt", mode = 'r') as f:
#     rows = f.read()
# # count = 0
# # with black_list.pipeline() as pipe:
# #     for row in rows :
# #         count += 1
# #         pipe.sadd("black_list", row)
# #         if(count % 1000 == 0):
# #             pipe.execute()
# #     pipe.execute()