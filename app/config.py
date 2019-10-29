import os

# 项目地址
base_path = os.path.dirname(os.path.dirname(__file__))

# 粗钢产能利用率
utilization = None

# 限产
limit_production = {
    "河北": {"河北", "唐山", "邯郸", "邢台"},
    "山东": {"山东"},
    "天津": {"天津"},
    "河南": {"河南", "济源"},
    "山西": {"山西", "阳泉"}
}

# 铁矿石成本
iron_ore_cost = 0

# 焦炭成本
coke_cost = 0

# 吨钢毛利率
gpm = 0

# 钢铁公司简称
corporation = {"沙钢", "河钢", "鞍钢", "宝山钢铁", "山东钢铁", "包钢钢联"}
