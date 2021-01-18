import processes

import inspect

##create สมมุติฐาน
rand_cond = processes.RamdomCondition()
rand_cond.add_condition((2, 8), 70) ## 2 -> 8 and 70%
rand_cond.add_condition((20, 30), 20) ## 20 -> 30 and 20%
rand_cond.add_condition((35, 40), 10)
process_list1 = processes.process_generate(rand_cond, 60) ##60process

rand_cond = processes.RamdomCondition()
rand_cond.add_condition((2, 8), 50) 
rand_cond.add_condition((20, 30), 30) 
rand_cond.add_condition((35, 40), 20)
process_list2 = processes.process_generate(rand_cond, 40) 

rand_cond = processes.RamdomCondition()
rand_cond.add_condition((2, 8), 40) 
rand_cond.add_condition((20, 30), 40) 
rand_cond.add_condition((35, 40), 20)
process_list3 = processes.process_generate(rand_cond, 20) 


print (process_list1)