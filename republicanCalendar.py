import ephem
import datetime
from datetime import date

"""
计算输入日期所在年份的秋分日
input: datetime.date
return: datetime.date
"""
def getAutumnEquinox(day: date) -> date:
    equinox = ephem.next_autumn_equinox(day)
    equinoxDatetime = equinox.datetime()
    equinoxDate = date(equinoxDatetime.year, equinoxDatetime.month, equinoxDatetime.day)
    return equinoxDate



"""
计算输入日期所在的共和历年份的新年日期
如果输入日期所在公历年的秋分日在日期之前，则该秋分日为日期所在共和历年份的新年
如果秋分日在日期之后，则上一个秋分日为新年
input: datetime.date
return: datetime.date
"""
def getNewYearDate(day: date) -> date:
    equinoxDay = getAutumnEquinox(day)
    if (equinoxDay <= day):
        return equinoxDay
    else:
        # 从今年的秋分日创建一个年份和月份均-1的日期lastYear，确保getAutumnEquinox(lastYear)返回去年的秋分日
        lastYear = date(equinoxDay.year - 1, equinoxDay.month - 1, equinoxDay.day)
        lastEquinoxDay = getAutumnEquinox(lastYear)
        return lastEquinoxDay

"""
返回共和历元年新年日期
共和历1年的公历日期为1792年9月22日
return: datetime.date
"""
def getFirstNewYearDate() -> date:
    newYear = date(1792, 9, 22)
    assert(getNewYearDate(newYear) == newYear)
    return newYear

"""
计算输入日期的共和历年份
输入日期所在年份的共和历新年所在的公历年份减1792，如果结果不小于零则加一
input: datetime.date
return: int
"""
def getYear(date: date) -> int:
    newYear = getNewYearDate(date)
    yearCount = newYear.year - getFirstNewYearDate().year
    if (yearCount >= 0):
        return yearCount + 1
    else:
        return yearCount

"""
计算输入日期的共和历年拥有的天数
input: datetime.date
return: int
"""
def daysInYear(date: date) -> int:
    newYear = getNewYearDate(date)
    newYearNextDay = newYear + datetime.timedelta(days=400)
    nextNewYear = getNewYearDate(newYearNextDay)
    timeDelta = nextNewYear - newYear
    return timeDelta.days

"""
计算输入日期的共和历年是否为闰年
input: datetime.date
return: bool
"""
def isLeap(date: date) -> bool:
    days = daysInYear(date)
    return days % 366 == 0

"""
计算输入日期距离共和历新年的天数
新年记为0
input: datetime.date
return: int
"""
def daysSinceNewYear(date: date) -> int:
    newYear = getNewYearDate(date)
    return (date - newYear).days

"""
计算输入日期所在月份
葡月记为0
input: datetime.date
return: int
"""
def getMonthsSinceNewYear(date: date) -> int:
    return int(daysSinceNewYear(date) / 30)

"""
计算输入日期在月份中的天数
1号记为0
input: datetime.date
return: int
"""
def getDaysSinceStartOfMonth(date: date) -> int:
    return daysSinceNewYear(date) % 30

"""
获取中文的月份名称
return: [str]
"""
def getMonthsChinese() -> list: 
    return ["葡月", "雾月", "霜月", "雪月", "雨月", "风月", "芽月", "花月", "牧月", "获月", "热月", "果月", ""]

"""
获取中文的日期名称
return: [[str]]
"""
def getDaysChinese() -> list:
    return [
        # 葡月
        ["葡萄日", "藏红花日", "板栗日", "秋水仙日", "马日", "凤仙花日", "红萝卜日", "苋日", "欧洲防风日", "酒槽日", "马铃薯日", "蜡菊日", "笋瓜日", "木犀草日", "驴日", "紫茉莉日", "南瓜日", "荞麦日", "向日葵日", "榨酒机日", "麻日", "桃日", "芜菁日", "孤挺花日", "黄牛日", "茄日", "辣椒日", "西红柿日", "大麦日", "桶日"],
        # 雾月
        ["苹果日", "芹菜日", "梨日", "甜菜日", "鹅日", "天芥菜日", "无花果日", "鸦葱日", "野生楸树日", "犁日", "婆罗门参日", "菱角日", "洋姜日", "苦苣日", "火鸡日", "参芹日", "水田芥日", "蓝雪花日", "石榴日", "耖日", "香根菊日", "意大利山楂日", "染色茜草日", "橙子日", "雉鸡日", "开心果日", "玫红山黧豆日", "榅桲日", "欧亚花楸日", "磙日"],
        # 霜月
        ["角风铃草日", "饲料甜菜日", "菊苣日", "欧山楂日", "猪日", "野苣日", "花椰菜日", "蜂蜜日", "刺柏日", "十字镐日", "蜡日", "辣根日", "雪松日", "枞树日", "西方狍日", "荆豆日", "柏树日", "常春藤日", "叉子圆柏日", "撅头日", "糖枫日", "帚石楠日", "芦苇日", "酸模日", "蟋蟀日", "松子日", "软木橡树日", "松露日", "橄榄日", "铲子日"],
        # 雪月
        ["泥炭日", "烟煤日", "沥青日", "硫磺日", "犬日", "熔岩日", "腐殖土日", "有机肥日", "硝石日", "连枷日", "花岗岩日", "黏土日", "板岩日", "砂岩日", "穴兔日", "燧石日", "泥灰石日", "石灰石日", "大理石日", "簸箕日", "石膏日", "盐日", "铁日", "铜日", "猫日", "锡日", "铅日", "锌日", "汞日", "筲箕日"],
        # 雨月
        ["洋瑞香日", "苔藓日", "假叶树日", "雪花莲日", "公牛日", "地中海荚蒾日", "木蹄层孔菌日", "欧洲瑞香日", "杨树日", "斧头日", "铁筷子日", "青花菜日", "月桂日", "榛树日", "母牛日", "黄杨日", "地衣日", "红豆杉日", "肺草日", "锲日", "菥蓂日", "亚麻叶瑞香日", "匍匐冰草日", "萹蓄日", "野兔日", "菘蓝日", "榛子日", "仙客来日", "白屈菜日", "雪橇日"],
        # 风月
        ["款冬日", "山茱萸日", "糖芥日", "女桢日", "公山羊日", "细辛日", "意大利鼠李日", "堇菜日", "黄花柳日", "锹日", "水仙日", "榆树日", "球果紫堇日", "钻果大蒜芥日", "家山羊日", "菠菜日", "多榔菊日", "琉璃繁缕日", "法国芫荽日", "合股线日", "茄参日", "香芹日", "假山葵日", "雏菊日", "金枪鱼日", "蒲公英日", "森林银莲花日", "铁线蕨日", "梣树日", "手钻日"],
        # 芽月
        ["报春花日", "悬铃木日", "芦笋日", "郁金香日", "母鸡日", "莙荙菜日", "桦树日", "丁香水仙日", "桤木日", "嫁接刀日", "蔓长春花日", "鹅耳枥日", "羊肚菌日", "欧洲山毛榉日", "蜂日", "生菜日", "落叶松日", "毒芹日", "水萝卜日", "蜂箱日", "南欧紫荆日", "萝蔓莴苣日", "欧洲七叶树日", "芝麻菜日", "鸽子日", "欧丁香日", "秋牡丹日", "三色堇日", "山桑子日", "孵蛋器日"],
        # 花月
        ["庭园玫瑰日", "橡树日", "蕨日", "山楂日", "夜莺日", "耧斗菜日", "铃兰日", "蘑菇日", "风信子日", "耙日", "大黄日", "红豆草日", "蒲草日", "硬骨忍冬日", "蚕日", "聚合草日", "小地榆日", "金庭荠日", "榆钱菠菜日", "锄日", "海石竹日", "贝母日", "玻璃苣日", "缬草日", "鲤鱼日", "欧卫矛日", "虾夷葱日", "牛舌草日", "白芥日", "牧羊曲柄杖日"],
        # 牧月
        ["紫花苜蓿日", "萱草日", "三叶草日", "当归日", "鸭子日", "蜜蜂花日", "燕麦草日", "头巾百合日", "欧百里香日", "大镰日", "草莓日", "药水苏日", "豌豆日", "刺槐日", "鹌鹑日", "康乃馨日", "接骨木日", "罂粟日", "椴树日", "草叉日", "矢车菊日", "果香菊日", "忍冬日", "猪殃殃日", "丁鱥日", "茉莉日", "马鞭草日", "百里香日", "芍药日", "运货马车日"],
        # 获月
        ["黑麦日", "燕麦日", "洋葱日", "婆婆纳日", "骡子日", "迷迭香日", "黄瓜日", "分葱日", "苦艾日", "镰刀日", "芫荽日", "菜蓟日", "丁子香日", "熏衣草日", "臆羚日", "烟草日", "红加仑日", "香豌豆日", "樱桃日", "公园日", "薄荷日", "孜然日", "菜豆日", "紫朱草日", "珍珠鸡日", "鼠尾草日", "大蒜日", "蚕豆日", "小麦日", "萧姆管日"],
        # 热月
        ["斯佩耳特小麦日", "毛蕊花日", "甜瓜日", "毒麦日", "公羊日", "木贼日", "蒿日", "红花日", "黑莓日", "喷壶日", "柳枝稷日", "盐角草日", "杏日", "罗勒日", "母绵羊日", "药蜀葵日", "亚麻日", "扁桃日", "龙胆日", "船闸日", "刺苞术日", "续随子日", "小扁豆日", "旋覆花日", "水獭日", "香桃木日", "西洋油菜日", "羽扇豆日", "棉花日", "磨坊日"],
        # 果月
        ["李子日", "小米日", "马勃日", "六棱大麦日", "鲑鱼日", "晚香玉日", "六棱麦日", "夹竹桃日", "甘草日", "折梯日", "西瓜日", "茴香日", "刺檗日", "核桃日", "鳟鱼日", "柠檬日", "起绒草日", "鼠李日", "万寿菊日", "篮日", "狗蔷薇日", "榛子日", "啤酒花日", "高粱日", "螯虾日", "酸橙日", "一枝黄花日", "玉米日", "甜栗日", "篮子日"],
        # 闰日
        ["美德日", "天才日", "劳动日", "舆论日", "奖励日", "革命日"]
    ]

"""
获取共和历日期
input: datetime.date
return: (int, int, int)
"""
def getRepublicanCalendarDay(date: date) -> tuple:
    year = getYear(date)
    month = getMonthsSinceNewYear(date)
    day = getDaysSinceStartOfMonth(date)
    return (year, month, day)

"""
获取共和历日期中文表达形式
input: datetime.date
return: (int, str, str)
"""
def getRepublicanCalendarDayInChinese(date: date) -> tuple:
    y, m, d = getRepublicanCalendarDay(date)
    year = y
    month = getMonthsChinese()[m]
    day = getDaysChinese()[m][d]
    return (year, month, day)

"""
获取今天的共和历日期
return: (int, int, int)
"""
def getRepublicanCalendarToday(date: date) -> tuple:
    return getRepublicanCalendarDay(date.today())


"""
获取今天的共和历日期中文表达形式
return: (int, str, str)
"""
def getRepublicanCalendarTodayInChinese() -> tuple:
    return getRepublicanCalendarDayInChinese(date.today())