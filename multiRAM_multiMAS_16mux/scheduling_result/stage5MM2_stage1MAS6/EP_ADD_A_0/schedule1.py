from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 142
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=5)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 0
	t2_in += MM_in[1]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 0
	t2_mem0 += MAIN_MEM_r[0]

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	S += t2_mem1 >= 0
	t2_mem1 += MAIN_MEM_r[1]

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 1
	t0_in += MM_in[1]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 1
	t0_mem0 += MAIN_MEM_r[0]

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	S += t0_mem1 >= 1
	t0_mem1 += MAIN_MEM_r[1]

	t2 = S.Task('t2', length=5, delay_cost=1)
	S += t2 >= 1
	t2 += MM[1]

	t0 = S.Task('t0', length=5, delay_cost=1)
	S += t0 >= 2
	t0 += MM[1]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 2
	t1_in += MM_in[0]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 2
	t1_mem0 += MAIN_MEM_r[0]

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	S += t1_mem1 >= 2
	t1_mem1 += MAIN_MEM_r[1]

	t1 = S.Task('t1', length=5, delay_cost=1)
	S += t1 >= 3
	t1 += MM[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 3
	t3_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 3
	t3_mem1 += MAIN_MEM_r[1]

	t3 = S.Task('t3', length=1, delay_cost=1)
	S += t3 >= 4
	t3 += MAS[1]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 4
	t4_mem0 += MAIN_MEM_r[0]

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	S += t4_mem1 >= 4
	t4_mem1 += MAIN_MEM_r[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 5
	t20_in += MM_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 5
	t20_mem0 += MM_MEM[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 5
	t20_mem1 += MAIN_MEM_r[1]

	t4 = S.Task('t4', length=1, delay_cost=1)
	S += t4 >= 5
	t4 += MAS[2]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 5
	t5_in += MM_in[1]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 5
	t5_mem0 += MAS_MEM[2]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 5
	t5_mem1 += MAS_MEM[5]

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	S += t16_mem0 >= 6
	t16_mem0 += MM_MEM[2]

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	S += t16_mem1 >= 6
	t16_mem1 += MM_MEM[3]

	t20 = S.Task('t20', length=5, delay_cost=1)
	S += t20 >= 6
	t20 += MM[0]

	t5 = S.Task('t5', length=5, delay_cost=1)
	S += t5 >= 6
	t5 += MM[1]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 6
	t8_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 6
	t8_mem1 += MAIN_MEM_r[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 7
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 7
	t11_mem1 += MM_MEM[3]

	t16 = S.Task('t16', length=1, delay_cost=1)
	S += t16 >= 7
	t16 += MAS[3]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 7
	t6_mem0 += MM_MEM[2]

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	S += t6_mem1 >= 7
	t6_mem1 += MM_MEM[1]

	t8 = S.Task('t8', length=1, delay_cost=1)
	S += t8 >= 7
	t8 += MAS[2]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 7
	t9_mem0 += MAIN_MEM_r[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 7
	t9_mem1 += MAIN_MEM_r[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 8
	t10_in += MM_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 8
	t10_mem0 += MAS_MEM[4]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 8
	t10_mem1 += MAS_MEM[9]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 8
	t11 += MAS[5]

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	S += t14_mem0 >= 8
	t14_mem0 += MAIN_MEM_r[0]

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	S += t14_mem1 >= 8
	t14_mem1 += MAIN_MEM_r[1]

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	S += t18_mem0 >= 8
	t18_mem0 += MM_MEM[2]

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	S += t18_mem1 >= 8
	t18_mem1 += MM_MEM[3]

	t6 = S.Task('t6', length=1, delay_cost=1)
	S += t6 >= 8
	t6 += MAS[1]

	t9 = S.Task('t9', length=1, delay_cost=1)
	S += t9 >= 8
	t9 += MAS[4]

	t10 = S.Task('t10', length=5, delay_cost=1)
	S += t10 >= 9
	t10 += MM[0]

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	S += t13_mem0 >= 9
	t13_mem0 += MAIN_MEM_r[0]

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	S += t13_mem1 >= 9
	t13_mem1 += MAIN_MEM_r[1]

	t14 = S.Task('t14', length=1, delay_cost=1)
	S += t14 >= 9
	t14 += MAS[0]

	t18 = S.Task('t18', length=1, delay_cost=1)
	S += t18 >= 9
	t18 += MAS[3]

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	S += t19_mem0 >= 9
	t19_mem0 += MM_MEM[2]

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	S += t19_mem1 >= 9
	t19_mem1 += MAS_MEM[7]

	t13 = S.Task('t13', length=1, delay_cost=1)
	S += t13 >= 10
	t13 += MAS[2]

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	S += t15_in >= 10
	t15_in += MM_in[1]

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	S += t15_mem0 >= 10
	t15_mem0 += MAS_MEM[4]

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	S += t15_mem1 >= 10
	t15_mem1 += MAS_MEM[1]

	t19 = S.Task('t19', length=1, delay_cost=1)
	S += t19 >= 10
	t19 += MAS[0]

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	S += t22_mem0 >= 10
	t22_mem0 += MM_MEM[0]

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	S += t22_mem1 >= 10
	t22_mem1 += MM_MEM[1]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 10
	t7_mem0 += MM_MEM[2]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 10
	t7_mem1 += MAS_MEM[3]

	t15 = S.Task('t15', length=5, delay_cost=1)
	S += t15 >= 11
	t15 += MM[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 11
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 11
	t21_mem1 += MM_MEM[1]

	t22 = S.Task('t22', length=1, delay_cost=1)
	S += t22 >= 11
	t22 += MAS[1]

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	S += t25_in >= 11
	t25_in += MM_in[0]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 11
	t25_mem0 += MAS_MEM[8]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 11
	t25_mem1 += MAS_MEM[3]

	t28_in = S.Task('t28_in', length=1, delay_cost=1)
	S += t28_in >= 11
	t28_in += MM_in[1]

	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	S += t28_mem0 >= 11
	t28_mem0 += MAS_MEM[0]

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	S += t28_mem1 >= 11
	t28_mem1 += MAS_MEM[9]

	t7 = S.Task('t7', length=1, delay_cost=1)
	S += t7 >= 11
	t7 += MAS[4]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 12
	t21 += MAS[0]

	t25 = S.Task('t25', length=5, delay_cost=1)
	S += t25 >= 12
	t25 += MM[0]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 12
	t27_in += MM_in[1]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 12
	t27_mem0 += MAS_MEM[2]

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	S += t27_mem1 >= 12
	t27_mem1 += MAS_MEM[1]

	t28 = S.Task('t28', length=5, delay_cost=1)
	S += t28 >= 12
	t28 += MM[1]

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	S += t12_mem0 >= 13
	t12_mem0 += MM_MEM[0]

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	S += t12_mem1 >= 13
	t12_mem1 += MAS_MEM[11]

	t27 = S.Task('t27', length=5, delay_cost=1)
	S += t27 >= 13
	t27 += MM[1]

	t12 = S.Task('t12', length=1, delay_cost=1)
	S += t12 >= 14
	t12 += MAS[3]

	t29_in = S.Task('t29_in', length=1, delay_cost=1)
	S += t29_in >= 14
	t29_in += MM_in[0]

	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	S += t29_mem0 >= 14
	t29_mem0 += MAS_MEM[0]

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	S += t29_mem1 >= 14
	t29_mem1 += MAS_MEM[7]

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	S += t17_mem0 >= 15
	t17_mem0 += MM_MEM[2]

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	S += t17_mem1 >= 15
	t17_mem1 += MAS_MEM[7]

	t29 = S.Task('t29', length=5, delay_cost=1)
	S += t29 >= 15
	t29 += MM[0]

	t17 = S.Task('t17', length=1, delay_cost=1)
	S += t17 >= 16
	t17 += MAS[5]

	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	S += t23_in >= 16
	t23_in += MM_in[0]

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	S += t23_mem0 >= 16
	t23_mem0 += MAS_MEM[10]

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	S += t23_mem1 >= 16
	t23_mem1 += MAIN_MEM_r[1]

	t23 = S.Task('t23', length=5, delay_cost=1)
	S += t23 >= 17
	t23 += MM[0]


	# new tasks
	t24 = S.Task('t24', length=5, delay_cost=1)
	t24 += alt(MM)
	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	t24_in += alt(MM_in)
	S += t24_in*MM_in[0]<=t24*MM[0]
	S += t24_in*MM_in[1]<=t24*MM[1]
	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	t24_mem0 += MAS_MEM[6]
	S += 14 < t24_mem0
	S += t24_mem0 <= t24

	t24_mem1 = S.Task('t24_mem1', length=1, delay_cost=1)
	t24_mem1 += MM_MEM[1]
	S += 21 < t24_mem1
	S += t24_mem1 <= t24

	t26 = S.Task('t26', length=5, delay_cost=1)
	t26 += alt(MM)
	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	t26_in += alt(MM_in)
	S += t26_in*MM_in[0]<=t26*MM[0]
	S += t26_in*MM_in[1]<=t26*MM[1]
	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	t26_mem0 += MAS_MEM[0]
	S += 10 < t26_mem0
	S += t26_mem0 <= t26

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	t26_mem1 += MM_MEM[1]
	S += 21 < t26_mem1
	S += t26_mem1 <= t26

	PZ_new = S.Task('PZ_new', length=5, delay_cost=1)
	PZ_new += alt(MM)
	PZ_new_in = S.Task('PZ_new_in', length=1, delay_cost=1)
	PZ_new_in += alt(MM_in)
	S += PZ_new_in*MM_in[0]<=PZ_new*MM[0]
	S += PZ_new_in*MM_in[1]<=PZ_new*MM[1]
	S += 0<PZ_new

	PZ_new_w = S.Task('PZ_new_w', length=1, delay_cost=1)
	PZ_new_w += alt(MAIN_MEM_w)
	S += PZ_new <= PZ_new_w

	PZ_new_mem0 = S.Task('PZ_new_mem0', length=1, delay_cost=1)
	PZ_new_mem0 += MM_MEM[0]
	S += 19 < PZ_new_mem0
	S += PZ_new_mem0 <= PZ_new

	PZ_new_mem1 = S.Task('PZ_new_mem1', length=1, delay_cost=1)
	PZ_new_mem1 += MM_MEM[3]
	S += 16 < PZ_new_mem1
	S += PZ_new_mem1 <= PZ_new

	PX_new = S.Task('PX_new', length=1, delay_cost=1)
	PX_new += alt(MAS)
	S += 0<PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(MAIN_MEM_w)
	S += PX_new <= PX_new_w

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += MM_MEM[0]
	S += 16 < PX_new_mem0
	S += PX_new_mem0 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(MM_MEM)
	S += (t24*MM[0])-1 < PX_new_mem1*MM_MEM[1]
	S += (t24*MM[1])-1 < PX_new_mem1*MM_MEM[3]
	S += PX_new_mem1 <= PX_new

	PY_new = S.Task('PY_new', length=1, delay_cost=1)
	PY_new += alt(MAS)
	S += 0<PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(MAIN_MEM_w)
	S += PY_new <= PY_new_w

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += MM_MEM[2]
	S += 17 < PY_new_mem0
	S += PY_new_mem0 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(MM_MEM)
	S += (t26*MM[0])-1 < PY_new_mem1*MM_MEM[1]
	S += (t26*MM[1])-1 < PY_new_mem1*MM_MEM[3]
	S += PY_new_mem1 <= PY_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM2_stage1MAS6/EP_ADD_A_0/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

