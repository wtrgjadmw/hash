from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 196
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=9)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=5)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 0
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 0
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 0
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 1
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 1
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 1
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=9, delay_cost=1)
	S += t2_t1 >= 1
	t2_t1 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 2
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 2
	t0_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=9, delay_cost=1)
	S += t2_t0 >= 2
	t2_t0 += MM[0]

	t0_t0 = S.Task('t0_t0', length=9, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 3
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 3
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 3
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=9, delay_cost=1)
	S += t0_t1 >= 4
	t0_t1 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MAS_in[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 5
	t0_t2_in += MAS_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 5
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 5
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MAS[1]

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	S += t0_t2 >= 6
	t0_t2 += MAS[1]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 6
	t2_t2_in += MAS_in[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 6
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 6
	t2_t2_mem1 += MAIN_MEM_r[1]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 7
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 7
	t0_t4_mem0 += MAS_MEM[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 7
	t0_t4_mem1 += MAS_MEM[3]

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	S += t2_t2 >= 7
	t2_t2 += MAS[1]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 7
	t2_t3_in += MAS_in[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 7
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 7
	t2_t3_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=9, delay_cost=1)
	S += t0_t4 >= 8
	t0_t4 += MM[0]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 8
	t16_t2_in += MAS_in[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 8
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 8
	t16_t2_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	S += t2_t3 >= 8
	t2_t3 += MAS[1]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 9
	t14_t2_in += MAS_in[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 9
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 9
	t14_t2_mem1 += MAIN_MEM_r[1]

	t16_t2 = S.Task('t16_t2', length=2, delay_cost=1)
	S += t16_t2 >= 9
	t16_t2 += MAS[0]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 9
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 9
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 9
	t2_t4_mem1 += MAS_MEM[3]

	t14_t2 = S.Task('t14_t2', length=2, delay_cost=1)
	S += t14_t2 >= 10
	t14_t2 += MAS[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 10
	t17_t2_in += MAS_in[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 10
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 10
	t17_t2_mem1 += MAIN_MEM_r[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 10
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 10
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 10
	t20_mem1 += MM_MEM[1]

	t2_t4 = S.Task('t2_t4', length=9, delay_cost=1)
	S += t2_t4 >= 10
	t2_t4 += MM[0]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 11
	new_TZ_t2_in += MAS_in[2]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 11
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 11
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t17_t2 = S.Task('t17_t2', length=2, delay_cost=1)
	S += t17_t2 >= 11
	t17_t2 += MAS[0]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 11
	t20 += MAS[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 11
	t2_t5_in += MAS_in[4]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 11
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 11
	t2_t5_mem1 += MM_MEM[1]

	new_TZ_t2 = S.Task('new_TZ_t2', length=2, delay_cost=1)
	S += new_TZ_t2 >= 12
	new_TZ_t2 += MAS[2]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 12
	t00_in += MAS_in[3]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 12
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 12
	t00_mem1 += MM_MEM[1]

	t2_t5 = S.Task('t2_t5', length=2, delay_cost=1)
	S += t2_t5 >= 12
	t2_t5 += MAS[4]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 12
	t30_in += MAS_in[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 12
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 12
	t30_mem1 += MAS_MEM[3]

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 13
	t00 += MAS[3]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 13
	t0_t5_in += MAS_in[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 13
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 13
	t0_t5_mem1 += MM_MEM[1]

	t30 = S.Task('t30', length=2, delay_cost=1)
	S += t30 >= 13
	t30 += MAS[2]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 13
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 13
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 13
	t7_t2_mem1 += MAIN_MEM_r[1]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 14
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 14
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 14
	c010_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 14
	t0_t5 += MAS[2]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 14
	t10_in += MAS_in[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += MAS_MEM[7]

	t7_t2 = S.Task('t7_t2', length=2, delay_cost=1)
	S += t7_t2 >= 14
	t7_t2 += MAS[0]

	c010 = S.Task('c010', length=9, delay_cost=1)
	S += c010 >= 15
	c010 += MM[0]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 15
	t10 += MAS[1]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 15
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 15
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 15
	t16_t0_mem1 += MAS_MEM[5]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 16
	t01_in += MAS_in[2]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 16
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 16
	t01_mem1 += MAS_MEM[5]

	t16_t0 = S.Task('t16_t0', length=9, delay_cost=1)
	S += t16_t0 >= 16
	t16_t0 += MM[0]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 16
	t9_t2_in += MAS_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 16
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 16
	t9_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=2, delay_cost=1)
	S += t01 >= 17
	t01 += MAS[2]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 17
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 17
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 17
	t17_t0_mem1 += MAS_MEM[3]

	t9_t2 = S.Task('t9_t2', length=2, delay_cost=1)
	S += t9_t2 >= 17
	t9_t2 += MAS[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 18
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 18
	c200_mem0 += MAS_MEM[2]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 18
	c200_mem1 += MAIN_MEM_r[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 18
	t11_in += MAS_in[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 18
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 18
	t11_mem1 += MAS_MEM[5]

	t17_t0 = S.Task('t17_t0', length=9, delay_cost=1)
	S += t17_t0 >= 18
	t17_t0 += MM[0]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 18
	t21_in += MAS_in[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 18
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 18
	t21_mem1 += MAS_MEM[9]

	c200 = S.Task('c200', length=9, delay_cost=1)
	S += c200 >= 19
	c200 += MM[0]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 19
	t11 += MAS[1]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 19
	t21 += MAS[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 20
	t31_in += MAS_in[3]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 20
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 20
	t31_mem1 += MAS_MEM[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 20
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 20
	t4_t3_mem0 += MAS_MEM[2]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 20
	t4_t3_mem1 += MAS_MEM[3]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 21
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 21
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 21
	c201_mem1 += MAIN_MEM_r[1]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 21
	t31 += MAS[3]

	t4_t3 = S.Task('t4_t3', length=9, delay_cost=1)
	S += t4_t3 >= 21
	t4_t3 += MM[0]

	c201 = S.Task('c201', length=9, delay_cost=1)
	S += c201 >= 22
	c201 += MM[0]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 22
	t4_t1_in += MAS_in[2]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 22
	t4_t1_mem0 += MAS_MEM[2]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 22
	t4_t1_mem1 += MAS_MEM[3]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 22
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 22
	t5_t3_mem0 += MAS_MEM[4]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 22
	t5_t3_mem1 += MAS_MEM[7]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 23
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 23
	c011_mem0 += MAS_MEM[6]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 23
	c011_mem1 += MAIN_MEM_r[1]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 23
	t4_t0_in += MAS_in[4]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 23
	t4_t0_mem0 += MAS_MEM[2]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 23
	t4_t0_mem1 += MAS_MEM[3]

	t4_t1 = S.Task('t4_t1', length=2, delay_cost=1)
	S += t4_t1 >= 23
	t4_t1 += MAS[2]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 23
	t5_t1_in += MAS_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 23
	t5_t1_mem0 += MAS_MEM[4]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 23
	t5_t1_mem1 += MAS_MEM[7]

	t5_t3 = S.Task('t5_t3', length=9, delay_cost=1)
	S += t5_t3 >= 23
	t5_t3 += MM[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 24
	c010_w += MAIN_MEM_w

	c011 = S.Task('c011', length=9, delay_cost=1)
	S += c011 >= 24
	c011 += MM[0]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 24
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 24
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 24
	t17_t1_mem1 += MAS_MEM[3]

	t4_t0 = S.Task('t4_t0', length=2, delay_cost=1)
	S += t4_t0 >= 24
	t4_t0 += MAS[4]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 24
	t5_t0_in += MAS_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 24
	t5_t0_mem0 += MAS_MEM[4]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 24
	t5_t0_mem1 += MAS_MEM[7]

	t5_t1 = S.Task('t5_t1', length=2, delay_cost=1)
	S += t5_t1 >= 24
	t5_t1 += MAS[0]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 25
	new_TX_t2_in += MAS_in[4]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 25
	new_TX_t2_mem0 += MAS_MEM[4]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 25
	new_TX_t2_mem1 += MAS_MEM[7]

	t17_t1 = S.Task('t17_t1', length=9, delay_cost=1)
	S += t17_t1 >= 25
	t17_t1 += MM[0]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 25
	t17_t3_in += MAS_in[3]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 25
	t17_t3_mem0 += MAS_MEM[2]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 25
	t17_t3_mem1 += MAS_MEM[3]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 25
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 25
	t4_t2_mem0 += MAS_MEM[8]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 25
	t4_t2_mem1 += MAS_MEM[5]

	t5_t0 = S.Task('t5_t0', length=2, delay_cost=1)
	S += t5_t0 >= 25
	t5_t0 += MAS[0]

	new_TX_t2 = S.Task('new_TX_t2', length=2, delay_cost=1)
	S += new_TX_t2 >= 26
	new_TX_t2 += MAS[4]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 26
	t13_t2_in += MAS_in[0]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 26
	t13_t2_mem0 += MAS_MEM[2]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 26
	t13_t2_mem1 += MAS_MEM[3]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 26
	t16_t3_in += MAS_in[2]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 26
	t16_t3_mem0 += MAS_MEM[4]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 26
	t16_t3_mem1 += MAS_MEM[7]

	t17_t3 = S.Task('t17_t3', length=2, delay_cost=1)
	S += t17_t3 >= 26
	t17_t3 += MAS[3]

	t4_t2 = S.Task('t4_t2', length=9, delay_cost=1)
	S += t4_t2 >= 26
	t4_t2 += MM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 26
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 26
	t5_t2_mem0 += MAS_MEM[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 26
	t5_t2_mem1 += MAS_MEM[1]

	t13_t2 = S.Task('t13_t2', length=2, delay_cost=1)
	S += t13_t2 >= 27
	t13_t2 += MAS[0]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 27
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 27
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 27
	t16_t1_mem1 += MAS_MEM[7]

	t16_t3 = S.Task('t16_t3', length=2, delay_cost=1)
	S += t16_t3 >= 27
	t16_t3 += MAS[2]

	t5_t2 = S.Task('t5_t2', length=9, delay_cost=1)
	S += t5_t2 >= 27
	t5_t2 += MM[0]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 28
	c200_w += MAIN_MEM_w

	t16_t1 = S.Task('t16_t1', length=9, delay_cost=1)
	S += t16_t1 >= 28
	t16_t1 += MM[0]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 28
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 28
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 28
	t16_t4_mem1 += MAS_MEM[5]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 28
	t6_t2_in += MAS_in[2]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 28
	t6_t2_mem0 += MAS_MEM[4]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 28
	t6_t2_mem1 += MAS_MEM[7]

	t16_t4 = S.Task('t16_t4', length=9, delay_cost=1)
	S += t16_t4 >= 29
	t16_t4 += MM[0]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 29
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 29
	t17_t4_mem0 += MAS_MEM[0]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 29
	t17_t4_mem1 += MAS_MEM[7]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 29
	t41_in += MAS_in[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 29
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 29
	t41_mem1 += MM_MEM[1]

	t6_t2 = S.Task('t6_t2', length=2, delay_cost=1)
	S += t6_t2 >= 29
	t6_t2 += MAS[2]

	t17_t4 = S.Task('t17_t4', length=9, delay_cost=1)
	S += t17_t4 >= 30
	t17_t4 += MM[0]

	t41 = S.Task('t41', length=2, delay_cost=1)
	S += t41 >= 30
	t41 += MAS[1]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 30
	t4_t5_in += MAS_in[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 30
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 30
	t4_t5_mem1 += MM_MEM[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 31
	c201_w += MAIN_MEM_w

	t4_t5 = S.Task('t4_t5', length=2, delay_cost=1)
	S += t4_t5 >= 31
	t4_t5 += MAS[3]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 31
	t51_in += MAS_in[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 31
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 31
	t51_mem1 += MM_MEM[1]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 31
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 31
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 31
	t7_t1_mem1 += MAS_MEM[3]

	t51 = S.Task('t51', length=2, delay_cost=1)
	S += t51 >= 32
	t51 += MAS[0]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 32
	t5_t5_in += MAS_in[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 32
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 32
	t5_t5_mem1 += MM_MEM[1]

	t7_t1 = S.Task('t7_t1', length=9, delay_cost=1)
	S += t7_t1 >= 32
	t7_t1 += MM[0]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 33
	c011_w += MAIN_MEM_w

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 33
	t170_in += MAS_in[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 33
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 33
	t170_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=2, delay_cost=1)
	S += t5_t5 >= 33
	t5_t5 += MAS[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 33
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 33
	t6_t1_mem0 += MAS_MEM[6]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 33
	t6_t1_mem1 += MAS_MEM[1]

	t170 = S.Task('t170', length=2, delay_cost=1)
	S += t170 >= 34
	t170 += MAS[1]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 34
	t40_in += MAS_in[3]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 34
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 34
	t40_mem1 += MAS_MEM[7]

	t6_t1 = S.Task('t6_t1', length=9, delay_cost=1)
	S += t6_t1 >= 34
	t6_t1 += MM[0]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 34
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 34
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 34
	t9_t1_mem1 += MAS_MEM[1]

	t40 = S.Task('t40', length=2, delay_cost=1)
	S += t40 >= 35
	t40 += MAS[3]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 35
	t50_in += MAS_in[4]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 35
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 35
	t50_mem1 += MAS_MEM[1]

	t9_t1 = S.Task('t9_t1', length=9, delay_cost=1)
	S += t9_t1 >= 35
	t9_t1 += MM[0]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 36
	t160_in += MAS_in[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 36
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 36
	t160_mem1 += MM_MEM[1]

	t50 = S.Task('t50', length=2, delay_cost=1)
	S += t50 >= 36
	t50 += MAS[4]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 36
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 36
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 36
	t7_t0_mem1 += MAS_MEM[7]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 36
	t7_t3_in += MAS_in[4]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 36
	t7_t3_mem0 += MAS_MEM[6]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 36
	t7_t3_mem1 += MAS_MEM[3]

	t160 = S.Task('t160', length=2, delay_cost=1)
	S += t160 >= 37
	t160 += MAS[0]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 37
	t17_t5_in += MAS_in[4]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 37
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 37
	t17_t5_mem1 += MM_MEM[1]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 37
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 37
	t6_t0_mem0 += MAS_MEM[4]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 37
	t6_t0_mem1 += MAS_MEM[9]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 37
	t6_t3_in += MAS_in[3]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 37
	t6_t3_mem0 += MAS_MEM[8]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 37
	t6_t3_mem1 += MAS_MEM[1]

	t7_t0 = S.Task('t7_t0', length=9, delay_cost=1)
	S += t7_t0 >= 37
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=2, delay_cost=1)
	S += t7_t3 >= 37
	t7_t3 += MAS[4]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 38
	c000_in += MAS_in[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 38
	c000_mem0 += MAS_MEM[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 38
	c000_mem1 += MAS_MEM[3]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 38
	t16_t5_in += MAS_in[4]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 38
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 38
	t16_t5_mem1 += MM_MEM[1]

	t17_t5 = S.Task('t17_t5', length=2, delay_cost=1)
	S += t17_t5 >= 38
	t17_t5 += MAS[4]

	t6_t0 = S.Task('t6_t0', length=9, delay_cost=1)
	S += t6_t0 >= 38
	t6_t0 += MM[0]

	t6_t3 = S.Task('t6_t3', length=2, delay_cost=1)
	S += t6_t3 >= 38
	t6_t3 += MAS[3]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 38
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 38
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 38
	t9_t0_mem1 += MAS_MEM[9]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 38
	t9_t3_in += MAS_in[3]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 38
	t9_t3_mem0 += MAS_MEM[8]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 38
	t9_t3_mem1 += MAS_MEM[1]

	c000 = S.Task('c000', length=2, delay_cost=1)
	S += c000 >= 39
	c000 += MAS[0]

	t16_t5 = S.Task('t16_t5', length=2, delay_cost=1)
	S += t16_t5 >= 39
	t16_t5 += MAS[4]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 39
	t171_in += MAS_in[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 39
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 39
	t171_mem1 += MAS_MEM[9]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 39
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 39
	t6_t4_mem0 += MAS_MEM[4]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 39
	t6_t4_mem1 += MAS_MEM[7]

	t9_t0 = S.Task('t9_t0', length=9, delay_cost=1)
	S += t9_t0 >= 39
	t9_t0 += MM[0]

	t9_t3 = S.Task('t9_t3', length=2, delay_cost=1)
	S += t9_t3 >= 39
	t9_t3 += MAS[3]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 40
	t161_in += MAS_in[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 40
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 40
	t161_mem1 += MAS_MEM[9]

	t171 = S.Task('t171', length=2, delay_cost=1)
	S += t171 >= 40
	t171 += MAS[3]

	t6_t4 = S.Task('t6_t4', length=9, delay_cost=1)
	S += t6_t4 >= 40
	t6_t4 += MM[0]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 40
	t9_t4_in += MM_in[0]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 40
	t9_t4_mem0 += MAS_MEM[0]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 40
	t9_t4_mem1 += MAS_MEM[7]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 41
	c000_w += MAIN_MEM_w

	t161 = S.Task('t161', length=2, delay_cost=1)
	S += t161 >= 41
	t161 += MAS[0]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 41
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 41
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 41
	t7_t4_mem1 += MAS_MEM[9]

	t9_t4 = S.Task('t9_t4', length=9, delay_cost=1)
	S += t9_t4 >= 41
	t9_t4 += MM[0]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 42
	c001_in += MAS_in[3]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 42
	c001_mem0 += MAS_MEM[0]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 42
	c001_mem1 += MAS_MEM[7]

	t7_t4 = S.Task('t7_t4', length=9, delay_cost=1)
	S += t7_t4 >= 42
	t7_t4 += MM[0]

	c001 = S.Task('c001', length=2, delay_cost=1)
	S += c001 >= 43
	c001 += MAS[3]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 45
	c001_w += MAIN_MEM_w

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 45
	t70_in += MAS_in[4]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 45
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 45
	t70_mem1 += MM_MEM[1]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 46
	t6_t5_in += MAS_in[0]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 46
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 46
	t6_t5_mem1 += MM_MEM[1]

	t70 = S.Task('t70', length=2, delay_cost=1)
	S += t70 >= 46
	t70 += MAS[4]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 47
	t60_in += MAS_in[3]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 47
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 47
	t60_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=2, delay_cost=1)
	S += t6_t5 >= 47
	t6_t5 += MAS[0]

	t60 = S.Task('t60', length=2, delay_cost=1)
	S += t60 >= 48
	t60 += MAS[3]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 48
	t61_in += MAS_in[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 48
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 48
	t61_mem1 += MAS_MEM[1]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 49
	new_TZ_t0_in += MM_in[0]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 49
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 49
	new_TZ_t0_mem1 += MAS_MEM[7]

	t61 = S.Task('t61', length=2, delay_cost=1)
	S += t61 >= 49
	t61 += MAS[0]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 49
	t80_in += MAS_in[1]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 49
	t80_mem0 += MAS_MEM[6]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 49
	t80_mem1 += MAS_MEM[9]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 49
	t90_in += MAS_in[4]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 49
	t90_mem0 += MM_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 49
	t90_mem1 += MM_MEM[1]

	new_TZ_t0 = S.Task('new_TZ_t0', length=9, delay_cost=1)
	S += new_TZ_t0 >= 50
	new_TZ_t0 += MM[0]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 50
	new_TZ_t1_in += MM_in[0]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 50
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 50
	new_TZ_t1_mem1 += MAS_MEM[1]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 50
	t7_t5_in += MAS_in[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 50
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 50
	t7_t5_mem1 += MM_MEM[1]

	t80 = S.Task('t80', length=2, delay_cost=1)
	S += t80 >= 50
	t80 += MAS[1]

	t90 = S.Task('t90', length=2, delay_cost=1)
	S += t90 >= 50
	t90 += MAS[4]

	new_TZ_t1 = S.Task('new_TZ_t1', length=9, delay_cost=1)
	S += new_TZ_t1 >= 51
	new_TZ_t1 += MM[0]

	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	S += new_TZ_t3_in >= 51
	new_TZ_t3_in += MAS_in[1]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 51
	new_TZ_t3_mem0 += MAS_MEM[6]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 51
	new_TZ_t3_mem1 += MAS_MEM[1]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 51
	t100_in += MAS_in[2]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 51
	t100_mem0 += MAS_MEM[8]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 51
	t100_mem1 += MAS_MEM[9]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 51
	t14_t0_in += MM_in[0]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 51
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 51
	t14_t0_mem1 += MAS_MEM[7]

	t7_t5 = S.Task('t7_t5', length=2, delay_cost=1)
	S += t7_t5 >= 51
	t7_t5 += MAS[1]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 51
	t9_t5_in += MAS_in[3]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 51
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 51
	t9_t5_mem1 += MM_MEM[1]

	new_TZ_t3 = S.Task('new_TZ_t3', length=2, delay_cost=1)
	S += new_TZ_t3 >= 52
	new_TZ_t3 += MAS[1]

	t100 = S.Task('t100', length=2, delay_cost=1)
	S += t100 >= 52
	t100 += MAS[2]

	t14_t0 = S.Task('t14_t0', length=9, delay_cost=1)
	S += t14_t0 >= 52
	t14_t0 += MM[0]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 52
	t14_t1_in += MM_in[0]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 52
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 52
	t14_t1_mem1 += MAS_MEM[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 52
	t71_in += MAS_in[2]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 52
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 52
	t71_mem1 += MAS_MEM[3]

	t9_t5 = S.Task('t9_t5', length=2, delay_cost=1)
	S += t9_t5 >= 52
	t9_t5 += MAS[3]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 53
	new_TZ_t4_in += MM_in[0]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 53
	new_TZ_t4_mem0 += MAS_MEM[4]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 53
	new_TZ_t4_mem1 += MAS_MEM[3]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 53
	t110_in += MAS_in[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 53
	t110_mem0 += MAS_MEM[2]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 53
	t110_mem1 += MAS_MEM[5]

	t14_t1 = S.Task('t14_t1', length=9, delay_cost=1)
	S += t14_t1 >= 53
	t14_t1 += MM[0]

	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	S += t14_t3_in >= 53
	t14_t3_in += MAS_in[2]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 53
	t14_t3_mem0 += MAS_MEM[6]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 53
	t14_t3_mem1 += MAS_MEM[1]

	t71 = S.Task('t71', length=2, delay_cost=1)
	S += t71 >= 53
	t71 += MAS[2]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 53
	t91_in += MAS_in[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 53
	t91_mem0 += MM_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 53
	t91_mem1 += MAS_MEM[7]

	new_TZ_t4 = S.Task('new_TZ_t4', length=9, delay_cost=1)
	S += new_TZ_t4 >= 54
	new_TZ_t4 += MM[0]

	t110 = S.Task('t110', length=2, delay_cost=1)
	S += t110 >= 54
	t110 += MAS[1]

	t14_t3 = S.Task('t14_t3', length=2, delay_cost=1)
	S += t14_t3 >= 54
	t14_t3 += MAS[2]

	t91 = S.Task('t91', length=2, delay_cost=1)
	S += t91 >= 54
	t91 += MAS[3]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 55
	t101_in += MAS_in[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 55
	t101_mem0 += MAS_MEM[6]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 55
	t101_mem1 += MAS_MEM[7]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 55
	t120_in += MAS_in[2]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 55
	t120_mem0 += MAS_MEM[2]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 55
	t120_mem1 += MAS_MEM[9]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 55
	t14_t4_in += MM_in[0]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 55
	t14_t4_mem0 += MAS_MEM[0]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 55
	t14_t4_mem1 += MAS_MEM[5]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 56
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 56
	new_TX_t0_mem0 += MAS_MEM[4]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 56
	new_TX_t0_mem1 += MAS_MEM[3]

	t101 = S.Task('t101', length=2, delay_cost=1)
	S += t101 >= 56
	t101 += MAS[0]

	t120 = S.Task('t120', length=2, delay_cost=1)
	S += t120 >= 56
	t120 += MAS[2]

	t14_t4 = S.Task('t14_t4', length=9, delay_cost=1)
	S += t14_t4 >= 56
	t14_t4 += MM[0]

	new_TX_t0 = S.Task('new_TX_t0', length=9, delay_cost=1)
	S += new_TX_t0 >= 57
	new_TX_t0 += MM[0]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 57
	t13_t0_in += MM_in[0]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 57
	t13_t0_mem0 += MAS_MEM[2]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 57
	t13_t0_mem1 += MAS_MEM[5]

	t13_t0 = S.Task('t13_t0', length=9, delay_cost=1)
	S += t13_t0 >= 58
	t13_t0 += MM[0]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 59
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 59
	new_TX_t1_mem0 += MAS_MEM[6]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 59
	new_TX_t1_mem1 += MAS_MEM[9]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 59
	new_TZ0_in += MAS_in[2]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 59
	new_TZ0_mem0 += MM_MEM[0]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 59
	new_TZ0_mem1 += MM_MEM[1]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 59
	t121_in += MAS_in[4]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 59
	t121_mem0 += MAS_MEM[8]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 59
	t121_mem1 += MAS_MEM[7]

	new_TX_t1 = S.Task('new_TX_t1', length=9, delay_cost=1)
	S += new_TX_t1 >= 60
	new_TX_t1 += MM[0]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 60
	new_TX_t3_in += MAS_in[3]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 60
	new_TX_t3_mem0 += MAS_MEM[2]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 60
	new_TX_t3_mem1 += MAS_MEM[9]

	new_TZ0 = S.Task('new_TZ0', length=2, delay_cost=1)
	S += new_TZ0 >= 60
	new_TZ0 += MAS[2]

	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	S += new_TZ_t5_in >= 60
	new_TZ_t5_in += MAS_in[1]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 60
	new_TZ_t5_mem0 += MM_MEM[0]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 60
	new_TZ_t5_mem1 += MM_MEM[1]

	t121 = S.Task('t121', length=2, delay_cost=1)
	S += t121 >= 60
	t121 += MAS[4]

	new_TX_t3 = S.Task('new_TX_t3', length=2, delay_cost=1)
	S += new_TX_t3 >= 61
	new_TX_t3 += MAS[3]

	new_TZ_t5 = S.Task('new_TZ_t5', length=2, delay_cost=1)
	S += new_TZ_t5 >= 61
	new_TZ_t5 += MAS[1]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 61
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 61
	t13_t1_mem0 += MAS_MEM[2]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 61
	t13_t1_mem1 += MAS_MEM[9]

	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	S += t14_t5_in >= 61
	t14_t5_in += MAS_in[1]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 61
	t14_t5_mem0 += MM_MEM[0]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 61
	t14_t5_mem1 += MM_MEM[1]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 62
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 62
	new_TX_t4_mem0 += MAS_MEM[8]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 62
	new_TX_t4_mem1 += MAS_MEM[7]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 62
	new_TZ0_w += MAIN_MEM_w

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 62
	new_TZ1_in += MAS_in[2]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 62
	new_TZ1_mem0 += MM_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 62
	new_TZ1_mem1 += MAS_MEM[3]

	t13_t1 = S.Task('t13_t1', length=9, delay_cost=1)
	S += t13_t1 >= 62
	t13_t1 += MM[0]

	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	S += t13_t3_in >= 62
	t13_t3_in += MAS_in[3]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 62
	t13_t3_mem0 += MAS_MEM[4]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 62
	t13_t3_mem1 += MAS_MEM[9]

	t14_t5 = S.Task('t14_t5', length=2, delay_cost=1)
	S += t14_t5 >= 62
	t14_t5 += MAS[1]

	new_TX_t4 = S.Task('new_TX_t4', length=9, delay_cost=1)
	S += new_TX_t4 >= 63
	new_TX_t4 += MM[0]

	new_TZ1 = S.Task('new_TZ1', length=2, delay_cost=1)
	S += new_TZ1 >= 63
	new_TZ1 += MAS[2]

	t13_t3 = S.Task('t13_t3', length=2, delay_cost=1)
	S += t13_t3 >= 63
	t13_t3 += MAS[3]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 63
	t140_in += MAS_in[2]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 63
	t140_mem0 += MM_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 63
	t140_mem1 += MM_MEM[1]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 64
	t13_t4_in += MM_in[0]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 64
	t13_t4_mem0 += MAS_MEM[0]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 64
	t13_t4_mem1 += MAS_MEM[7]

	t140 = S.Task('t140', length=2, delay_cost=1)
	S += t140 >= 64
	t140 += MAS[2]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 64
	t141_in += MAS_in[2]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 64
	t141_mem0 += MM_MEM[0]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 64
	t141_mem1 += MAS_MEM[3]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 65
	new_TZ1_w += MAIN_MEM_w

	t13_t4 = S.Task('t13_t4', length=9, delay_cost=1)
	S += t13_t4 >= 65
	t13_t4 += MM[0]

	t141 = S.Task('t141', length=2, delay_cost=1)
	S += t141 >= 65
	t141 += MAS[2]

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 68
	new_TX0_in += MAS_in[2]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 68
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 68
	new_TX0_mem1 += MM_MEM[1]

	new_TX0 = S.Task('new_TX0', length=2, delay_cost=1)
	S += new_TX0 >= 69
	new_TX0 += MAS[2]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 69
	new_TX_t5_in += MAS_in[4]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 69
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 69
	new_TX_t5_mem1 += MM_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=2, delay_cost=1)
	S += new_TX_t5 >= 70
	new_TX_t5 += MAS[4]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 70
	t130_in += MAS_in[2]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 70
	t130_mem0 += MM_MEM[0]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 70
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 71
	new_TX0_w += MAIN_MEM_w

	t130 = S.Task('t130', length=2, delay_cost=1)
	S += t130 >= 71
	t130 += MAS[2]

	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	S += t13_t5_in >= 71
	t13_t5_in += MAS_in[1]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 71
	t13_t5_mem0 += MM_MEM[0]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 71
	t13_t5_mem1 += MM_MEM[1]

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 72
	new_TX1_in += MAS_in[2]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 72
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 72
	new_TX1_mem1 += MAS_MEM[9]

	t13_t5 = S.Task('t13_t5', length=2, delay_cost=1)
	S += t13_t5 >= 72
	t13_t5 += MAS[1]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 72
	t150_in += MAS_in[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 72
	t150_mem0 += MAS_MEM[4]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 72
	t150_mem1 += MAS_MEM[5]

	new_TX1 = S.Task('new_TX1', length=2, delay_cost=1)
	S += new_TX1 >= 73
	new_TX1 += MAS[2]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 73
	t131_in += MAS_in[2]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 73
	t131_mem0 += MM_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 73
	t131_mem1 += MAS_MEM[3]

	t150 = S.Task('t150', length=2, delay_cost=1)
	S += t150 >= 73
	t150 += MAS[1]

	t131 = S.Task('t131', length=2, delay_cost=1)
	S += t131 >= 74
	t131 += MAS[2]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 75
	new_TX1_w += MAIN_MEM_w


	# new tasks
	t81 = S.Task('t81', length=2, delay_cost=1)
	t81 += alt(MAS)
	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	t81_in += alt(MAS_in)
	S += t81_in*MAS_in[0]<=t81*MAS[0]

	S += t81_in*MAS_in[1]<=t81*MAS[1]

	S += t81_in*MAS_in[2]<=t81*MAS[2]

	S += t81_in*MAS_in[3]<=t81*MAS[3]

	S += t81_in*MAS_in[4]<=t81*MAS[4]

	S += t81<58

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += MAS_MEM[0]
	S += 50 < t81_mem0
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += MAS_MEM[5]
	S += 54 < t81_mem1
	S += t81_mem1 <= t81

	t111 = S.Task('t111', length=2, delay_cost=1)
	t111 += alt(MAS)
	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	t111_in += alt(MAS_in)
	S += t111_in*MAS_in[0]<=t111*MAS[0]

	S += t111_in*MAS_in[1]<=t111*MAS[1]

	S += t111_in*MAS_in[2]<=t111*MAS[2]

	S += t111_in*MAS_in[3]<=t111*MAS[3]

	S += t111_in*MAS_in[4]<=t111*MAS[4]

	S += t111<60

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t111_mem0*MAS_MEM[0]
	S += (t81*MAS[1])-1 < t111_mem0*MAS_MEM[2]
	S += (t81*MAS[2])-1 < t111_mem0*MAS_MEM[4]
	S += (t81*MAS[3])-1 < t111_mem0*MAS_MEM[6]
	S += (t81*MAS[4])-1 < t111_mem0*MAS_MEM[8]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += MAS_MEM[1]
	S += 57 < t111_mem1
	S += t111_mem1 <= t111

	t151 = S.Task('t151', length=2, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	S += t151_in*MAS_in[1]<=t151*MAS[1]

	S += t151_in*MAS_in[2]<=t151*MAS[2]

	S += t151_in*MAS_in[3]<=t151*MAS[3]

	S += t151_in*MAS_in[4]<=t151*MAS[4]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[4]
	S += 75 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[5]
	S += 66 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=2, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += new_TY0_in*MAS_in[1]<=new_TY0*MAS[1]

	S += new_TY0_in*MAS_in[2]<=new_TY0*MAS[2]

	S += new_TY0_in*MAS_in[3]<=new_TY0*MAS[3]

	S += new_TY0_in*MAS_in[4]<=new_TY0*MAS[4]

	S += 52<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[3]
	S += 74 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=2, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += new_TY1_in*MAS_in[1]<=new_TY1*MAS[1]

	S += new_TY1_in*MAS_in[2]<=new_TY1*MAS[2]

	S += new_TY1_in*MAS_in[3]<=new_TY1*MAS[3]

	S += new_TY1_in*MAS_in[4]<=new_TY1*MAS[4]

	S += 53<new_TY1

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
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS5/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

