
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？



#字典：
    #字典中存储数据的格式必须是key:value
    #在python中，能拿到key，就肯定能拿到value
    #key：必须是可哈希的的数据类型

games = {"暴雪":"使命召唤","蓝洞":"绝地求生","育碧":"孤岛惊魂"}
for k,v in games.items():
    print(k)
    print(v)

games["R星"] = "荒野大镖客"
games["R星"] = "GTA V"
games.pop("R星")
print(games)

# 有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
dicts = {}
list = []
number = "k:1|k1:2|k2:3|k3:4"
frist_ret = number.split("|")
for i in frist_ret:
    print(i)
    ret = i.split(":")
    dicts[ret[0]] = ret[1]
print(dicts)
