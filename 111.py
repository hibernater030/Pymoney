def fish_allocation_and_port_check(water_temp, total_fishermen, base_fish_weight, fisherman_quota):
    """
    Parameters:
        water_temp (float): 今日的水溫
        total_fishermen (int): 今日漁夫總人數
        base_fish_weight (float): 基礎漁貨量
        fisherman_quota (float): 每位漁夫的每日捕撈量
    Returns:
        str: 漁夫捕撈分配結果或判斷漁民是否能入港
    """

    adjusted_catch = base_fish_weight * (1 - water_temp / 100)
    
    
    per_fisherman_catch = adjusted_catch / total_fishermen / water_temp

    if per_fisherman_catch < fisherman_quota:
        
        shortage = fisherman_quota - per_fisherman_catch
        return f"魚貨不足，無法滿足需求！需減少總捕撈量 {shortage:.2f} 單位，該漁民無法入港。"
    else:
        return f"每位漁夫可捕撈 {per_fisherman_catch:.2f} 單位魚量。該漁民可順利入港。"

if __name__ == "__main__":
    print("請輸入以下資訊：")

 
    water_temp = float(input("今日水溫: "))
    total_fishermen = int(input("今日漁夫總人數: "))
    base_fish_weight = float(input("基礎漁貨量: "))
    fisherman_quota = float(input("每位漁夫每日捕撈量: "))

    
    result = fish_allocation_and_port_check(water_temp, total_fishermen, base_fish_weight, fisherman_quota)
    print(result)
