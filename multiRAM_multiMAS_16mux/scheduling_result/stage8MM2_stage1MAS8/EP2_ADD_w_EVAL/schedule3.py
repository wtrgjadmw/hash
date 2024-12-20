from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 181
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=8)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 0
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 0
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 0
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t0 = S.Task('t0_t0', length=8, delay_cost=1)
	S += t0_t0 >= 1
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 1
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 1
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 1
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=8, delay_cost=1)
	S += t0_t1 >= 2
	t0_t1 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 2
	t2_t1_in += MM_in[0]

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

	t2_t1 = S.Task('t2_t1', length=8, delay_cost=1)
	S += t2_t1 >= 3
	t2_t1 += MM[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 4
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 4
	t0_t2_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=8, delay_cost=1)
	S += t2_t0 >= 4
	t2_t0 += MM[0]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 5
	t0_t2 += MAS[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 5
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 5
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 6
	t0_t3 += MAS[5]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 6
	t0_t4_in += MM_in[1]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 6
	t0_t4_mem0 += MAS_MEM[0]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 6
	t0_t4_mem1 += MAS_MEM[11]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 6
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 6
	t2_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=8, delay_cost=1)
	S += t0_t4 >= 7
	t0_t4 += MM[1]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 7
	t2_t2 += MAS[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 7
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 7
	t2_t3_mem1 += MAIN_MEM_r[1]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 8
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 8
	t17_t2_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 8
	t2_t3 += MAS[6]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[1]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[13]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 9
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 9
	t00_mem1 += MM_MEM[1]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 9
	t17_t2 += MAS[4]

	t2_t4 = S.Task('t2_t4', length=8, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[1]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 9
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 9
	t7_t2_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 10
	t00 += MAS[4]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 10
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 10
	t0_t5_mem1 += MM_MEM[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 10
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 10
	t10_mem1 += MAS_MEM[9]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 10
	t7_t2 += MAS[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 11
	c200_in += MM_in[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 11
	c200_mem0 += MAS_MEM[6]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 11
	c200_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 11
	t0_t5 += MAS[6]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 11
	t10 += MAS[3]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 11
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 11
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 11
	t17_t0_mem1 += MAS_MEM[7]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 11
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 11
	t20_mem1 += MM_MEM[1]

	c200 = S.Task('c200', length=8, delay_cost=1)
	S += c200 >= 12
	c200 += MM[1]

	t17_t0 = S.Task('t17_t0', length=8, delay_cost=1)
	S += t17_t0 >= 12
	t17_t0 += MM[0]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 12
	t20 += MAS[4]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 12
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 12
	t2_t5_mem1 += MM_MEM[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 12
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 12
	t30_mem1 += MAS_MEM[9]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 13
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 13
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 13
	c010_mem1 += MAIN_MEM_r[1]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 13
	t16_t0_in += MM_in[1]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 13
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 13
	t16_t0_mem1 += MAS_MEM[5]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 13
	t2_t5 += MAS[1]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 13
	t30 += MAS[2]

	c010 = S.Task('c010', length=8, delay_cost=1)
	S += c010 >= 14
	c010 += MM[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 14
	t01_mem0 += MM_MEM[2]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 14
	t01_mem1 += MAS_MEM[13]

	t16_t0 = S.Task('t16_t0', length=8, delay_cost=1)
	S += t16_t0 >= 14
	t16_t0 += MM[1]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 14
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 14
	t9_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 15
	t01 += MAS[6]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 15
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 15
	t11_mem1 += MAS_MEM[13]

	t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
	S += t9_t2 >= 15
	t9_t2 += MAS[4]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 16
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 16
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 16
	t11 += MAS[7]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 16
	t21_mem0 += MM_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 16
	t21_mem1 += MAS_MEM[3]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 16
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 16
	t4_t3_mem0 += MAS_MEM[6]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 16
	t4_t3_mem1 += MAS_MEM[15]

	new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
	S += new_TZ_t2 >= 17
	new_TZ_t2 += MAS[5]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 17
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 17
	t16_t2_mem1 += MAIN_MEM_r[1]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 17
	t21 += MAS[2]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 17
	t4_t0_mem0 += MAS_MEM[6]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 17
	t4_t0_mem1 += MAS_MEM[15]

	t4_t3 = S.Task('t4_t3', length=8, delay_cost=1)
	S += t4_t3 >= 17
	t4_t3 += MM[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 18
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 18
	t14_t2_mem1 += MAIN_MEM_r[1]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 18
	t16_t2 += MAS[7]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 18
	t4_t0 += MAS[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 18
	t4_t1_mem0 += MAS_MEM[6]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 18
	t4_t1_mem1 += MAS_MEM[15]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 19
	c201_in += MM_in[1]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 19
	c201_mem0 += MAS_MEM[14]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 19
	c201_mem1 += MAIN_MEM_r[1]

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 19
	t14_t2 += MAS[4]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 19
	t17_t3_mem0 += MAS_MEM[6]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 19
	t17_t3_mem1 += MAS_MEM[15]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 19
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 19
	t31_mem1 += MAS_MEM[5]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 19
	t4_t1 += MAS[0]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 19
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 19
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 19
	t4_t2_mem1 += MAS_MEM[1]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 20
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 20
	c011_mem0 += MAS_MEM[14]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 20
	c011_mem1 += MAIN_MEM_r[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 20
	c200_w += MAIN_MEM_w

	c201 = S.Task('c201', length=8, delay_cost=1)
	S += c201 >= 20
	c201 += MM[1]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 20
	t17_t3 += MAS[2]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 20
	t31 += MAS[7]

	t4_t2 = S.Task('t4_t2', length=8, delay_cost=1)
	S += t4_t2 >= 20
	t4_t2 += MM[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 20
	t5_t3_in += MM_in[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 20
	t5_t3_mem0 += MAS_MEM[4]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 20
	t5_t3_mem1 += MAS_MEM[15]

	c011 = S.Task('c011', length=8, delay_cost=1)
	S += c011 >= 21
	c011 += MM[0]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 21
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 21
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 21
	t17_t1_mem1 += MAS_MEM[15]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 21
	t17_t4_in += MM_in[1]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 21
	t17_t4_mem0 += MAS_MEM[8]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 21
	t17_t4_mem1 += MAS_MEM[5]

	t5_t3 = S.Task('t5_t3', length=8, delay_cost=1)
	S += t5_t3 >= 21
	t5_t3 += MM[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 22
	c010_w += MAIN_MEM_w

	t17_t1 = S.Task('t17_t1', length=8, delay_cost=1)
	S += t17_t1 >= 22
	t17_t1 += MM[0]

	t17_t4 = S.Task('t17_t4', length=8, delay_cost=1)
	S += t17_t4 >= 22
	t17_t4 += MM[1]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 22
	t5_t0_mem0 += MAS_MEM[4]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 22
	t5_t0_mem1 += MAS_MEM[15]

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	S += t5_t0 >= 23
	t5_t0 += MAS[3]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 23
	t5_t1_mem0 += MAS_MEM[4]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 23
	t5_t1_mem1 += MAS_MEM[15]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 24
	t16_t1_in += MM_in[1]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 24
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 24
	t16_t1_mem1 += MAS_MEM[15]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 24
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 24
	t41_mem1 += MM_MEM[1]

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	S += t5_t1 >= 24
	t5_t1 += MAS[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 24
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 24
	t5_t2_mem0 += MAS_MEM[6]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 24
	t5_t2_mem1 += MAS_MEM[7]

	t16_t1 = S.Task('t16_t1', length=8, delay_cost=1)
	S += t16_t1 >= 25
	t16_t1 += MM[1]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 25
	t16_t3_mem0 += MAS_MEM[4]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 25
	t16_t3_mem1 += MAS_MEM[15]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 25
	t41 += MAS[0]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 25
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 25
	t4_t5_mem1 += MM_MEM[1]

	t5_t2 = S.Task('t5_t2', length=8, delay_cost=1)
	S += t5_t2 >= 25
	t5_t2 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 25
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 25
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 25
	t7_t1_mem1 += MAS_MEM[1]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 26
	new_TX_t2_mem0 += MAS_MEM[4]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 26
	new_TX_t2_mem1 += MAS_MEM[15]

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	S += t16_t3 >= 26
	t16_t3 += MAS[3]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 26
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 26
	t16_t4_mem0 += MAS_MEM[14]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 26
	t16_t4_mem1 += MAS_MEM[7]

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 26
	t4_t5 += MAS[6]

	t7_t1 = S.Task('t7_t1', length=8, delay_cost=1)
	S += t7_t1 >= 26
	t7_t1 += MM[1]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 27
	new_TX_t2 += MAS[4]

	t16_t4 = S.Task('t16_t4', length=8, delay_cost=1)
	S += t16_t4 >= 27
	t16_t4 += MM[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 27
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 27
	t40_mem1 += MAS_MEM[13]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 27
	t6_t2_mem0 += MAS_MEM[4]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 27
	t6_t2_mem1 += MAS_MEM[15]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 28
	c201_w += MAIN_MEM_w

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 28
	t13_t2_mem0 += MAS_MEM[6]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 28
	t13_t2_mem1 += MAS_MEM[15]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 28
	t40 += MAS[4]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 28
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 28
	t51_mem1 += MM_MEM[3]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 28
	t6_t2 += MAS[2]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 28
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 28
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 28
	t7_t0_mem1 += MAS_MEM[9]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 28
	t7_t3_mem0 += MAS_MEM[8]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 28
	t7_t3_mem1 += MAS_MEM[1]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 29
	c011_w += MAIN_MEM_w

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	S += t13_t2 >= 29
	t13_t2 += MAS[7]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 29
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 29
	t17_t5_mem1 += MM_MEM[1]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 29
	t51 += MAS[6]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 29
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 29
	t5_t5_mem1 += MM_MEM[3]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 29
	t6_t1_in += MM_in[1]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 29
	t6_t1_mem0 += MAS_MEM[14]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 29
	t6_t1_mem1 += MAS_MEM[13]

	t7_t0 = S.Task('t7_t0', length=8, delay_cost=1)
	S += t7_t0 >= 29
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 29
	t7_t3 += MAS[0]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 29
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 29
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 29
	t7_t4_mem1 += MAS_MEM[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 30
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 30
	t170_mem1 += MM_MEM[1]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 30
	t171_mem0 += MM_MEM[2]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 30
	t171_mem1 += MAS_MEM[15]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 30
	t17_t5 += MAS[7]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 30
	t5_t5 += MAS[6]

	t6_t1 = S.Task('t6_t1', length=8, delay_cost=1)
	S += t6_t1 >= 30
	t6_t1 += MM[1]

	t7_t4 = S.Task('t7_t4', length=8, delay_cost=1)
	S += t7_t4 >= 30
	t7_t4 += MM[0]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 30
	t9_t1_in += MM_in[1]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 30
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 30
	t9_t1_mem1 += MAS_MEM[13]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 31
	t170 += MAS[7]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 31
	t171 += MAS[5]

	t9_t1 = S.Task('t9_t1', length=8, delay_cost=1)
	S += t9_t1 >= 31
	t9_t1 += MM[1]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 32
	t160_mem0 += MM_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 32
	t160_mem1 += MM_MEM[3]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 32
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 32
	t50_mem1 += MAS_MEM[13]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 33
	c000_mem0 += MAS_MEM[14]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 33
	c000_mem1 += MAS_MEM[15]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 33
	t160 += MAS[7]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 33
	t16_t5_mem0 += MM_MEM[2]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 33
	t16_t5_mem1 += MM_MEM[3]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 33
	t50 += MAS[5]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 33
	t6_t0_in += MM_in[1]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 33
	t6_t0_mem0 += MAS_MEM[4]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 33
	t6_t0_mem1 += MAS_MEM[11]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 33
	t6_t3_mem0 += MAS_MEM[10]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 33
	t6_t3_mem1 += MAS_MEM[13]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 34
	c000 += MAS[2]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 34
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 34
	t161_mem1 += MAS_MEM[3]

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	S += t16_t5 >= 34
	t16_t5 += MAS[1]

	t6_t0 = S.Task('t6_t0', length=8, delay_cost=1)
	S += t6_t0 >= 34
	t6_t0 += MM[1]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 34
	t6_t3 += MAS[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 34
	t6_t4_in += MM_in[1]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 34
	t6_t4_mem0 += MAS_MEM[4]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 34
	t6_t4_mem1 += MAS_MEM[1]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 34
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 34
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 34
	t9_t0_mem1 += MAS_MEM[11]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 34
	t9_t3_mem0 += MAS_MEM[10]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 34
	t9_t3_mem1 += MAS_MEM[13]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 35
	c000_w += MAIN_MEM_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 35
	c001_mem0 += MAS_MEM[14]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 35
	c001_mem1 += MAS_MEM[11]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 35
	t161 += MAS[7]

	t6_t4 = S.Task('t6_t4', length=8, delay_cost=1)
	S += t6_t4 >= 35
	t6_t4 += MM[1]

	t9_t0 = S.Task('t9_t0', length=8, delay_cost=1)
	S += t9_t0 >= 35
	t9_t0 += MM[0]

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	S += t9_t3 >= 35
	t9_t3 += MAS[5]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 36
	c001 += MAS[2]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 36
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 36
	t7_t5_mem1 += MM_MEM[3]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 36
	t9_t4_in += MM_in[1]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 36
	t9_t4_mem0 += MAS_MEM[8]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 36
	t9_t4_mem1 += MAS_MEM[11]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 37
	c001_w += MAIN_MEM_w

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 37
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 37
	t71_mem1 += MAS_MEM[9]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 37
	t7_t5 += MAS[4]

	t9_t4 = S.Task('t9_t4', length=8, delay_cost=1)
	S += t9_t4 >= 37
	t9_t4 += MM[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 38
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 38
	t70_mem1 += MM_MEM[3]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 38
	t71 += MAS[3]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 39
	t70 += MAS[7]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 41
	t6_t5_mem0 += MM_MEM[2]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 41
	t6_t5_mem1 += MM_MEM[3]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 42
	t61_mem0 += MM_MEM[2]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 42
	t61_mem1 += MAS_MEM[15]

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	S += t6_t5 >= 42
	t6_t5 += MAS[7]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 42
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 42
	t9_t5_mem1 += MM_MEM[3]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 43
	t14_t1_in += MM_in[1]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 43
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 43
	t14_t1_mem1 += MAS_MEM[3]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 43
	t60_mem0 += MM_MEM[2]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 43
	t60_mem1 += MM_MEM[3]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 43
	t61 += MAS[1]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 43
	t81_mem0 += MAS_MEM[2]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 43
	t81_mem1 += MAS_MEM[7]

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	S += t9_t5 >= 43
	t9_t5 += MAS[4]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 44
	t14_t0_in += MM_in[0]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 44
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 44
	t14_t0_mem1 += MAS_MEM[11]

	t14_t1 = S.Task('t14_t1', length=8, delay_cost=1)
	S += t14_t1 >= 44
	t14_t1 += MM[1]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 44
	t14_t3_mem0 += MAS_MEM[10]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 44
	t14_t3_mem1 += MAS_MEM[3]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 44
	t60 += MAS[5]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 44
	t81 += MAS[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 44
	t90_mem0 += MM_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 44
	t90_mem1 += MM_MEM[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 44
	t91_mem0 += MM_MEM[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 44
	t91_mem1 += MAS_MEM[9]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 45
	new_TZ_t1_in += MM_in[0]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 45
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 45
	new_TZ_t1_mem1 += MAS_MEM[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 45
	t100_mem0 += MAS_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 45
	t100_mem1 += MAS_MEM[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 45
	t101_mem0 += MAS_MEM[4]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 45
	t101_mem1 += MAS_MEM[5]

	t14_t0 = S.Task('t14_t0', length=8, delay_cost=1)
	S += t14_t0 >= 45
	t14_t0 += MM[0]

	t14_t3 = S.Task('t14_t3', length=1, delay_cost=1)
	S += t14_t3 >= 45
	t14_t3 += MAS[5]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 45
	t14_t4_in += MM_in[1]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 45
	t14_t4_mem0 += MAS_MEM[8]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 45
	t14_t4_mem1 += MAS_MEM[11]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 45
	t80_mem0 += MAS_MEM[10]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 45
	t80_mem1 += MAS_MEM[15]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 45
	t90 += MAS[0]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 45
	t91 += MAS[2]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 46
	new_TZ_t0_in += MM_in[1]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 46
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 46
	new_TZ_t0_mem1 += MAS_MEM[11]

	new_TZ_t1 = S.Task('new_TZ_t1', length=8, delay_cost=1)
	S += new_TZ_t1 >= 46
	new_TZ_t1 += MM[0]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 46
	new_TZ_t3_mem0 += MAS_MEM[10]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 46
	new_TZ_t3_mem1 += MAS_MEM[3]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 46
	t100 += MAS[7]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 46
	t101 += MAS[3]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 46
	t110_mem0 += MAS_MEM[8]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 46
	t110_mem1 += MAS_MEM[15]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 46
	t111_mem0 += MAS_MEM[4]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 46
	t111_mem1 += MAS_MEM[7]

	t14_t4 = S.Task('t14_t4', length=8, delay_cost=1)
	S += t14_t4 >= 46
	t14_t4 += MM[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 46
	t80 += MAS[4]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 47
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 47
	new_TX_t0_mem0 += MAS_MEM[4]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 47
	new_TX_t0_mem1 += MAS_MEM[11]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 47
	new_TX_t1_in += MM_in[1]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 47
	new_TX_t1_mem0 += MAS_MEM[14]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 47
	new_TX_t1_mem1 += MAS_MEM[13]

	new_TZ_t0 = S.Task('new_TZ_t0', length=8, delay_cost=1)
	S += new_TZ_t0 >= 47
	new_TZ_t0 += MM[1]

	new_TZ_t3 = S.Task('new_TZ_t3', length=1, delay_cost=1)
	S += new_TZ_t3 >= 47
	new_TZ_t3 += MAS[1]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 47
	t110 += MAS[5]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 47
	t111 += MAS[6]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 47
	t120_mem0 += MAS_MEM[10]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 47
	t120_mem1 += MAS_MEM[1]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 47
	t121_mem0 += MAS_MEM[12]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 47
	t121_mem1 += MAS_MEM[5]

	new_TX_t0 = S.Task('new_TX_t0', length=8, delay_cost=1)
	S += new_TX_t0 >= 48
	new_TX_t0 += MM[0]

	new_TX_t1 = S.Task('new_TX_t1', length=8, delay_cost=1)
	S += new_TX_t1 >= 48
	new_TX_t1 += MM[1]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 48
	new_TX_t3_mem0 += MAS_MEM[10]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 48
	new_TX_t3_mem1 += MAS_MEM[13]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 48
	t120 += MAS[7]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 48
	t121 += MAS[4]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 48
	t13_t0_in += MM_in[1]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 48
	t13_t0_mem0 += MAS_MEM[6]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 48
	t13_t0_mem1 += MAS_MEM[15]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 48
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 48
	t13_t1_mem0 += MAS_MEM[14]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 48
	t13_t1_mem1 += MAS_MEM[9]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 49
	new_TX_t3 += MAS[7]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 49
	new_TX_t4_in += MM_in[1]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 49
	new_TX_t4_mem0 += MAS_MEM[8]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 49
	new_TX_t4_mem1 += MAS_MEM[15]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 49
	new_TZ_t4_in += MM_in[0]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 49
	new_TZ_t4_mem0 += MAS_MEM[10]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 49
	new_TZ_t4_mem1 += MAS_MEM[3]

	t13_t0 = S.Task('t13_t0', length=8, delay_cost=1)
	S += t13_t0 >= 49
	t13_t0 += MM[1]

	t13_t1 = S.Task('t13_t1', length=8, delay_cost=1)
	S += t13_t1 >= 49
	t13_t1 += MM[0]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 49
	t13_t3_mem0 += MAS_MEM[14]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 49
	t13_t3_mem1 += MAS_MEM[9]

	new_TX_t4 = S.Task('new_TX_t4', length=8, delay_cost=1)
	S += new_TX_t4 >= 50
	new_TX_t4 += MM[1]

	new_TZ_t4 = S.Task('new_TZ_t4', length=8, delay_cost=1)
	S += new_TZ_t4 >= 50
	new_TZ_t4 += MM[0]

	t13_t3 = S.Task('t13_t3', length=1, delay_cost=1)
	S += t13_t3 >= 50
	t13_t3 += MAS[5]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 50
	t13_t4_in += MM_in[0]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 50
	t13_t4_mem0 += MAS_MEM[14]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 50
	t13_t4_mem1 += MAS_MEM[11]

	t13_t4 = S.Task('t13_t4', length=8, delay_cost=1)
	S += t13_t4 >= 51
	t13_t4 += MM[0]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 52
	t14_t5_mem0 += MM_MEM[0]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 52
	t14_t5_mem1 += MM_MEM[3]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 53
	t140_mem0 += MM_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 53
	t140_mem1 += MM_MEM[3]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 53
	t141_mem0 += MM_MEM[2]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 53
	t141_mem1 += MAS_MEM[11]

	t14_t5 = S.Task('t14_t5', length=1, delay_cost=1)
	S += t14_t5 >= 53
	t14_t5 += MAS[5]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 54
	new_TZ0_mem0 += MM_MEM[2]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 54
	new_TZ0_mem1 += MM_MEM[1]

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 54
	t140 += MAS[4]

	t141 = S.Task('t141', length=1, delay_cost=1)
	S += t141 >= 54
	t141 += MAS[5]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 55
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 55
	new_TX0_mem1 += MM_MEM[3]

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	S += new_TZ0 >= 55
	new_TZ0 += MAS[6]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 55
	new_TZ_t5_mem0 += MM_MEM[2]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 55
	new_TZ_t5_mem1 += MM_MEM[1]

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	S += new_TX0 >= 56
	new_TX0 += MAS[5]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 56
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 56
	new_TX_t5_mem1 += MM_MEM[3]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 56
	new_TZ0_w += MAIN_MEM_w

	new_TZ_t5 = S.Task('new_TZ_t5', length=1, delay_cost=1)
	S += new_TZ_t5 >= 56
	new_TZ_t5 += MAS[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 56
	t130_mem0 += MM_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 56
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 57
	new_TX0_w += MAIN_MEM_w

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	S += new_TX_t5 >= 57
	new_TX_t5 += MAS[1]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 57
	new_TZ1_mem0 += MM_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 57
	new_TZ1_mem1 += MAS_MEM[1]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 57
	t130 += MAS[4]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 57
	t13_t5_mem0 += MM_MEM[2]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 57
	t13_t5_mem1 += MM_MEM[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 57
	t150_mem0 += MAS_MEM[8]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 57
	t150_mem1 += MAS_MEM[9]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 58
	new_TX1_mem0 += MM_MEM[2]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 58
	new_TX1_mem1 += MAS_MEM[3]

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	S += new_TZ1 >= 58
	new_TZ1 += MAS[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 58
	t131_mem0 += MM_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 58
	t131_mem1 += MAS_MEM[13]

	t13_t5 = S.Task('t13_t5', length=1, delay_cost=1)
	S += t13_t5 >= 58
	t13_t5 += MAS[6]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 58
	t150 += MAS[1]

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	S += new_TX1 >= 59
	new_TX1 += MAS[3]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 59
	new_TZ1_w += MAIN_MEM_w

	t131 = S.Task('t131', length=1, delay_cost=1)
	S += t131 >= 59
	t131 += MAS[6]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 60
	new_TX1_w += MAIN_MEM_w


	# new tasks
	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)
	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[12]
	S += 59 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[11]
	S += 54 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(MAS)
	S += 45<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[3]
	S += 58 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(MAS)
	S += 44<new_TY1

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

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM2_stage1MAS8/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

