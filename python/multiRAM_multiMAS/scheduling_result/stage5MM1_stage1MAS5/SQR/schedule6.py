from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 155
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 0
	c_t0_t3_t1_in += MM_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 0
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 0
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=5, delay_cost=1)
	S += c_t0_t3_t1 >= 1
	c_t0_t3_t1 += MM[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 1
	c_t1_t3_t1_in += MM_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 1
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 1
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 2
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 2
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 2
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=5, delay_cost=1)
	S += c_t1_t3_t1 >= 2
	c_t1_t3_t1 += MM[0]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 3
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 3
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 3
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=5, delay_cost=1)
	S += c_t1_t3_t0 >= 3
	c_t1_t3_t0 += MM[0]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=5, delay_cost=1)
	S += c_t0_t3_t0 >= 4
	c_t0_t3_t0 += MM[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 4
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 4
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 5
	c_t1_t10 += MAS[2]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 5
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 5
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=1, delay_cost=1)
	S += c_t2_a1_1 >= 6
	c_t2_a1_1 += MAS[0]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 6
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 6
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 7
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 7
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 7
	c_t1_t3_t5_mem0 += MM_MEM[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 7
	c_t1_t3_t5_mem1 += MM_MEM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 7
	c_t2_t10 += MAS[3]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 8
	c_t0_t10 += MAS[4]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 8
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 8
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 8
	c_t0_t3_t5_mem0 += MM_MEM[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 8
	c_t0_t3_t5_mem1 += MM_MEM[1]

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=1, delay_cost=1)
	S += c_t1_t3_t5 >= 8
	c_t1_t3_t5 += MAS[2]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	S += c_t0_t3_t2 >= 9
	c_t0_t3_t2 += MAS[1]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=1, delay_cost=1)
	S += c_t0_t3_t5 >= 9
	c_t0_t3_t5 += MAS[3]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 9
	c_t1_t30_mem0 += MM_MEM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 9
	c_t1_t30_mem1 += MM_MEM[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 9
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 9
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 10
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 10
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 10
	c_t0_t30_mem0 += MM_MEM[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 10
	c_t0_t30_mem1 += MM_MEM[1]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 10
	c_t1_t30 += MAS[3]

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 10
	c_t2_t11 += MAS[2]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 10
	c_t2_t2_t3_mem0 += MAS_MEM[6]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 10
	c_t2_t2_t3_mem1 += MAS_MEM[5]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 11
	c_t010_mem0 += MAS_MEM[0]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 11
	c_t010_mem1 += MAS_MEM[1]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 11
	c_t0_t11 += MAS[1]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 11
	c_t0_t2_t3_mem0 += MAS_MEM[8]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 11
	c_t0_t2_t3_mem1 += MAS_MEM[3]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 11
	c_t0_t30 += MAS[0]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 11
	c_t110_mem0 += MAS_MEM[6]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 11
	c_t110_mem1 += MAS_MEM[7]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 11
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 11
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=1, delay_cost=1)
	S += c_t2_t2_t3 >= 11
	c_t2_t2_t3 += MAS[4]

	c_s0010_mem0 = S.Task('c_s0010_mem0', length=1, delay_cost=1)
	S += c_s0010_mem0 >= 12
	c_s0010_mem0 += MAS_MEM[8]

	c_s0010_mem1 = S.Task('c_s0010_mem1', length=1, delay_cost=1)
	S += c_s0010_mem1 >= 12
	c_s0010_mem1 += MAS_MEM[5]

	c_t010 = S.Task('c_t010', length=1, delay_cost=1)
	S += c_t010 >= 12
	c_t010 += MAS[4]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=1, delay_cost=1)
	S += c_t0_t2_t3 >= 12
	c_t0_t2_t3 += MAS[1]

	c_t110 = S.Task('c_t110', length=1, delay_cost=1)
	S += c_t110 >= 12
	c_t110 += MAS[2]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	S += c_t1_t3_t2 >= 12
	c_t1_t3_t2 += MAS[0]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 12
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 12
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_s0010 = S.Task('c_s0010', length=1, delay_cost=1)
	S += c_s0010 >= 13
	c_s0010 += MAS[0]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 13
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 13
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=1, delay_cost=1)
	S += c_t2_a1_0 >= 13
	c_t2_a1_0 += MAS[3]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 14
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 14
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 14
	c_t1_t11 += MAS[0]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 14
	c_t1_t2_t3_mem0 += MAS_MEM[4]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 14
	c_t1_t2_t3_mem1 += MAS_MEM[1]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=1, delay_cost=1)
	S += c_t0_a1_0 >= 15
	c_t0_a1_0 += MAS[4]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 15
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 15
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=1, delay_cost=1)
	S += c_t1_t2_t3 >= 15
	c_t1_t2_t3 += MAS[0]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 16
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 16
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=1, delay_cost=1)
	S += c_t1_a1_0 >= 16
	c_t1_a1_0 += MAS[0]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	S += c_t0_t3_t3 >= 17
	c_t0_t3_t3 += MAS[0]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 17
	c_t0_t3_t4_in += MM_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 17
	c_t0_t3_t4_mem0 += MAS_MEM[2]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 17
	c_t0_t3_t4_mem1 += MAS_MEM[1]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 17
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 17
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 18
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 18
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=5, delay_cost=1)
	S += c_t0_t3_t4 >= 18
	c_t0_t3_t4 += MM[0]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=1, delay_cost=1)
	S += c_t1_a1_1 >= 18
	c_t1_a1_1 += MAS[2]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=1, delay_cost=1)
	S += c_t0_a1_1 >= 19
	c_t0_a1_1 += MAS[4]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 19
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 19
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	S += c_t1_t3_t3 >= 20
	c_t1_t3_t3 += MAS[1]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 20
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 20
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 20
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=5, delay_cost=1)
	S += c_t2_t3_t0 >= 21
	c_t2_t3_t0 += MM[0]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 21
	c_t2_t3_t1_in += MM_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 21
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 21
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 22
	c_t0_t31_mem0 += MM_MEM[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 22
	c_t0_t31_mem1 += MAS_MEM[7]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 22
	c_t1_t3_t4_in += MM_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 22
	c_t1_t3_t4_mem0 += MAS_MEM[0]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 22
	c_t1_t3_t4_mem1 += MAS_MEM[3]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=5, delay_cost=1)
	S += c_t2_t3_t1 >= 22
	c_t2_t3_t1 += MM[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 22
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 22
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 23
	c_t0_t31 += MAS[1]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 23
	c_t0_t40_mem0 += MAS_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 23
	c_t0_t40_mem1 += MAS_MEM[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 23
	c_t0_t41_mem0 += MAS_MEM[2]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 23
	c_t0_t41_mem1 += MAS_MEM[1]

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=5, delay_cost=1)
	S += c_t1_t3_t4 >= 23
	c_t1_t3_t4 += MM[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 23
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 23
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 23
	c_t5001 += MAS[3]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 24
	c_t011_mem0 += MAS_MEM[2]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 24
	c_t011_mem1 += MAS_MEM[3]

	c_t0_t40 = S.Task('c_t0_t40', length=1, delay_cost=1)
	S += c_t0_t40 >= 24
	c_t0_t40 += MAS[0]

	c_t0_t41 = S.Task('c_t0_t41', length=1, delay_cost=1)
	S += c_t0_t41 >= 24
	c_t0_t41 += MAS[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 24
	c_t0_t50_mem0 += MAS_MEM[0]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 24
	c_t0_t50_mem1 += MAS_MEM[1]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 24
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 24
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 24
	c_t3010 += MAS[1]

	c_t011 = S.Task('c_t011', length=1, delay_cost=1)
	S += c_t011 >= 25
	c_t011 += MAS[0]

	c_t0_t50 = S.Task('c_t0_t50', length=1, delay_cost=1)
	S += c_t0_t50 >= 25
	c_t0_t50 += MAS[1]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 25
	c_t0_t51_mem0 += MAS_MEM[2]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 25
	c_t0_t51_mem1 += MAS_MEM[7]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	S += c_t2_t3_t3 >= 25
	c_t2_t3_t3 += MAS[3]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 25
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 25
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t0_t51 = S.Task('c_t0_t51', length=1, delay_cost=1)
	S += c_t0_t51 >= 26
	c_t0_t51 += MAS[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 26
	c_t2_t30_mem0 += MM_MEM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 26
	c_t2_t30_mem1 += MM_MEM[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 26
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 26
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 26
	c_t5000 += MAS[3]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 26
	c_t5_t3_t2_mem0 += MAS_MEM[6]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 26
	c_t5_t3_t2_mem1 += MAS_MEM[7]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 27
	c_t210_mem0 += MAS_MEM[0]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 27
	c_t210_mem1 += MAS_MEM[1]

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 27
	c_t2_t30 += MAS[0]

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 27
	c_t2_t3_t5_mem0 += MM_MEM[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 27
	c_t2_t3_t5_mem1 += MM_MEM[1]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 27
	c_t4011 += MAS[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 27
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 27
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=1, delay_cost=1)
	S += c_t5_t3_t2 >= 27
	c_t5_t3_t2 += MAS[3]

	c_s1010_mem0 = S.Task('c_s1010_mem0', length=1, delay_cost=1)
	S += c_s1010_mem0 >= 28
	c_s1010_mem0 += MAS_MEM[4]

	c_s1010_mem1 = S.Task('c_s1010_mem1', length=1, delay_cost=1)
	S += c_s1010_mem1 >= 28
	c_s1010_mem1 += MAS_MEM[9]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 28
	c_t1_t31_mem0 += MM_MEM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 28
	c_t1_t31_mem1 += MAS_MEM[5]

	c_t210 = S.Task('c_t210', length=1, delay_cost=1)
	S += c_t210 >= 28
	c_t210 += MAS[4]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=1, delay_cost=1)
	S += c_t2_t3_t5 >= 28
	c_t2_t3_t5 += MAS[2]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 28
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 28
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 28
	c_t5011 += MAS[1]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 28
	c_t5_t3_t1_in += MM_in[0]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 28
	c_t5_t3_t1_mem0 += MAS_MEM[6]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 28
	c_t5_t3_t1_mem1 += MAS_MEM[3]

	c_s1010 = S.Task('c_s1010', length=1, delay_cost=1)
	S += c_s1010 >= 29
	c_s1010 += MAS[0]

	c_s2010_mem0 = S.Task('c_s2010_mem0', length=1, delay_cost=1)
	S += c_s2010_mem0 >= 29
	c_s2010_mem0 += MAS_MEM[8]

	c_s2010_mem1 = S.Task('c_s2010_mem1', length=1, delay_cost=1)
	S += c_s2010_mem1 >= 29
	c_s2010_mem1 += MAS_MEM[9]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 29
	c_t1_t31 += MAS[1]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 29
	c_t1_t41_mem0 += MAS_MEM[2]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 29
	c_t1_t41_mem1 += MAS_MEM[7]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 29
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 29
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 29
	c_t5010 += MAS[2]

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 29
	c_t5_a1_0_mem0 += MAS_MEM[4]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 29
	c_t5_a1_0_mem1 += MAS_MEM[3]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 29
	c_t5_t3_t0_in += MM_in[0]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 29
	c_t5_t3_t0_mem0 += MAS_MEM[6]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 29
	c_t5_t3_t0_mem1 += MAS_MEM[5]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=5, delay_cost=1)
	S += c_t5_t3_t1 >= 29
	c_t5_t3_t1 += MM[0]

	c_s2010 = S.Task('c_s2010', length=1, delay_cost=1)
	S += c_s2010 >= 30
	c_s2010 += MAS[2]

	c_t1_t41 = S.Task('c_t1_t41', length=1, delay_cost=1)
	S += c_t1_t41 >= 30
	c_t1_t41 += MAS[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 30
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 30
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 30
	c_t4000 += MAS[0]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=1, delay_cost=1)
	S += c_t5_a1_0 >= 30
	c_t5_a1_0 += MAS[4]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 30
	c_t5_a1_1_mem0 += MAS_MEM[2]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 30
	c_t5_a1_1_mem1 += MAS_MEM[5]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 30
	c_t5_t00_mem0 += MAS_MEM[6]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 30
	c_t5_t00_mem1 += MAS_MEM[9]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=5, delay_cost=1)
	S += c_t5_t3_t0 >= 30
	c_t5_t3_t0 += MM[0]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 30
	c_t5_t3_t3_mem0 += MAS_MEM[4]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 30
	c_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 31
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 31
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 31
	c_t3011 += MAS[0]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 31
	c_t3_a1_1_mem0 += MAS_MEM[0]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 31
	c_t3_a1_1_mem1 += MAS_MEM[3]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 31
	c_t3_t3_t3_mem0 += MAS_MEM[2]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 31
	c_t3_t3_t3_mem1 += MAS_MEM[1]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=1, delay_cost=1)
	S += c_t5_a1_1 >= 31
	c_t5_a1_1 += MAS[2]

	c_t5_t00 = S.Task('c_t5_t00', length=1, delay_cost=1)
	S += c_t5_t00 >= 31
	c_t5_t00 += MAS[3]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 31
	c_t5_t10_mem0 += MAS_MEM[6]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 31
	c_t5_t10_mem1 += MAS_MEM[5]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=1, delay_cost=1)
	S += c_t5_t3_t3 >= 31
	c_t5_t3_t3 += MAS[1]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	S += c_t2_t3_t2 >= 32
	c_t2_t3_t2 += MAS[0]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 32
	c_t2_t3_t4_in += MM_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 32
	c_t2_t3_t4_mem0 += MAS_MEM[0]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 32
	c_t2_t3_t4_mem1 += MAS_MEM[7]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 32
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 32
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 32
	c_t3_a1_0_mem0 += MAS_MEM[2]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 32
	c_t3_a1_0_mem1 += MAS_MEM[1]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=1, delay_cost=1)
	S += c_t3_a1_1 >= 32
	c_t3_a1_1 += MAS[1]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=1, delay_cost=1)
	S += c_t3_t3_t3 >= 32
	c_t3_t3_t3 += MAS[4]

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	S += c_t5_t10 >= 32
	c_t5_t10 += MAS[2]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 32
	c_t5_t11_mem0 += MAS_MEM[6]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 32
	c_t5_t11_mem1 += MAS_MEM[3]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=5, delay_cost=1)
	S += c_t2_t3_t4 >= 33
	c_t2_t3_t4 += MM[0]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 33
	c_t3001 += MAS[0]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=1, delay_cost=1)
	S += c_t3_a1_0 >= 33
	c_t3_a1_0 += MAS[2]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 33
	c_t3_t3_t1_in += MM_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 33
	c_t3_t3_t1_mem0 += MAS_MEM[0]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 33
	c_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 33
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 33
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 33
	c_t5_t01_mem0 += MAS_MEM[6]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 33
	c_t5_t01_mem1 += MAS_MEM[5]

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	S += c_t5_t11 >= 33
	c_t5_t11 += MAS[1]

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem0 >= 33
	c_t5_t2_t3_mem0 += MAS_MEM[4]

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem1 >= 33
	c_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 34
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 34
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 34
	c_t3_t11_mem0 += MAS_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 34
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=5, delay_cost=1)
	S += c_t3_t3_t1 >= 34
	c_t3_t3_t1 += MM[0]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 34
	c_t4001 += MAS[2]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 34
	c_t4_t3_t1_in += MM_in[0]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 34
	c_t4_t3_t1_mem0 += MAS_MEM[4]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 34
	c_t4_t3_t1_mem1 += MAS_MEM[3]

	c_t5_t01 = S.Task('c_t5_t01', length=1, delay_cost=1)
	S += c_t5_t01 >= 34
	c_t5_t01 += MAS[0]

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=1, delay_cost=1)
	S += c_t5_t2_t3 >= 34
	c_t5_t2_t3 += MAS[3]

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem0 >= 34
	c_t5_t3_t5_mem0 += MM_MEM[0]

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem1 >= 34
	c_t5_t3_t5_mem1 += MM_MEM[1]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 35
	c_t3000 += MAS[4]

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	S += c_t3_t11 >= 35
	c_t3_t11 += MAS[2]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 35
	c_t3_t3_t2_mem0 += MAS_MEM[8]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 35
	c_t3_t3_t2_mem1 += MAS_MEM[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 35
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 35
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 35
	c_t4_t11_mem0 += MAS_MEM[4]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 35
	c_t4_t11_mem1 += MAS_MEM[3]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=5, delay_cost=1)
	S += c_t4_t3_t1 >= 35
	c_t4_t3_t1 += MM[0]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 35
	c_t4_t3_t2_mem0 += MAS_MEM[0]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 35
	c_t4_t3_t2_mem1 += MAS_MEM[5]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 35
	c_t5_t30_mem0 += MM_MEM[0]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 35
	c_t5_t30_mem1 += MM_MEM[1]

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=1, delay_cost=1)
	S += c_t5_t3_t5 >= 35
	c_t5_t3_t5 += MAS[0]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 36
	c_t0_t01_mem0 += MAIN_MEM_r[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 36
	c_t0_t01_mem1 += MAS_MEM[9]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 36
	c_t3_t3_t0_in += MM_in[0]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 36
	c_t3_t3_t0_mem0 += MAS_MEM[8]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 36
	c_t3_t3_t0_mem1 += MAS_MEM[3]

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=1, delay_cost=1)
	S += c_t3_t3_t2 >= 36
	c_t3_t3_t2 += MAS[1]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 36
	c_t4010 += MAS[0]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 36
	c_t4_t10_mem0 += MAS_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 36
	c_t4_t10_mem1 += MAS_MEM[1]

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	S += c_t4_t11 >= 36
	c_t4_t11 += MAS[4]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=1, delay_cost=1)
	S += c_t4_t3_t2 >= 36
	c_t4_t3_t2 += MAS[2]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 36
	c_t510_mem0 += MAS_MEM[6]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 36
	c_t510_mem1 += MAS_MEM[7]

	c_t5_t30 = S.Task('c_t5_t30', length=1, delay_cost=1)
	S += c_t5_t30 >= 36
	c_t5_t30 += MAS[3]

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	S += c_t0_t01 >= 37
	c_t0_t01 += MAS[3]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 37
	c_t2_t00_mem0 += MAIN_MEM_r[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 37
	c_t2_t00_mem1 += MAS_MEM[7]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 37
	c_t2_t31_mem0 += MM_MEM[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 37
	c_t2_t31_mem1 += MAS_MEM[5]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 37
	c_t3_t10_mem0 += MAS_MEM[8]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 37
	c_t3_t10_mem1 += MAS_MEM[3]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=5, delay_cost=1)
	S += c_t3_t3_t0 >= 37
	c_t3_t3_t0 += MM[0]

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	S += c_t4_t10 >= 37
	c_t4_t10 += MAS[1]

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem0 >= 37
	c_t4_t2_t3_mem0 += MAS_MEM[2]

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem1 >= 37
	c_t4_t2_t3_mem1 += MAS_MEM[9]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 37
	c_t4_t3_t0_in += MM_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 37
	c_t4_t3_t0_mem0 += MAS_MEM[0]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 37
	c_t4_t3_t0_mem1 += MAS_MEM[1]

	c_t510 = S.Task('c_t510', length=1, delay_cost=1)
	S += c_t510 >= 37
	c_t510 += MAS[2]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 38
	c_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 38
	c_t1_t01_mem1 += MAS_MEM[5]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 38
	c_t211_mem0 += MAS_MEM[8]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 38
	c_t211_mem1 += MAS_MEM[9]

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	S += c_t2_t00 >= 38
	c_t2_t00 += MAS[0]

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	S += c_t2_t31 >= 38
	c_t2_t31 += MAS[4]

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	S += c_t3_t10 >= 38
	c_t3_t10 += MAS[2]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 38
	c_t4_a1_1_mem0 += MAS_MEM[2]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 38
	c_t4_a1_1_mem1 += MAS_MEM[1]

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=1, delay_cost=1)
	S += c_t4_t2_t3 >= 38
	c_t4_t2_t3 += MAS[1]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=5, delay_cost=1)
	S += c_t4_t3_t0 >= 38
	c_t4_t3_t0 += MM[0]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 38
	c_t4_t3_t3_mem0 += MAS_MEM[0]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 38
	c_t4_t3_t3_mem1 += MAS_MEM[3]

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	S += c_t1_t01 >= 39
	c_t1_t01 += MAS[1]

	c_t211 = S.Task('c_t211', length=1, delay_cost=1)
	S += c_t211 >= 39
	c_t211 += MAS[2]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 39
	c_t2_t01_mem0 += MAIN_MEM_r[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 39
	c_t2_t01_mem1 += MAS_MEM[1]

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem0 >= 39
	c_t3_t2_t3_mem0 += MAS_MEM[4]

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem1 >= 39
	c_t3_t2_t3_mem1 += MAS_MEM[5]

	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	S += c_t3_t3_t4_in >= 39
	c_t3_t3_t4_in += MM_in[0]

	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem0 >= 39
	c_t3_t3_t4_mem0 += MAS_MEM[2]

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem1 >= 39
	c_t3_t3_t4_mem1 += MAS_MEM[9]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 39
	c_t4_a1_0_mem0 += MAS_MEM[0]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 39
	c_t4_a1_0_mem1 += MAS_MEM[3]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=1, delay_cost=1)
	S += c_t4_a1_1 >= 39
	c_t4_a1_1 += MAS[0]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=1, delay_cost=1)
	S += c_t4_t3_t3 >= 39
	c_t4_t3_t3 += MAS[4]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 40
	c_t1_t00_mem0 += MAIN_MEM_r[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 40
	c_t1_t00_mem1 += MAS_MEM[1]

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	S += c_t2_t01 >= 40
	c_t2_t01 += MAS[0]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 40
	c_t3_t00_mem0 += MAS_MEM[8]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 40
	c_t3_t00_mem1 += MAS_MEM[5]

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=1, delay_cost=1)
	S += c_t3_t2_t3 >= 40
	c_t3_t2_t3 += MAS[1]

	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=5, delay_cost=1)
	S += c_t3_t3_t4 >= 40
	c_t3_t3_t4 += MM[0]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=1, delay_cost=1)
	S += c_t4_a1_0 >= 40
	c_t4_a1_0 += MAS[3]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 40
	c_t4_t00_mem0 += MAS_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 40
	c_t4_t00_mem1 += MAS_MEM[7]

	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	S += c_t5_t3_t4_in >= 40
	c_t5_t3_t4_in += MM_in[0]

	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem0 >= 40
	c_t5_t3_t4_mem0 += MAS_MEM[6]

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem1 >= 40
	c_t5_t3_t4_mem1 += MAS_MEM[3]

	c_t6_y1_1_mem0 = S.Task('c_t6_y1_1_mem0', length=1, delay_cost=1)
	S += c_t6_y1_1_mem0 >= 40
	c_t6_y1_1_mem0 += MAS_MEM[4]

	c_t6_y1_1_mem1 = S.Task('c_t6_y1_1_mem1', length=1, delay_cost=1)
	S += c_t6_y1_1_mem1 >= 40
	c_t6_y1_1_mem1 += MAS_MEM[9]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 41
	c_t0_t00_mem0 += MAIN_MEM_r[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 41
	c_t0_t00_mem1 += MAS_MEM[9]

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	S += c_t1_t00 >= 41
	c_t1_t00 += MAS[1]

	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	S += c_t1_t2_t0_in >= 41
	c_t1_t2_t0_in += MM_in[0]

	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem0 >= 41
	c_t1_t2_t0_mem0 += MAS_MEM[2]

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem1 >= 41
	c_t1_t2_t0_mem1 += MAS_MEM[5]

	c_t3_t00 = S.Task('c_t3_t00', length=1, delay_cost=1)
	S += c_t3_t00 >= 41
	c_t3_t00 += MAS[4]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 41
	c_t3_t01_mem0 += MAS_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 41
	c_t3_t01_mem1 += MAS_MEM[3]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 41
	c_t3_t30_mem0 += MM_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 41
	c_t3_t30_mem1 += MM_MEM[1]

	c_t4_t00 = S.Task('c_t4_t00', length=1, delay_cost=1)
	S += c_t4_t00 >= 41
	c_t4_t00 += MAS[0]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 41
	c_t4_t01_mem0 += MAS_MEM[4]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 41
	c_t4_t01_mem1 += MAS_MEM[1]

	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=5, delay_cost=1)
	S += c_t5_t3_t4 >= 41
	c_t5_t3_t4 += MM[0]

	c_t6_y1_1 = S.Task('c_t6_y1_1', length=1, delay_cost=1)
	S += c_t6_y1_1 >= 41
	c_t6_y1_1 += MAS[2]

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	S += c_t0_t00 >= 42
	c_t0_t00 += MAS[0]

	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=5, delay_cost=1)
	S += c_t1_t2_t0 >= 42
	c_t1_t2_t0 += MM[0]

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem0 >= 42
	c_t1_t2_t2_mem0 += MAS_MEM[2]

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem1 >= 42
	c_t1_t2_t2_mem1 += MAS_MEM[3]

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem0 >= 42
	c_t2_t2_t2_mem0 += MAS_MEM[0]

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem1 >= 42
	c_t2_t2_t2_mem1 += MAS_MEM[1]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 42
	c_t310_mem0 += MAS_MEM[6]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 42
	c_t310_mem1 += MAS_MEM[7]

	c_t3_t01 = S.Task('c_t3_t01', length=1, delay_cost=1)
	S += c_t3_t01 >= 42
	c_t3_t01 += MAS[4]

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	S += c_t3_t30 >= 42
	c_t3_t30 += MAS[3]

	c_t4_t01 = S.Task('c_t4_t01', length=1, delay_cost=1)
	S += c_t4_t01 >= 42
	c_t4_t01 += MAS[1]

	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	S += c_t4_t3_t4_in >= 42
	c_t4_t3_t4_in += MM_in[0]

	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem0 >= 42
	c_t4_t3_t4_mem0 += MAS_MEM[4]

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem1 >= 42
	c_t4_t3_t4_mem1 += MAS_MEM[9]

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem0 >= 42
	c_t4_t3_t5_mem0 += MM_MEM[0]

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem1 >= 42
	c_t4_t3_t5_mem1 += MM_MEM[1]

	c_t6_y1_0_mem0 = S.Task('c_t6_y1_0_mem0', length=1, delay_cost=1)
	S += c_t6_y1_0_mem0 >= 42
	c_t6_y1_0_mem0 += MAS_MEM[8]

	c_t6_y1_0_mem1 = S.Task('c_t6_y1_0_mem1', length=1, delay_cost=1)
	S += c_t6_y1_0_mem1 >= 42
	c_t6_y1_0_mem1 += MAS_MEM[5]

	c_s210_mem0 = S.Task('c_s210_mem0', length=1, delay_cost=1)
	S += c_s210_mem0 >= 43
	c_s210_mem0 += MAS_MEM[4]

	c_s210_mem1 = S.Task('c_s210_mem1', length=1, delay_cost=1)
	S += c_s210_mem1 >= 43
	c_s210_mem1 += MAS_MEM[5]

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem0 >= 43
	c_t0_t2_t2_mem0 += MAS_MEM[0]

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem1 >= 43
	c_t0_t2_t2_mem1 += MAS_MEM[7]

	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	S += c_t1_t2_t1_in >= 43
	c_t1_t2_t1_in += MM_in[0]

	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem0 >= 43
	c_t1_t2_t1_mem0 += MAS_MEM[2]

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem1 >= 43
	c_t1_t2_t1_mem1 += MAS_MEM[1]

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=1, delay_cost=1)
	S += c_t1_t2_t2 >= 43
	c_t1_t2_t2 += MAS[4]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 43
	c_t1_t40_mem0 += MAS_MEM[6]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 43
	c_t1_t40_mem1 += MAS_MEM[3]

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=1, delay_cost=1)
	S += c_t2_t2_t2 >= 43
	c_t2_t2_t2 += MAS[1]

	c_t310 = S.Task('c_t310', length=1, delay_cost=1)
	S += c_t310 >= 43
	c_t310 += MAS[3]

	c_t3_t2_t2_mem0 = S.Task('c_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem0 >= 43
	c_t3_t2_t2_mem0 += MAS_MEM[8]

	c_t3_t2_t2_mem1 = S.Task('c_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem1 >= 43
	c_t3_t2_t2_mem1 += MAS_MEM[9]

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem0 >= 43
	c_t3_t3_t5_mem0 += MM_MEM[0]

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem1 >= 43
	c_t3_t3_t5_mem1 += MM_MEM[1]

	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=5, delay_cost=1)
	S += c_t4_t3_t4 >= 43
	c_t4_t3_t4 += MM[0]

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=1, delay_cost=1)
	S += c_t4_t3_t5 >= 43
	c_t4_t3_t5 += MAS[0]

	c_t6_y1_0 = S.Task('c_t6_y1_0', length=1, delay_cost=1)
	S += c_t6_y1_0 >= 43
	c_t6_y1_0 += MAS[2]

	c_s210 = S.Task('c_s210', length=1, delay_cost=1)
	S += c_s210 >= 44
	c_s210 += MAS[3]

	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_in >= 44
	c_t0_t2_t1_in += MM_in[0]

	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem0 >= 44
	c_t0_t2_t1_mem0 += MAS_MEM[6]

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem1 >= 44
	c_t0_t2_t1_mem1 += MAS_MEM[3]

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=1, delay_cost=1)
	S += c_t0_t2_t2 >= 44
	c_t0_t2_t2 += MAS[4]

	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=5, delay_cost=1)
	S += c_t1_t2_t1 >= 44
	c_t1_t2_t1 += MM[0]

	c_t1_t40 = S.Task('c_t1_t40', length=1, delay_cost=1)
	S += c_t1_t40 >= 44
	c_t1_t40 += MAS[2]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 44
	c_t2_t40_mem0 += MAS_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 44
	c_t2_t40_mem1 += MAS_MEM[9]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 44
	c_t2_t41_mem0 += MAS_MEM[8]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 44
	c_t2_t41_mem1 += MAS_MEM[1]

	c_t3_t2_t2 = S.Task('c_t3_t2_t2', length=1, delay_cost=1)
	S += c_t3_t2_t2 >= 44
	c_t3_t2_t2 += MAS[1]

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=1, delay_cost=1)
	S += c_t3_t3_t5 >= 44
	c_t3_t3_t5 += MAS[0]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 44
	c_t4_t30_mem0 += MM_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 44
	c_t4_t30_mem1 += MM_MEM[1]

	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_in >= 45
	c_t0_t2_t0_in += MM_in[0]

	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem0 >= 45
	c_t0_t2_t0_mem0 += MAS_MEM[0]

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem1 >= 45
	c_t0_t2_t0_mem1 += MAS_MEM[9]

	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=5, delay_cost=1)
	S += c_t0_t2_t1 >= 45
	c_t0_t2_t1 += MM[0]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 45
	c_t111_mem0 += MAS_MEM[2]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 45
	c_t111_mem1 += MAS_MEM[3]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 45
	c_t1_t50_mem0 += MAS_MEM[6]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 45
	c_t1_t50_mem1 += MAS_MEM[5]

	c_t2_t40 = S.Task('c_t2_t40', length=1, delay_cost=1)
	S += c_t2_t40 >= 45
	c_t2_t40 += MAS[1]

	c_t2_t41 = S.Task('c_t2_t41', length=1, delay_cost=1)
	S += c_t2_t41 >= 45
	c_t2_t41 += MAS[4]

	c_t4_t30 = S.Task('c_t4_t30', length=1, delay_cost=1)
	S += c_t4_t30 >= 45
	c_t4_t30 += MAS[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 45
	c_t5_t31_mem0 += MM_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 45
	c_t5_t31_mem1 += MAS_MEM[1]

	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=5, delay_cost=1)
	S += c_t0_t2_t0 >= 46
	c_t0_t2_t0 += MM[0]

	c_t111 = S.Task('c_t111', length=1, delay_cost=1)
	S += c_t111 >= 46
	c_t111 += MAS[1]

	c_t1_t50 = S.Task('c_t1_t50', length=1, delay_cost=1)
	S += c_t1_t50 >= 46
	c_t1_t50 += MAS[2]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 46
	c_t1_t51_mem0 += MAS_MEM[2]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 46
	c_t1_t51_mem1 += MAS_MEM[3]

	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	S += c_t2_t2_t1_in >= 46
	c_t2_t2_t1_in += MM_in[0]

	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem0 >= 46
	c_t2_t2_t1_mem0 += MAS_MEM[0]

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem1 >= 46
	c_t2_t2_t1_mem1 += MAS_MEM[5]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 46
	c_t2_t51_mem0 += MAS_MEM[8]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 46
	c_t2_t51_mem1 += MAS_MEM[9]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 46
	c_t3_t31_mem0 += MM_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 46
	c_t3_t31_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=1, delay_cost=1)
	S += c_t5_t31 >= 46
	c_t5_t31 += MAS[0]

	c_s1011_mem0 = S.Task('c_s1011_mem0', length=1, delay_cost=1)
	S += c_s1011_mem0 >= 47
	c_s1011_mem0 += MAS_MEM[2]

	c_s1011_mem1 = S.Task('c_s1011_mem1', length=1, delay_cost=1)
	S += c_s1011_mem1 >= 47
	c_s1011_mem1 += MAS_MEM[5]

	c_t1_t51 = S.Task('c_t1_t51', length=1, delay_cost=1)
	S += c_t1_t51 >= 47
	c_t1_t51 += MAS[1]

	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	S += c_t2_t2_t0_in >= 47
	c_t2_t2_t0_in += MM_in[0]

	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem0 >= 47
	c_t2_t2_t0_mem0 += MAS_MEM[0]

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem1 >= 47
	c_t2_t2_t0_mem1 += MAS_MEM[7]

	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=5, delay_cost=1)
	S += c_t2_t2_t1 >= 47
	c_t2_t2_t1 += MM[0]

	c_t2_t51 = S.Task('c_t2_t51', length=1, delay_cost=1)
	S += c_t2_t51 >= 47
	c_t2_t51 += MAS[4]

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	S += c_t3_t31 >= 47
	c_t3_t31 += MAS[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 47
	c_t4_t31_mem0 += MM_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 47
	c_t4_t31_mem1 += MAS_MEM[1]

	c_s1011 = S.Task('c_s1011', length=1, delay_cost=1)
	S += c_s1011 >= 48
	c_s1011 += MAS[3]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 48
	c_t1_t20_mem0 += MM_MEM[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 48
	c_t1_t20_mem1 += MM_MEM[1]

	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=5, delay_cost=1)
	S += c_t2_t2_t0 >= 48
	c_t2_t2_t0 += MM[0]

	c_t4_t2_t1_in = S.Task('c_t4_t2_t1_in', length=1, delay_cost=1)
	S += c_t4_t2_t1_in >= 48
	c_t4_t2_t1_in += MM_in[0]

	c_t4_t2_t1_mem0 = S.Task('c_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem0 >= 48
	c_t4_t2_t1_mem0 += MAS_MEM[2]

	c_t4_t2_t1_mem1 = S.Task('c_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem1 >= 48
	c_t4_t2_t1_mem1 += MAS_MEM[9]

	c_t4_t2_t2_mem0 = S.Task('c_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem0 >= 48
	c_t4_t2_t2_mem0 += MAS_MEM[0]

	c_t4_t2_t2_mem1 = S.Task('c_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem1 >= 48
	c_t4_t2_t2_mem1 += MAS_MEM[3]

	c_t4_t31 = S.Task('c_t4_t31', length=1, delay_cost=1)
	S += c_t4_t31 >= 48
	c_t4_t31 += MAS[0]

	c_t5_t2_t2_mem0 = S.Task('c_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem0 >= 48
	c_t5_t2_t2_mem0 += MAS_MEM[6]

	c_t5_t2_t2_mem1 = S.Task('c_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem1 >= 48
	c_t5_t2_t2_mem1 += MAS_MEM[1]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 49
	c_t1_t20 += MAS[0]

	c_t1_t2_t5_mem0 = S.Task('c_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem0 >= 49
	c_t1_t2_t5_mem0 += MM_MEM[0]

	c_t1_t2_t5_mem1 = S.Task('c_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem1 >= 49
	c_t1_t2_t5_mem1 += MM_MEM[1]

	c_t3_t2_t1_in = S.Task('c_t3_t2_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_in >= 49
	c_t3_t2_t1_in += MM_in[0]

	c_t3_t2_t1_mem0 = S.Task('c_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem0 >= 49
	c_t3_t2_t1_mem0 += MAS_MEM[8]

	c_t3_t2_t1_mem1 = S.Task('c_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem1 >= 49
	c_t3_t2_t1_mem1 += MAS_MEM[5]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 49
	c_t410_mem0 += MAS_MEM[0]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 49
	c_t410_mem1 += MAS_MEM[1]

	c_t4_t2_t1 = S.Task('c_t4_t2_t1', length=5, delay_cost=1)
	S += c_t4_t2_t1 >= 49
	c_t4_t2_t1 += MM[0]

	c_t4_t2_t2 = S.Task('c_t4_t2_t2', length=1, delay_cost=1)
	S += c_t4_t2_t2 >= 49
	c_t4_t2_t2 += MAS[4]

	c_t5_t2_t2 = S.Task('c_t5_t2_t2', length=1, delay_cost=1)
	S += c_t5_t2_t2 >= 49
	c_t5_t2_t2 += MAS[2]

	c_s010_mem0 = S.Task('c_s010_mem0', length=1, delay_cost=1)
	S += c_s010_mem0 >= 50
	c_s010_mem0 += MAS_MEM[6]

	c_s010_mem1 = S.Task('c_s010_mem1', length=1, delay_cost=1)
	S += c_s010_mem1 >= 50
	c_s010_mem1 += MAS_MEM[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 50
	c_t0_t20_mem0 += MM_MEM[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 50
	c_t0_t20_mem1 += MM_MEM[1]

	c_t1_t2_t5 = S.Task('c_t1_t2_t5', length=1, delay_cost=1)
	S += c_t1_t2_t5 >= 50
	c_t1_t2_t5 += MAS[1]

	c_t3_t2_t0_in = S.Task('c_t3_t2_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_in >= 50
	c_t3_t2_t0_in += MM_in[0]

	c_t3_t2_t0_mem0 = S.Task('c_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem0 >= 50
	c_t3_t2_t0_mem0 += MAS_MEM[8]

	c_t3_t2_t0_mem1 = S.Task('c_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem1 >= 50
	c_t3_t2_t0_mem1 += MAS_MEM[5]

	c_t3_t2_t1 = S.Task('c_t3_t2_t1', length=5, delay_cost=1)
	S += c_t3_t2_t1 >= 50
	c_t3_t2_t1 += MM[0]

	c_t410 = S.Task('c_t410', length=1, delay_cost=1)
	S += c_t410 >= 50
	c_t410 += MAS[2]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 50
	c_t5_t41_mem0 += MAS_MEM[0]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 50
	c_t5_t41_mem1 += MAS_MEM[7]

	c_s010 = S.Task('c_s010', length=1, delay_cost=1)
	S += c_s010 >= 51
	c_s010 += MAS[3]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 51
	c_t0_t20 += MAS[0]

	c_t0_t2_t5_mem0 = S.Task('c_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem0 >= 51
	c_t0_t2_t5_mem0 += MM_MEM[0]

	c_t0_t2_t5_mem1 = S.Task('c_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem1 >= 51
	c_t0_t2_t5_mem1 += MM_MEM[1]

	c_t3_t2_t0 = S.Task('c_t3_t2_t0', length=5, delay_cost=1)
	S += c_t3_t2_t0 >= 51
	c_t3_t2_t0 += MM[0]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 51
	c_t3_t40_mem0 += MAS_MEM[6]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 51
	c_t3_t40_mem1 += MAS_MEM[1]

	c_t5_t2_t1_in = S.Task('c_t5_t2_t1_in', length=1, delay_cost=1)
	S += c_t5_t2_t1_in >= 51
	c_t5_t2_t1_in += MM_in[0]

	c_t5_t2_t1_mem0 = S.Task('c_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem0 >= 51
	c_t5_t2_t1_mem0 += MAS_MEM[0]

	c_t5_t2_t1_mem1 = S.Task('c_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem1 >= 51
	c_t5_t2_t1_mem1 += MAS_MEM[3]

	c_t5_t41 = S.Task('c_t5_t41', length=1, delay_cost=1)
	S += c_t5_t41 >= 51
	c_t5_t41 += MAS[1]

	c_s1110_mem0 = S.Task('c_s1110_mem0', length=1, delay_cost=1)
	S += c_s1110_mem0 >= 52
	c_s1110_mem0 += MAS_MEM[4]

	c_s1110_mem1 = S.Task('c_s1110_mem1', length=1, delay_cost=1)
	S += c_s1110_mem1 >= 52
	c_s1110_mem1 += MAS_MEM[1]

	c_t0_t2_t5 = S.Task('c_t0_t2_t5', length=1, delay_cost=1)
	S += c_t0_t2_t5 >= 52
	c_t0_t2_t5 += MAS[4]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 52
	c_t2_t20_mem0 += MM_MEM[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 52
	c_t2_t20_mem1 += MM_MEM[1]

	c_t2_t2_t4_in = S.Task('c_t2_t2_t4_in', length=1, delay_cost=1)
	S += c_t2_t2_t4_in >= 52
	c_t2_t2_t4_in += MM_in[0]

	c_t2_t2_t4_mem0 = S.Task('c_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem0 >= 52
	c_t2_t2_t4_mem0 += MAS_MEM[2]

	c_t2_t2_t4_mem1 = S.Task('c_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem1 >= 52
	c_t2_t2_t4_mem1 += MAS_MEM[9]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 52
	c_t2_t50_mem0 += MAS_MEM[0]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 52
	c_t2_t50_mem1 += MAS_MEM[3]

	c_t3_t40 = S.Task('c_t3_t40', length=1, delay_cost=1)
	S += c_t3_t40 >= 52
	c_t3_t40 += MAS[0]

	c_t5_t2_t1 = S.Task('c_t5_t2_t1', length=5, delay_cost=1)
	S += c_t5_t2_t1 >= 52
	c_t5_t2_t1 += MM[0]

	c_s1110 = S.Task('c_s1110', length=1, delay_cost=1)
	S += c_s1110 >= 53
	c_s1110 += MAS[3]

	c_s2011_mem0 = S.Task('c_s2011_mem0', length=1, delay_cost=1)
	S += c_s2011_mem0 >= 53
	c_s2011_mem0 += MAS_MEM[4]

	c_s2011_mem1 = S.Task('c_s2011_mem1', length=1, delay_cost=1)
	S += c_s2011_mem1 >= 53
	c_s2011_mem1 += MAS_MEM[1]

	c_t0_t2_t4_in = S.Task('c_t0_t2_t4_in', length=1, delay_cost=1)
	S += c_t0_t2_t4_in >= 53
	c_t0_t2_t4_in += MM_in[0]

	c_t0_t2_t4_mem0 = S.Task('c_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem0 >= 53
	c_t0_t2_t4_mem0 += MAS_MEM[8]

	c_t0_t2_t4_mem1 = S.Task('c_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem1 >= 53
	c_t0_t2_t4_mem1 += MAS_MEM[3]

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	S += c_t2_t20 >= 53
	c_t2_t20 += MAS[0]

	c_t2_t2_t4 = S.Task('c_t2_t2_t4', length=5, delay_cost=1)
	S += c_t2_t2_t4 >= 53
	c_t2_t2_t4 += MM[0]

	c_t2_t2_t5_mem0 = S.Task('c_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem0 >= 53
	c_t2_t2_t5_mem0 += MM_MEM[0]

	c_t2_t2_t5_mem1 = S.Task('c_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem1 >= 53
	c_t2_t2_t5_mem1 += MM_MEM[1]

	c_t2_t50 = S.Task('c_t2_t50', length=1, delay_cost=1)
	S += c_t2_t50 >= 53
	c_t2_t50 += MAS[1]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 53
	c_t3_t41_mem0 += MAS_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 53
	c_t3_t41_mem1 += MAS_MEM[7]

	c_s0011_mem0 = S.Task('c_s0011_mem0', length=1, delay_cost=1)
	S += c_s0011_mem0 >= 54
	c_s0011_mem0 += MAS_MEM[0]

	c_s0011_mem1 = S.Task('c_s0011_mem1', length=1, delay_cost=1)
	S += c_s0011_mem1 >= 54
	c_s0011_mem1 += MAS_MEM[3]

	c_s2011 = S.Task('c_s2011', length=1, delay_cost=1)
	S += c_s2011 >= 54
	c_s2011 += MAS[4]

	c_t0_t2_t4 = S.Task('c_t0_t2_t4', length=5, delay_cost=1)
	S += c_t0_t2_t4 >= 54
	c_t0_t2_t4 += MM[0]

	c_t1_t2_t4_in = S.Task('c_t1_t2_t4_in', length=1, delay_cost=1)
	S += c_t1_t2_t4_in >= 54
	c_t1_t2_t4_in += MM_in[0]

	c_t1_t2_t4_mem0 = S.Task('c_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem0 >= 54
	c_t1_t2_t4_mem0 += MAS_MEM[8]

	c_t1_t2_t4_mem1 = S.Task('c_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem1 >= 54
	c_t1_t2_t4_mem1 += MAS_MEM[1]

	c_t2_t2_t5 = S.Task('c_t2_t2_t5', length=1, delay_cost=1)
	S += c_t2_t2_t5 >= 54
	c_t2_t2_t5 += MAS[1]

	c_t3_t41 = S.Task('c_t3_t41', length=1, delay_cost=1)
	S += c_t3_t41 >= 54
	c_t3_t41 += MAS[0]

	c_s0011 = S.Task('c_s0011', length=1, delay_cost=1)
	S += c_s0011 >= 55
	c_s0011 += MAS[0]

	c_t1_t2_t4 = S.Task('c_t1_t2_t4', length=5, delay_cost=1)
	S += c_t1_t2_t4 >= 55
	c_t1_t2_t4 += MM[0]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 55
	c_t311_mem0 += MAS_MEM[0]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 55
	c_t311_mem1 += MAS_MEM[1]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 55
	c_t3_t20_mem0 += MM_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 55
	c_t3_t20_mem1 += MM_MEM[1]

	c_t5_t2_t0_in = S.Task('c_t5_t2_t0_in', length=1, delay_cost=1)
	S += c_t5_t2_t0_in >= 55
	c_t5_t2_t0_in += MM_in[0]

	c_t5_t2_t0_mem0 = S.Task('c_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem0 >= 55
	c_t5_t2_t0_mem0 += MAS_MEM[6]

	c_t5_t2_t0_mem1 = S.Task('c_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem1 >= 55
	c_t5_t2_t0_mem1 += MAS_MEM[5]

	c_t311 = S.Task('c_t311', length=1, delay_cost=1)
	S += c_t311 >= 56
	c_t311 += MAS[3]

	c_t3_t20 = S.Task('c_t3_t20', length=1, delay_cost=1)
	S += c_t3_t20 >= 56
	c_t3_t20 += MAS[0]

	c_t3_t2_t5_mem0 = S.Task('c_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem0 >= 56
	c_t3_t2_t5_mem0 += MM_MEM[0]

	c_t3_t2_t5_mem1 = S.Task('c_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem1 >= 56
	c_t3_t2_t5_mem1 += MM_MEM[1]

	c_t4_t2_t0_in = S.Task('c_t4_t2_t0_in', length=1, delay_cost=1)
	S += c_t4_t2_t0_in >= 56
	c_t4_t2_t0_in += MM_in[0]

	c_t4_t2_t0_mem0 = S.Task('c_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem0 >= 56
	c_t4_t2_t0_mem0 += MAS_MEM[0]

	c_t4_t2_t0_mem1 = S.Task('c_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem1 >= 56
	c_t4_t2_t0_mem1 += MAS_MEM[3]

	c_t5_t2_t0 = S.Task('c_t5_t2_t0', length=5, delay_cost=1)
	S += c_t5_t2_t0 >= 56
	c_t5_t2_t0 += MM[0]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 56
	c_t5_t40_mem0 += MAS_MEM[6]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 56
	c_t5_t40_mem1 += MAS_MEM[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 57
	c_t2_t21_mem0 += MM_MEM[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 57
	c_t2_t21_mem1 += MAS_MEM[3]

	c_t3_t2_t5 = S.Task('c_t3_t2_t5', length=1, delay_cost=1)
	S += c_t3_t2_t5 >= 57
	c_t3_t2_t5 += MAS[1]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 57
	c_t411_mem0 += MAS_MEM[0]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 57
	c_t411_mem1 += MAS_MEM[1]

	c_t4_t2_t0 = S.Task('c_t4_t2_t0', length=5, delay_cost=1)
	S += c_t4_t2_t0 >= 57
	c_t4_t2_t0 += MM[0]

	c_t5_t2_t4_in = S.Task('c_t5_t2_t4_in', length=1, delay_cost=1)
	S += c_t5_t2_t4_in >= 57
	c_t5_t2_t4_in += MM_in[0]

	c_t5_t2_t4_mem0 = S.Task('c_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem0 >= 57
	c_t5_t2_t4_mem0 += MAS_MEM[4]

	c_t5_t2_t4_mem1 = S.Task('c_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem1 >= 57
	c_t5_t2_t4_mem1 += MAS_MEM[7]

	c_t5_t40 = S.Task('c_t5_t40', length=1, delay_cost=1)
	S += c_t5_t40 >= 57
	c_t5_t40 += MAS[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 58
	c_t0_t21_mem0 += MM_MEM[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 58
	c_t0_t21_mem1 += MAS_MEM[9]

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	S += c_t2_t21 >= 58
	c_t2_t21 += MAS[0]

	c_t3_t2_t4_in = S.Task('c_t3_t2_t4_in', length=1, delay_cost=1)
	S += c_t3_t2_t4_in >= 58
	c_t3_t2_t4_in += MM_in[0]

	c_t3_t2_t4_mem0 = S.Task('c_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem0 >= 58
	c_t3_t2_t4_mem0 += MAS_MEM[2]

	c_t3_t2_t4_mem1 = S.Task('c_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem1 >= 58
	c_t3_t2_t4_mem1 += MAS_MEM[3]

	c_t411 = S.Task('c_t411', length=1, delay_cost=1)
	S += c_t411 >= 58
	c_t411 += MAS[3]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 58
	c_t4_t41_mem0 += MAS_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 58
	c_t4_t41_mem1 += MAS_MEM[1]

	c_t5_t2_t4 = S.Task('c_t5_t2_t4', length=5, delay_cost=1)
	S += c_t5_t2_t4 >= 58
	c_t5_t2_t4 += MM[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 59
	c_t0_t21 += MAS[3]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 59
	c_t1_t21_mem0 += MM_MEM[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 59
	c_t1_t21_mem1 += MAS_MEM[3]

	c_t3_t2_t4 = S.Task('c_t3_t2_t4', length=5, delay_cost=1)
	S += c_t3_t2_t4 >= 59
	c_t3_t2_t4 += MM[0]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 59
	c_t4_t40_mem0 += MAS_MEM[0]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 59
	c_t4_t40_mem1 += MAS_MEM[1]

	c_t4_t41 = S.Task('c_t4_t41', length=1, delay_cost=1)
	S += c_t4_t41 >= 59
	c_t4_t41 += MAS[0]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 60
	c_t1_t21 += MAS[0]

	c_t4_t2_t4_in = S.Task('c_t4_t2_t4_in', length=1, delay_cost=1)
	S += c_t4_t2_t4_in >= 60
	c_t4_t2_t4_in += MM_in[0]

	c_t4_t2_t4_mem0 = S.Task('c_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem0 >= 60
	c_t4_t2_t4_mem0 += MAS_MEM[8]

	c_t4_t2_t4_mem1 = S.Task('c_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem1 >= 60
	c_t4_t2_t4_mem1 += MAS_MEM[3]

	c_t4_t40 = S.Task('c_t4_t40', length=1, delay_cost=1)
	S += c_t4_t40 >= 60
	c_t4_t40 += MAS[2]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 60
	c_t511_mem0 += MAS_MEM[0]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 60
	c_t511_mem1 += MAS_MEM[1]

	c_t5_t2_t5_mem0 = S.Task('c_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem0 >= 60
	c_t5_t2_t5_mem0 += MM_MEM[0]

	c_t5_t2_t5_mem1 = S.Task('c_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem1 >= 60
	c_t5_t2_t5_mem1 += MM_MEM[1]

	c_t4_t2_t4 = S.Task('c_t4_t2_t4', length=5, delay_cost=1)
	S += c_t4_t2_t4 >= 61
	c_t4_t2_t4 += MM[0]

	c_t511 = S.Task('c_t511', length=1, delay_cost=1)
	S += c_t511 >= 61
	c_t511 += MAS[2]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 61
	c_t5_t20_mem0 += MM_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 61
	c_t5_t20_mem1 += MM_MEM[1]

	c_t5_t2_t5 = S.Task('c_t5_t2_t5', length=1, delay_cost=1)
	S += c_t5_t2_t5 >= 61
	c_t5_t2_t5 += MAS[0]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 62
	c_t4_t20_mem0 += MM_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 62
	c_t4_t20_mem1 += MM_MEM[1]

	c_t5_t20 = S.Task('c_t5_t20', length=1, delay_cost=1)
	S += c_t5_t20 >= 62
	c_t5_t20 += MAS[3]

	c_t4_t20 = S.Task('c_t4_t20', length=1, delay_cost=1)
	S += c_t4_t20 >= 63
	c_t4_t20 += MAS[1]

	c_t4_t2_t5_mem0 = S.Task('c_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem0 >= 63
	c_t4_t2_t5_mem0 += MM_MEM[0]

	c_t4_t2_t5_mem1 = S.Task('c_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem1 >= 63
	c_t4_t2_t5_mem1 += MM_MEM[1]

	c_t4_t2_t5 = S.Task('c_t4_t2_t5', length=1, delay_cost=1)
	S += c_t4_t2_t5 >= 64
	c_t4_t2_t5 += MAS[0]


	# new tasks
	c_t000 = S.Task('c_t000', length=1, delay_cost=1)
	c_t000 += alt(MAS)

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	c_t000_mem0 += MAS_MEM[0]
	S += 51 < c_t000_mem0
	S += c_t000_mem0 <= c_t000

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	c_t000_mem1 += MAS_MEM[3]
	S += 25 < c_t000_mem1
	S += c_t000_mem1 <= c_t000

	c_t001 = S.Task('c_t001', length=1, delay_cost=1)
	c_t001 += alt(MAS)

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	c_t001_mem0 += MAS_MEM[6]
	S += 59 < c_t001_mem0
	S += c_t001_mem0 <= c_t001

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	c_t001_mem1 += MAS_MEM[1]
	S += 26 < c_t001_mem1
	S += c_t001_mem1 <= c_t001

	c_t100 = S.Task('c_t100', length=1, delay_cost=1)
	c_t100 += alt(MAS)

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	c_t100_mem0 += MAS_MEM[0]
	S += 49 < c_t100_mem0
	S += c_t100_mem0 <= c_t100

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	c_t100_mem1 += MAS_MEM[5]
	S += 46 < c_t100_mem1
	S += c_t100_mem1 <= c_t100

	c_t101 = S.Task('c_t101', length=1, delay_cost=1)
	c_t101 += alt(MAS)

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	c_t101_mem0 += MAS_MEM[0]
	S += 60 < c_t101_mem0
	S += c_t101_mem0 <= c_t101

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	c_t101_mem1 += MAS_MEM[3]
	S += 47 < c_t101_mem1
	S += c_t101_mem1 <= c_t101

	c_t200 = S.Task('c_t200', length=1, delay_cost=1)
	c_t200 += alt(MAS)

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	c_t200_mem0 += MAS_MEM[0]
	S += 53 < c_t200_mem0
	S += c_t200_mem0 <= c_t200

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	c_t200_mem1 += MAS_MEM[3]
	S += 53 < c_t200_mem1
	S += c_t200_mem1 <= c_t200

	c_t201 = S.Task('c_t201', length=1, delay_cost=1)
	c_t201 += alt(MAS)

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	c_t201_mem0 += MAS_MEM[0]
	S += 58 < c_t201_mem0
	S += c_t201_mem0 <= c_t201

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	c_t201_mem1 += MAS_MEM[9]
	S += 47 < c_t201_mem1
	S += c_t201_mem1 <= c_t201

	c_t3_t21 = S.Task('c_t3_t21', length=1, delay_cost=1)
	c_t3_t21 += alt(MAS)

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	c_t3_t21_mem0 += MM_MEM[0]
	S += 63 < c_t3_t21_mem0
	S += c_t3_t21_mem0 <= c_t3_t21

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	c_t3_t21_mem1 += MAS_MEM[3]
	S += 57 < c_t3_t21_mem1
	S += c_t3_t21_mem1 <= c_t3_t21

	c_t3_t50 = S.Task('c_t3_t50', length=1, delay_cost=1)
	c_t3_t50 += alt(MAS)

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	c_t3_t50_mem0 += MAS_MEM[6]
	S += 42 < c_t3_t50_mem0
	S += c_t3_t50_mem0 <= c_t3_t50

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	c_t3_t50_mem1 += MAS_MEM[1]
	S += 52 < c_t3_t50_mem1
	S += c_t3_t50_mem1 <= c_t3_t50

	c_t3_t51 = S.Task('c_t3_t51', length=1, delay_cost=1)
	c_t3_t51 += alt(MAS)

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	c_t3_t51_mem0 += MAS_MEM[0]
	S += 47 < c_t3_t51_mem0
	S += c_t3_t51_mem0 <= c_t3_t51

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	c_t3_t51_mem1 += MAS_MEM[1]
	S += 54 < c_t3_t51_mem1
	S += c_t3_t51_mem1 <= c_t3_t51

	c_t4_t21 = S.Task('c_t4_t21', length=1, delay_cost=1)
	c_t4_t21 += alt(MAS)

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	c_t4_t21_mem0 += MM_MEM[0]
	S += 65 < c_t4_t21_mem0
	S += c_t4_t21_mem0 <= c_t4_t21

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	c_t4_t21_mem1 += MAS_MEM[1]
	S += 64 < c_t4_t21_mem1
	S += c_t4_t21_mem1 <= c_t4_t21

	c_t4_t50 = S.Task('c_t4_t50', length=1, delay_cost=1)
	c_t4_t50 += alt(MAS)

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	c_t4_t50_mem0 += MAS_MEM[0]
	S += 45 < c_t4_t50_mem0
	S += c_t4_t50_mem0 <= c_t4_t50

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	c_t4_t50_mem1 += MAS_MEM[5]
	S += 60 < c_t4_t50_mem1
	S += c_t4_t50_mem1 <= c_t4_t50

	c_t4_t51 = S.Task('c_t4_t51', length=1, delay_cost=1)
	c_t4_t51 += alt(MAS)

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	c_t4_t51_mem0 += MAS_MEM[0]
	S += 48 < c_t4_t51_mem0
	S += c_t4_t51_mem0 <= c_t4_t51

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	c_t4_t51_mem1 += MAS_MEM[1]
	S += 59 < c_t4_t51_mem1
	S += c_t4_t51_mem1 <= c_t4_t51

	c_t5_t21 = S.Task('c_t5_t21', length=1, delay_cost=1)
	c_t5_t21 += alt(MAS)

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	c_t5_t21_mem0 += MM_MEM[0]
	S += 62 < c_t5_t21_mem0
	S += c_t5_t21_mem0 <= c_t5_t21

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	c_t5_t21_mem1 += MAS_MEM[1]
	S += 61 < c_t5_t21_mem1
	S += c_t5_t21_mem1 <= c_t5_t21

	c_t5_t50 = S.Task('c_t5_t50', length=1, delay_cost=1)
	c_t5_t50 += alt(MAS)

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	c_t5_t50_mem0 += MAS_MEM[6]
	S += 36 < c_t5_t50_mem0
	S += c_t5_t50_mem0 <= c_t5_t50

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	c_t5_t50_mem1 += MAS_MEM[1]
	S += 57 < c_t5_t50_mem1
	S += c_t5_t50_mem1 <= c_t5_t50

	c_t5_t51 = S.Task('c_t5_t51', length=1, delay_cost=1)
	c_t5_t51 += alt(MAS)

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	c_t5_t51_mem0 += MAS_MEM[0]
	S += 46 < c_t5_t51_mem0
	S += c_t5_t51_mem0 <= c_t5_t51

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	c_t5_t51_mem1 += MAS_MEM[3]
	S += 51 < c_t5_t51_mem1
	S += c_t5_t51_mem1 <= c_t5_t51

	c_s011 = S.Task('c_s011', length=1, delay_cost=1)
	c_s011 += alt(MAS)

	c_s011_mem0 = S.Task('c_s011_mem0', length=1, delay_cost=1)
	c_s011_mem0 += MAS_MEM[6]
	S += 56 < c_s011_mem0
	S += c_s011_mem0 <= c_s011

	c_s011_mem1 = S.Task('c_s011_mem1', length=1, delay_cost=1)
	c_s011_mem1 += MAS_MEM[1]
	S += 55 < c_s011_mem1
	S += c_s011_mem1 <= c_s011

	c_s1111 = S.Task('c_s1111', length=1, delay_cost=1)
	c_s1111 += alt(MAS)

	c_s1111_mem0 = S.Task('c_s1111_mem0', length=1, delay_cost=1)
	c_s1111_mem0 += MAS_MEM[6]
	S += 58 < c_s1111_mem0
	S += c_s1111_mem0 <= c_s1111

	c_s1111_mem1 = S.Task('c_s1111_mem1', length=1, delay_cost=1)
	c_s1111_mem1 += MAS_MEM[7]
	S += 48 < c_s1111_mem1
	S += c_s1111_mem1 <= c_s1111

	c_s211 = S.Task('c_s211', length=1, delay_cost=1)
	c_s211 += alt(MAS)

	c_s211_mem0 = S.Task('c_s211_mem0', length=1, delay_cost=1)
	c_s211_mem0 += MAS_MEM[4]
	S += 61 < c_s211_mem0
	S += c_s211_mem0 <= c_s211

	c_s211_mem1 = S.Task('c_s211_mem1', length=1, delay_cost=1)
	c_s211_mem1 += MAS_MEM[9]
	S += 54 < c_s211_mem1
	S += c_s211_mem1 <= c_s211

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(MAS)

	S += 36<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[4]
	S += 12 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[7]
	S += 44 < c210_mem1
	S += c210_mem1 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c_t300 = S.Task('c_t300', length=1, delay_cost=1)
	c_t300 += alt(MAS)

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	c_t300_mem0 += MAS_MEM[0]
	S += 56 < c_t300_mem0
	S += c_t300_mem0 <= c_t300

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	c_t300_mem1 += alt(MAS_MEM)
	S += (c_t3_t50*MAS[0])-1 < c_t300_mem1*MAS_MEM[1]
	S += (c_t3_t50*MAS[1])-1 < c_t300_mem1*MAS_MEM[3]
	S += (c_t3_t50*MAS[2])-1 < c_t300_mem1*MAS_MEM[5]
	S += (c_t3_t50*MAS[3])-1 < c_t300_mem1*MAS_MEM[7]
	S += (c_t3_t50*MAS[4])-1 < c_t300_mem1*MAS_MEM[9]
	S += c_t300_mem1 <= c_t300

	c_t301 = S.Task('c_t301', length=1, delay_cost=1)
	c_t301 += alt(MAS)

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	c_t301_mem0 += alt(MAS_MEM)
	S += (c_t3_t21*MAS[0])-1 < c_t301_mem0*MAS_MEM[0]
	S += (c_t3_t21*MAS[1])-1 < c_t301_mem0*MAS_MEM[2]
	S += (c_t3_t21*MAS[2])-1 < c_t301_mem0*MAS_MEM[4]
	S += (c_t3_t21*MAS[3])-1 < c_t301_mem0*MAS_MEM[6]
	S += (c_t3_t21*MAS[4])-1 < c_t301_mem0*MAS_MEM[8]
	S += c_t301_mem0 <= c_t301

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	c_t301_mem1 += alt(MAS_MEM)
	S += (c_t3_t51*MAS[0])-1 < c_t301_mem1*MAS_MEM[1]
	S += (c_t3_t51*MAS[1])-1 < c_t301_mem1*MAS_MEM[3]
	S += (c_t3_t51*MAS[2])-1 < c_t301_mem1*MAS_MEM[5]
	S += (c_t3_t51*MAS[3])-1 < c_t301_mem1*MAS_MEM[7]
	S += (c_t3_t51*MAS[4])-1 < c_t301_mem1*MAS_MEM[9]
	S += c_t301_mem1 <= c_t301

	c_t400 = S.Task('c_t400', length=1, delay_cost=1)
	c_t400 += alt(MAS)

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	c_t400_mem0 += MAS_MEM[2]
	S += 63 < c_t400_mem0
	S += c_t400_mem0 <= c_t400

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	c_t400_mem1 += alt(MAS_MEM)
	S += (c_t4_t50*MAS[0])-1 < c_t400_mem1*MAS_MEM[1]
	S += (c_t4_t50*MAS[1])-1 < c_t400_mem1*MAS_MEM[3]
	S += (c_t4_t50*MAS[2])-1 < c_t400_mem1*MAS_MEM[5]
	S += (c_t4_t50*MAS[3])-1 < c_t400_mem1*MAS_MEM[7]
	S += (c_t4_t50*MAS[4])-1 < c_t400_mem1*MAS_MEM[9]
	S += c_t400_mem1 <= c_t400

	c_t401 = S.Task('c_t401', length=1, delay_cost=1)
	c_t401 += alt(MAS)

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	c_t401_mem0 += alt(MAS_MEM)
	S += (c_t4_t21*MAS[0])-1 < c_t401_mem0*MAS_MEM[0]
	S += (c_t4_t21*MAS[1])-1 < c_t401_mem0*MAS_MEM[2]
	S += (c_t4_t21*MAS[2])-1 < c_t401_mem0*MAS_MEM[4]
	S += (c_t4_t21*MAS[3])-1 < c_t401_mem0*MAS_MEM[6]
	S += (c_t4_t21*MAS[4])-1 < c_t401_mem0*MAS_MEM[8]
	S += c_t401_mem0 <= c_t401

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	c_t401_mem1 += alt(MAS_MEM)
	S += (c_t4_t51*MAS[0])-1 < c_t401_mem1*MAS_MEM[1]
	S += (c_t4_t51*MAS[1])-1 < c_t401_mem1*MAS_MEM[3]
	S += (c_t4_t51*MAS[2])-1 < c_t401_mem1*MAS_MEM[5]
	S += (c_t4_t51*MAS[3])-1 < c_t401_mem1*MAS_MEM[7]
	S += (c_t4_t51*MAS[4])-1 < c_t401_mem1*MAS_MEM[9]
	S += c_t401_mem1 <= c_t401

	c_t500 = S.Task('c_t500', length=1, delay_cost=1)
	c_t500 += alt(MAS)

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	c_t500_mem0 += MAS_MEM[6]
	S += 62 < c_t500_mem0
	S += c_t500_mem0 <= c_t500

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	c_t500_mem1 += alt(MAS_MEM)
	S += (c_t5_t50*MAS[0])-1 < c_t500_mem1*MAS_MEM[1]
	S += (c_t5_t50*MAS[1])-1 < c_t500_mem1*MAS_MEM[3]
	S += (c_t5_t50*MAS[2])-1 < c_t500_mem1*MAS_MEM[5]
	S += (c_t5_t50*MAS[3])-1 < c_t500_mem1*MAS_MEM[7]
	S += (c_t5_t50*MAS[4])-1 < c_t500_mem1*MAS_MEM[9]
	S += c_t500_mem1 <= c_t500

	c_t501 = S.Task('c_t501', length=1, delay_cost=1)
	c_t501 += alt(MAS)

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	c_t501_mem0 += alt(MAS_MEM)
	S += (c_t5_t21*MAS[0])-1 < c_t501_mem0*MAS_MEM[0]
	S += (c_t5_t21*MAS[1])-1 < c_t501_mem0*MAS_MEM[2]
	S += (c_t5_t21*MAS[2])-1 < c_t501_mem0*MAS_MEM[4]
	S += (c_t5_t21*MAS[3])-1 < c_t501_mem0*MAS_MEM[6]
	S += (c_t5_t21*MAS[4])-1 < c_t501_mem0*MAS_MEM[8]
	S += c_t501_mem0 <= c_t501

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	c_t501_mem1 += alt(MAS_MEM)
	S += (c_t5_t51*MAS[0])-1 < c_t501_mem1*MAS_MEM[1]
	S += (c_t5_t51*MAS[1])-1 < c_t501_mem1*MAS_MEM[3]
	S += (c_t5_t51*MAS[2])-1 < c_t501_mem1*MAS_MEM[5]
	S += (c_t5_t51*MAS[3])-1 < c_t501_mem1*MAS_MEM[7]
	S += (c_t5_t51*MAS[4])-1 < c_t501_mem1*MAS_MEM[9]
	S += c_t501_mem1 <= c_t501

	c_s0000 = S.Task('c_s0000', length=1, delay_cost=1)
	c_s0000 += alt(MAS)

	c_s0000_mem0 = S.Task('c_s0000_mem0', length=1, delay_cost=1)
	c_s0000_mem0 += alt(MAS_MEM)
	S += (c_t000*MAS[0])-1 < c_s0000_mem0*MAS_MEM[0]
	S += (c_t000*MAS[1])-1 < c_s0000_mem0*MAS_MEM[2]
	S += (c_t000*MAS[2])-1 < c_s0000_mem0*MAS_MEM[4]
	S += (c_t000*MAS[3])-1 < c_s0000_mem0*MAS_MEM[6]
	S += (c_t000*MAS[4])-1 < c_s0000_mem0*MAS_MEM[8]
	S += c_s0000_mem0 <= c_s0000

	c_s0000_mem1 = S.Task('c_s0000_mem1', length=1, delay_cost=1)
	c_s0000_mem1 += alt(MAS_MEM)
	S += (c_t100*MAS[0])-1 < c_s0000_mem1*MAS_MEM[1]
	S += (c_t100*MAS[1])-1 < c_s0000_mem1*MAS_MEM[3]
	S += (c_t100*MAS[2])-1 < c_s0000_mem1*MAS_MEM[5]
	S += (c_t100*MAS[3])-1 < c_s0000_mem1*MAS_MEM[7]
	S += (c_t100*MAS[4])-1 < c_s0000_mem1*MAS_MEM[9]
	S += c_s0000_mem1 <= c_s0000

	c_s0001 = S.Task('c_s0001', length=1, delay_cost=1)
	c_s0001 += alt(MAS)

	c_s0001_mem0 = S.Task('c_s0001_mem0', length=1, delay_cost=1)
	c_s0001_mem0 += alt(MAS_MEM)
	S += (c_t001*MAS[0])-1 < c_s0001_mem0*MAS_MEM[0]
	S += (c_t001*MAS[1])-1 < c_s0001_mem0*MAS_MEM[2]
	S += (c_t001*MAS[2])-1 < c_s0001_mem0*MAS_MEM[4]
	S += (c_t001*MAS[3])-1 < c_s0001_mem0*MAS_MEM[6]
	S += (c_t001*MAS[4])-1 < c_s0001_mem0*MAS_MEM[8]
	S += c_s0001_mem0 <= c_s0001

	c_s0001_mem1 = S.Task('c_s0001_mem1', length=1, delay_cost=1)
	c_s0001_mem1 += alt(MAS_MEM)
	S += (c_t101*MAS[0])-1 < c_s0001_mem1*MAS_MEM[1]
	S += (c_t101*MAS[1])-1 < c_s0001_mem1*MAS_MEM[3]
	S += (c_t101*MAS[2])-1 < c_s0001_mem1*MAS_MEM[5]
	S += (c_t101*MAS[3])-1 < c_s0001_mem1*MAS_MEM[7]
	S += (c_t101*MAS[4])-1 < c_s0001_mem1*MAS_MEM[9]
	S += c_s0001_mem1 <= c_s0001

	c_s1000 = S.Task('c_s1000', length=1, delay_cost=1)
	c_s1000 += alt(MAS)

	c_s1000_mem0 = S.Task('c_s1000_mem0', length=1, delay_cost=1)
	c_s1000_mem0 += alt(MAS_MEM)
	S += (c_t100*MAS[0])-1 < c_s1000_mem0*MAS_MEM[0]
	S += (c_t100*MAS[1])-1 < c_s1000_mem0*MAS_MEM[2]
	S += (c_t100*MAS[2])-1 < c_s1000_mem0*MAS_MEM[4]
	S += (c_t100*MAS[3])-1 < c_s1000_mem0*MAS_MEM[6]
	S += (c_t100*MAS[4])-1 < c_s1000_mem0*MAS_MEM[8]
	S += c_s1000_mem0 <= c_s1000

	c_s1000_mem1 = S.Task('c_s1000_mem1', length=1, delay_cost=1)
	c_s1000_mem1 += alt(MAS_MEM)
	S += (c_t200*MAS[0])-1 < c_s1000_mem1*MAS_MEM[1]
	S += (c_t200*MAS[1])-1 < c_s1000_mem1*MAS_MEM[3]
	S += (c_t200*MAS[2])-1 < c_s1000_mem1*MAS_MEM[5]
	S += (c_t200*MAS[3])-1 < c_s1000_mem1*MAS_MEM[7]
	S += (c_t200*MAS[4])-1 < c_s1000_mem1*MAS_MEM[9]
	S += c_s1000_mem1 <= c_s1000

	c_s1001 = S.Task('c_s1001', length=1, delay_cost=1)
	c_s1001 += alt(MAS)

	c_s1001_mem0 = S.Task('c_s1001_mem0', length=1, delay_cost=1)
	c_s1001_mem0 += alt(MAS_MEM)
	S += (c_t101*MAS[0])-1 < c_s1001_mem0*MAS_MEM[0]
	S += (c_t101*MAS[1])-1 < c_s1001_mem0*MAS_MEM[2]
	S += (c_t101*MAS[2])-1 < c_s1001_mem0*MAS_MEM[4]
	S += (c_t101*MAS[3])-1 < c_s1001_mem0*MAS_MEM[6]
	S += (c_t101*MAS[4])-1 < c_s1001_mem0*MAS_MEM[8]
	S += c_s1001_mem0 <= c_s1001

	c_s1001_mem1 = S.Task('c_s1001_mem1', length=1, delay_cost=1)
	c_s1001_mem1 += alt(MAS_MEM)
	S += (c_t201*MAS[0])-1 < c_s1001_mem1*MAS_MEM[1]
	S += (c_t201*MAS[1])-1 < c_s1001_mem1*MAS_MEM[3]
	S += (c_t201*MAS[2])-1 < c_s1001_mem1*MAS_MEM[5]
	S += (c_t201*MAS[3])-1 < c_s1001_mem1*MAS_MEM[7]
	S += (c_t201*MAS[4])-1 < c_s1001_mem1*MAS_MEM[9]
	S += c_s1001_mem1 <= c_s1001

	c_s2000 = S.Task('c_s2000', length=1, delay_cost=1)
	c_s2000 += alt(MAS)

	c_s2000_mem0 = S.Task('c_s2000_mem0', length=1, delay_cost=1)
	c_s2000_mem0 += alt(MAS_MEM)
	S += (c_t200*MAS[0])-1 < c_s2000_mem0*MAS_MEM[0]
	S += (c_t200*MAS[1])-1 < c_s2000_mem0*MAS_MEM[2]
	S += (c_t200*MAS[2])-1 < c_s2000_mem0*MAS_MEM[4]
	S += (c_t200*MAS[3])-1 < c_s2000_mem0*MAS_MEM[6]
	S += (c_t200*MAS[4])-1 < c_s2000_mem0*MAS_MEM[8]
	S += c_s2000_mem0 <= c_s2000

	c_s2000_mem1 = S.Task('c_s2000_mem1', length=1, delay_cost=1)
	c_s2000_mem1 += alt(MAS_MEM)
	S += (c_t000*MAS[0])-1 < c_s2000_mem1*MAS_MEM[1]
	S += (c_t000*MAS[1])-1 < c_s2000_mem1*MAS_MEM[3]
	S += (c_t000*MAS[2])-1 < c_s2000_mem1*MAS_MEM[5]
	S += (c_t000*MAS[3])-1 < c_s2000_mem1*MAS_MEM[7]
	S += (c_t000*MAS[4])-1 < c_s2000_mem1*MAS_MEM[9]
	S += c_s2000_mem1 <= c_s2000

	c_s2001 = S.Task('c_s2001', length=1, delay_cost=1)
	c_s2001 += alt(MAS)

	c_s2001_mem0 = S.Task('c_s2001_mem0', length=1, delay_cost=1)
	c_s2001_mem0 += alt(MAS_MEM)
	S += (c_t201*MAS[0])-1 < c_s2001_mem0*MAS_MEM[0]
	S += (c_t201*MAS[1])-1 < c_s2001_mem0*MAS_MEM[2]
	S += (c_t201*MAS[2])-1 < c_s2001_mem0*MAS_MEM[4]
	S += (c_t201*MAS[3])-1 < c_s2001_mem0*MAS_MEM[6]
	S += (c_t201*MAS[4])-1 < c_s2001_mem0*MAS_MEM[8]
	S += c_s2001_mem0 <= c_s2001

	c_s2001_mem1 = S.Task('c_s2001_mem1', length=1, delay_cost=1)
	c_s2001_mem1 += alt(MAS_MEM)
	S += (c_t001*MAS[0])-1 < c_s2001_mem1*MAS_MEM[1]
	S += (c_t001*MAS[1])-1 < c_s2001_mem1*MAS_MEM[3]
	S += (c_t001*MAS[2])-1 < c_s2001_mem1*MAS_MEM[5]
	S += (c_t001*MAS[3])-1 < c_s2001_mem1*MAS_MEM[7]
	S += (c_t001*MAS[4])-1 < c_s2001_mem1*MAS_MEM[9]
	S += c_s2001_mem1 <= c_s2001

	c_s1_y1_0 = S.Task('c_s1_y1_0', length=1, delay_cost=1)
	c_s1_y1_0 += alt(MAS)

	c_s1_y1_0_mem0 = S.Task('c_s1_y1_0_mem0', length=1, delay_cost=1)
	c_s1_y1_0_mem0 += MAS_MEM[6]
	S += 53 < c_s1_y1_0_mem0
	S += c_s1_y1_0_mem0 <= c_s1_y1_0

	c_s1_y1_0_mem1 = S.Task('c_s1_y1_0_mem1', length=1, delay_cost=1)
	c_s1_y1_0_mem1 += alt(MAS_MEM)
	S += (c_s1111*MAS[0])-1 < c_s1_y1_0_mem1*MAS_MEM[1]
	S += (c_s1111*MAS[1])-1 < c_s1_y1_0_mem1*MAS_MEM[3]
	S += (c_s1111*MAS[2])-1 < c_s1_y1_0_mem1*MAS_MEM[5]
	S += (c_s1111*MAS[3])-1 < c_s1_y1_0_mem1*MAS_MEM[7]
	S += (c_s1111*MAS[4])-1 < c_s1_y1_0_mem1*MAS_MEM[9]
	S += c_s1_y1_0_mem1 <= c_s1_y1_0

	c_s1_y1_1 = S.Task('c_s1_y1_1', length=1, delay_cost=1)
	c_s1_y1_1 += alt(MAS)

	c_s1_y1_1_mem0 = S.Task('c_s1_y1_1_mem0', length=1, delay_cost=1)
	c_s1_y1_1_mem0 += alt(MAS_MEM)
	S += (c_s1111*MAS[0])-1 < c_s1_y1_1_mem0*MAS_MEM[0]
	S += (c_s1111*MAS[1])-1 < c_s1_y1_1_mem0*MAS_MEM[2]
	S += (c_s1111*MAS[2])-1 < c_s1_y1_1_mem0*MAS_MEM[4]
	S += (c_s1111*MAS[3])-1 < c_s1_y1_1_mem0*MAS_MEM[6]
	S += (c_s1111*MAS[4])-1 < c_s1_y1_1_mem0*MAS_MEM[8]
	S += c_s1_y1_1_mem0 <= c_s1_y1_1

	c_s1_y1_1_mem1 = S.Task('c_s1_y1_1_mem1', length=1, delay_cost=1)
	c_s1_y1_1_mem1 += MAS_MEM[7]
	S += 53 < c_s1_y1_1_mem1
	S += c_s1_y1_1_mem1 <= c_s1_y1_1

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(MAS)

	S += 36<c110

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[6]
	S += 51 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += alt(MAS_MEM)
	S += (c_t200*MAS[0])-1 < c110_mem1*MAS_MEM[1]
	S += (c_t200*MAS[1])-1 < c110_mem1*MAS_MEM[3]
	S += (c_t200*MAS[2])-1 < c110_mem1*MAS_MEM[5]
	S += (c_t200*MAS[3])-1 < c110_mem1*MAS_MEM[7]
	S += (c_t200*MAS[4])-1 < c110_mem1*MAS_MEM[9]
	S += c110_mem1 <= c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(MAS)

	S += 31<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MAS_MEM)
	S += (c_s011*MAS[0])-1 < c111_mem0*MAS_MEM[0]
	S += (c_s011*MAS[1])-1 < c111_mem0*MAS_MEM[2]
	S += (c_s011*MAS[2])-1 < c111_mem0*MAS_MEM[4]
	S += (c_s011*MAS[3])-1 < c111_mem0*MAS_MEM[6]
	S += (c_s011*MAS[4])-1 < c111_mem0*MAS_MEM[8]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(MAS_MEM)
	S += (c_t201*MAS[0])-1 < c111_mem1*MAS_MEM[1]
	S += (c_t201*MAS[1])-1 < c111_mem1*MAS_MEM[3]
	S += (c_t201*MAS[2])-1 < c111_mem1*MAS_MEM[5]
	S += (c_t201*MAS[3])-1 < c111_mem1*MAS_MEM[7]
	S += (c_t201*MAS[4])-1 < c111_mem1*MAS_MEM[9]
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(MAS)

	S += 28<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += MAS_MEM[2]
	S += 46 < c211_mem0
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(MAS_MEM)
	S += (c_s211*MAS[0])-1 < c211_mem1*MAS_MEM[1]
	S += (c_s211*MAS[1])-1 < c211_mem1*MAS_MEM[3]
	S += (c_s211*MAS[2])-1 < c211_mem1*MAS_MEM[5]
	S += (c_s211*MAS[3])-1 < c211_mem1*MAS_MEM[7]
	S += (c_s211*MAS[4])-1 < c211_mem1*MAS_MEM[9]
	S += c211_mem1 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c_s000 = S.Task('c_s000', length=1, delay_cost=1)
	c_s000 += alt(MAS)

	c_s000_mem0 = S.Task('c_s000_mem0', length=1, delay_cost=1)
	c_s000_mem0 += alt(MAS_MEM)
	S += (c_t300*MAS[0])-1 < c_s000_mem0*MAS_MEM[0]
	S += (c_t300*MAS[1])-1 < c_s000_mem0*MAS_MEM[2]
	S += (c_t300*MAS[2])-1 < c_s000_mem0*MAS_MEM[4]
	S += (c_t300*MAS[3])-1 < c_s000_mem0*MAS_MEM[6]
	S += (c_t300*MAS[4])-1 < c_s000_mem0*MAS_MEM[8]
	S += c_s000_mem0 <= c_s000

	c_s000_mem1 = S.Task('c_s000_mem1', length=1, delay_cost=1)
	c_s000_mem1 += alt(MAS_MEM)
	S += (c_s0000*MAS[0])-1 < c_s000_mem1*MAS_MEM[1]
	S += (c_s0000*MAS[1])-1 < c_s000_mem1*MAS_MEM[3]
	S += (c_s0000*MAS[2])-1 < c_s000_mem1*MAS_MEM[5]
	S += (c_s0000*MAS[3])-1 < c_s000_mem1*MAS_MEM[7]
	S += (c_s0000*MAS[4])-1 < c_s000_mem1*MAS_MEM[9]
	S += c_s000_mem1 <= c_s000

	c_s001 = S.Task('c_s001', length=1, delay_cost=1)
	c_s001 += alt(MAS)

	c_s001_mem0 = S.Task('c_s001_mem0', length=1, delay_cost=1)
	c_s001_mem0 += alt(MAS_MEM)
	S += (c_t301*MAS[0])-1 < c_s001_mem0*MAS_MEM[0]
	S += (c_t301*MAS[1])-1 < c_s001_mem0*MAS_MEM[2]
	S += (c_t301*MAS[2])-1 < c_s001_mem0*MAS_MEM[4]
	S += (c_t301*MAS[3])-1 < c_s001_mem0*MAS_MEM[6]
	S += (c_t301*MAS[4])-1 < c_s001_mem0*MAS_MEM[8]
	S += c_s001_mem0 <= c_s001

	c_s001_mem1 = S.Task('c_s001_mem1', length=1, delay_cost=1)
	c_s001_mem1 += alt(MAS_MEM)
	S += (c_s0001*MAS[0])-1 < c_s001_mem1*MAS_MEM[1]
	S += (c_s0001*MAS[1])-1 < c_s001_mem1*MAS_MEM[3]
	S += (c_s0001*MAS[2])-1 < c_s001_mem1*MAS_MEM[5]
	S += (c_s0001*MAS[3])-1 < c_s001_mem1*MAS_MEM[7]
	S += (c_s0001*MAS[4])-1 < c_s001_mem1*MAS_MEM[9]
	S += c_s001_mem1 <= c_s001

	c_s1100 = S.Task('c_s1100', length=1, delay_cost=1)
	c_s1100 += alt(MAS)

	c_s1100_mem0 = S.Task('c_s1100_mem0', length=1, delay_cost=1)
	c_s1100_mem0 += alt(MAS_MEM)
	S += (c_t400*MAS[0])-1 < c_s1100_mem0*MAS_MEM[0]
	S += (c_t400*MAS[1])-1 < c_s1100_mem0*MAS_MEM[2]
	S += (c_t400*MAS[2])-1 < c_s1100_mem0*MAS_MEM[4]
	S += (c_t400*MAS[3])-1 < c_s1100_mem0*MAS_MEM[6]
	S += (c_t400*MAS[4])-1 < c_s1100_mem0*MAS_MEM[8]
	S += c_s1100_mem0 <= c_s1100

	c_s1100_mem1 = S.Task('c_s1100_mem1', length=1, delay_cost=1)
	c_s1100_mem1 += alt(MAS_MEM)
	S += (c_s1000*MAS[0])-1 < c_s1100_mem1*MAS_MEM[1]
	S += (c_s1000*MAS[1])-1 < c_s1100_mem1*MAS_MEM[3]
	S += (c_s1000*MAS[2])-1 < c_s1100_mem1*MAS_MEM[5]
	S += (c_s1000*MAS[3])-1 < c_s1100_mem1*MAS_MEM[7]
	S += (c_s1000*MAS[4])-1 < c_s1100_mem1*MAS_MEM[9]
	S += c_s1100_mem1 <= c_s1100

	c_s1101 = S.Task('c_s1101', length=1, delay_cost=1)
	c_s1101 += alt(MAS)

	c_s1101_mem0 = S.Task('c_s1101_mem0', length=1, delay_cost=1)
	c_s1101_mem0 += alt(MAS_MEM)
	S += (c_t401*MAS[0])-1 < c_s1101_mem0*MAS_MEM[0]
	S += (c_t401*MAS[1])-1 < c_s1101_mem0*MAS_MEM[2]
	S += (c_t401*MAS[2])-1 < c_s1101_mem0*MAS_MEM[4]
	S += (c_t401*MAS[3])-1 < c_s1101_mem0*MAS_MEM[6]
	S += (c_t401*MAS[4])-1 < c_s1101_mem0*MAS_MEM[8]
	S += c_s1101_mem0 <= c_s1101

	c_s1101_mem1 = S.Task('c_s1101_mem1', length=1, delay_cost=1)
	c_s1101_mem1 += alt(MAS_MEM)
	S += (c_s1001*MAS[0])-1 < c_s1101_mem1*MAS_MEM[1]
	S += (c_s1001*MAS[1])-1 < c_s1101_mem1*MAS_MEM[3]
	S += (c_s1001*MAS[2])-1 < c_s1101_mem1*MAS_MEM[5]
	S += (c_s1001*MAS[3])-1 < c_s1101_mem1*MAS_MEM[7]
	S += (c_s1001*MAS[4])-1 < c_s1101_mem1*MAS_MEM[9]
	S += c_s1101_mem1 <= c_s1101

	c_s200 = S.Task('c_s200', length=1, delay_cost=1)
	c_s200 += alt(MAS)

	c_s200_mem0 = S.Task('c_s200_mem0', length=1, delay_cost=1)
	c_s200_mem0 += alt(MAS_MEM)
	S += (c_t500*MAS[0])-1 < c_s200_mem0*MAS_MEM[0]
	S += (c_t500*MAS[1])-1 < c_s200_mem0*MAS_MEM[2]
	S += (c_t500*MAS[2])-1 < c_s200_mem0*MAS_MEM[4]
	S += (c_t500*MAS[3])-1 < c_s200_mem0*MAS_MEM[6]
	S += (c_t500*MAS[4])-1 < c_s200_mem0*MAS_MEM[8]
	S += c_s200_mem0 <= c_s200

	c_s200_mem1 = S.Task('c_s200_mem1', length=1, delay_cost=1)
	c_s200_mem1 += alt(MAS_MEM)
	S += (c_s2000*MAS[0])-1 < c_s200_mem1*MAS_MEM[1]
	S += (c_s2000*MAS[1])-1 < c_s200_mem1*MAS_MEM[3]
	S += (c_s2000*MAS[2])-1 < c_s200_mem1*MAS_MEM[5]
	S += (c_s2000*MAS[3])-1 < c_s200_mem1*MAS_MEM[7]
	S += (c_s2000*MAS[4])-1 < c_s200_mem1*MAS_MEM[9]
	S += c_s200_mem1 <= c_s200

	c_s201 = S.Task('c_s201', length=1, delay_cost=1)
	c_s201 += alt(MAS)

	c_s201_mem0 = S.Task('c_s201_mem0', length=1, delay_cost=1)
	c_s201_mem0 += alt(MAS_MEM)
	S += (c_t501*MAS[0])-1 < c_s201_mem0*MAS_MEM[0]
	S += (c_t501*MAS[1])-1 < c_s201_mem0*MAS_MEM[2]
	S += (c_t501*MAS[2])-1 < c_s201_mem0*MAS_MEM[4]
	S += (c_t501*MAS[3])-1 < c_s201_mem0*MAS_MEM[6]
	S += (c_t501*MAS[4])-1 < c_s201_mem0*MAS_MEM[8]
	S += c_s201_mem0 <= c_s201

	c_s201_mem1 = S.Task('c_s201_mem1', length=1, delay_cost=1)
	c_s201_mem1 += alt(MAS_MEM)
	S += (c_s2001*MAS[0])-1 < c_s201_mem1*MAS_MEM[1]
	S += (c_s2001*MAS[1])-1 < c_s201_mem1*MAS_MEM[3]
	S += (c_s2001*MAS[2])-1 < c_s201_mem1*MAS_MEM[5]
	S += (c_s2001*MAS[3])-1 < c_s201_mem1*MAS_MEM[7]
	S += (c_s2001*MAS[4])-1 < c_s201_mem1*MAS_MEM[9]
	S += c_s201_mem1 <= c_s201

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 42<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(MAS_MEM)
	S += (c_t000*MAS[0])-1 < c000_mem0*MAS_MEM[0]
	S += (c_t000*MAS[1])-1 < c000_mem0*MAS_MEM[2]
	S += (c_t000*MAS[2])-1 < c000_mem0*MAS_MEM[4]
	S += (c_t000*MAS[3])-1 < c000_mem0*MAS_MEM[6]
	S += (c_t000*MAS[4])-1 < c000_mem0*MAS_MEM[8]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (c_s1_y1_0*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (c_s1_y1_0*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (c_s1_y1_0*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (c_s1_y1_0*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += (c_s1_y1_0*MAS[4])-1 < c000_mem1*MAS_MEM[9]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 37<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(MAS_MEM)
	S += (c_t001*MAS[0])-1 < c001_mem0*MAS_MEM[0]
	S += (c_t001*MAS[1])-1 < c001_mem0*MAS_MEM[2]
	S += (c_t001*MAS[2])-1 < c001_mem0*MAS_MEM[4]
	S += (c_t001*MAS[3])-1 < c001_mem0*MAS_MEM[6]
	S += (c_t001*MAS[4])-1 < c001_mem0*MAS_MEM[8]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (c_s1_y1_1*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (c_s1_y1_1*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (c_s1_y1_1*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (c_s1_y1_1*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += (c_s1_y1_1*MAS[4])-1 < c001_mem1*MAS_MEM[9]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(MAS)

	S += 29<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAS_MEM[8]
	S += 12 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (c_s1100*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (c_s1100*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (c_s1100*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (c_s1100*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += (c_s1100*MAS[4])-1 < c010_mem1*MAS_MEM[9]
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)

	S += 31<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[0]
	S += 25 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c_s1101*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c_s1101*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (c_s1101*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (c_s1101*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += (c_s1101*MAS[4])-1 < c011_mem1*MAS_MEM[9]
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(MAS)

	S += 41<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (c_s000*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (c_s000*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (c_s000*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (c_s000*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += (c_s000*MAS[4])-1 < c100_mem0*MAS_MEM[8]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MAS_MEM[5]
	S += 43 < c100_mem1
	S += c100_mem1 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)

	S += 39<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (c_s001*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (c_s001*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (c_s001*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (c_s001*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += (c_s001*MAS[4])-1 < c101_mem0*MAS_MEM[8]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += MAS_MEM[5]
	S += 41 < c101_mem1
	S += c101_mem1 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(MAS)

	S += 38<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (c_t100*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (c_t100*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (c_t100*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (c_t100*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += (c_t100*MAS[4])-1 < c200_mem0*MAS_MEM[8]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += alt(MAS_MEM)
	S += (c_s200*MAS[0])-1 < c200_mem1*MAS_MEM[1]
	S += (c_s200*MAS[1])-1 < c200_mem1*MAS_MEM[3]
	S += (c_s200*MAS[2])-1 < c200_mem1*MAS_MEM[5]
	S += (c_s200*MAS[3])-1 < c200_mem1*MAS_MEM[7]
	S += (c_s200*MAS[4])-1 < c200_mem1*MAS_MEM[9]
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(MAS)

	S += 40<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (c_t101*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (c_t101*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (c_t101*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (c_t101*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += (c_t101*MAS[4])-1 < c201_mem0*MAS_MEM[8]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(MAS_MEM)
	S += (c_s201*MAS[0])-1 < c201_mem1*MAS_MEM[1]
	S += (c_s201*MAS[1])-1 < c201_mem1*MAS_MEM[3]
	S += (c_s201*MAS[2])-1 < c201_mem1*MAS_MEM[5]
	S += (c_s201*MAS[3])-1 < c201_mem1*MAS_MEM[7]
	S += (c_s201*MAS[4])-1 < c201_mem1*MAS_MEM[9]
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS5/SQR/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

