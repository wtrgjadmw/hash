from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 201
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 0
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 0
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 0
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=10, delay_cost=1)
	S += c_t2_t0_t1 >= 1
	c_t2_t0_t1 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 1
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 1
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 1
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 2
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 2
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 2
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=10, delay_cost=1)
	S += c_t2_t1_t1 >= 2
	c_t2_t1_t1 += MM[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 3
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 3
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 3
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=10, delay_cost=1)
	S += c_t2_t0_t0 >= 3
	c_t2_t0_t0 += MM[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=4, delay_cost=1)
	S += c_t0_t1_t2 >= 4
	c_t0_t1_t2 += MAS[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 4
	c_t2_t0_t2_in += MAS_in[4]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 4
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 4
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 5
	c_t1_t21_in += MAS_in[6]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 5
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 5
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=4, delay_cost=1)
	S += c_t2_t0_t2 >= 5
	c_t2_t0_t2 += MAS[4]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 6
	c_t1_t1_t0_in += MM_in[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 6
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 6
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=4, delay_cost=1)
	S += c_t1_t21 >= 6
	c_t1_t21 += MAS[6]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 7
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 7
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 7
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=10, delay_cost=1)
	S += c_t1_t1_t0 >= 7
	c_t1_t1_t0 += MM[1]

	c_t0_t30 = S.Task('c_t0_t30', length=4, delay_cost=1)
	S += c_t0_t30 >= 8
	c_t0_t30 += MAS[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 8
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 8
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 8
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 9
	c_t0_t0_t2_in += MAS_in[6]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 9
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 9
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=10, delay_cost=1)
	S += c_t1_t1_t1 >= 9
	c_t1_t1_t1 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=4, delay_cost=1)
	S += c_t0_t0_t2 >= 10
	c_t0_t0_t2 += MAS[6]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 10
	c_t1_t0_t0_in += MM_in[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 10
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 10
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 11
	c_t0_t20_in += MAS_in[2]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 11
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 11
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=10, delay_cost=1)
	S += c_t1_t0_t0 >= 11
	c_t1_t0_t0 += MM[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 12
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 12
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 12
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=4, delay_cost=1)
	S += c_t0_t20 >= 12
	c_t0_t20 += MAS[2]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 12
	c_t2_t00_in += MAS_in[7]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 12
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 12
	c_t2_t00_mem1 += MM_MEM[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=4, delay_cost=1)
	S += c_t0_t0_t3 >= 13
	c_t0_t0_t3 += MAS[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 13
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 13
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 13
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t00 = S.Task('c_t2_t00', length=4, delay_cost=1)
	S += c_t2_t00 >= 13
	c_t2_t00 += MAS[7]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 13
	c_t2_t0_t5_in += MAS_in[7]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 13
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 13
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 14
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 14
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 14
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=4, delay_cost=1)
	S += c_t1_t30 >= 14
	c_t1_t30 += MAS[0]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=4, delay_cost=1)
	S += c_t2_t0_t5 >= 14
	c_t2_t0_t5 += MAS[7]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 15
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 15
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 15
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 15
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 15
	c_t0_t4_t0_mem0 += MAS_MEM[4]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 15
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=4, delay_cost=1)
	S += c_t1_t1_t2 >= 15
	c_t1_t1_t2 += MAS[0]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 16
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 16
	c_t0_t0_t4_mem0 += MAS_MEM[12]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 16
	c_t0_t0_t4_mem1 += MAS_MEM[1]

	c_t0_t31 = S.Task('c_t0_t31', length=4, delay_cost=1)
	S += c_t0_t31 >= 16
	c_t0_t31 += MAS[0]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=10, delay_cost=1)
	S += c_t0_t4_t0 >= 16
	c_t0_t4_t0 += MM[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 16
	c_t2_t1_t0_in += MM_in[1]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 16
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 16
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=10, delay_cost=1)
	S += c_t0_t0_t4 >= 17
	c_t0_t0_t4 += MM[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 17
	c_t1_t20_in += MAS_in[3]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 17
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 17
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=10, delay_cost=1)
	S += c_t2_t1_t0 >= 17
	c_t2_t1_t0 += MM[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 18
	c_t1_t10_in += MAS_in[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 18
	c_t1_t10_mem0 += MM_MEM[2]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 18
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 18
	c_t1_t1_t3_in += MAS_in[7]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 18
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 18
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=4, delay_cost=1)
	S += c_t1_t20 >= 18
	c_t1_t20 += MAS[3]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 19
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 19
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 19
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t10 = S.Task('c_t1_t10', length=4, delay_cost=1)
	S += c_t1_t10 >= 19
	c_t1_t10 += MAS[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=4, delay_cost=1)
	S += c_t1_t1_t3 >= 19
	c_t1_t1_t3 += MAS[7]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 19
	c_t1_t1_t5_in += MAS_in[2]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 19
	c_t1_t1_t5_mem0 += MM_MEM[2]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 19
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 19
	c_t1_t31_in += MAS_in[3]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 19
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 19
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=4, delay_cost=1)
	S += c_t0_t4_t3 >= 20
	c_t0_t4_t3 += MAS[1]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 20
	c_t1_t0_t3_in += MAS_in[6]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 20
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 20
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=4, delay_cost=1)
	S += c_t1_t1_t5 >= 20
	c_t1_t1_t5 += MAS[2]

	c_t1_t31 = S.Task('c_t1_t31', length=4, delay_cost=1)
	S += c_t1_t31 >= 20
	c_t1_t31 += MAS[3]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 21
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 21
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 21
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=4, delay_cost=1)
	S += c_t1_t0_t3 >= 21
	c_t1_t0_t3 += MAS[6]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 21
	c_t1_t4_t2_in += MAS_in[6]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 21
	c_t1_t4_t2_mem0 += MAS_MEM[6]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 21
	c_t1_t4_t2_mem1 += MAS_MEM[13]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=4, delay_cost=1)
	S += c_t0_t1_t3 >= 22
	c_t0_t1_t3 += MAS[0]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 22
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 22
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 22
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 22
	c_t1_t1_t4_in += MM_in[1]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 22
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 22
	c_t1_t1_t4_mem1 += MAS_MEM[15]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 22
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 22
	c_t1_t4_t0_mem0 += MAS_MEM[6]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 22
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=4, delay_cost=1)
	S += c_t1_t4_t2 >= 22
	c_t1_t4_t2 += MAS[6]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=4, delay_cost=1)
	S += c_t1_t0_t2 >= 23
	c_t1_t0_t2 += MAS[0]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=10, delay_cost=1)
	S += c_t1_t1_t4 >= 23
	c_t1_t1_t4 += MM[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=10, delay_cost=1)
	S += c_t1_t4_t0 >= 23
	c_t1_t4_t0 += MM[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 23
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 23
	c_t1_t4_t1_mem0 += MAS_MEM[12]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 23
	c_t1_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 23
	c_t2_t0_t3_in += MAS_in[2]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 23
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 23
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 24
	c_t1_t0_t1_in += MM_in[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 24
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 24
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=10, delay_cost=1)
	S += c_t1_t4_t1 >= 24
	c_t1_t4_t1 += MM[0]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 24
	c_t1_t4_t3_in += MAS_in[4]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 24
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 24
	c_t1_t4_t3_mem1 += MAS_MEM[7]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=4, delay_cost=1)
	S += c_t2_t0_t3 >= 24
	c_t2_t0_t3 += MAS[2]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 25
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 25
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 25
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 25
	c_t0_t1_t4_in += MM_in[1]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 25
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 25
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=10, delay_cost=1)
	S += c_t1_t0_t1 >= 25
	c_t1_t0_t1 += MM[1]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=4, delay_cost=1)
	S += c_t1_t4_t3 >= 25
	c_t1_t4_t3 += MAS[4]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 26
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 26
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 26
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=10, delay_cost=1)
	S += c_t0_t0_t1 >= 26
	c_t0_t0_t1 += MM[0]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=10, delay_cost=1)
	S += c_t0_t1_t4 >= 26
	c_t0_t1_t4 += MM[1]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 26
	c_t1_t0_t4_in += MM_in[1]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 26
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 26
	c_t1_t0_t4_mem1 += MAS_MEM[13]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 26
	c_t2_t1_t5_in += MAS_in[7]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 26
	c_t2_t1_t5_mem0 += MM_MEM[2]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 26
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=10, delay_cost=1)
	S += c_t0_t0_t0 >= 27
	c_t0_t0_t0 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 27
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 27
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 27
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=10, delay_cost=1)
	S += c_t1_t0_t4 >= 27
	c_t1_t0_t4 += MM[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 27
	c_t2_t0_t4_in += MM_in[1]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 27
	c_t2_t0_t4_mem0 += MAS_MEM[8]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 27
	c_t2_t0_t4_mem1 += MAS_MEM[5]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 27
	c_t2_t10_in += MAS_in[5]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 27
	c_t2_t10_mem0 += MM_MEM[2]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 27
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=4, delay_cost=1)
	S += c_t2_t1_t5 >= 27
	c_t2_t1_t5 += MAS[7]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=10, delay_cost=1)
	S += c_t0_t1_t1 >= 28
	c_t0_t1_t1 += MM[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 28
	c_t0_t21_in += MAS_in[2]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 28
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 28
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 28
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 28
	c_t1_t4_t4_mem0 += MAS_MEM[12]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 28
	c_t1_t4_t4_mem1 += MAS_MEM[9]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=10, delay_cost=1)
	S += c_t2_t0_t4 >= 28
	c_t2_t0_t4 += MM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=4, delay_cost=1)
	S += c_t2_t10 >= 28
	c_t2_t10 += MAS[5]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 29
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 29
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 29
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t21 = S.Task('c_t0_t21', length=4, delay_cost=1)
	S += c_t0_t21 >= 29
	c_t0_t21 += MAS[2]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=10, delay_cost=1)
	S += c_t1_t4_t4 >= 29
	c_t1_t4_t4 += MM[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=10, delay_cost=1)
	S += c_t0_t1_t0 >= 30
	c_t0_t1_t0 += MM[0]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 30
	c_t3110_in += MAS_in[2]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 30
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 30
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 31
	c_t2_t50_in += MAS_in[5]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 31
	c_t2_t50_mem0 += MAS_MEM[14]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 31
	c_t2_t50_mem1 += MAS_MEM[11]

	c_t3110 = S.Task('c_t3110', length=4, delay_cost=1)
	S += c_t3110 >= 31
	c_t3110 += MAS[2]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 31
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 31
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 31
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 32
	c_t0_t4_t1_in += MM_in[1]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 32
	c_t0_t4_t1_mem0 += MAS_MEM[4]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 32
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 32
	c_t1_t11_in += MAS_in[6]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 32
	c_t1_t11_mem0 += MM_MEM[2]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 32
	c_t1_t11_mem1 += MAS_MEM[5]

	c_t2_t50 = S.Task('c_t2_t50', length=4, delay_cost=1)
	S += c_t2_t50 >= 32
	c_t2_t50 += MAS[5]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 32
	c_t3111_in += MAS_in[2]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 32
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 32
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=4, delay_cost=1)
	S += c_t5010 >= 32
	c_t5010 += MAS[0]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=10, delay_cost=1)
	S += c_t0_t4_t1 >= 33
	c_t0_t4_t1 += MM[1]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 33
	c_t0_t4_t2_in += MAS_in[2]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 33
	c_t0_t4_t2_mem0 += MAS_MEM[4]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 33
	c_t0_t4_t2_mem1 += MAS_MEM[5]

	c_t1_t11 = S.Task('c_t1_t11', length=4, delay_cost=1)
	S += c_t1_t11 >= 33
	c_t1_t11 += MAS[6]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 33
	c_t1_t4_t5_in += MAS_in[5]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 33
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 33
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 33
	c_t3000_in += MAS_in[6]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 33
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 33
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3111 = S.Task('c_t3111', length=4, delay_cost=1)
	S += c_t3111 >= 33
	c_t3111 += MAS[2]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=4, delay_cost=1)
	S += c_t0_t4_t2 >= 34
	c_t0_t4_t2 += MAS[2]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 34
	c_t1_t00_in += MAS_in[6]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 34
	c_t1_t00_mem0 += MM_MEM[2]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 34
	c_t1_t00_mem1 += MM_MEM[3]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 34
	c_t1_t40_in += MAS_in[0]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 34
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 34
	c_t1_t40_mem1 += MM_MEM[1]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=4, delay_cost=1)
	S += c_t1_t4_t5 >= 34
	c_t1_t4_t5 += MAS[5]

	c_t3000 = S.Task('c_t3000', length=4, delay_cost=1)
	S += c_t3000 >= 34
	c_t3000 += MAS[6]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 34
	c_t5110_in += MAS_in[2]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 34
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 34
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t1_t00 = S.Task('c_t1_t00', length=4, delay_cost=1)
	S += c_t1_t00 >= 35
	c_t1_t00 += MAS[6]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 35
	c_t1_t0_t5_in += MAS_in[3]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 35
	c_t1_t0_t5_mem0 += MM_MEM[2]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 35
	c_t1_t0_t5_mem1 += MM_MEM[3]

	c_t1_t40 = S.Task('c_t1_t40', length=4, delay_cost=1)
	S += c_t1_t40 >= 35
	c_t1_t40 += MAS[0]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 35
	c_t5100_in += MAS_in[5]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 35
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 35
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=4, delay_cost=1)
	S += c_t5110 >= 35
	c_t5110 += MAS[2]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 36
	c_t0_t00_in += MAS_in[6]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 36
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 36
	c_t0_t00_mem1 += MM_MEM[1]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=4, delay_cost=1)
	S += c_t1_t0_t5 >= 36
	c_t1_t0_t5 += MAS[3]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 36
	c_t3_t1_t3_in += MAS_in[5]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 36
	c_t3_t1_t3_mem0 += MAS_MEM[4]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 36
	c_t3_t1_t3_mem1 += MAS_MEM[5]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 36
	c_t5001_in += MAS_in[4]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 36
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 36
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=4, delay_cost=1)
	S += c_t5100 >= 36
	c_t5100 += MAS[5]

	c_t0_t00 = S.Task('c_t0_t00', length=4, delay_cost=1)
	S += c_t0_t00 >= 37
	c_t0_t00 += MAS[6]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 37
	c_t0_t0_t5_in += MAS_in[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 37
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 37
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 37
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 37
	c_t0_t4_t4_mem0 += MAS_MEM[4]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 37
	c_t0_t4_t4_mem1 += MAS_MEM[3]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 37
	c_t2_t01_in += MAS_in[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 37
	c_t2_t01_mem0 += MM_MEM[2]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 37
	c_t2_t01_mem1 += MAS_MEM[15]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 37
	c_t3010_in += MAS_in[3]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 37
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 37
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=4, delay_cost=1)
	S += c_t3_t1_t3 >= 37
	c_t3_t1_t3 += MAS[5]

	c_t5001 = S.Task('c_t5001', length=4, delay_cost=1)
	S += c_t5001 >= 37
	c_t5001 += MAS[4]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=4, delay_cost=1)
	S += c_t0_t0_t5 >= 38
	c_t0_t0_t5 += MAS[2]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=10, delay_cost=1)
	S += c_t0_t4_t4 >= 38
	c_t0_t4_t4 += MM[0]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 38
	c_t1_t50_in += MAS_in[6]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 38
	c_t1_t50_mem0 += MAS_MEM[12]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 38
	c_t1_t50_mem1 += MAS_MEM[1]

	c_t2_t01 = S.Task('c_t2_t01', length=4, delay_cost=1)
	S += c_t2_t01 >= 38
	c_t2_t01 += MAS[0]

	c_t3010 = S.Task('c_t3010', length=4, delay_cost=1)
	S += c_t3010 >= 38
	c_t3010 += MAS[3]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 38
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 38
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 38
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 38
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 38
	c_t5_t1_t0_mem0 += MAS_MEM[0]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 38
	c_t5_t1_t0_mem1 += MAS_MEM[5]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 39
	c_t0_t1_t5_in += MAS_in[4]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 39
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 39
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 39
	c_t1_t01_in += MAS_in[0]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 39
	c_t1_t01_mem0 += MM_MEM[2]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 39
	c_t1_t01_mem1 += MAS_MEM[7]

	c_t1_t50 = S.Task('c_t1_t50', length=4, delay_cost=1)
	S += c_t1_t50 >= 39
	c_t1_t50 += MAS[6]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 39
	c_t4000_in += MAS_in[3]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 39
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 39
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=4, delay_cost=1)
	S += c_t4010 >= 39
	c_t4010 += MAS[0]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=10, delay_cost=1)
	S += c_t5_t1_t0 >= 39
	c_t5_t1_t0 += MM[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 39
	c_t5_t30_in += MAS_in[6]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 39
	c_t5_t30_mem0 += MAS_MEM[10]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 39
	c_t5_t30_mem1 += MAS_MEM[5]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 40
	c_t0_t10_in += MAS_in[5]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 40
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 40
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=4, delay_cost=1)
	S += c_t0_t1_t5 >= 40
	c_t0_t1_t5 += MAS[4]

	c_t1_t01 = S.Task('c_t1_t01', length=4, delay_cost=1)
	S += c_t1_t01 >= 40
	c_t1_t01 += MAS[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 40
	c_t2_t1_t3_in += MAS_in[6]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 40
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 40
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=4, delay_cost=1)
	S += c_t4000 >= 40
	c_t4000 += MAS[3]

	c_t5_t30 = S.Task('c_t5_t30', length=4, delay_cost=1)
	S += c_t5_t30 >= 40
	c_t5_t30 += MAS[6]

	c_t0_t10 = S.Task('c_t0_t10', length=4, delay_cost=1)
	S += c_t0_t10 >= 41
	c_t0_t10 += MAS[5]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=4, delay_cost=1)
	S += c_t2_t1_t3 >= 41
	c_t2_t1_t3 += MAS[6]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 41
	c_t3_t1_t0_in += MM_in[1]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 41
	c_t3_t1_t0_mem0 += MAS_MEM[6]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 41
	c_t3_t1_t0_mem1 += MAS_MEM[5]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 41
	c_t3_t20_in += MAS_in[5]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 41
	c_t3_t20_mem0 += MAS_MEM[12]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 41
	c_t3_t20_mem1 += MAS_MEM[7]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 41
	c_t4101_in += MAS_in[3]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 41
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 41
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 42
	c_t0_t4_t5_in += MAS_in[5]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 42
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 42
	c_t0_t4_t5_mem1 += MM_MEM[3]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 42
	c_t2_t30_in += MAS_in[2]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 42
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 42
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=10, delay_cost=1)
	S += c_t3_t1_t0 >= 42
	c_t3_t1_t0 += MM[1]

	c_t3_t20 = S.Task('c_t3_t20', length=4, delay_cost=1)
	S += c_t3_t20 >= 42
	c_t3_t20 += MAS[5]

	c_t4101 = S.Task('c_t4101', length=4, delay_cost=1)
	S += c_t4101 >= 42
	c_t4101 += MAS[3]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 43
	c_t0_t11_in += MAS_in[5]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 43
	c_t0_t11_mem0 += MM_MEM[2]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 43
	c_t0_t11_mem1 += MAS_MEM[9]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 43
	c_t0_t40_in += MAS_in[1]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 43
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 43
	c_t0_t40_mem1 += MM_MEM[3]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=4, delay_cost=1)
	S += c_t0_t4_t5 >= 43
	c_t0_t4_t5 += MAS[5]

	c_t2_t30 = S.Task('c_t2_t30', length=4, delay_cost=1)
	S += c_t2_t30 >= 43
	c_t2_t30 += MAS[2]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 43
	c_t4110_in += MAS_in[0]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 43
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 43
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 43
	c_t4_t20_in += MAS_in[4]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 43
	c_t4_t20_mem0 += MAS_MEM[6]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 43
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 44
	c_t0_t01_in += MAS_in[5]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 44
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 44
	c_t0_t01_mem1 += MAS_MEM[5]

	c_t0_t11 = S.Task('c_t0_t11', length=4, delay_cost=1)
	S += c_t0_t11 >= 44
	c_t0_t11 += MAS[5]

	c_t0_t40 = S.Task('c_t0_t40', length=4, delay_cost=1)
	S += c_t0_t40 >= 44
	c_t0_t40 += MAS[1]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 44
	c_t0_t50_in += MAS_in[6]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 44
	c_t0_t50_mem0 += MAS_MEM[12]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 44
	c_t0_t50_mem1 += MAS_MEM[11]

	c_t4110 = S.Task('c_t4110', length=4, delay_cost=1)
	S += c_t4110 >= 44
	c_t4110 += MAS[0]

	c_t4_t20 = S.Task('c_t4_t20', length=4, delay_cost=1)
	S += c_t4_t20 >= 44
	c_t4_t20 += MAS[4]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 44
	c_t5011_in += MAS_in[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 44
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 44
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t01 = S.Task('c_t0_t01', length=4, delay_cost=1)
	S += c_t0_t01 >= 45
	c_t0_t01 += MAS[5]

	c_t0_t50 = S.Task('c_t0_t50', length=4, delay_cost=1)
	S += c_t0_t50 >= 45
	c_t0_t50 += MAS[6]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 45
	c_t3100_in += MAS_in[2]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 45
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 45
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=4, delay_cost=1)
	S += c_t5011 >= 45
	c_t5011 += MAS[3]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 46
	c_t3011_in += MAS_in[3]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 46
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 46
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3100 = S.Task('c_t3100', length=4, delay_cost=1)
	S += c_t3100 >= 46
	c_t3100 += MAS[2]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 47
	c_t3001_in += MAS_in[2]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 47
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 47
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=4, delay_cost=1)
	S += c_t3011 >= 47
	c_t3011 += MAS[3]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 47
	c_t4_t1_t0_in += MM_in[1]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 47
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 47
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 48
	c_t2_t31_in += MAS_in[4]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 48
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 48
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=4, delay_cost=1)
	S += c_t3001 >= 48
	c_t3001 += MAS[2]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=10, delay_cost=1)
	S += c_t4_t1_t0 >= 48
	c_t4_t1_t0 += MM[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 48
	c_t5_t1_t2_in += MAS_in[6]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 48
	c_t5_t1_t2_mem0 += MAS_MEM[0]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 48
	c_t5_t1_t2_mem1 += MAS_MEM[7]

	c_t2_t31 = S.Task('c_t2_t31', length=4, delay_cost=1)
	S += c_t2_t31 >= 49
	c_t2_t31 += MAS[4]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 49
	c_t3_t0_t0_in += MM_in[1]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 49
	c_t3_t0_t0_mem0 += MAS_MEM[12]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 49
	c_t3_t0_t0_mem1 += MAS_MEM[5]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 49
	c_t4100_in += MAS_in[0]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 49
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 49
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=4, delay_cost=1)
	S += c_t5_t1_t2 >= 49
	c_t5_t1_t2 += MAS[6]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 49
	c_t5_t21_in += MAS_in[2]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 49
	c_t5_t21_mem0 += MAS_MEM[8]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 49
	c_t5_t21_mem1 += MAS_MEM[7]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 50
	c_t3101_in += MAS_in[7]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 50
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 50
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=10, delay_cost=1)
	S += c_t3_t0_t0 >= 50
	c_t3_t0_t0 += MM[1]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 50
	c_t3_t1_t2_in += MAS_in[4]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 50
	c_t3_t1_t2_mem0 += MAS_MEM[6]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 50
	c_t3_t1_t2_mem1 += MAS_MEM[7]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 50
	c_t3_t30_in += MAS_in[1]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 50
	c_t3_t30_mem0 += MAS_MEM[4]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 50
	c_t3_t30_mem1 += MAS_MEM[5]

	c_t4100 = S.Task('c_t4100', length=4, delay_cost=1)
	S += c_t4100 >= 50
	c_t4100 += MAS[0]

	c_t5_t21 = S.Task('c_t5_t21', length=4, delay_cost=1)
	S += c_t5_t21 >= 50
	c_t5_t21 += MAS[2]

	c_t3101 = S.Task('c_t3101', length=4, delay_cost=1)
	S += c_t3101 >= 51
	c_t3101 += MAS[7]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 51
	c_t3_t1_t1_in += MM_in[1]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 51
	c_t3_t1_t1_mem0 += MAS_MEM[6]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 51
	c_t3_t1_t1_mem1 += MAS_MEM[5]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=4, delay_cost=1)
	S += c_t3_t1_t2 >= 51
	c_t3_t1_t2 += MAS[4]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 51
	c_t3_t21_in += MAS_in[5]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 51
	c_t3_t21_mem0 += MAS_MEM[4]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 51
	c_t3_t21_mem1 += MAS_MEM[7]

	c_t3_t30 = S.Task('c_t3_t30', length=4, delay_cost=1)
	S += c_t3_t30 >= 51
	c_t3_t30 += MAS[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 51
	c_t5000_in += MAS_in[4]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 51
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 51
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 52
	c_t2_t20_in += MAS_in[7]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 52
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 52
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 52
	c_t2_t4_t3_in += MAS_in[4]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 52
	c_t2_t4_t3_mem0 += MAS_MEM[4]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 52
	c_t2_t4_t3_mem1 += MAS_MEM[9]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 52
	c_t3_t0_t2_in += MAS_in[0]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 52
	c_t3_t0_t2_mem0 += MAS_MEM[12]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 52
	c_t3_t0_t2_mem1 += MAS_MEM[5]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=10, delay_cost=1)
	S += c_t3_t1_t1 >= 52
	c_t3_t1_t1 += MM[1]

	c_t3_t21 = S.Task('c_t3_t21', length=4, delay_cost=1)
	S += c_t3_t21 >= 52
	c_t3_t21 += MAS[5]

	c_t5000 = S.Task('c_t5000', length=4, delay_cost=1)
	S += c_t5000 >= 52
	c_t5000 += MAS[4]

	c_t2_t20 = S.Task('c_t2_t20', length=4, delay_cost=1)
	S += c_t2_t20 >= 53
	c_t2_t20 += MAS[7]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=4, delay_cost=1)
	S += c_t2_t4_t3 >= 53
	c_t2_t4_t3 += MAS[4]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=4, delay_cost=1)
	S += c_t3_t0_t2 >= 53
	c_t3_t0_t2 += MAS[0]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 53
	c_t4_t0_t0_in += MM_in[1]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 53
	c_t4_t0_t0_mem0 += MAS_MEM[6]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 53
	c_t4_t0_t0_mem1 += MAS_MEM[1]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 53
	c_t4_t0_t3_in += MAS_in[4]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 53
	c_t4_t0_t3_mem0 += MAS_MEM[0]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 53
	c_t4_t0_t3_mem1 += MAS_MEM[7]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 53
	c_t5111_in += MAS_in[5]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 53
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 53
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 54
	c_t3_t0_t1_in += MM_in[1]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 54
	c_t3_t0_t1_mem0 += MAS_MEM[4]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 54
	c_t3_t0_t1_mem1 += MAS_MEM[15]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 54
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 54
	c_t3_t1_t4_mem0 += MAS_MEM[8]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 54
	c_t3_t1_t4_mem1 += MAS_MEM[11]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 54
	c_t3_t31_in += MAS_in[4]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 54
	c_t3_t31_mem0 += MAS_MEM[14]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 54
	c_t3_t31_mem1 += MAS_MEM[5]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 54
	c_t4011_in += MAS_in[5]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 54
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 54
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=10, delay_cost=1)
	S += c_t4_t0_t0 >= 54
	c_t4_t0_t0 += MM[1]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=4, delay_cost=1)
	S += c_t4_t0_t3 >= 54
	c_t4_t0_t3 += MAS[4]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 54
	c_t4_t30_in += MAS_in[6]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 54
	c_t4_t30_mem0 += MAS_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 54
	c_t4_t30_mem1 += MAS_MEM[1]

	c_t5111 = S.Task('c_t5111', length=4, delay_cost=1)
	S += c_t5111 >= 54
	c_t5111 += MAS[5]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=10, delay_cost=1)
	S += c_t3_t0_t1 >= 55
	c_t3_t0_t1 += MM[1]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 55
	c_t3_t0_t3_in += MAS_in[5]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 55
	c_t3_t0_t3_mem0 += MAS_MEM[4]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 55
	c_t3_t0_t3_mem1 += MAS_MEM[15]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=10, delay_cost=1)
	S += c_t3_t1_t4 >= 55
	c_t3_t1_t4 += MM[0]

	c_t3_t31 = S.Task('c_t3_t31', length=4, delay_cost=1)
	S += c_t3_t31 >= 55
	c_t3_t31 += MAS[4]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 55
	c_t3_t4_t2_in += MAS_in[6]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 55
	c_t3_t4_t2_mem0 += MAS_MEM[10]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 55
	c_t3_t4_t2_mem1 += MAS_MEM[11]

	c_t4011 = S.Task('c_t4011', length=4, delay_cost=1)
	S += c_t4011 >= 55
	c_t4011 += MAS[5]

	c_t4_t30 = S.Task('c_t4_t30', length=4, delay_cost=1)
	S += c_t4_t30 >= 55
	c_t4_t30 += MAS[6]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 55
	c_t5101_in += MAS_in[0]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 55
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 55
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 55
	c_t5_t0_t2_in += MAS_in[2]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 55
	c_t5_t0_t2_mem0 += MAS_MEM[8]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 55
	c_t5_t0_t2_mem1 += MAS_MEM[9]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 56
	c_t2_t1_t2_in += MAS_in[5]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 56
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 56
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 56
	c_t2_t4_t0_in += MM_in[1]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 56
	c_t2_t4_t0_mem0 += MAS_MEM[14]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 56
	c_t2_t4_t0_mem1 += MAS_MEM[5]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=4, delay_cost=1)
	S += c_t3_t0_t3 >= 56
	c_t3_t0_t3 += MAS[5]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=4, delay_cost=1)
	S += c_t3_t4_t2 >= 56
	c_t3_t4_t2 += MAS[6]

	c_t5101 = S.Task('c_t5101', length=4, delay_cost=1)
	S += c_t5101 >= 56
	c_t5101 += MAS[0]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 56
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 56
	c_t5_t0_t0_mem0 += MAS_MEM[8]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 56
	c_t5_t0_t0_mem1 += MAS_MEM[11]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=4, delay_cost=1)
	S += c_t5_t0_t2 >= 56
	c_t5_t0_t2 += MAS[2]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=4, delay_cost=1)
	S += c_t2_t1_t2 >= 57
	c_t2_t1_t2 += MAS[5]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=10, delay_cost=1)
	S += c_t2_t4_t0 >= 57
	c_t2_t4_t0 += MM[1]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 57
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 57
	c_t3_t4_t0_mem0 += MAS_MEM[10]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 57
	c_t3_t4_t0_mem1 += MAS_MEM[3]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 57
	c_t4001_in += MAS_in[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 57
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 57
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=10, delay_cost=1)
	S += c_t5_t0_t0 >= 57
	c_t5_t0_t0 += MM[0]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 57
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 57
	c_t5_t1_t3_mem0 += MAS_MEM[4]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 57
	c_t5_t1_t3_mem1 += MAS_MEM[11]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 57
	c_t5_t20_in += MAS_in[4]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 57
	c_t5_t20_mem0 += MAS_MEM[8]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 57
	c_t5_t20_mem1 += MAS_MEM[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=10, delay_cost=1)
	S += c_t3_t4_t0 >= 58
	c_t3_t4_t0 += MM[0]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 58
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 58
	c_t3_t4_t1_mem0 += MAS_MEM[10]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 58
	c_t3_t4_t1_mem1 += MAS_MEM[9]

	c_t4001 = S.Task('c_t4001', length=4, delay_cost=1)
	S += c_t4001 >= 58
	c_t4001 += MAS[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 58
	c_t4111_in += MAS_in[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 58
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 58
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 58
	c_t4_t1_t2_in += MAS_in[4]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 58
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 58
	c_t4_t1_t2_mem1 += MAS_MEM[11]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 58
	c_t4_t4_t0_in += MM_in[1]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 58
	c_t4_t4_t0_mem0 += MAS_MEM[8]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 58
	c_t4_t4_t0_mem1 += MAS_MEM[13]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=4, delay_cost=1)
	S += c_t5_t1_t3 >= 58
	c_t5_t1_t3 += MAS[2]

	c_t5_t20 = S.Task('c_t5_t20', length=4, delay_cost=1)
	S += c_t5_t20 >= 58
	c_t5_t20 += MAS[4]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 59
	c_t2_t21_in += MAS_in[6]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 59
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 59
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=10, delay_cost=1)
	S += c_t3_t4_t1 >= 59
	c_t3_t4_t1 += MM[0]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 59
	c_t3_t4_t3_in += MAS_in[3]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 59
	c_t3_t4_t3_mem0 += MAS_MEM[2]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 59
	c_t3_t4_t3_mem1 += MAS_MEM[9]

	c_t4111 = S.Task('c_t4111', length=4, delay_cost=1)
	S += c_t4111 >= 59
	c_t4111 += MAS[0]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=4, delay_cost=1)
	S += c_t4_t1_t2 >= 59
	c_t4_t1_t2 += MAS[4]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=10, delay_cost=1)
	S += c_t4_t4_t0 >= 59
	c_t4_t4_t0 += MM[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 59
	c_t5_t0_t3_in += MAS_in[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 59
	c_t5_t0_t3_mem0 += MAS_MEM[10]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 59
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 59
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 59
	c_t5_t1_t1_mem0 += MAS_MEM[6]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 59
	c_t5_t1_t1_mem1 += MAS_MEM[11]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 60
	c_t2_t1_t4_in += MM_in[1]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 60
	c_t2_t1_t4_mem0 += MAS_MEM[10]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 60
	c_t2_t1_t4_mem1 += MAS_MEM[13]

	c_t2_t21 = S.Task('c_t2_t21', length=4, delay_cost=1)
	S += c_t2_t21 >= 60
	c_t2_t21 += MAS[6]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=4, delay_cost=1)
	S += c_t3_t4_t3 >= 60
	c_t3_t4_t3 += MAS[3]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 60
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 60
	c_t5_t0_t1_mem0 += MAS_MEM[8]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 60
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=4, delay_cost=1)
	S += c_t5_t0_t3 >= 60
	c_t5_t0_t3 += MAS[1]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=10, delay_cost=1)
	S += c_t5_t1_t1 >= 60
	c_t5_t1_t1 += MM[0]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 60
	c_t5_t31_in += MAS_in[4]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 60
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 60
	c_t5_t31_mem1 += MAS_MEM[11]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=10, delay_cost=1)
	S += c_t2_t1_t4 >= 61
	c_t2_t1_t4 += MM[1]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 61
	c_t3_t10_in += MAS_in[1]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 61
	c_t3_t10_mem0 += MM_MEM[2]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 61
	c_t3_t10_mem1 += MM_MEM[3]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 61
	c_t4_t0_t1_in += MM_in[1]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 61
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 61
	c_t4_t0_t1_mem1 += MAS_MEM[7]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 61
	c_t4_t0_t2_in += MAS_in[5]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 61
	c_t4_t0_t2_mem0 += MAS_MEM[6]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 61
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=10, delay_cost=1)
	S += c_t5_t0_t1 >= 61
	c_t5_t0_t1 += MM[0]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 61
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 61
	c_t5_t1_t4_mem0 += MAS_MEM[12]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 61
	c_t5_t1_t4_mem1 += MAS_MEM[5]

	c_t5_t31 = S.Task('c_t5_t31', length=4, delay_cost=1)
	S += c_t5_t31 >= 61
	c_t5_t31 += MAS[4]

	c_t3_t10 = S.Task('c_t3_t10', length=4, delay_cost=1)
	S += c_t3_t10 >= 62
	c_t3_t10 += MAS[1]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 62
	c_t3_t1_t5_in += MAS_in[1]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 62
	c_t3_t1_t5_mem0 += MM_MEM[2]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 62
	c_t3_t1_t5_mem1 += MM_MEM[3]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=10, delay_cost=1)
	S += c_t4_t0_t1 >= 62
	c_t4_t0_t1 += MM[1]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=4, delay_cost=1)
	S += c_t4_t0_t2 >= 62
	c_t4_t0_t2 += MAS[5]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 62
	c_t4_t1_t1_in += MM_in[1]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 62
	c_t4_t1_t1_mem0 += MAS_MEM[10]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 62
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 62
	c_t4_t21_in += MAS_in[3]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 62
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 62
	c_t4_t21_mem1 += MAS_MEM[11]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=10, delay_cost=1)
	S += c_t5_t1_t4 >= 62
	c_t5_t1_t4 += MM[0]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 62
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 62
	c_t5_t4_t0_mem0 += MAS_MEM[8]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 62
	c_t5_t4_t0_mem1 += MAS_MEM[13]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 63
	c_t2_t4_t1_in += MM_in[1]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 63
	c_t2_t4_t1_mem0 += MAS_MEM[12]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 63
	c_t2_t4_t1_mem1 += MAS_MEM[9]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 63
	c_t2_t4_t2_in += MAS_in[5]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 63
	c_t2_t4_t2_mem0 += MAS_MEM[14]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 63
	c_t2_t4_t2_mem1 += MAS_MEM[13]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=4, delay_cost=1)
	S += c_t3_t1_t5 >= 63
	c_t3_t1_t5 += MAS[1]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=10, delay_cost=1)
	S += c_t4_t1_t1 >= 63
	c_t4_t1_t1 += MM[1]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 63
	c_t4_t1_t3_in += MAS_in[3]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 63
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 63
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	c_t4_t21 = S.Task('c_t4_t21', length=4, delay_cost=1)
	S += c_t4_t21 >= 63
	c_t4_t21 += MAS[3]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 63
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 63
	c_t5_t0_t4_mem0 += MAS_MEM[4]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 63
	c_t5_t0_t4_mem1 += MAS_MEM[3]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=10, delay_cost=1)
	S += c_t5_t4_t0 >= 63
	c_t5_t4_t0 += MM[0]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 63
	c_t5_t4_t2_in += MAS_in[4]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 63
	c_t5_t4_t2_mem0 += MAS_MEM[8]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 63
	c_t5_t4_t2_mem1 += MAS_MEM[5]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=10, delay_cost=1)
	S += c_t2_t4_t1 >= 64
	c_t2_t4_t1 += MM[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=4, delay_cost=1)
	S += c_t2_t4_t2 >= 64
	c_t2_t4_t2 += MAS[5]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 64
	c_t3_t00_in += MAS_in[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 64
	c_t3_t00_mem0 += MM_MEM[2]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 64
	c_t3_t00_mem1 += MM_MEM[3]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 64
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 64
	c_t3_t0_t4_mem0 += MAS_MEM[0]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 64
	c_t3_t0_t4_mem1 += MAS_MEM[11]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=4, delay_cost=1)
	S += c_t4_t1_t3 >= 64
	c_t4_t1_t3 += MAS[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 64
	c_t4_t31_in += MAS_in[3]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 64
	c_t4_t31_mem0 += MAS_MEM[6]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 64
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=10, delay_cost=1)
	S += c_t5_t0_t4 >= 64
	c_t5_t0_t4 += MM[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 64
	c_t5_t4_t1_in += MM_in[1]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 64
	c_t5_t4_t1_mem0 += MAS_MEM[4]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 64
	c_t5_t4_t1_mem1 += MAS_MEM[9]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=4, delay_cost=1)
	S += c_t5_t4_t2 >= 64
	c_t5_t4_t2 += MAS[4]

	c_t3_t00 = S.Task('c_t3_t00', length=4, delay_cost=1)
	S += c_t3_t00 >= 65
	c_t3_t00 += MAS[1]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=10, delay_cost=1)
	S += c_t3_t0_t4 >= 65
	c_t3_t0_t4 += MM[0]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 65
	c_t3_t0_t5_in += MAS_in[1]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 65
	c_t3_t0_t5_mem0 += MM_MEM[2]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 65
	c_t3_t0_t5_mem1 += MM_MEM[3]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 65
	c_t4_t0_t4_in += MM_in[1]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 65
	c_t4_t0_t4_mem0 += MAS_MEM[10]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 65
	c_t4_t0_t4_mem1 += MAS_MEM[9]

	c_t4_t31 = S.Task('c_t4_t31', length=4, delay_cost=1)
	S += c_t4_t31 >= 65
	c_t4_t31 += MAS[3]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=10, delay_cost=1)
	S += c_t5_t4_t1 >= 65
	c_t5_t4_t1 += MM[1]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=4, delay_cost=1)
	S += c_t3_t0_t5 >= 66
	c_t3_t0_t5 += MAS[1]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=10, delay_cost=1)
	S += c_t4_t0_t4 >= 66
	c_t4_t0_t4 += MM[1]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 66
	c_t4_t4_t2_in += MAS_in[5]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 66
	c_t4_t4_t2_mem0 += MAS_MEM[8]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 66
	c_t4_t4_t2_mem1 += MAS_MEM[7]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 66
	c_t5_t4_t3_in += MAS_in[1]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 66
	c_t5_t4_t3_mem0 += MAS_MEM[12]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 66
	c_t5_t4_t3_mem1 += MAS_MEM[9]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 67
	c_t2_t4_t4_in += MM_in[1]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 67
	c_t2_t4_t4_mem0 += MAS_MEM[10]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 67
	c_t2_t4_t4_mem1 += MAS_MEM[9]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 67
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 67
	c_t4_t1_t4_mem0 += MAS_MEM[8]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 67
	c_t4_t1_t4_mem1 += MAS_MEM[7]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=4, delay_cost=1)
	S += c_t4_t4_t2 >= 67
	c_t4_t4_t2 += MAS[5]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=4, delay_cost=1)
	S += c_t5_t4_t3 >= 67
	c_t5_t4_t3 += MAS[1]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=10, delay_cost=1)
	S += c_t2_t4_t4 >= 68
	c_t2_t4_t4 += MM[1]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=10, delay_cost=1)
	S += c_t4_t1_t4 >= 68
	c_t4_t1_t4 += MM[0]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 68
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 68
	c_t4_t4_t1_mem0 += MAS_MEM[6]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 68
	c_t4_t4_t1_mem1 += MAS_MEM[7]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=10, delay_cost=1)
	S += c_t4_t4_t1 >= 69
	c_t4_t4_t1 += MM[0]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 69
	c_t4_t4_t3_in += MAS_in[5]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 69
	c_t4_t4_t3_mem0 += MAS_MEM[12]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 69
	c_t4_t4_t3_mem1 += MAS_MEM[7]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 69
	c_t5_t10_in += MAS_in[4]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 69
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 69
	c_t5_t10_mem1 += MM_MEM[1]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 70
	c_t2_t11_in += MAS_in[5]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 70
	c_t2_t11_mem0 += MM_MEM[2]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 70
	c_t2_t11_mem1 += MAS_MEM[15]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=4, delay_cost=1)
	S += c_t4_t4_t3 >= 70
	c_t4_t4_t3 += MAS[5]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 70
	c_t5_t00_in += MAS_in[4]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 70
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 70
	c_t5_t00_mem1 += MM_MEM[1]

	c_t5_t10 = S.Task('c_t5_t10', length=4, delay_cost=1)
	S += c_t5_t10 >= 70
	c_t5_t10 += MAS[4]

	c_t2_t11 = S.Task('c_t2_t11', length=4, delay_cost=1)
	S += c_t2_t11 >= 71
	c_t2_t11 += MAS[5]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 71
	c_t4_t00_in += MAS_in[5]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 71
	c_t4_t00_mem0 += MM_MEM[2]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 71
	c_t4_t00_mem1 += MM_MEM[3]

	c_t5_t00 = S.Task('c_t5_t00', length=4, delay_cost=1)
	S += c_t5_t00 >= 71
	c_t5_t00 += MAS[4]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 71
	c_t5_t0_t5_in += MAS_in[0]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 71
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 71
	c_t5_t0_t5_mem1 += MM_MEM[1]

	c_t4_t00 = S.Task('c_t4_t00', length=4, delay_cost=1)
	S += c_t4_t00 >= 72
	c_t4_t00 += MAS[5]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 72
	c_t4_t10_in += MAS_in[5]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 72
	c_t4_t10_mem0 += MM_MEM[2]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 72
	c_t4_t10_mem1 += MM_MEM[3]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=4, delay_cost=1)
	S += c_t5_t0_t5 >= 72
	c_t5_t0_t5 += MAS[0]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 72
	c_t5_t1_t5_in += MAS_in[0]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 72
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 72
	c_t5_t1_t5_mem1 += MM_MEM[1]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 73
	c_t2_t4_t5_in += MAS_in[1]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 73
	c_t2_t4_t5_mem0 += MM_MEM[2]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 73
	c_t2_t4_t5_mem1 += MM_MEM[3]

	c_t4_t10 = S.Task('c_t4_t10', length=4, delay_cost=1)
	S += c_t4_t10 >= 73
	c_t4_t10 += MAS[5]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=4, delay_cost=1)
	S += c_t5_t1_t5 >= 73
	c_t5_t1_t5 += MAS[0]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=4, delay_cost=1)
	S += c_t2_t4_t5 >= 74
	c_t2_t4_t5 += MAS[1]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 74
	c_t4_t0_t5_in += MAS_in[5]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 74
	c_t4_t0_t5_mem0 += MM_MEM[2]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 74
	c_t4_t0_t5_mem1 += MM_MEM[3]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 75
	c_t2_t40_in += MAS_in[1]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 75
	c_t2_t40_mem0 += MM_MEM[2]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 75
	c_t2_t40_mem1 += MM_MEM[3]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=4, delay_cost=1)
	S += c_t4_t0_t5 >= 75
	c_t4_t0_t5 += MAS[5]

	c_t2_t40 = S.Task('c_t2_t40', length=4, delay_cost=1)
	S += c_t2_t40 >= 76
	c_t2_t40 += MAS[1]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 76
	c_t4_t1_t5_in += MAS_in[3]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 76
	c_t4_t1_t5_mem0 += MM_MEM[2]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 76
	c_t4_t1_t5_mem1 += MM_MEM[3]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=4, delay_cost=1)
	S += c_t4_t1_t5 >= 77
	c_t4_t1_t5 += MAS[3]


	# new tasks
	c_t0_t41 = S.Task('c_t0_t41', length=4, delay_cost=1)
	c_t0_t41 += alt(MAS)
	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	c_t0_t41_in += alt(MAS_in)
	S += c_t0_t41_in*MAS_in[0]<=c_t0_t41*MAS[0]

	S += c_t0_t41_in*MAS_in[1]<=c_t0_t41*MAS[1]

	S += c_t0_t41_in*MAS_in[2]<=c_t0_t41*MAS[2]

	S += c_t0_t41_in*MAS_in[3]<=c_t0_t41*MAS[3]

	S += c_t0_t41_in*MAS_in[4]<=c_t0_t41*MAS[4]

	S += c_t0_t41_in*MAS_in[5]<=c_t0_t41*MAS[5]

	S += c_t0_t41_in*MAS_in[6]<=c_t0_t41*MAS[6]

	S += c_t0_t41_in*MAS_in[7]<=c_t0_t41*MAS[7]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	c_t0_t41_mem0 += MM_MEM[0]
	S += 47 < c_t0_t41_mem0
	S += c_t0_t41_mem0 <= c_t0_t41

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	c_t0_t41_mem1 += MAS_MEM[11]
	S += 46 < c_t0_t41_mem1
	S += c_t0_t41_mem1 <= c_t0_t41

	c_t0_s00 = S.Task('c_t0_s00', length=4, delay_cost=1)
	c_t0_s00 += alt(MAS)
	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	c_t0_s00_in += alt(MAS_in)
	S += c_t0_s00_in*MAS_in[0]<=c_t0_s00*MAS[0]

	S += c_t0_s00_in*MAS_in[1]<=c_t0_s00*MAS[1]

	S += c_t0_s00_in*MAS_in[2]<=c_t0_s00*MAS[2]

	S += c_t0_s00_in*MAS_in[3]<=c_t0_s00*MAS[3]

	S += c_t0_s00_in*MAS_in[4]<=c_t0_s00*MAS[4]

	S += c_t0_s00_in*MAS_in[5]<=c_t0_s00*MAS[5]

	S += c_t0_s00_in*MAS_in[6]<=c_t0_s00*MAS[6]

	S += c_t0_s00_in*MAS_in[7]<=c_t0_s00*MAS[7]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	c_t0_s00_mem0 += MAS_MEM[10]
	S += 44 < c_t0_s00_mem0
	S += c_t0_s00_mem0 <= c_t0_s00

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	c_t0_s00_mem1 += MAS_MEM[11]
	S += 47 < c_t0_s00_mem1
	S += c_t0_s00_mem1 <= c_t0_s00

	c_t0_s01 = S.Task('c_t0_s01', length=4, delay_cost=1)
	c_t0_s01 += alt(MAS)
	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	c_t0_s01_in += alt(MAS_in)
	S += c_t0_s01_in*MAS_in[0]<=c_t0_s01*MAS[0]

	S += c_t0_s01_in*MAS_in[1]<=c_t0_s01*MAS[1]

	S += c_t0_s01_in*MAS_in[2]<=c_t0_s01*MAS[2]

	S += c_t0_s01_in*MAS_in[3]<=c_t0_s01*MAS[3]

	S += c_t0_s01_in*MAS_in[4]<=c_t0_s01*MAS[4]

	S += c_t0_s01_in*MAS_in[5]<=c_t0_s01*MAS[5]

	S += c_t0_s01_in*MAS_in[6]<=c_t0_s01*MAS[6]

	S += c_t0_s01_in*MAS_in[7]<=c_t0_s01*MAS[7]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	c_t0_s01_mem0 += MAS_MEM[10]
	S += 47 < c_t0_s01_mem0
	S += c_t0_s01_mem0 <= c_t0_s01

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	c_t0_s01_mem1 += MAS_MEM[11]
	S += 44 < c_t0_s01_mem1
	S += c_t0_s01_mem1 <= c_t0_s01

	c_t0_t51 = S.Task('c_t0_t51', length=4, delay_cost=1)
	c_t0_t51 += alt(MAS)
	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	c_t0_t51_in += alt(MAS_in)
	S += c_t0_t51_in*MAS_in[0]<=c_t0_t51*MAS[0]

	S += c_t0_t51_in*MAS_in[1]<=c_t0_t51*MAS[1]

	S += c_t0_t51_in*MAS_in[2]<=c_t0_t51*MAS[2]

	S += c_t0_t51_in*MAS_in[3]<=c_t0_t51*MAS[3]

	S += c_t0_t51_in*MAS_in[4]<=c_t0_t51*MAS[4]

	S += c_t0_t51_in*MAS_in[5]<=c_t0_t51*MAS[5]

	S += c_t0_t51_in*MAS_in[6]<=c_t0_t51*MAS[6]

	S += c_t0_t51_in*MAS_in[7]<=c_t0_t51*MAS[7]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	c_t0_t51_mem0 += MAS_MEM[10]
	S += 48 < c_t0_t51_mem0
	S += c_t0_t51_mem0 <= c_t0_t51

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	c_t0_t51_mem1 += MAS_MEM[11]
	S += 47 < c_t0_t51_mem1
	S += c_t0_t51_mem1 <= c_t0_t51

	c_t010 = S.Task('c_t010', length=4, delay_cost=1)
	c_t010 += alt(MAS)
	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	c_t010_in += alt(MAS_in)
	S += c_t010_in*MAS_in[0]<=c_t010*MAS[0]

	S += c_t010_in*MAS_in[1]<=c_t010*MAS[1]

	S += c_t010_in*MAS_in[2]<=c_t010*MAS[2]

	S += c_t010_in*MAS_in[3]<=c_t010*MAS[3]

	S += c_t010_in*MAS_in[4]<=c_t010*MAS[4]

	S += c_t010_in*MAS_in[5]<=c_t010*MAS[5]

	S += c_t010_in*MAS_in[6]<=c_t010*MAS[6]

	S += c_t010_in*MAS_in[7]<=c_t010*MAS[7]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	c_t010_mem0 += MAS_MEM[2]
	S += 47 < c_t010_mem0
	S += c_t010_mem0 <= c_t010

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	c_t010_mem1 += MAS_MEM[13]
	S += 48 < c_t010_mem1
	S += c_t010_mem1 <= c_t010

	c_t1_t41 = S.Task('c_t1_t41', length=4, delay_cost=1)
	c_t1_t41 += alt(MAS)
	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	c_t1_t41_in += alt(MAS_in)
	S += c_t1_t41_in*MAS_in[0]<=c_t1_t41*MAS[0]

	S += c_t1_t41_in*MAS_in[1]<=c_t1_t41*MAS[1]

	S += c_t1_t41_in*MAS_in[2]<=c_t1_t41*MAS[2]

	S += c_t1_t41_in*MAS_in[3]<=c_t1_t41*MAS[3]

	S += c_t1_t41_in*MAS_in[4]<=c_t1_t41*MAS[4]

	S += c_t1_t41_in*MAS_in[5]<=c_t1_t41*MAS[5]

	S += c_t1_t41_in*MAS_in[6]<=c_t1_t41*MAS[6]

	S += c_t1_t41_in*MAS_in[7]<=c_t1_t41*MAS[7]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	c_t1_t41_mem0 += MM_MEM[0]
	S += 38 < c_t1_t41_mem0
	S += c_t1_t41_mem0 <= c_t1_t41

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	c_t1_t41_mem1 += MAS_MEM[11]
	S += 37 < c_t1_t41_mem1
	S += c_t1_t41_mem1 <= c_t1_t41

	c_t1_s00 = S.Task('c_t1_s00', length=4, delay_cost=1)
	c_t1_s00 += alt(MAS)
	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	c_t1_s00_in += alt(MAS_in)
	S += c_t1_s00_in*MAS_in[0]<=c_t1_s00*MAS[0]

	S += c_t1_s00_in*MAS_in[1]<=c_t1_s00*MAS[1]

	S += c_t1_s00_in*MAS_in[2]<=c_t1_s00*MAS[2]

	S += c_t1_s00_in*MAS_in[3]<=c_t1_s00*MAS[3]

	S += c_t1_s00_in*MAS_in[4]<=c_t1_s00*MAS[4]

	S += c_t1_s00_in*MAS_in[5]<=c_t1_s00*MAS[5]

	S += c_t1_s00_in*MAS_in[6]<=c_t1_s00*MAS[6]

	S += c_t1_s00_in*MAS_in[7]<=c_t1_s00*MAS[7]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	c_t1_s00_mem0 += MAS_MEM[0]
	S += 22 < c_t1_s00_mem0
	S += c_t1_s00_mem0 <= c_t1_s00

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	c_t1_s00_mem1 += MAS_MEM[13]
	S += 36 < c_t1_s00_mem1
	S += c_t1_s00_mem1 <= c_t1_s00

	c_t1_s01 = S.Task('c_t1_s01', length=4, delay_cost=1)
	c_t1_s01 += alt(MAS)
	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	c_t1_s01_in += alt(MAS_in)
	S += c_t1_s01_in*MAS_in[0]<=c_t1_s01*MAS[0]

	S += c_t1_s01_in*MAS_in[1]<=c_t1_s01*MAS[1]

	S += c_t1_s01_in*MAS_in[2]<=c_t1_s01*MAS[2]

	S += c_t1_s01_in*MAS_in[3]<=c_t1_s01*MAS[3]

	S += c_t1_s01_in*MAS_in[4]<=c_t1_s01*MAS[4]

	S += c_t1_s01_in*MAS_in[5]<=c_t1_s01*MAS[5]

	S += c_t1_s01_in*MAS_in[6]<=c_t1_s01*MAS[6]

	S += c_t1_s01_in*MAS_in[7]<=c_t1_s01*MAS[7]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	c_t1_s01_mem0 += MAS_MEM[12]
	S += 36 < c_t1_s01_mem0
	S += c_t1_s01_mem0 <= c_t1_s01

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	c_t1_s01_mem1 += MAS_MEM[1]
	S += 22 < c_t1_s01_mem1
	S += c_t1_s01_mem1 <= c_t1_s01

	c_t1_t51 = S.Task('c_t1_t51', length=4, delay_cost=1)
	c_t1_t51 += alt(MAS)
	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	c_t1_t51_in += alt(MAS_in)
	S += c_t1_t51_in*MAS_in[0]<=c_t1_t51*MAS[0]

	S += c_t1_t51_in*MAS_in[1]<=c_t1_t51*MAS[1]

	S += c_t1_t51_in*MAS_in[2]<=c_t1_t51*MAS[2]

	S += c_t1_t51_in*MAS_in[3]<=c_t1_t51*MAS[3]

	S += c_t1_t51_in*MAS_in[4]<=c_t1_t51*MAS[4]

	S += c_t1_t51_in*MAS_in[5]<=c_t1_t51*MAS[5]

	S += c_t1_t51_in*MAS_in[6]<=c_t1_t51*MAS[6]

	S += c_t1_t51_in*MAS_in[7]<=c_t1_t51*MAS[7]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	c_t1_t51_mem0 += MAS_MEM[0]
	S += 43 < c_t1_t51_mem0
	S += c_t1_t51_mem0 <= c_t1_t51

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	c_t1_t51_mem1 += MAS_MEM[13]
	S += 36 < c_t1_t51_mem1
	S += c_t1_t51_mem1 <= c_t1_t51

	c_t110 = S.Task('c_t110', length=4, delay_cost=1)
	c_t110 += alt(MAS)
	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	c_t110_in += alt(MAS_in)
	S += c_t110_in*MAS_in[0]<=c_t110*MAS[0]

	S += c_t110_in*MAS_in[1]<=c_t110*MAS[1]

	S += c_t110_in*MAS_in[2]<=c_t110*MAS[2]

	S += c_t110_in*MAS_in[3]<=c_t110*MAS[3]

	S += c_t110_in*MAS_in[4]<=c_t110*MAS[4]

	S += c_t110_in*MAS_in[5]<=c_t110*MAS[5]

	S += c_t110_in*MAS_in[6]<=c_t110*MAS[6]

	S += c_t110_in*MAS_in[7]<=c_t110*MAS[7]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	c_t110_mem0 += MAS_MEM[0]
	S += 38 < c_t110_mem0
	S += c_t110_mem0 <= c_t110

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	c_t110_mem1 += MAS_MEM[13]
	S += 42 < c_t110_mem1
	S += c_t110_mem1 <= c_t110

	c_t2_t41 = S.Task('c_t2_t41', length=4, delay_cost=1)
	c_t2_t41 += alt(MAS)
	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	c_t2_t41_in += alt(MAS_in)
	S += c_t2_t41_in*MAS_in[0]<=c_t2_t41*MAS[0]

	S += c_t2_t41_in*MAS_in[1]<=c_t2_t41*MAS[1]

	S += c_t2_t41_in*MAS_in[2]<=c_t2_t41*MAS[2]

	S += c_t2_t41_in*MAS_in[3]<=c_t2_t41*MAS[3]

	S += c_t2_t41_in*MAS_in[4]<=c_t2_t41*MAS[4]

	S += c_t2_t41_in*MAS_in[5]<=c_t2_t41*MAS[5]

	S += c_t2_t41_in*MAS_in[6]<=c_t2_t41*MAS[6]

	S += c_t2_t41_in*MAS_in[7]<=c_t2_t41*MAS[7]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	c_t2_t41_mem0 += MM_MEM[2]
	S += 77 < c_t2_t41_mem0
	S += c_t2_t41_mem0 <= c_t2_t41

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	c_t2_t41_mem1 += MAS_MEM[3]
	S += 77 < c_t2_t41_mem1
	S += c_t2_t41_mem1 <= c_t2_t41

	c_t2_s00 = S.Task('c_t2_s00', length=4, delay_cost=1)
	c_t2_s00 += alt(MAS)
	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	c_t2_s00_in += alt(MAS_in)
	S += c_t2_s00_in*MAS_in[0]<=c_t2_s00*MAS[0]

	S += c_t2_s00_in*MAS_in[1]<=c_t2_s00*MAS[1]

	S += c_t2_s00_in*MAS_in[2]<=c_t2_s00*MAS[2]

	S += c_t2_s00_in*MAS_in[3]<=c_t2_s00*MAS[3]

	S += c_t2_s00_in*MAS_in[4]<=c_t2_s00*MAS[4]

	S += c_t2_s00_in*MAS_in[5]<=c_t2_s00*MAS[5]

	S += c_t2_s00_in*MAS_in[6]<=c_t2_s00*MAS[6]

	S += c_t2_s00_in*MAS_in[7]<=c_t2_s00*MAS[7]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	c_t2_s00_mem0 += MAS_MEM[10]
	S += 31 < c_t2_s00_mem0
	S += c_t2_s00_mem0 <= c_t2_s00

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	c_t2_s00_mem1 += MAS_MEM[11]
	S += 74 < c_t2_s00_mem1
	S += c_t2_s00_mem1 <= c_t2_s00

	c_t2_s01 = S.Task('c_t2_s01', length=4, delay_cost=1)
	c_t2_s01 += alt(MAS)
	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	c_t2_s01_in += alt(MAS_in)
	S += c_t2_s01_in*MAS_in[0]<=c_t2_s01*MAS[0]

	S += c_t2_s01_in*MAS_in[1]<=c_t2_s01*MAS[1]

	S += c_t2_s01_in*MAS_in[2]<=c_t2_s01*MAS[2]

	S += c_t2_s01_in*MAS_in[3]<=c_t2_s01*MAS[3]

	S += c_t2_s01_in*MAS_in[4]<=c_t2_s01*MAS[4]

	S += c_t2_s01_in*MAS_in[5]<=c_t2_s01*MAS[5]

	S += c_t2_s01_in*MAS_in[6]<=c_t2_s01*MAS[6]

	S += c_t2_s01_in*MAS_in[7]<=c_t2_s01*MAS[7]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	c_t2_s01_mem0 += MAS_MEM[10]
	S += 74 < c_t2_s01_mem0
	S += c_t2_s01_mem0 <= c_t2_s01

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	c_t2_s01_mem1 += MAS_MEM[11]
	S += 31 < c_t2_s01_mem1
	S += c_t2_s01_mem1 <= c_t2_s01

	c_t2_t51 = S.Task('c_t2_t51', length=4, delay_cost=1)
	c_t2_t51 += alt(MAS)
	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	c_t2_t51_in += alt(MAS_in)
	S += c_t2_t51_in*MAS_in[0]<=c_t2_t51*MAS[0]

	S += c_t2_t51_in*MAS_in[1]<=c_t2_t51*MAS[1]

	S += c_t2_t51_in*MAS_in[2]<=c_t2_t51*MAS[2]

	S += c_t2_t51_in*MAS_in[3]<=c_t2_t51*MAS[3]

	S += c_t2_t51_in*MAS_in[4]<=c_t2_t51*MAS[4]

	S += c_t2_t51_in*MAS_in[5]<=c_t2_t51*MAS[5]

	S += c_t2_t51_in*MAS_in[6]<=c_t2_t51*MAS[6]

	S += c_t2_t51_in*MAS_in[7]<=c_t2_t51*MAS[7]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	c_t2_t51_mem0 += MAS_MEM[0]
	S += 41 < c_t2_t51_mem0
	S += c_t2_t51_mem0 <= c_t2_t51

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	c_t2_t51_mem1 += MAS_MEM[11]
	S += 74 < c_t2_t51_mem1
	S += c_t2_t51_mem1 <= c_t2_t51

	c_t210 = S.Task('c_t210', length=4, delay_cost=1)
	c_t210 += alt(MAS)
	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	c_t210_in += alt(MAS_in)
	S += c_t210_in*MAS_in[0]<=c_t210*MAS[0]

	S += c_t210_in*MAS_in[1]<=c_t210*MAS[1]

	S += c_t210_in*MAS_in[2]<=c_t210*MAS[2]

	S += c_t210_in*MAS_in[3]<=c_t210*MAS[3]

	S += c_t210_in*MAS_in[4]<=c_t210*MAS[4]

	S += c_t210_in*MAS_in[5]<=c_t210*MAS[5]

	S += c_t210_in*MAS_in[6]<=c_t210*MAS[6]

	S += c_t210_in*MAS_in[7]<=c_t210*MAS[7]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	c_t210_mem0 += MAS_MEM[2]
	S += 79 < c_t210_mem0
	S += c_t210_mem0 <= c_t210

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	c_t210_mem1 += MAS_MEM[11]
	S += 35 < c_t210_mem1
	S += c_t210_mem1 <= c_t210

	c_t3_t01 = S.Task('c_t3_t01', length=4, delay_cost=1)
	c_t3_t01 += alt(MAS)
	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	c_t3_t01_in += alt(MAS_in)
	S += c_t3_t01_in*MAS_in[0]<=c_t3_t01*MAS[0]

	S += c_t3_t01_in*MAS_in[1]<=c_t3_t01*MAS[1]

	S += c_t3_t01_in*MAS_in[2]<=c_t3_t01*MAS[2]

	S += c_t3_t01_in*MAS_in[3]<=c_t3_t01*MAS[3]

	S += c_t3_t01_in*MAS_in[4]<=c_t3_t01*MAS[4]

	S += c_t3_t01_in*MAS_in[5]<=c_t3_t01*MAS[5]

	S += c_t3_t01_in*MAS_in[6]<=c_t3_t01*MAS[6]

	S += c_t3_t01_in*MAS_in[7]<=c_t3_t01*MAS[7]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	c_t3_t01_mem0 += MM_MEM[0]
	S += 74 < c_t3_t01_mem0
	S += c_t3_t01_mem0 <= c_t3_t01

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	c_t3_t01_mem1 += MAS_MEM[3]
	S += 69 < c_t3_t01_mem1
	S += c_t3_t01_mem1 <= c_t3_t01

	c_t3_t11 = S.Task('c_t3_t11', length=4, delay_cost=1)
	c_t3_t11 += alt(MAS)
	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	c_t3_t11_in += alt(MAS_in)
	S += c_t3_t11_in*MAS_in[0]<=c_t3_t11*MAS[0]

	S += c_t3_t11_in*MAS_in[1]<=c_t3_t11*MAS[1]

	S += c_t3_t11_in*MAS_in[2]<=c_t3_t11*MAS[2]

	S += c_t3_t11_in*MAS_in[3]<=c_t3_t11*MAS[3]

	S += c_t3_t11_in*MAS_in[4]<=c_t3_t11*MAS[4]

	S += c_t3_t11_in*MAS_in[5]<=c_t3_t11*MAS[5]

	S += c_t3_t11_in*MAS_in[6]<=c_t3_t11*MAS[6]

	S += c_t3_t11_in*MAS_in[7]<=c_t3_t11*MAS[7]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	c_t3_t11_mem0 += MM_MEM[0]
	S += 64 < c_t3_t11_mem0
	S += c_t3_t11_mem0 <= c_t3_t11

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	c_t3_t11_mem1 += MAS_MEM[3]
	S += 66 < c_t3_t11_mem1
	S += c_t3_t11_mem1 <= c_t3_t11

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=10, delay_cost=1)
	c_t3_t4_t4 += alt(MM)
	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	c_t3_t4_t4_in += alt(MM_in)
	S += c_t3_t4_t4_in*MM_in[0]<=c_t3_t4_t4*MM[0]
	S += c_t3_t4_t4_in*MM_in[1]<=c_t3_t4_t4*MM[1]
	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	c_t3_t4_t4_mem0 += MAS_MEM[12]
	S += 59 < c_t3_t4_t4_mem0
	S += c_t3_t4_t4_mem0 <= c_t3_t4_t4

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	c_t3_t4_t4_mem1 += MAS_MEM[7]
	S += 63 < c_t3_t4_t4_mem1
	S += c_t3_t4_t4_mem1 <= c_t3_t4_t4

	c_t3_t40 = S.Task('c_t3_t40', length=4, delay_cost=1)
	c_t3_t40 += alt(MAS)
	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	c_t3_t40_in += alt(MAS_in)
	S += c_t3_t40_in*MAS_in[0]<=c_t3_t40*MAS[0]

	S += c_t3_t40_in*MAS_in[1]<=c_t3_t40*MAS[1]

	S += c_t3_t40_in*MAS_in[2]<=c_t3_t40*MAS[2]

	S += c_t3_t40_in*MAS_in[3]<=c_t3_t40*MAS[3]

	S += c_t3_t40_in*MAS_in[4]<=c_t3_t40*MAS[4]

	S += c_t3_t40_in*MAS_in[5]<=c_t3_t40*MAS[5]

	S += c_t3_t40_in*MAS_in[6]<=c_t3_t40*MAS[6]

	S += c_t3_t40_in*MAS_in[7]<=c_t3_t40*MAS[7]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	c_t3_t40_mem0 += MM_MEM[0]
	S += 67 < c_t3_t40_mem0
	S += c_t3_t40_mem0 <= c_t3_t40

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	c_t3_t40_mem1 += MM_MEM[1]
	S += 68 < c_t3_t40_mem1
	S += c_t3_t40_mem1 <= c_t3_t40

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=4, delay_cost=1)
	c_t3_t4_t5 += alt(MAS)
	c_t3_t4_t5_in = S.Task('c_t3_t4_t5_in', length=1, delay_cost=1)
	c_t3_t4_t5_in += alt(MAS_in)
	S += c_t3_t4_t5_in*MAS_in[0]<=c_t3_t4_t5*MAS[0]

	S += c_t3_t4_t5_in*MAS_in[1]<=c_t3_t4_t5*MAS[1]

	S += c_t3_t4_t5_in*MAS_in[2]<=c_t3_t4_t5*MAS[2]

	S += c_t3_t4_t5_in*MAS_in[3]<=c_t3_t4_t5*MAS[3]

	S += c_t3_t4_t5_in*MAS_in[4]<=c_t3_t4_t5*MAS[4]

	S += c_t3_t4_t5_in*MAS_in[5]<=c_t3_t4_t5*MAS[5]

	S += c_t3_t4_t5_in*MAS_in[6]<=c_t3_t4_t5*MAS[6]

	S += c_t3_t4_t5_in*MAS_in[7]<=c_t3_t4_t5*MAS[7]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	c_t3_t4_t5_mem0 += MM_MEM[0]
	S += 67 < c_t3_t4_t5_mem0
	S += c_t3_t4_t5_mem0 <= c_t3_t4_t5

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	c_t3_t4_t5_mem1 += MM_MEM[1]
	S += 68 < c_t3_t4_t5_mem1
	S += c_t3_t4_t5_mem1 <= c_t3_t4_t5

	c_t3_t50 = S.Task('c_t3_t50', length=4, delay_cost=1)
	c_t3_t50 += alt(MAS)
	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	c_t3_t50_in += alt(MAS_in)
	S += c_t3_t50_in*MAS_in[0]<=c_t3_t50*MAS[0]

	S += c_t3_t50_in*MAS_in[1]<=c_t3_t50*MAS[1]

	S += c_t3_t50_in*MAS_in[2]<=c_t3_t50*MAS[2]

	S += c_t3_t50_in*MAS_in[3]<=c_t3_t50*MAS[3]

	S += c_t3_t50_in*MAS_in[4]<=c_t3_t50*MAS[4]

	S += c_t3_t50_in*MAS_in[5]<=c_t3_t50*MAS[5]

	S += c_t3_t50_in*MAS_in[6]<=c_t3_t50*MAS[6]

	S += c_t3_t50_in*MAS_in[7]<=c_t3_t50*MAS[7]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	c_t3_t50_mem0 += MAS_MEM[2]
	S += 68 < c_t3_t50_mem0
	S += c_t3_t50_mem0 <= c_t3_t50

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	c_t3_t50_mem1 += MAS_MEM[3]
	S += 65 < c_t3_t50_mem1
	S += c_t3_t50_mem1 <= c_t3_t50

	c_t4_t01 = S.Task('c_t4_t01', length=4, delay_cost=1)
	c_t4_t01 += alt(MAS)
	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	c_t4_t01_in += alt(MAS_in)
	S += c_t4_t01_in*MAS_in[0]<=c_t4_t01*MAS[0]

	S += c_t4_t01_in*MAS_in[1]<=c_t4_t01*MAS[1]

	S += c_t4_t01_in*MAS_in[2]<=c_t4_t01*MAS[2]

	S += c_t4_t01_in*MAS_in[3]<=c_t4_t01*MAS[3]

	S += c_t4_t01_in*MAS_in[4]<=c_t4_t01*MAS[4]

	S += c_t4_t01_in*MAS_in[5]<=c_t4_t01*MAS[5]

	S += c_t4_t01_in*MAS_in[6]<=c_t4_t01*MAS[6]

	S += c_t4_t01_in*MAS_in[7]<=c_t4_t01*MAS[7]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	c_t4_t01_mem0 += MM_MEM[2]
	S += 75 < c_t4_t01_mem0
	S += c_t4_t01_mem0 <= c_t4_t01

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	c_t4_t01_mem1 += MAS_MEM[11]
	S += 78 < c_t4_t01_mem1
	S += c_t4_t01_mem1 <= c_t4_t01

	c_t4_t11 = S.Task('c_t4_t11', length=4, delay_cost=1)
	c_t4_t11 += alt(MAS)
	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	c_t4_t11_in += alt(MAS_in)
	S += c_t4_t11_in*MAS_in[0]<=c_t4_t11*MAS[0]

	S += c_t4_t11_in*MAS_in[1]<=c_t4_t11*MAS[1]

	S += c_t4_t11_in*MAS_in[2]<=c_t4_t11*MAS[2]

	S += c_t4_t11_in*MAS_in[3]<=c_t4_t11*MAS[3]

	S += c_t4_t11_in*MAS_in[4]<=c_t4_t11*MAS[4]

	S += c_t4_t11_in*MAS_in[5]<=c_t4_t11*MAS[5]

	S += c_t4_t11_in*MAS_in[6]<=c_t4_t11*MAS[6]

	S += c_t4_t11_in*MAS_in[7]<=c_t4_t11*MAS[7]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	c_t4_t11_mem0 += MM_MEM[0]
	S += 77 < c_t4_t11_mem0
	S += c_t4_t11_mem0 <= c_t4_t11

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	c_t4_t11_mem1 += MAS_MEM[7]
	S += 80 < c_t4_t11_mem1
	S += c_t4_t11_mem1 <= c_t4_t11

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=10, delay_cost=1)
	c_t4_t4_t4 += alt(MM)
	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	c_t4_t4_t4_in += alt(MM_in)
	S += c_t4_t4_t4_in*MM_in[0]<=c_t4_t4_t4*MM[0]
	S += c_t4_t4_t4_in*MM_in[1]<=c_t4_t4_t4*MM[1]
	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	c_t4_t4_t4_mem0 += MAS_MEM[10]
	S += 70 < c_t4_t4_t4_mem0
	S += c_t4_t4_t4_mem0 <= c_t4_t4_t4

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	c_t4_t4_t4_mem1 += MAS_MEM[11]
	S += 73 < c_t4_t4_t4_mem1
	S += c_t4_t4_t4_mem1 <= c_t4_t4_t4

	c_t4_t40 = S.Task('c_t4_t40', length=4, delay_cost=1)
	c_t4_t40 += alt(MAS)
	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	c_t4_t40_in += alt(MAS_in)
	S += c_t4_t40_in*MAS_in[0]<=c_t4_t40*MAS[0]

	S += c_t4_t40_in*MAS_in[1]<=c_t4_t40*MAS[1]

	S += c_t4_t40_in*MAS_in[2]<=c_t4_t40*MAS[2]

	S += c_t4_t40_in*MAS_in[3]<=c_t4_t40*MAS[3]

	S += c_t4_t40_in*MAS_in[4]<=c_t4_t40*MAS[4]

	S += c_t4_t40_in*MAS_in[5]<=c_t4_t40*MAS[5]

	S += c_t4_t40_in*MAS_in[6]<=c_t4_t40*MAS[6]

	S += c_t4_t40_in*MAS_in[7]<=c_t4_t40*MAS[7]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	c_t4_t40_mem0 += MM_MEM[2]
	S += 68 < c_t4_t40_mem0
	S += c_t4_t40_mem0 <= c_t4_t40

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	c_t4_t40_mem1 += MM_MEM[1]
	S += 78 < c_t4_t40_mem1
	S += c_t4_t40_mem1 <= c_t4_t40

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=4, delay_cost=1)
	c_t4_t4_t5 += alt(MAS)
	c_t4_t4_t5_in = S.Task('c_t4_t4_t5_in', length=1, delay_cost=1)
	c_t4_t4_t5_in += alt(MAS_in)
	S += c_t4_t4_t5_in*MAS_in[0]<=c_t4_t4_t5*MAS[0]

	S += c_t4_t4_t5_in*MAS_in[1]<=c_t4_t4_t5*MAS[1]

	S += c_t4_t4_t5_in*MAS_in[2]<=c_t4_t4_t5*MAS[2]

	S += c_t4_t4_t5_in*MAS_in[3]<=c_t4_t4_t5*MAS[3]

	S += c_t4_t4_t5_in*MAS_in[4]<=c_t4_t4_t5*MAS[4]

	S += c_t4_t4_t5_in*MAS_in[5]<=c_t4_t4_t5*MAS[5]

	S += c_t4_t4_t5_in*MAS_in[6]<=c_t4_t4_t5*MAS[6]

	S += c_t4_t4_t5_in*MAS_in[7]<=c_t4_t4_t5*MAS[7]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	c_t4_t4_t5_mem0 += MM_MEM[2]
	S += 68 < c_t4_t4_t5_mem0
	S += c_t4_t4_t5_mem0 <= c_t4_t4_t5

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	c_t4_t4_t5_mem1 += MM_MEM[1]
	S += 78 < c_t4_t4_t5_mem1
	S += c_t4_t4_t5_mem1 <= c_t4_t4_t5

	c_t4_t50 = S.Task('c_t4_t50', length=4, delay_cost=1)
	c_t4_t50 += alt(MAS)
	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	c_t4_t50_in += alt(MAS_in)
	S += c_t4_t50_in*MAS_in[0]<=c_t4_t50*MAS[0]

	S += c_t4_t50_in*MAS_in[1]<=c_t4_t50*MAS[1]

	S += c_t4_t50_in*MAS_in[2]<=c_t4_t50*MAS[2]

	S += c_t4_t50_in*MAS_in[3]<=c_t4_t50*MAS[3]

	S += c_t4_t50_in*MAS_in[4]<=c_t4_t50*MAS[4]

	S += c_t4_t50_in*MAS_in[5]<=c_t4_t50*MAS[5]

	S += c_t4_t50_in*MAS_in[6]<=c_t4_t50*MAS[6]

	S += c_t4_t50_in*MAS_in[7]<=c_t4_t50*MAS[7]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	c_t4_t50_mem0 += MAS_MEM[10]
	S += 75 < c_t4_t50_mem0
	S += c_t4_t50_mem0 <= c_t4_t50

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	c_t4_t50_mem1 += MAS_MEM[11]
	S += 76 < c_t4_t50_mem1
	S += c_t4_t50_mem1 <= c_t4_t50

	c_t5_t01 = S.Task('c_t5_t01', length=4, delay_cost=1)
	c_t5_t01 += alt(MAS)
	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	c_t5_t01_in += alt(MAS_in)
	S += c_t5_t01_in*MAS_in[0]<=c_t5_t01*MAS[0]

	S += c_t5_t01_in*MAS_in[1]<=c_t5_t01*MAS[1]

	S += c_t5_t01_in*MAS_in[2]<=c_t5_t01*MAS[2]

	S += c_t5_t01_in*MAS_in[3]<=c_t5_t01*MAS[3]

	S += c_t5_t01_in*MAS_in[4]<=c_t5_t01*MAS[4]

	S += c_t5_t01_in*MAS_in[5]<=c_t5_t01*MAS[5]

	S += c_t5_t01_in*MAS_in[6]<=c_t5_t01*MAS[6]

	S += c_t5_t01_in*MAS_in[7]<=c_t5_t01*MAS[7]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	c_t5_t01_mem0 += MM_MEM[0]
	S += 73 < c_t5_t01_mem0
	S += c_t5_t01_mem0 <= c_t5_t01

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	c_t5_t01_mem1 += MAS_MEM[1]
	S += 75 < c_t5_t01_mem1
	S += c_t5_t01_mem1 <= c_t5_t01

	c_t5_t11 = S.Task('c_t5_t11', length=4, delay_cost=1)
	c_t5_t11 += alt(MAS)
	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	c_t5_t11_in += alt(MAS_in)
	S += c_t5_t11_in*MAS_in[0]<=c_t5_t11*MAS[0]

	S += c_t5_t11_in*MAS_in[1]<=c_t5_t11*MAS[1]

	S += c_t5_t11_in*MAS_in[2]<=c_t5_t11*MAS[2]

	S += c_t5_t11_in*MAS_in[3]<=c_t5_t11*MAS[3]

	S += c_t5_t11_in*MAS_in[4]<=c_t5_t11*MAS[4]

	S += c_t5_t11_in*MAS_in[5]<=c_t5_t11*MAS[5]

	S += c_t5_t11_in*MAS_in[6]<=c_t5_t11*MAS[6]

	S += c_t5_t11_in*MAS_in[7]<=c_t5_t11*MAS[7]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	c_t5_t11_mem0 += MM_MEM[0]
	S += 71 < c_t5_t11_mem0
	S += c_t5_t11_mem0 <= c_t5_t11

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	c_t5_t11_mem1 += MAS_MEM[1]
	S += 76 < c_t5_t11_mem1
	S += c_t5_t11_mem1 <= c_t5_t11

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=10, delay_cost=1)
	c_t5_t4_t4 += alt(MM)
	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	c_t5_t4_t4_in += alt(MM_in)
	S += c_t5_t4_t4_in*MM_in[0]<=c_t5_t4_t4*MM[0]
	S += c_t5_t4_t4_in*MM_in[1]<=c_t5_t4_t4*MM[1]
	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	c_t5_t4_t4_mem0 += MAS_MEM[8]
	S += 67 < c_t5_t4_t4_mem0
	S += c_t5_t4_t4_mem0 <= c_t5_t4_t4

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	c_t5_t4_t4_mem1 += MAS_MEM[3]
	S += 70 < c_t5_t4_t4_mem1
	S += c_t5_t4_t4_mem1 <= c_t5_t4_t4

	c_t5_t40 = S.Task('c_t5_t40', length=4, delay_cost=1)
	c_t5_t40 += alt(MAS)
	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	c_t5_t40_in += alt(MAS_in)
	S += c_t5_t40_in*MAS_in[0]<=c_t5_t40*MAS[0]

	S += c_t5_t40_in*MAS_in[1]<=c_t5_t40*MAS[1]

	S += c_t5_t40_in*MAS_in[2]<=c_t5_t40*MAS[2]

	S += c_t5_t40_in*MAS_in[3]<=c_t5_t40*MAS[3]

	S += c_t5_t40_in*MAS_in[4]<=c_t5_t40*MAS[4]

	S += c_t5_t40_in*MAS_in[5]<=c_t5_t40*MAS[5]

	S += c_t5_t40_in*MAS_in[6]<=c_t5_t40*MAS[6]

	S += c_t5_t40_in*MAS_in[7]<=c_t5_t40*MAS[7]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	c_t5_t40_mem0 += MM_MEM[0]
	S += 72 < c_t5_t40_mem0
	S += c_t5_t40_mem0 <= c_t5_t40

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	c_t5_t40_mem1 += MM_MEM[3]
	S += 74 < c_t5_t40_mem1
	S += c_t5_t40_mem1 <= c_t5_t40

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=4, delay_cost=1)
	c_t5_t4_t5 += alt(MAS)
	c_t5_t4_t5_in = S.Task('c_t5_t4_t5_in', length=1, delay_cost=1)
	c_t5_t4_t5_in += alt(MAS_in)
	S += c_t5_t4_t5_in*MAS_in[0]<=c_t5_t4_t5*MAS[0]

	S += c_t5_t4_t5_in*MAS_in[1]<=c_t5_t4_t5*MAS[1]

	S += c_t5_t4_t5_in*MAS_in[2]<=c_t5_t4_t5*MAS[2]

	S += c_t5_t4_t5_in*MAS_in[3]<=c_t5_t4_t5*MAS[3]

	S += c_t5_t4_t5_in*MAS_in[4]<=c_t5_t4_t5*MAS[4]

	S += c_t5_t4_t5_in*MAS_in[5]<=c_t5_t4_t5*MAS[5]

	S += c_t5_t4_t5_in*MAS_in[6]<=c_t5_t4_t5*MAS[6]

	S += c_t5_t4_t5_in*MAS_in[7]<=c_t5_t4_t5*MAS[7]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	c_t5_t4_t5_mem0 += MM_MEM[0]
	S += 72 < c_t5_t4_t5_mem0
	S += c_t5_t4_t5_mem0 <= c_t5_t4_t5

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	c_t5_t4_t5_mem1 += MM_MEM[3]
	S += 74 < c_t5_t4_t5_mem1
	S += c_t5_t4_t5_mem1 <= c_t5_t4_t5

	c_t5_t50 = S.Task('c_t5_t50', length=4, delay_cost=1)
	c_t5_t50 += alt(MAS)
	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	c_t5_t50_in += alt(MAS_in)
	S += c_t5_t50_in*MAS_in[0]<=c_t5_t50*MAS[0]

	S += c_t5_t50_in*MAS_in[1]<=c_t5_t50*MAS[1]

	S += c_t5_t50_in*MAS_in[2]<=c_t5_t50*MAS[2]

	S += c_t5_t50_in*MAS_in[3]<=c_t5_t50*MAS[3]

	S += c_t5_t50_in*MAS_in[4]<=c_t5_t50*MAS[4]

	S += c_t5_t50_in*MAS_in[5]<=c_t5_t50*MAS[5]

	S += c_t5_t50_in*MAS_in[6]<=c_t5_t50*MAS[6]

	S += c_t5_t50_in*MAS_in[7]<=c_t5_t50*MAS[7]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	c_t5_t50_mem0 += MAS_MEM[8]
	S += 74 < c_t5_t50_mem0
	S += c_t5_t50_mem0 <= c_t5_t50

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	c_t5_t50_mem1 += MAS_MEM[9]
	S += 73 < c_t5_t50_mem1
	S += c_t5_t50_mem1 <= c_t5_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS8/MUL/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

