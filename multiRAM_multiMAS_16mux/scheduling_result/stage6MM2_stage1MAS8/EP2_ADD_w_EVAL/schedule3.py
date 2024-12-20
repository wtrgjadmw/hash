from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 170
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 0
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 0
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 0
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 1
	t0_t0_in += MM_in[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 1
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 1
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=6, delay_cost=1)
	S += t0_t1 >= 1
	t0_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=6, delay_cost=1)
	S += t0_t0 >= 2
	t0_t0 += MM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 2
	t2_t1_in += MM_in[1]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 2
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 2
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 3
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 3
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 3
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=6, delay_cost=1)
	S += t2_t1 >= 3
	t2_t1 += MM[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=6, delay_cost=1)
	S += t2_t0 >= 4
	t2_t0 += MM[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 5
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 5
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MAS[4]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 6
	t0_t2 += MAS[2]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 6
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 6
	t0_t4_mem0 += MAS_MEM[4]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 6
	t0_t4_mem1 += MAS_MEM[9]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 6
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 6
	t2_t2_mem1 += MAIN_MEM_r[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 7
	t00_mem0 += MM_MEM[2]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 7
	t00_mem1 += MM_MEM[1]

	t0_t4 = S.Task('t0_t4', length=6, delay_cost=1)
	S += t0_t4 >= 7
	t0_t4 += MM[0]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 7
	t2_t2 += MAS[6]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 7
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 7
	t2_t3_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 8
	t00 += MAS[4]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 8
	t0_t5_mem0 += MM_MEM[2]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 8
	t0_t5_mem1 += MM_MEM[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 8
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 8
	t10_mem1 += MAS_MEM[9]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 8
	t2_t3 += MAS[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[1]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[12]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[5]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 9
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 9
	c200_mem0 += MAS_MEM[10]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 9
	c200_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 9
	t0_t5 += MAS[2]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 9
	t10 += MAS[5]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 9
	t17_t0_in += MM_in[1]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 9
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 9
	t17_t0_mem1 += MAS_MEM[11]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 9
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 9
	t20_mem1 += MM_MEM[3]

	t2_t4 = S.Task('t2_t4', length=6, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[1]

	c200 = S.Task('c200', length=6, delay_cost=1)
	S += c200 >= 10
	c200 += MM[0]

	t17_t0 = S.Task('t17_t0', length=6, delay_cost=1)
	S += t17_t0 >= 10
	t17_t0 += MM[1]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 10
	t20 += MAS[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 10
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 10
	t2_t5_mem1 += MM_MEM[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 10
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 10
	t30_mem1 += MAS_MEM[3]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 11
	c010_in += MM_in[1]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 11
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 11
	c010_mem1 += MAIN_MEM_r[1]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 11
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 11
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 11
	t16_t0_mem1 += MAS_MEM[5]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 11
	t2_t5 += MAS[0]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 11
	t30 += MAS[2]

	c010 = S.Task('c010', length=6, delay_cost=1)
	S += c010 >= 12
	c010 += MM[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 12
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 12
	t01_mem1 += MAS_MEM[5]

	t16_t0 = S.Task('t16_t0', length=6, delay_cost=1)
	S += t16_t0 >= 12
	t16_t0 += MM[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 12
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 12
	t17_t2_mem1 += MAIN_MEM_r[1]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 13
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 13
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 13
	t01 += MAS[0]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 13
	t17_t2 += MAS[5]

	new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
	S += new_TZ_t2 >= 14
	new_TZ_t2 += MAS[1]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 14
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 14
	t16_t2_mem1 += MAIN_MEM_r[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 14
	t21_mem0 += MM_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 14
	t21_mem1 += MAS_MEM[1]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 15
	t16_t2 += MAS[4]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 15
	t21 += MAS[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 15
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 15
	t31_mem1 += MAS_MEM[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 16
	c200_w += MAIN_MEM_w

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 16
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 16
	t14_t2_mem1 += MAIN_MEM_r[1]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 16
	t31 += MAS[7]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 16
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 16
	t5_t3_mem0 += MAS_MEM[4]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 16
	t5_t3_mem1 += MAS_MEM[15]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 17
	c011_in += MM_in[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 17
	c011_mem0 += MAS_MEM[14]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 17
	c011_mem1 += MAIN_MEM_r[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 17
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 17
	t11_mem1 += MAS_MEM[1]

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 17
	t14_t2 += MAS[7]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 17
	t5_t1_mem0 += MAS_MEM[4]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 17
	t5_t1_mem1 += MAS_MEM[15]

	t5_t3 = S.Task('t5_t3', length=6, delay_cost=1)
	S += t5_t3 >= 17
	t5_t3 += MM[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 18
	c010_w += MAIN_MEM_w

	c011 = S.Task('c011', length=6, delay_cost=1)
	S += c011 >= 18
	c011 += MM[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 18
	t11 += MAS[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 18
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 18
	t4_t3_mem0 += MAS_MEM[10]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 18
	t4_t3_mem1 += MAS_MEM[1]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 18
	t5_t0_mem0 += MAS_MEM[4]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 18
	t5_t0_mem1 += MAS_MEM[15]

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	S += t5_t1 >= 18
	t5_t1 += MAS[3]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 18
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 18
	t9_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 19
	t4_t0_mem0 += MAS_MEM[10]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 19
	t4_t0_mem1 += MAS_MEM[1]

	t4_t3 = S.Task('t4_t3', length=6, delay_cost=1)
	S += t4_t3 >= 19
	t4_t3 += MM[0]

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	S += t5_t0 >= 19
	t5_t0 += MAS[1]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 19
	t5_t2_in += MM_in[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 19
	t5_t2_mem0 += MAS_MEM[2]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 19
	t5_t2_mem1 += MAS_MEM[7]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 19
	t6_t2_mem0 += MAS_MEM[4]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 19
	t6_t2_mem1 += MAS_MEM[15]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 19
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 19
	t7_t2_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
	S += t9_t2 >= 19
	t9_t2 += MAS[6]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 20
	c201_in += MM_in[1]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 20
	c201_mem0 += MAS_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 20
	c201_mem1 += MAIN_MEM_r[1]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 20
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 20
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 20
	t16_t1_mem1 += MAS_MEM[15]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 20
	t4_t0 += MAS[5]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 20
	t4_t1_mem0 += MAS_MEM[10]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 20
	t4_t1_mem1 += MAS_MEM[1]

	t5_t2 = S.Task('t5_t2', length=6, delay_cost=1)
	S += t5_t2 >= 20
	t5_t2 += MM[1]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 20
	t6_t2 += MAS[3]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 20
	t7_t2 += MAS[6]

	c201 = S.Task('c201', length=6, delay_cost=1)
	S += c201 >= 21
	c201 += MM[1]

	t16_t1 = S.Task('t16_t1', length=6, delay_cost=1)
	S += t16_t1 >= 21
	t16_t1 += MM[0]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 21
	t16_t3_mem0 += MAS_MEM[4]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 21
	t16_t3_mem1 += MAS_MEM[15]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 21
	t17_t1_in += MM_in[1]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 21
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 21
	t17_t1_mem1 += MAS_MEM[1]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 21
	t4_t1 += MAS[2]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 21
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 21
	t4_t2_mem0 += MAS_MEM[10]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 21
	t4_t2_mem1 += MAS_MEM[5]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 22
	new_TX_t2_mem0 += MAS_MEM[4]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 22
	new_TX_t2_mem1 += MAS_MEM[15]

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	S += t16_t3 >= 22
	t16_t3 += MAS[6]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 22
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 22
	t16_t4_mem0 += MAS_MEM[8]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 22
	t16_t4_mem1 += MAS_MEM[13]

	t17_t1 = S.Task('t17_t1', length=6, delay_cost=1)
	S += t17_t1 >= 22
	t17_t1 += MM[1]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 22
	t17_t3_mem0 += MAS_MEM[10]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 22
	t17_t3_mem1 += MAS_MEM[1]

	t4_t2 = S.Task('t4_t2', length=6, delay_cost=1)
	S += t4_t2 >= 22
	t4_t2 += MM[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 22
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 22
	t51_mem1 += MM_MEM[1]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 23
	new_TX_t2 += MAS[3]

	t16_t4 = S.Task('t16_t4', length=6, delay_cost=1)
	S += t16_t4 >= 23
	t16_t4 += MM[0]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 23
	t17_t3 += MAS[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 23
	t17_t4_in += MM_in[1]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 23
	t17_t4_mem0 += MAS_MEM[10]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 23
	t17_t4_mem1 += MAS_MEM[3]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 23
	t51 += MAS[6]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 23
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 23
	t5_t5_mem1 += MM_MEM[1]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 23
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 23
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 23
	t9_t1_mem1 += MAS_MEM[13]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 24
	c011_w += MAIN_MEM_w

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 24
	t13_t2_mem0 += MAS_MEM[10]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 24
	t13_t2_mem1 += MAS_MEM[1]

	t17_t4 = S.Task('t17_t4', length=6, delay_cost=1)
	S += t17_t4 >= 24
	t17_t4 += MM[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 24
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 24
	t41_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 24
	t5_t5 += MAS[5]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 24
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 24
	t6_t1_mem0 += MAS_MEM[14]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 24
	t6_t1_mem1 += MAS_MEM[13]

	t9_t1 = S.Task('t9_t1', length=6, delay_cost=1)
	S += t9_t1 >= 24
	t9_t1 += MM[0]

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	S += t13_t2 >= 25
	t13_t2 += MAS[0]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 25
	t41 += MAS[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 25
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 25
	t4_t5_mem1 += MM_MEM[1]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 25
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 25
	t50_mem1 += MAS_MEM[11]

	t6_t1 = S.Task('t6_t1', length=6, delay_cost=1)
	S += t6_t1 >= 25
	t6_t1 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 25
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 25
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 25
	t7_t1_mem1 += MAS_MEM[7]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 26
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 26
	t160_mem1 += MM_MEM[1]

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 26
	t4_t5 += MAS[1]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 26
	t50 += MAS[5]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 26
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 26
	t6_t0_mem0 += MAS_MEM[4]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 26
	t6_t0_mem1 += MAS_MEM[11]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 26
	t6_t3_mem0 += MAS_MEM[10]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 26
	t6_t3_mem1 += MAS_MEM[13]

	t7_t1 = S.Task('t7_t1', length=6, delay_cost=1)
	S += t7_t1 >= 26
	t7_t1 += MM[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 27
	c201_w += MAIN_MEM_w

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 27
	t160 += MAS[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 27
	t170_mem0 += MM_MEM[2]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 27
	t170_mem1 += MM_MEM[3]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 27
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 27
	t40_mem1 += MAS_MEM[3]

	t6_t0 = S.Task('t6_t0', length=6, delay_cost=1)
	S += t6_t0 >= 27
	t6_t0 += MM[0]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 27
	t6_t3 += MAS[3]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 27
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 27
	t6_t4_mem0 += MAS_MEM[6]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 27
	t6_t4_mem1 += MAS_MEM[7]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 27
	t9_t0_in += MM_in[1]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 27
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 27
	t9_t0_mem1 += MAS_MEM[11]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 27
	t9_t3_mem0 += MAS_MEM[10]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 27
	t9_t3_mem1 += MAS_MEM[13]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 28
	c000_mem0 += MAS_MEM[2]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 28
	c000_mem1 += MAS_MEM[13]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 28
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 28
	t16_t5_mem1 += MM_MEM[1]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 28
	t170 += MAS[6]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 28
	t17_t5_mem0 += MM_MEM[2]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 28
	t17_t5_mem1 += MM_MEM[3]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 28
	t40 += MAS[2]

	t6_t4 = S.Task('t6_t4', length=6, delay_cost=1)
	S += t6_t4 >= 28
	t6_t4 += MM[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 28
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 28
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 28
	t7_t0_mem1 += MAS_MEM[5]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 28
	t7_t3_mem0 += MAS_MEM[4]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 28
	t7_t3_mem1 += MAS_MEM[7]

	t9_t0 = S.Task('t9_t0', length=6, delay_cost=1)
	S += t9_t0 >= 28
	t9_t0 += MM[1]

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	S += t9_t3 >= 28
	t9_t3 += MAS[1]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 28
	t9_t4_in += MM_in[1]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 28
	t9_t4_mem0 += MAS_MEM[12]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 28
	t9_t4_mem1 += MAS_MEM[3]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 29
	c000 += MAS[2]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 29
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 29
	t161_mem1 += MAS_MEM[1]

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	S += t16_t5 >= 29
	t16_t5 += MAS[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 29
	t171_mem0 += MM_MEM[2]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 29
	t171_mem1 += MAS_MEM[13]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 29
	t17_t5 += MAS[6]

	t7_t0 = S.Task('t7_t0', length=6, delay_cost=1)
	S += t7_t0 >= 29
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 29
	t7_t3 += MAS[1]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 29
	t7_t4_in += MM_in[1]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 29
	t7_t4_mem0 += MAS_MEM[12]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 29
	t7_t4_mem1 += MAS_MEM[3]

	t9_t4 = S.Task('t9_t4', length=6, delay_cost=1)
	S += t9_t4 >= 29
	t9_t4 += MM[1]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 30
	c000_w += MAIN_MEM_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 30
	c001_mem0 += MAS_MEM[8]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 30
	c001_mem1 += MAS_MEM[11]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 30
	t161 += MAS[4]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 30
	t171 += MAS[0]

	t7_t4 = S.Task('t7_t4', length=6, delay_cost=1)
	S += t7_t4 >= 30
	t7_t4 += MM[1]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 31
	c001 += MAS[6]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 32
	c001_w += MAIN_MEM_w

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 32
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 32
	t6_t5_mem1 += MM_MEM[1]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 33
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 33
	t61_mem1 += MAS_MEM[9]

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	S += t6_t5 >= 33
	t6_t5 += MAS[4]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 33
	t9_t5_mem0 += MM_MEM[2]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 33
	t9_t5_mem1 += MM_MEM[1]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 34
	new_TZ_t1_in += MM_in[0]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 34
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 34
	new_TZ_t1_mem1 += MAS_MEM[1]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 34
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 34
	t60_mem1 += MM_MEM[1]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 34
	t61 += MAS[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 34
	t91_mem0 += MM_MEM[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 34
	t91_mem1 += MAS_MEM[5]

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	S += t9_t5 >= 34
	t9_t5 += MAS[2]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 35
	new_TZ_t0_in += MM_in[0]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 35
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 35
	new_TZ_t0_mem1 += MAS_MEM[13]

	new_TZ_t1 = S.Task('new_TZ_t1', length=6, delay_cost=1)
	S += new_TZ_t1 >= 35
	new_TZ_t1 += MM[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 35
	t101_mem0 += MAS_MEM[2]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 35
	t101_mem1 += MAS_MEM[3]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 35
	t14_t3_mem0 += MAS_MEM[12]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 35
	t14_t3_mem1 += MAS_MEM[1]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 35
	t60 += MAS[6]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 35
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 35
	t7_t5_mem1 += MM_MEM[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 35
	t90_mem0 += MM_MEM[2]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 35
	t90_mem1 += MM_MEM[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 35
	t91 += MAS[1]

	new_TZ_t0 = S.Task('new_TZ_t0', length=6, delay_cost=1)
	S += new_TZ_t0 >= 36
	new_TZ_t0 += MM[0]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 36
	new_TZ_t3_mem0 += MAS_MEM[12]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 36
	new_TZ_t3_mem1 += MAS_MEM[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 36
	t100_mem0 += MAS_MEM[8]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 36
	t100_mem1 += MAS_MEM[9]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 36
	t101 += MAS[2]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 36
	t14_t0_in += MM_in[1]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 36
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 36
	t14_t0_mem1 += MAS_MEM[13]

	t14_t3 = S.Task('t14_t3', length=1, delay_cost=1)
	S += t14_t3 >= 36
	t14_t3 += MAS[1]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 36
	t14_t4_in += MM_in[0]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 36
	t14_t4_mem0 += MAS_MEM[14]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 36
	t14_t4_mem1 += MAS_MEM[3]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 36
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 36
	t70_mem1 += MM_MEM[3]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 36
	t71_mem0 += MM_MEM[2]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 36
	t71_mem1 += MAS_MEM[7]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 36
	t7_t5 += MAS[3]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 36
	t90 += MAS[4]

	new_TZ_t3 = S.Task('new_TZ_t3', length=1, delay_cost=1)
	S += new_TZ_t3 >= 37
	new_TZ_t3 += MAS[3]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 37
	new_TZ_t4_in += MM_in[0]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 37
	new_TZ_t4_mem0 += MAS_MEM[2]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 37
	new_TZ_t4_mem1 += MAS_MEM[7]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 37
	t100 += MAS[6]

	t14_t0 = S.Task('t14_t0', length=6, delay_cost=1)
	S += t14_t0 >= 37
	t14_t0 += MM[1]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 37
	t14_t1_in += MM_in[1]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 37
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 37
	t14_t1_mem1 += MAS_MEM[1]

	t14_t4 = S.Task('t14_t4', length=6, delay_cost=1)
	S += t14_t4 >= 37
	t14_t4 += MM[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 37
	t70 += MAS[7]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 37
	t71 += MAS[5]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 37
	t80_mem0 += MAS_MEM[12]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 37
	t80_mem1 += MAS_MEM[15]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 37
	t81_mem0 += MAS_MEM[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 37
	t81_mem1 += MAS_MEM[11]

	new_TZ_t4 = S.Task('new_TZ_t4', length=6, delay_cost=1)
	S += new_TZ_t4 >= 38
	new_TZ_t4 += MM[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 38
	t110_mem0 += MAS_MEM[10]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 38
	t110_mem1 += MAS_MEM[13]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 38
	t111_mem0 += MAS_MEM[0]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 38
	t111_mem1 += MAS_MEM[5]

	t14_t1 = S.Task('t14_t1', length=6, delay_cost=1)
	S += t14_t1 >= 38
	t14_t1 += MM[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 38
	t80 += MAS[5]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 38
	t81 += MAS[0]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 39
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 39
	new_TX_t0_mem0 += MAS_MEM[4]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 39
	new_TX_t0_mem1 += MAS_MEM[7]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 39
	new_TX_t1_in += MM_in[1]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 39
	new_TX_t1_mem0 += MAS_MEM[14]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 39
	new_TX_t1_mem1 += MAS_MEM[1]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 39
	t110 += MAS[3]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 39
	t111 += MAS[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 39
	t120_mem0 += MAS_MEM[6]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 39
	t120_mem1 += MAS_MEM[9]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 39
	t121_mem0 += MAS_MEM[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 39
	t121_mem1 += MAS_MEM[3]

	new_TX_t0 = S.Task('new_TX_t0', length=6, delay_cost=1)
	S += new_TX_t0 >= 40
	new_TX_t0 += MM[0]

	new_TX_t1 = S.Task('new_TX_t1', length=6, delay_cost=1)
	S += new_TX_t1 >= 40
	new_TX_t1 += MM[1]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 40
	new_TX_t3_mem0 += MAS_MEM[6]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 40
	new_TX_t3_mem1 += MAS_MEM[1]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 40
	t120 += MAS[5]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 40
	t121 += MAS[7]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 40
	t13_t0_in += MM_in[1]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 40
	t13_t0_mem0 += MAS_MEM[10]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 40
	t13_t0_mem1 += MAS_MEM[11]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 40
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 40
	t13_t1_mem0 += MAS_MEM[0]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 40
	t13_t1_mem1 += MAS_MEM[15]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 41
	new_TX_t3 += MAS[2]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 41
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 41
	new_TX_t4_mem0 += MAS_MEM[6]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 41
	new_TX_t4_mem1 += MAS_MEM[5]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 41
	new_TZ0_mem0 += MM_MEM[0]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 41
	new_TZ0_mem1 += MM_MEM[1]

	t13_t0 = S.Task('t13_t0', length=6, delay_cost=1)
	S += t13_t0 >= 41
	t13_t0 += MM[1]

	t13_t1 = S.Task('t13_t1', length=6, delay_cost=1)
	S += t13_t1 >= 41
	t13_t1 += MM[0]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 41
	t13_t3_mem0 += MAS_MEM[10]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 41
	t13_t3_mem1 += MAS_MEM[15]

	new_TX_t4 = S.Task('new_TX_t4', length=6, delay_cost=1)
	S += new_TX_t4 >= 42
	new_TX_t4 += MM[0]

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	S += new_TZ0 >= 42
	new_TZ0 += MAS[3]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 42
	new_TZ_t5_mem0 += MM_MEM[0]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 42
	new_TZ_t5_mem1 += MM_MEM[1]

	t13_t3 = S.Task('t13_t3', length=1, delay_cost=1)
	S += t13_t3 >= 42
	t13_t3 += MAS[0]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 42
	t13_t4_in += MM_in[1]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 42
	t13_t4_mem0 += MAS_MEM[0]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 42
	t13_t4_mem1 += MAS_MEM[1]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 43
	new_TZ0_w += MAIN_MEM_w

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 43
	new_TZ1_mem0 += MM_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 43
	new_TZ1_mem1 += MAS_MEM[9]

	new_TZ_t5 = S.Task('new_TZ_t5', length=1, delay_cost=1)
	S += new_TZ_t5 >= 43
	new_TZ_t5 += MAS[4]

	t13_t4 = S.Task('t13_t4', length=6, delay_cost=1)
	S += t13_t4 >= 43
	t13_t4 += MM[1]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 43
	t14_t5_mem0 += MM_MEM[2]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 43
	t14_t5_mem1 += MM_MEM[3]

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	S += new_TZ1 >= 44
	new_TZ1 += MAS[0]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 44
	t140_mem0 += MM_MEM[2]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 44
	t140_mem1 += MM_MEM[3]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 44
	t141_mem0 += MM_MEM[0]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 44
	t141_mem1 += MAS_MEM[3]

	t14_t5 = S.Task('t14_t5', length=1, delay_cost=1)
	S += t14_t5 >= 44
	t14_t5 += MAS[1]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 45
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 45
	new_TX0_mem1 += MM_MEM[3]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 45
	new_TZ1_w += MAIN_MEM_w

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 45
	t140 += MAS[4]

	t141 = S.Task('t141', length=1, delay_cost=1)
	S += t141 >= 45
	t141 += MAS[6]

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	S += new_TX0 >= 46
	new_TX0 += MAS[0]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 46
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 46
	new_TX_t5_mem1 += MM_MEM[3]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 46
	t130_mem0 += MM_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 46
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 47
	new_TX0_w += MAIN_MEM_w

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 47
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 47
	new_TX1_mem1 += MAS_MEM[5]

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	S += new_TX_t5 >= 47
	new_TX_t5 += MAS[2]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 47
	t130 += MAS[5]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 47
	t13_t5_mem0 += MM_MEM[2]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 47
	t13_t5_mem1 += MM_MEM[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 47
	t150_mem0 += MAS_MEM[10]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 47
	t150_mem1 += MAS_MEM[9]

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	S += new_TX1 >= 48
	new_TX1 += MAS[7]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 48
	t131_mem0 += MM_MEM[2]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 48
	t131_mem1 += MAS_MEM[7]

	t13_t5 = S.Task('t13_t5', length=1, delay_cost=1)
	S += t13_t5 >= 48
	t13_t5 += MAS[3]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 48
	t150 += MAS[1]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 49
	new_TX1_w += MAIN_MEM_w

	t131 = S.Task('t131', length=1, delay_cost=1)
	S += t131 >= 49
	t131 += MAS[5]


	# new tasks
	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)
	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[10]
	S += 49 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[13]
	S += 45 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(MAS)
	S += 37<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[3]
	S += 48 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(MAS)
	S += 38<new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(MAIN_MEM_w)
	S += new_TY1 <= new_TY1_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += MAIN_MEM_r[0]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TY1_mem1*MAS_MEM[1]
	S += (t151*MAS[1])-1 < new_TY1_mem1*MAS_MEM[3]
	S += (t151*MAS[2])-1 < new_TY1_mem1*MAS_MEM[5]
	S += (t151*MAS[3])-1 < new_TY1_mem1*MAS_MEM[7]
	S += (t151*MAS[4])-1 < new_TY1_mem1*MAS_MEM[9]
	S += (t151*MAS[5])-1 < new_TY1_mem1*MAS_MEM[11]
	S += (t151*MAS[6])-1 < new_TY1_mem1*MAS_MEM[13]
	S += (t151*MAS[7])-1 < new_TY1_mem1*MAS_MEM[15]
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS8/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

