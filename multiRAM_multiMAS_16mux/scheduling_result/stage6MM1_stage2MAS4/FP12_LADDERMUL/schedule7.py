from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 231
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 0
	d_t1_a1_1_in += MAS_in[0]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 0
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 0
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=2, delay_cost=1)
	S += d_t1_a1_1 >= 1
	d_t1_a1_1 += MAS[0]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 1
	d_t2_t10_in += MAS_in[3]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 1
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 1
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=2, delay_cost=1)
	S += d_t2_t10 >= 2
	d_t2_t10 += MAS[3]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 2
	d_t2_t3_t2_in += MAS_in[1]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 2
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 2
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 3
	d_t0_t11_in += MAS_in[1]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 3
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 3
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=2, delay_cost=1)
	S += d_t2_t3_t2 >= 3
	d_t2_t3_t2 += MAS[1]

	d_t0_t11 = S.Task('d_t0_t11', length=2, delay_cost=1)
	S += d_t0_t11 >= 4
	d_t0_t11 += MAS[1]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 4
	d_t2_t3_t3_in += MAS_in[1]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 4
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 4
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 5
	d_t1_t3_t3_in += MAS_in[0]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 5
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 5
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=2, delay_cost=1)
	S += d_t2_t3_t3 >= 5
	d_t2_t3_t3 += MAS[1]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=2, delay_cost=1)
	S += d_t1_t3_t3 >= 6
	d_t1_t3_t3 += MAS[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 6
	d_t2_a1_1_in += MAS_in[0]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 6
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 6
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 6
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 6
	d_t2_t3_t4_mem0 += MAS_MEM[2]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 6
	d_t2_t3_t4_mem1 += MAS_MEM[3]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=2, delay_cost=1)
	S += d_t2_a1_1 >= 7
	d_t2_a1_1 += MAS[0]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=6, delay_cost=1)
	S += d_t2_t3_t4 >= 7
	d_t2_t3_t4 += MM[0]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 7
	d_t3000_in += MAS_in[2]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 7
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 7
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 8
	d_t0_a1_0_in += MAS_in[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 8
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 8
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=2, delay_cost=1)
	S += d_t3000 >= 8
	d_t3000 += MAS[2]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=2, delay_cost=1)
	S += d_t0_a1_0 >= 9
	d_t0_a1_0 += MAS[0]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 9
	d_t0_a1_1_in += MAS_in[0]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 9
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 9
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=2, delay_cost=1)
	S += d_t0_a1_1 >= 10
	d_t0_a1_1 += MAS[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 10
	d_t1_a1_0_in += MAS_in[0]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 10
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 10
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 11
	d_t0_t3_t3_in += MAS_in[1]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 11
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 11
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=2, delay_cost=1)
	S += d_t1_a1_0 >= 11
	d_t1_a1_0 += MAS[0]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=2, delay_cost=1)
	S += d_t0_t3_t3 >= 12
	d_t0_t3_t3 += MAS[1]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 12
	d_t3011_in += MAS_in[1]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 12
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 12
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 13
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 13
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 13
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=2, delay_cost=1)
	S += d_t3011 >= 13
	d_t3011 += MAS[1]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 14
	d_t1_t3_t2_in += MAS_in[0]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 14
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 14
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=6, delay_cost=1)
	S += d_t2_t3_t0 >= 14
	d_t2_t3_t0 += MM[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=2, delay_cost=1)
	S += d_t1_t3_t2 >= 15
	d_t1_t3_t2 += MAS[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 15
	d_t2_a1_0_in += MAS_in[3]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 15
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 15
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 16
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 16
	d_t1_t3_t4_mem0 += MAS_MEM[0]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 16
	d_t1_t3_t4_mem1 += MAS_MEM[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=2, delay_cost=1)
	S += d_t2_a1_0 >= 16
	d_t2_a1_0 += MAS[3]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 16
	d_t4001_in += MAS_in[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 16
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 16
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=6, delay_cost=1)
	S += d_t1_t3_t4 >= 17
	d_t1_t3_t4 += MM[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 17
	d_t3010_in += MAS_in[0]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 17
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 17
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=2, delay_cost=1)
	S += d_t4001 >= 17
	d_t4001 += MAS[0]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 18
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 18
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 18
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t3010 = S.Task('d_t3010', length=2, delay_cost=1)
	S += d_t3010 >= 18
	d_t3010 += MAS[0]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 19
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 19
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 19
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=6, delay_cost=1)
	S += d_t2_t3_t1 >= 19
	d_t2_t3_t1 += MM[0]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 19
	d_t3_t10_in += MAS_in[3]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 19
	d_t3_t10_mem0 += MAS_MEM[4]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 19
	d_t3_t10_mem1 += MAS_MEM[1]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 19
	d_t3_t3_t3_in += MAS_in[1]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 19
	d_t3_t3_t3_mem0 += MAS_MEM[0]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 19
	d_t3_t3_t3_mem1 += MAS_MEM[3]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 20
	d_t1_t10_in += MAS_in[3]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 20
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 20
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=6, delay_cost=1)
	S += d_t1_t3_t0 >= 20
	d_t1_t3_t0 += MM[0]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 20
	d_t3_a1_0_in += MAS_in[2]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 20
	d_t3_a1_0_mem0 += MAS_MEM[0]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 20
	d_t3_a1_0_mem1 += MAS_MEM[3]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 20
	d_t3_a1_1_in += MAS_in[0]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 20
	d_t3_a1_1_mem0 += MAS_MEM[2]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 20
	d_t3_a1_1_mem1 += MAS_MEM[1]

	d_t3_t10 = S.Task('d_t3_t10', length=2, delay_cost=1)
	S += d_t3_t10 >= 20
	d_t3_t10 += MAS[3]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=2, delay_cost=1)
	S += d_t3_t3_t3 >= 20
	d_t3_t3_t3 += MAS[1]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 21
	d_t0_t3_t2_in += MAS_in[1]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 21
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 21
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t1_t10 = S.Task('d_t1_t10', length=2, delay_cost=1)
	S += d_t1_t10 >= 21
	d_t1_t10 += MAS[3]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=2, delay_cost=1)
	S += d_t3_a1_0 >= 21
	d_t3_a1_0 += MAS[2]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=2, delay_cost=1)
	S += d_t3_a1_1 >= 21
	d_t3_a1_1 += MAS[0]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 21
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 21
	d_t3_t3_t0_mem0 += MAS_MEM[4]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 21
	d_t3_t3_t0_mem1 += MAS_MEM[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=2, delay_cost=1)
	S += d_t0_t3_t2 >= 22
	d_t0_t3_t2 += MAS[1]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=6, delay_cost=1)
	S += d_t3_t3_t0 >= 22
	d_t3_t3_t0 += MM[0]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 22
	d_t4000_in += MAS_in[3]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 22
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 22
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 23
	d_t0_t10_in += MAS_in[1]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 23
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 23
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 23
	d_t0_t3_t4_in += MM_in[0]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 23
	d_t0_t3_t4_mem0 += MAS_MEM[2]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 23
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t4000 = S.Task('d_t4000', length=2, delay_cost=1)
	S += d_t4000 >= 23
	d_t4000 += MAS[3]

	d_t0_t10 = S.Task('d_t0_t10', length=2, delay_cost=1)
	S += d_t0_t10 >= 24
	d_t0_t10 += MAS[1]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=6, delay_cost=1)
	S += d_t0_t3_t4 >= 24
	d_t0_t3_t4 += MM[0]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 24
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 24
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 24
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 24
	d_t2_t30_in += MAS_in[1]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 24
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 24
	d_t2_t30_mem1 += MM_MEM[1]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 24
	d_t4_t3_t2_in += MAS_in[2]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 24
	d_t4_t3_t2_mem0 += MAS_MEM[6]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 24
	d_t4_t3_t2_mem1 += MAS_MEM[1]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 25
	d_t0_t2_t3_in += MAS_in[3]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 25
	d_t0_t2_t3_mem0 += MAS_MEM[2]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 25
	d_t0_t2_t3_mem1 += MAS_MEM[3]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 25
	d_t1_t11_in += MAS_in[2]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 25
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 25
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=6, delay_cost=1)
	S += d_t1_t3_t1 >= 25
	d_t1_t3_t1 += MM[0]

	d_t2_t30 = S.Task('d_t2_t30', length=2, delay_cost=1)
	S += d_t2_t30 >= 25
	d_t2_t30 += MAS[1]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 25
	d_t2_t3_t5_in += MAS_in[1]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 25
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 25
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=2, delay_cost=1)
	S += d_t4_t3_t2 >= 25
	d_t4_t3_t2 += MAS[2]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=2, delay_cost=1)
	S += d_t0_t2_t3 >= 26
	d_t0_t2_t3 += MAS[3]

	d_t1_t11 = S.Task('d_t1_t11', length=2, delay_cost=1)
	S += d_t1_t11 >= 26
	d_t1_t11 += MAS[2]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 26
	d_t2_t11_in += MAS_in[3]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 26
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 26
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=2, delay_cost=1)
	S += d_t2_t3_t5 >= 26
	d_t2_t3_t5 += MAS[1]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 27
	d_t1_t2_t3_in += MAS_in[2]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 27
	d_t1_t2_t3_mem0 += MAS_MEM[6]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 27
	d_t1_t2_t3_mem1 += MAS_MEM[5]

	d_t2_t11 = S.Task('d_t2_t11', length=2, delay_cost=1)
	S += d_t2_t11 >= 27
	d_t2_t11 += MAS[3]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 27
	d_t3001_in += MAS_in[3]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 27
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 27
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 28
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 28
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 28
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=2, delay_cost=1)
	S += d_t1_t2_t3 >= 28
	d_t1_t2_t3 += MAS[2]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 28
	d_t2_t2_t3_in += MAS_in[1]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 28
	d_t2_t2_t3_mem0 += MAS_MEM[6]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 28
	d_t2_t2_t3_mem1 += MAS_MEM[7]

	d_t3001 = S.Task('d_t3001', length=2, delay_cost=1)
	S += d_t3001 >= 28
	d_t3001 += MAS[3]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 29
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 29
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 29
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=6, delay_cost=1)
	S += d_t0_t3_t1 >= 29
	d_t0_t3_t1 += MM[0]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=2, delay_cost=1)
	S += d_t2_t2_t3 >= 29
	d_t2_t2_t3 += MAS[1]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 29
	d_t3_t11_in += MAS_in[3]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 29
	d_t3_t11_mem0 += MAS_MEM[6]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 29
	d_t3_t11_mem1 += MAS_MEM[3]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 29
	d_t3_t3_t2_in += MAS_in[2]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 29
	d_t3_t3_t2_mem0 += MAS_MEM[4]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 29
	d_t3_t3_t2_mem1 += MAS_MEM[7]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 30
	c_t1_t31_in += MAS_in[2]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 30
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 30
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=6, delay_cost=1)
	S += d_t0_t3_t0 >= 30
	d_t0_t3_t0 += MM[0]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 30
	d_t1_t3_t5_in += MAS_in[0]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 30
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 30
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t3_t11 = S.Task('d_t3_t11', length=2, delay_cost=1)
	S += d_t3_t11 >= 30
	d_t3_t11 += MAS[3]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 30
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 30
	d_t3_t3_t1_mem0 += MAS_MEM[6]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 30
	d_t3_t3_t1_mem1 += MAS_MEM[3]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=2, delay_cost=1)
	S += d_t3_t3_t2 >= 30
	d_t3_t3_t2 += MAS[2]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 31
	c_t1_t0_t3_in += MAS_in[0]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 31
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 31
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 31
	c_t1_t31 += MAS[2]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 31
	d_t1_t30_in += MAS_in[2]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 31
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 31
	d_t1_t30_mem1 += MM_MEM[1]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=2, delay_cost=1)
	S += d_t1_t3_t5 >= 31
	d_t1_t3_t5 += MAS[0]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=6, delay_cost=1)
	S += d_t3_t3_t1 >= 31
	d_t3_t3_t1 += MM[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 32
	c_t1_t0_t3 += MAS[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 32
	c_t1_t21_in += MAS_in[2]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 32
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 32
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t1_t30 = S.Task('d_t1_t30', length=2, delay_cost=1)
	S += d_t1_t30 >= 32
	d_t1_t30 += MAS[2]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 33
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 33
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 33
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 33
	c_t1_t21 += MAS[2]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 34
	c_t0_t31_in += MAS_in[2]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 34
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 34
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 34
	c_t1_t0_t2 += MAS[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 34
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 34
	c_t1_t4_t1_mem0 += MAS_MEM[4]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 34
	c_t1_t4_t1_mem1 += MAS_MEM[5]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 35
	c_t0_t20_in += MAS_in[3]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 35
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 35
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 35
	c_t0_t31 += MAS[2]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 35
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 35
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 35
	c_t1_t0_t4_mem1 += MAS_MEM[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=6, delay_cost=1)
	S += c_t1_t4_t1 >= 35
	c_t1_t4_t1 += MM[0]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 35
	d_t0_t3_t5_in += MAS_in[2]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 35
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 35
	d_t0_t3_t5_mem1 += MM_MEM[1]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 36
	c_t0_t20 += MAS[3]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=6, delay_cost=1)
	S += c_t1_t0_t4 >= 36
	c_t1_t0_t4 += MM[0]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 36
	d_t0_t30_in += MAS_in[0]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 36
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 36
	d_t0_t30_mem1 += MM_MEM[1]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=2, delay_cost=1)
	S += d_t0_t3_t5 >= 36
	d_t0_t3_t5 += MAS[2]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 36
	d_t5010_in += MAS_in[3]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 36
	d_t5010_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 36
	d_t5010_mem1 += MAIN_MEM_r[1]

	d_t0_t30 = S.Task('d_t0_t30', length=2, delay_cost=1)
	S += d_t0_t30 >= 37
	d_t0_t30 += MAS[0]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 37
	d_t4011_in += MAS_in[1]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 37
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 37
	d_t4011_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=2, delay_cost=1)
	S += d_t5010 >= 37
	d_t5010 += MAS[3]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 38
	c_t1_t1_t3_in += MAS_in[3]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 38
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 38
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	d_t4011 = S.Task('d_t4011', length=2, delay_cost=1)
	S += d_t4011 >= 38
	d_t4011 += MAS[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 39
	c_t0_t30_in += MAS_in[2]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 39
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 39
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 39
	c_t1_t1_t3 += MAS[3]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 39
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 39
	d_t4_t3_t1_mem0 += MAS_MEM[0]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 39
	d_t4_t3_t1_mem1 += MAS_MEM[3]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 40
	c_t0_t30 += MAS[2]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 40
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 40
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 40
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 40
	d_t4_t11_in += MAS_in[2]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 40
	d_t4_t11_mem0 += MAS_MEM[0]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 40
	d_t4_t11_mem1 += MAS_MEM[3]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=6, delay_cost=1)
	S += d_t4_t3_t1 >= 40
	d_t4_t3_t1 += MM[0]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 41
	c_t0_t0_t2_in += MAS_in[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 41
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 41
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 41
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 41
	c_t0_t4_t0_mem0 += MAS_MEM[6]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 41
	c_t0_t4_t0_mem1 += MAS_MEM[5]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 41
	c_t1_t30 += MAS[0]

	d_t4_t11 = S.Task('d_t4_t11', length=2, delay_cost=1)
	S += d_t4_t11 >= 41
	d_t4_t11 += MAS[2]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 42
	c_t0_t0_t2 += MAS[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 42
	c_t0_t21_in += MAS_in[2]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 42
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 42
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=6, delay_cost=1)
	S += c_t0_t4_t0 >= 42
	c_t0_t4_t0 += MM[0]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 42
	c_t1_t4_t3_in += MAS_in[1]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 42
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 42
	c_t1_t4_t3_mem1 += MAS_MEM[5]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 43
	c_t0_t21 += MAS[2]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 43
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 43
	c_t0_t4_t3_mem0 += MAS_MEM[4]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 43
	c_t0_t4_t3_mem1 += MAS_MEM[5]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 43
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 43
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 43
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=2, delay_cost=1)
	S += c_t1_t4_t3 >= 43
	c_t1_t4_t3 += MAS[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 44
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 44
	c_t0_t4_t1_mem0 += MAS_MEM[4]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 44
	c_t0_t4_t1_mem1 += MAS_MEM[5]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=2, delay_cost=1)
	S += c_t0_t4_t3 >= 44
	c_t0_t4_t3 += MAS[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=6, delay_cost=1)
	S += c_t1_t1_t1 >= 44
	c_t1_t1_t1 += MM[0]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 44
	d_t4010_in += MAS_in[3]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 44
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 44
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 45
	c_t0_t0_t3_in += MAS_in[1]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 45
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 45
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=6, delay_cost=1)
	S += c_t0_t4_t1 >= 45
	c_t0_t4_t1 += MM[0]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 45
	c_t0_t4_t2_in += MAS_in[3]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 45
	c_t0_t4_t2_mem0 += MAS_MEM[6]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 45
	c_t0_t4_t2_mem1 += MAS_MEM[5]

	d_t4010 = S.Task('d_t4010', length=2, delay_cost=1)
	S += d_t4010 >= 45
	d_t4010 += MAS[3]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 46
	c_t0_t0_t3 += MAS[1]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 46
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 46
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 46
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=2, delay_cost=1)
	S += c_t0_t4_t2 >= 46
	c_t0_t4_t2 += MAS[3]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 46
	d_t4_a1_0_in += MAS_in[3]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 46
	d_t4_a1_0_mem0 += MAS_MEM[6]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 46
	d_t4_a1_0_mem1 += MAS_MEM[3]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 46
	d_t4_a1_1_in += MAS_in[2]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 46
	d_t4_a1_1_mem0 += MAS_MEM[2]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 46
	d_t4_a1_1_mem1 += MAS_MEM[7]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 47
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 47
	c_t0_t0_t4_mem0 += MAS_MEM[0]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 47
	c_t0_t0_t4_mem1 += MAS_MEM[3]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 47
	c_t0_t1_t2_in += MAS_in[2]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 47
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 47
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 47
	c_t0_t1_t3 += MAS[0]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=2, delay_cost=1)
	S += d_t4_a1_0 >= 47
	d_t4_a1_0 += MAS[3]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=2, delay_cost=1)
	S += d_t4_a1_1 >= 47
	d_t4_a1_1 += MAS[2]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 47
	d_t4_t10_in += MAS_in[1]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 47
	d_t4_t10_mem0 += MAS_MEM[6]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 47
	d_t4_t10_mem1 += MAS_MEM[7]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=6, delay_cost=1)
	S += c_t0_t0_t4 >= 48
	c_t0_t0_t4 += MM[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 48
	c_t0_t1_t2 += MAS[2]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 48
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 48
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 48
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	d_t4_t10 = S.Task('d_t4_t10', length=2, delay_cost=1)
	S += d_t4_t10 >= 48
	d_t4_t10 += MAS[1]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 48
	d_t4_t3_t3_in += MAS_in[0]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 48
	d_t4_t3_t3_mem0 += MAS_MEM[6]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 48
	d_t4_t3_t3_mem1 += MAS_MEM[3]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=6, delay_cost=1)
	S += c_t1_t1_t0 >= 49
	c_t1_t1_t0 += MM[0]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 49
	d_t4_t3_t0_in += MM_in[0]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 49
	d_t4_t3_t0_mem0 += MAS_MEM[6]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 49
	d_t4_t3_t0_mem1 += MAS_MEM[7]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=2, delay_cost=1)
	S += d_t4_t3_t3 >= 49
	d_t4_t3_t3 += MAS[0]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 49
	d_t5001_in += MAS_in[2]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 49
	d_t5001_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 49
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 50
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 50
	c_t0_t1_t4_mem0 += MAS_MEM[4]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 50
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=6, delay_cost=1)
	S += d_t4_t3_t0 >= 50
	d_t4_t3_t0 += MM[0]

	d_t5001 = S.Task('d_t5001', length=2, delay_cost=1)
	S += d_t5001 >= 50
	d_t5001 += MAS[2]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 50
	d_t5011_in += MAS_in[0]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 50
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 50
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=6, delay_cost=1)
	S += c_t0_t1_t4 >= 51
	c_t0_t1_t4 += MM[0]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 51
	d_t5000_in += MAS_in[2]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 51
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 51
	d_t5000_mem1 += MAIN_MEM_r[1]

	d_t5011 = S.Task('d_t5011', length=2, delay_cost=1)
	S += d_t5011 >= 51
	d_t5011 += MAS[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 52
	c_t1_t20_in += MAS_in[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 52
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 52
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	d_t5000 = S.Task('d_t5000', length=2, delay_cost=1)
	S += d_t5000 >= 52
	d_t5000 += MAS[2]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 52
	d_t5_a1_1_in += MAS_in[2]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 52
	d_t5_a1_1_mem0 += MAS_MEM[0]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 52
	d_t5_a1_1_mem1 += MAS_MEM[7]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 52
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 52
	d_t5_t3_t1_mem0 += MAS_MEM[4]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 52
	d_t5_t3_t1_mem1 += MAS_MEM[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 53
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 53
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 53
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 53
	c_t1_t20 += MAS[0]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=2, delay_cost=1)
	S += d_t5_a1_1 >= 53
	d_t5_a1_1 += MAS[2]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 53
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 53
	d_t5_t3_t0_mem0 += MAS_MEM[4]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 53
	d_t5_t3_t0_mem1 += MAS_MEM[7]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=6, delay_cost=1)
	S += d_t5_t3_t1 >= 53
	d_t5_t3_t1 += MM[0]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 53
	d_t5_t3_t3_in += MAS_in[2]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 53
	d_t5_t3_t3_mem0 += MAS_MEM[6]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 53
	d_t5_t3_t3_mem1 += MAS_MEM[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 54
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 54
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 54
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 54
	c_t1_t1_t2 += MAS[0]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 54
	c_t1_t1_t5_in += MAS_in[1]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 54
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 54
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 54
	c_t1_t4_t2_in += MAS_in[3]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 54
	c_t1_t4_t2_mem0 += MAS_MEM[0]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 54
	c_t1_t4_t2_mem1 += MAS_MEM[5]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 54
	d_t5_a1_0_in += MAS_in[0]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 54
	d_t5_a1_0_mem0 += MAS_MEM[6]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 54
	d_t5_a1_0_mem1 += MAS_MEM[1]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 54
	d_t5_t10_in += MAS_in[2]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 54
	d_t5_t10_mem0 += MAS_MEM[4]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 54
	d_t5_t10_mem1 += MAS_MEM[7]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=6, delay_cost=1)
	S += d_t5_t3_t0 >= 54
	d_t5_t3_t0 += MM[0]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=2, delay_cost=1)
	S += d_t5_t3_t3 >= 54
	d_t5_t3_t3 += MAS[2]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 55
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 55
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 55
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=6, delay_cost=1)
	S += c_t1_t0_t1 >= 55
	c_t1_t0_t1 += MM[0]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 55
	c_t1_t10_in += MAS_in[1]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 55
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 55
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=2, delay_cost=1)
	S += c_t1_t1_t5 >= 55
	c_t1_t1_t5 += MAS[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=2, delay_cost=1)
	S += c_t1_t4_t2 >= 55
	c_t1_t4_t2 += MAS[3]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=2, delay_cost=1)
	S += d_t5_a1_0 >= 55
	d_t5_a1_0 += MAS[0]

	d_t5_t10 = S.Task('d_t5_t10', length=2, delay_cost=1)
	S += d_t5_t10 >= 55
	d_t5_t10 += MAS[2]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 55
	d_t5_t11_in += MAS_in[0]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 55
	d_t5_t11_mem0 += MAS_MEM[4]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 55
	d_t5_t11_mem1 += MAS_MEM[1]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 56
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 56
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 56
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=6, delay_cost=1)
	S += c_t1_t0_t0 >= 56
	c_t1_t0_t0 += MM[0]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 56
	c_t1_t10 += MAS[1]

	d_t5_t11 = S.Task('d_t5_t11', length=2, delay_cost=1)
	S += d_t5_t11 >= 56
	d_t5_t11 += MAS[0]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 56
	d_t5_t3_t2_in += MAS_in[3]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 56
	d_t5_t3_t2_mem0 += MAS_MEM[4]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 56
	d_t5_t3_t2_mem1 += MAS_MEM[5]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 57
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 57
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 57
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=6, delay_cost=1)
	S += c_t0_t1_t1 >= 57
	c_t0_t1_t1 += MM[0]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=2, delay_cost=1)
	S += d_t5_t3_t2 >= 57
	d_t5_t3_t2 += MAS[3]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 58
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 58
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 58
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=6, delay_cost=1)
	S += c_t0_t1_t0 >= 58
	c_t0_t1_t0 += MM[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 59
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 59
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 59
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=6, delay_cost=1)
	S += c_t0_t0_t1 >= 59
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=6, delay_cost=1)
	S += c_t0_t0_t0 >= 60
	c_t0_t0_t0 += MM[0]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 60
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 60
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 60
	c_t1_t1_t4_mem1 += MAS_MEM[7]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 60
	c_t3001_in += MAS_in[2]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 60
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 60
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 61
	c_t1_t0_t5_in += MAS_in[2]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 61
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 61
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=6, delay_cost=1)
	S += c_t1_t1_t4 >= 61
	c_t1_t1_t4 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 61
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 61
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 61
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 61
	c_t3001 += MAS[2]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 62
	c_t1_t00_in += MAS_in[2]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 62
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 62
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=2, delay_cost=1)
	S += c_t1_t0_t5 >= 62
	c_t1_t0_t5 += MAS[2]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 62
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 62
	c_t1_t4_t0_mem0 += MAS_MEM[0]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 62
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=6, delay_cost=1)
	S += c_t2_t0_t0 >= 62
	c_t2_t0_t0 += MM[0]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 62
	c_t2_t21_in += MAS_in[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 62
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 62
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 63
	c_t0_t10_in += MAS_in[2]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 63
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 63
	c_t0_t10_mem1 += MM_MEM[1]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 63
	c_t1_t00 += MAS[2]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=6, delay_cost=1)
	S += c_t1_t4_t0 >= 63
	c_t1_t4_t0 += MM[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 63
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 63
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 63
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 63
	c_t2_t21 += MAS[0]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 64
	c_t0_t10 += MAS[2]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 64
	c_t0_t1_t5_in += MAS_in[2]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 64
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 64
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=6, delay_cost=1)
	S += c_t2_t0_t1 >= 64
	c_t2_t0_t1 += MM[0]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 64
	c_t2_t20_in += MAS_in[0]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 64
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 64
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 65
	c_t0_t0_t5_in += MAS_in[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 65
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 65
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=2, delay_cost=1)
	S += c_t0_t1_t5 >= 65
	c_t0_t1_t5 += MAS[2]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 65
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 65
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 65
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 65
	c_t2_t20 += MAS[0]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 66
	c_t0_t00_in += MAS_in[1]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 66
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 66
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=2, delay_cost=1)
	S += c_t0_t0_t5 >= 66
	c_t0_t0_t5 += MAS[2]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=6, delay_cost=1)
	S += c_t2_t1_t0 >= 66
	c_t2_t1_t0 += MM[0]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 66
	c_t2_t4_t2_in += MAS_in[0]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 66
	c_t2_t4_t2_mem0 += MAS_MEM[0]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 66
	c_t2_t4_t2_mem1 += MAS_MEM[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 66
	c_t3000_in += MAS_in[2]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 66
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 66
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 67
	c_t0_t00 += MAS[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 67
	c_t2_t30_in += MAS_in[2]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 67
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 67
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=2, delay_cost=1)
	S += c_t2_t4_t2 >= 67
	c_t2_t4_t2 += MAS[0]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 67
	c_t3000 += MAS[2]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 68
	c_t2_t30 += MAS[2]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 68
	c_t3100_in += MAS_in[3]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 68
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 68
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 68
	c_t3_t0_t2_in += MAS_in[1]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 68
	c_t3_t0_t2_mem0 += MAS_MEM[4]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 68
	c_t3_t0_t2_mem1 += MAS_MEM[5]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 69
	c_t2_t00_in += MAS_in[3]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 69
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 69
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 69
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 69
	c_t2_t4_t0_mem0 += MAS_MEM[0]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 69
	c_t2_t4_t0_mem1 += MAS_MEM[5]

	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	S += c_t3100 >= 69
	c_t3100 += MAS[3]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=2, delay_cost=1)
	S += c_t3_t0_t2 >= 69
	c_t3_t0_t2 += MAS[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 69
	c_t4010_in += MAS_in[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 69
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 69
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 70
	c_t2_t00 += MAS[3]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 70
	c_t2_t0_t5_in += MAS_in[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 70
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 70
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 70
	c_t2_t31_in += MAS_in[3]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 70
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 70
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=6, delay_cost=1)
	S += c_t2_t4_t0 >= 70
	c_t2_t4_t0 += MM[0]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 70
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 70
	c_t3_t0_t0_mem0 += MAS_MEM[4]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 70
	c_t3_t0_t0_mem1 += MAS_MEM[7]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 70
	c_t4010 += MAS[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=2, delay_cost=1)
	S += c_t2_t0_t5 >= 71
	c_t2_t0_t5 += MAS[1]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 71
	c_t2_t31 += MAS[3]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 71
	c_t3010_in += MAS_in[2]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 71
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 71
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=6, delay_cost=1)
	S += c_t3_t0_t0 >= 71
	c_t3_t0_t0 += MM[0]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 72
	c_t2_t4_t3_in += MAS_in[2]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 72
	c_t2_t4_t3_mem0 += MAS_MEM[4]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 72
	c_t2_t4_t3_mem1 += MAS_MEM[7]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 72
	c_t3010 += MAS[2]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 72
	c_t3110_in += MAS_in[3]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 72
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 72
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 73
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 73
	c_t2_t4_t1_mem0 += MAS_MEM[0]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 73
	c_t2_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=2, delay_cost=1)
	S += c_t2_t4_t3 >= 73
	c_t2_t4_t3 += MAS[2]

	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	S += c_t3110 >= 73
	c_t3110 += MAS[3]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 73
	c_t3_t20_in += MAS_in[3]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 73
	c_t3_t20_mem0 += MAS_MEM[4]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 73
	c_t3_t20_mem1 += MAS_MEM[5]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 73
	c_t4000_in += MAS_in[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 73
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 73
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=6, delay_cost=1)
	S += c_t2_t4_t1 >= 74
	c_t2_t4_t1 += MM[0]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 74
	c_t3111_in += MAS_in[3]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 74
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 74
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 74
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 74
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 74
	c_t3_t1_t0_mem1 += MAS_MEM[7]

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	S += c_t3_t20 >= 74
	c_t3_t20 += MAS[3]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 74
	c_t4000 += MAS[0]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 75
	c_t3101_in += MAS_in[3]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 75
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 75
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	S += c_t3111 >= 75
	c_t3111 += MAS[3]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=6, delay_cost=1)
	S += c_t3_t1_t0 >= 75
	c_t3_t1_t0 += MM[0]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 75
	c_t3_t30_in += MAS_in[0]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 75
	c_t3_t30_mem0 += MAS_MEM[6]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 75
	c_t3_t30_mem1 += MAS_MEM[7]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 75
	c_t4_t20_in += MAS_in[2]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 75
	c_t4_t20_mem0 += MAS_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 75
	c_t4_t20_mem1 += MAS_MEM[3]

	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	S += c_t3101 >= 76
	c_t3101 += MAS[3]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 76
	c_t3_t1_t3_in += MAS_in[3]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 76
	c_t3_t1_t3_mem0 += MAS_MEM[6]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 76
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 76
	c_t3_t30 += MAS[0]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 76
	c_t4011_in += MAS_in[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 76
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 76
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	S += c_t4_t20 >= 76
	c_t4_t20 += MAS[2]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 77
	c_t3_t0_t3_in += MAS_in[0]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 77
	c_t3_t0_t3_mem0 += MAS_MEM[6]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 77
	c_t3_t0_t3_mem1 += MAS_MEM[7]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=2, delay_cost=1)
	S += c_t3_t1_t3 >= 77
	c_t3_t1_t3 += MAS[3]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 77
	c_t4011 += MAS[0]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 77
	c_t4110_in += MAS_in[2]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 77
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 77
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 78
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 78
	c_t3_t0_t1_mem0 += MAS_MEM[4]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 78
	c_t3_t0_t1_mem1 += MAS_MEM[7]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=2, delay_cost=1)
	S += c_t3_t0_t3 >= 78
	c_t3_t0_t3 += MAS[0]

	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	S += c_t4110 >= 78
	c_t4110 += MAS[2]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 78
	c_t4111_in += MAS_in[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 78
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 78
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 78
	c_t4_t1_t2_in += MAS_in[2]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 78
	c_t4_t1_t2_mem0 += MAS_MEM[2]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 78
	c_t4_t1_t2_mem1 += MAS_MEM[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=6, delay_cost=1)
	S += c_t3_t0_t1 >= 79
	c_t3_t0_t1 += MM[0]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 79
	c_t3_t31_in += MAS_in[0]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 79
	c_t3_t31_mem0 += MAS_MEM[6]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 79
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 79
	c_t4001_in += MAS_in[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 79
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 79
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	S += c_t4111 >= 79
	c_t4111 += MAS[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 79
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 79
	c_t4_t1_t0_mem0 += MAS_MEM[2]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 79
	c_t4_t1_t0_mem1 += MAS_MEM[5]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=2, delay_cost=1)
	S += c_t4_t1_t2 >= 79
	c_t4_t1_t2 += MAS[2]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 80
	c_t3011_in += MAS_in[3]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 80
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 80
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 80
	c_t3_t31 += MAS[0]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 80
	c_t4001 += MAS[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=6, delay_cost=1)
	S += c_t4_t1_t0 >= 80
	c_t4_t1_t0 += MM[0]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 80
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 80
	c_t4_t1_t1_mem0 += MAS_MEM[0]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 80
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 81
	c_t3011 += MAS[3]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 81
	c_t4_t0_t2_in += MAS_in[0]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 81
	c_t4_t0_t2_mem0 += MAS_MEM[0]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 81
	c_t4_t0_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=6, delay_cost=1)
	S += c_t4_t1_t1 >= 81
	c_t4_t1_t1 += MM[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 81
	c_t4_t1_t3_in += MAS_in[1]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 81
	c_t4_t1_t3_mem0 += MAS_MEM[4]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 81
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 81
	c_t5000_in += MAS_in[2]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 81
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 81
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 82
	c_t3_t1_t2_in += MAS_in[2]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 82
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 82
	c_t3_t1_t2_mem1 += MAS_MEM[7]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=2, delay_cost=1)
	S += c_t4_t0_t2 >= 82
	c_t4_t0_t2 += MAS[0]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=2, delay_cost=1)
	S += c_t4_t1_t3 >= 82
	c_t4_t1_t3 += MAS[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 82
	c_t4_t21_in += MAS_in[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 82
	c_t4_t21_mem0 += MAS_MEM[2]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 82
	c_t4_t21_mem1 += MAS_MEM[1]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 82
	c_t5000 += MAS[2]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 82
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 82
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 82
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 83
	c_t2_t0_t2_in += MAS_in[1]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 83
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 83
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=2, delay_cost=1)
	S += c_t3_t1_t2 >= 83
	c_t3_t1_t2 += MAS[2]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 83
	c_t3_t21_in += MAS_in[2]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 83
	c_t3_t21_mem0 += MAS_MEM[4]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 83
	c_t3_t21_mem1 += MAS_MEM[7]

	c_t4_t21 = S.Task('c_t4_t21', length=2, delay_cost=1)
	S += c_t4_t21 >= 83
	c_t4_t21 += MAS[0]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 83
	c_t5001 += MAS[1]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	S += c_t2_t0_t2 >= 84
	c_t2_t0_t2 += MAS[1]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 84
	c_t2_t1_t2_in += MAS_in[2]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 84
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 84
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 84
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 84
	c_t3_t1_t1_mem0 += MAS_MEM[6]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 84
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t3_t21 = S.Task('c_t3_t21', length=2, delay_cost=1)
	S += c_t3_t21 >= 84
	c_t3_t21 += MAS[2]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 84
	c_t5_t0_t2_in += MAS_in[1]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 84
	c_t5_t0_t2_mem0 += MAS_MEM[4]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 84
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	S += c_t2_t1_t2 >= 85
	c_t2_t1_t2 += MAS[2]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=6, delay_cost=1)
	S += c_t3_t1_t1 >= 85
	c_t3_t1_t1 += MM[0]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 85
	c_t4100_in += MAS_in[3]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 85
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 85
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=2, delay_cost=1)
	S += c_t5_t0_t2 >= 85
	c_t5_t0_t2 += MAS[1]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 86
	c_t2_t1_t3_in += MAS_in[0]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 86
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 86
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	S += c_t4100 >= 86
	c_t4100 += MAS[3]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	S += c_t2_t1_t3 >= 87
	c_t2_t1_t3 += MAS[0]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 87
	c_t4101_in += MAS_in[3]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 87
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 87
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 87
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 87
	c_t4_t0_t0_mem0 += MAS_MEM[0]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 87
	c_t4_t0_t0_mem1 += MAS_MEM[7]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 87
	c_t4_t30_in += MAS_in[0]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 87
	c_t4_t30_mem0 += MAS_MEM[6]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 87
	c_t4_t30_mem1 += MAS_MEM[5]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 88
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 88
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 88
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	S += c_t4101 >= 88
	c_t4101 += MAS[3]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=6, delay_cost=1)
	S += c_t4_t0_t0 >= 88
	c_t4_t0_t0 += MM[0]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 88
	c_t4_t30 += MAS[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 89
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 89
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 89
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=6, delay_cost=1)
	S += c_t2_t1_t1 >= 89
	c_t2_t1_t1 += MM[0]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 89
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 89
	c_t4_t0_t1_mem0 += MAS_MEM[2]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 89
	c_t4_t0_t1_mem1 += MAS_MEM[7]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 89
	c_t4_t31_in += MAS_in[2]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 89
	c_t4_t31_mem0 += MAS_MEM[6]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 89
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	S += c_t2_t0_t3 >= 90
	c_t2_t0_t3 += MAS[0]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 90
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 90
	c_t2_t1_t4_mem0 += MAS_MEM[4]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 90
	c_t2_t1_t4_mem1 += MAS_MEM[1]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=6, delay_cost=1)
	S += c_t4_t0_t1 >= 90
	c_t4_t0_t1 += MM[0]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 90
	c_t4_t0_t3_in += MAS_in[1]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 90
	c_t4_t0_t3_mem0 += MAS_MEM[6]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 90
	c_t4_t0_t3_mem1 += MAS_MEM[7]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 90
	c_t4_t31 += MAS[2]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 90
	c_t5011_in += MAS_in[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 90
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 90
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 91
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 91
	c_t2_t0_t4_mem0 += MAS_MEM[2]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 91
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=6, delay_cost=1)
	S += c_t2_t1_t4 >= 91
	c_t2_t1_t4 += MM[0]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=2, delay_cost=1)
	S += c_t4_t0_t3 >= 91
	c_t4_t0_t3 += MAS[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 91
	c_t5011 += MAS[0]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 91
	c_t5101_in += MAS_in[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 91
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 91
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=6, delay_cost=1)
	S += c_t2_t0_t4 >= 92
	c_t2_t0_t4 += MM[0]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 92
	c_t5100_in += MAS_in[2]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 92
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 92
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5101 = S.Task('c_t5101', length=2, delay_cost=1)
	S += c_t5101 >= 92
	c_t5101 += MAS[1]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 92
	c_t5_t21_in += MAS_in[0]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 92
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 92
	c_t5_t21_mem1 += MAS_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 93
	c_t5010_in += MAS_in[2]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 93
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 93
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=2, delay_cost=1)
	S += c_t5100 >= 93
	c_t5100 += MAS[2]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 93
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 93
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 93
	c_t5_t0_t1_mem1 += MAS_MEM[3]

	c_t5_t21 = S.Task('c_t5_t21', length=2, delay_cost=1)
	S += c_t5_t21 >= 93
	c_t5_t21 += MAS[0]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 94
	c_t2_t1_t5_in += MAS_in[0]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 94
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 94
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 94
	c_t5010 += MAS[2]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 94
	c_t5110_in += MAS_in[1]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 94
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 94
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 94
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 94
	c_t5_t0_t0_mem0 += MAS_MEM[4]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 94
	c_t5_t0_t0_mem1 += MAS_MEM[5]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=6, delay_cost=1)
	S += c_t5_t0_t1 >= 94
	c_t5_t0_t1 += MM[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 95
	c_t2_t10_in += MAS_in[2]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 95
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 95
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=2, delay_cost=1)
	S += c_t2_t1_t5 >= 95
	c_t2_t1_t5 += MAS[0]

	c_t5110 = S.Task('c_t5110', length=2, delay_cost=1)
	S += c_t5110 >= 95
	c_t5110 += MAS[1]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 95
	c_t5111_in += MAS_in[0]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 95
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 95
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=6, delay_cost=1)
	S += c_t5_t0_t0 >= 95
	c_t5_t0_t0 += MM[0]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 95
	c_t5_t0_t3_in += MAS_in[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 95
	c_t5_t0_t3_mem0 += MAS_MEM[4]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 95
	c_t5_t0_t3_mem1 += MAS_MEM[3]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 96
	c_t2_t10 += MAS[2]

	c_t5111 = S.Task('c_t5111', length=2, delay_cost=1)
	S += c_t5111 >= 96
	c_t5111 += MAS[0]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=2, delay_cost=1)
	S += c_t5_t0_t3 >= 96
	c_t5_t0_t3 += MAS[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 96
	c_t5_t1_t2_in += MAS_in[0]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 96
	c_t5_t1_t2_mem0 += MAS_MEM[4]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 96
	c_t5_t1_t2_mem1 += MAS_MEM[1]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 96
	d_t2_t00_in += MAS_in[3]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 96
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 96
	d_t2_t00_mem1 += MAS_MEM[7]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=2, delay_cost=1)
	S += c_t5_t1_t2 >= 97
	c_t5_t1_t2 += MAS[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 97
	c_t5_t30_in += MAS_in[2]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 97
	c_t5_t30_mem0 += MAS_MEM[4]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 97
	c_t5_t30_mem1 += MAS_MEM[3]

	d_t2_t00 = S.Task('d_t2_t00', length=2, delay_cost=1)
	S += d_t2_t00 >= 97
	d_t2_t00 += MAS[3]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 97
	d_t2_t01_in += MAS_in[0]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 97
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 97
	d_t2_t01_mem1 += MAS_MEM[1]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 98
	c_t5_t20_in += MAS_in[1]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 98
	c_t5_t20_mem0 += MAS_MEM[4]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 98
	c_t5_t20_mem1 += MAS_MEM[5]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 98
	c_t5_t30 += MAS[2]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 98
	d_t0_t01_in += MAS_in[2]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 98
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 98
	d_t0_t01_mem1 += MAS_MEM[1]

	d_t2_t01 = S.Task('d_t2_t01', length=2, delay_cost=1)
	S += d_t2_t01 >= 98
	d_t2_t01 += MAS[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 99
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 99
	c_t5_t1_t0_mem0 += MAS_MEM[4]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 99
	c_t5_t1_t0_mem1 += MAS_MEM[3]

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	S += c_t5_t20 >= 99
	c_t5_t20 += MAS[1]

	d_t0_t01 = S.Task('d_t0_t01', length=2, delay_cost=1)
	S += d_t0_t01 >= 99
	d_t0_t01 += MAS[2]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 99
	d_t1_t01_in += MAS_in[3]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 99
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 99
	d_t1_t01_mem1 += MAS_MEM[1]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=6, delay_cost=1)
	S += c_t5_t1_t0 >= 100
	c_t5_t1_t0 += MM[0]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 100
	d_t1_t00_in += MAS_in[2]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 100
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 100
	d_t1_t00_mem1 += MAS_MEM[1]

	d_t1_t01 = S.Task('d_t1_t01', length=2, delay_cost=1)
	S += d_t1_t01 >= 100
	d_t1_t01 += MAS[3]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 101
	d_t0_t00_in += MAS_in[3]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 101
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 101
	d_t0_t00_mem1 += MAS_MEM[1]

	d_t1_t00 = S.Task('d_t1_t00', length=2, delay_cost=1)
	S += d_t1_t00 >= 101
	d_t1_t00 += MAS[2]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 102
	c_t5_t31_in += MAS_in[3]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 102
	c_t5_t31_mem0 += MAS_MEM[2]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 102
	c_t5_t31_mem1 += MAS_MEM[1]

	d_t0_t00 = S.Task('d_t0_t00', length=2, delay_cost=1)
	S += d_t0_t00 >= 102
	d_t0_t00 += MAS[3]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 103
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 103
	c_t5_t1_t3_mem0 += MAS_MEM[2]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 103
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 103
	c_t5_t31 += MAS[3]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 104
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 104
	c_t5_t1_t1_mem0 += MAS_MEM[0]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 104
	c_t5_t1_t1_mem1 += MAS_MEM[1]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=2, delay_cost=1)
	S += c_t5_t1_t3 >= 104
	c_t5_t1_t3 += MAS[2]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=6, delay_cost=1)
	S += c_t5_t1_t1 >= 105
	c_t5_t1_t1 += MM[0]


	# new tasks
	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=6, delay_cost=1)
	d_t0_t2_t0 += alt(MM)
	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	d_t0_t2_t0_in += alt(MM_in)
	S += d_t0_t2_t0_in*MM_in[0]<=d_t0_t2_t0*MM[0]
	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	d_t0_t2_t0_mem0 += MAS_MEM[6]
	S += 103 < d_t0_t2_t0_mem0
	S += d_t0_t2_t0_mem0 <= d_t0_t2_t0

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	d_t0_t2_t0_mem1 += MAS_MEM[3]
	S += 25 < d_t0_t2_t0_mem1
	S += d_t0_t2_t0_mem1 <= d_t0_t2_t0

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=6, delay_cost=1)
	d_t0_t2_t1 += alt(MM)
	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	d_t0_t2_t1_in += alt(MM_in)
	S += d_t0_t2_t1_in*MM_in[0]<=d_t0_t2_t1*MM[0]
	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	d_t0_t2_t1_mem0 += MAS_MEM[4]
	S += 100 < d_t0_t2_t1_mem0
	S += d_t0_t2_t1_mem0 <= d_t0_t2_t1

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	d_t0_t2_t1_mem1 += MAS_MEM[3]
	S += 5 < d_t0_t2_t1_mem1
	S += d_t0_t2_t1_mem1 <= d_t0_t2_t1

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=2, delay_cost=1)
	d_t0_t2_t2 += alt(MAS)
	d_t0_t2_t2_in = S.Task('d_t0_t2_t2_in', length=1, delay_cost=1)
	d_t0_t2_t2_in += alt(MAS_in)
	S += d_t0_t2_t2_in*MAS_in[0]<=d_t0_t2_t2*MAS[0]

	S += d_t0_t2_t2_in*MAS_in[1]<=d_t0_t2_t2*MAS[1]

	S += d_t0_t2_t2_in*MAS_in[2]<=d_t0_t2_t2*MAS[2]

	S += d_t0_t2_t2_in*MAS_in[3]<=d_t0_t2_t2*MAS[3]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	d_t0_t2_t2_mem0 += MAS_MEM[6]
	S += 103 < d_t0_t2_t2_mem0
	S += d_t0_t2_t2_mem0 <= d_t0_t2_t2

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	d_t0_t2_t2_mem1 += MAS_MEM[5]
	S += 100 < d_t0_t2_t2_mem1
	S += d_t0_t2_t2_mem1 <= d_t0_t2_t2

	d_t0_t31 = S.Task('d_t0_t31', length=2, delay_cost=1)
	d_t0_t31 += alt(MAS)
	d_t0_t31_in = S.Task('d_t0_t31_in', length=1, delay_cost=1)
	d_t0_t31_in += alt(MAS_in)
	S += d_t0_t31_in*MAS_in[0]<=d_t0_t31*MAS[0]

	S += d_t0_t31_in*MAS_in[1]<=d_t0_t31*MAS[1]

	S += d_t0_t31_in*MAS_in[2]<=d_t0_t31*MAS[2]

	S += d_t0_t31_in*MAS_in[3]<=d_t0_t31*MAS[3]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	d_t0_t31_mem0 += MM_MEM[0]
	S += 29 < d_t0_t31_mem0
	S += d_t0_t31_mem0 <= d_t0_t31

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	d_t0_t31_mem1 += MAS_MEM[5]
	S += 37 < d_t0_t31_mem1
	S += d_t0_t31_mem1 <= d_t0_t31

	d_t010 = S.Task('d_t010', length=2, delay_cost=1)
	d_t010 += alt(MAS)
	d_t010_in = S.Task('d_t010_in', length=1, delay_cost=1)
	d_t010_in += alt(MAS_in)
	S += d_t010_in*MAS_in[0]<=d_t010*MAS[0]

	S += d_t010_in*MAS_in[1]<=d_t010*MAS[1]

	S += d_t010_in*MAS_in[2]<=d_t010*MAS[2]

	S += d_t010_in*MAS_in[3]<=d_t010*MAS[3]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	d_t010_mem0 += MAS_MEM[0]
	S += 38 < d_t010_mem0
	S += d_t010_mem0 <= d_t010

	d_t010_mem1 = S.Task('d_t010_mem1', length=1, delay_cost=1)
	d_t010_mem1 += MAS_MEM[1]
	S += 38 < d_t010_mem1
	S += d_t010_mem1 <= d_t010

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=6, delay_cost=1)
	d_t1_t2_t0 += alt(MM)
	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	d_t1_t2_t0_in += alt(MM_in)
	S += d_t1_t2_t0_in*MM_in[0]<=d_t1_t2_t0*MM[0]
	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	d_t1_t2_t0_mem0 += MAS_MEM[4]
	S += 102 < d_t1_t2_t0_mem0
	S += d_t1_t2_t0_mem0 <= d_t1_t2_t0

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	d_t1_t2_t0_mem1 += MAS_MEM[7]
	S += 22 < d_t1_t2_t0_mem1
	S += d_t1_t2_t0_mem1 <= d_t1_t2_t0

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=6, delay_cost=1)
	d_t1_t2_t1 += alt(MM)
	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	d_t1_t2_t1_in += alt(MM_in)
	S += d_t1_t2_t1_in*MM_in[0]<=d_t1_t2_t1*MM[0]
	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	d_t1_t2_t1_mem0 += MAS_MEM[6]
	S += 101 < d_t1_t2_t1_mem0
	S += d_t1_t2_t1_mem0 <= d_t1_t2_t1

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	d_t1_t2_t1_mem1 += MAS_MEM[5]
	S += 27 < d_t1_t2_t1_mem1
	S += d_t1_t2_t1_mem1 <= d_t1_t2_t1

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=2, delay_cost=1)
	d_t1_t2_t2 += alt(MAS)
	d_t1_t2_t2_in = S.Task('d_t1_t2_t2_in', length=1, delay_cost=1)
	d_t1_t2_t2_in += alt(MAS_in)
	S += d_t1_t2_t2_in*MAS_in[0]<=d_t1_t2_t2*MAS[0]

	S += d_t1_t2_t2_in*MAS_in[1]<=d_t1_t2_t2*MAS[1]

	S += d_t1_t2_t2_in*MAS_in[2]<=d_t1_t2_t2*MAS[2]

	S += d_t1_t2_t2_in*MAS_in[3]<=d_t1_t2_t2*MAS[3]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	d_t1_t2_t2_mem0 += MAS_MEM[4]
	S += 102 < d_t1_t2_t2_mem0
	S += d_t1_t2_t2_mem0 <= d_t1_t2_t2

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	d_t1_t2_t2_mem1 += MAS_MEM[7]
	S += 101 < d_t1_t2_t2_mem1
	S += d_t1_t2_t2_mem1 <= d_t1_t2_t2

	d_t1_t31 = S.Task('d_t1_t31', length=2, delay_cost=1)
	d_t1_t31 += alt(MAS)
	d_t1_t31_in = S.Task('d_t1_t31_in', length=1, delay_cost=1)
	d_t1_t31_in += alt(MAS_in)
	S += d_t1_t31_in*MAS_in[0]<=d_t1_t31*MAS[0]

	S += d_t1_t31_in*MAS_in[1]<=d_t1_t31*MAS[1]

	S += d_t1_t31_in*MAS_in[2]<=d_t1_t31*MAS[2]

	S += d_t1_t31_in*MAS_in[3]<=d_t1_t31*MAS[3]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	d_t1_t31_mem0 += MM_MEM[0]
	S += 22 < d_t1_t31_mem0
	S += d_t1_t31_mem0 <= d_t1_t31

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	d_t1_t31_mem1 += MAS_MEM[1]
	S += 32 < d_t1_t31_mem1
	S += d_t1_t31_mem1 <= d_t1_t31

	d_t110 = S.Task('d_t110', length=2, delay_cost=1)
	d_t110 += alt(MAS)
	d_t110_in = S.Task('d_t110_in', length=1, delay_cost=1)
	d_t110_in += alt(MAS_in)
	S += d_t110_in*MAS_in[0]<=d_t110*MAS[0]

	S += d_t110_in*MAS_in[1]<=d_t110*MAS[1]

	S += d_t110_in*MAS_in[2]<=d_t110*MAS[2]

	S += d_t110_in*MAS_in[3]<=d_t110*MAS[3]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	d_t110_mem0 += MAS_MEM[4]
	S += 33 < d_t110_mem0
	S += d_t110_mem0 <= d_t110

	d_t110_mem1 = S.Task('d_t110_mem1', length=1, delay_cost=1)
	d_t110_mem1 += MAS_MEM[5]
	S += 33 < d_t110_mem1
	S += d_t110_mem1 <= d_t110

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=6, delay_cost=1)
	d_t2_t2_t0 += alt(MM)
	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	d_t2_t2_t0_in += alt(MM_in)
	S += d_t2_t2_t0_in*MM_in[0]<=d_t2_t2_t0*MM[0]
	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	d_t2_t2_t0_mem0 += MAS_MEM[6]
	S += 98 < d_t2_t2_t0_mem0
	S += d_t2_t2_t0_mem0 <= d_t2_t2_t0

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	d_t2_t2_t0_mem1 += MAS_MEM[7]
	S += 3 < d_t2_t2_t0_mem1
	S += d_t2_t2_t0_mem1 <= d_t2_t2_t0

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=6, delay_cost=1)
	d_t2_t2_t1 += alt(MM)
	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	d_t2_t2_t1_in += alt(MM_in)
	S += d_t2_t2_t1_in*MM_in[0]<=d_t2_t2_t1*MM[0]
	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	d_t2_t2_t1_mem0 += MAS_MEM[0]
	S += 99 < d_t2_t2_t1_mem0
	S += d_t2_t2_t1_mem0 <= d_t2_t2_t1

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	d_t2_t2_t1_mem1 += MAS_MEM[7]
	S += 28 < d_t2_t2_t1_mem1
	S += d_t2_t2_t1_mem1 <= d_t2_t2_t1

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=2, delay_cost=1)
	d_t2_t2_t2 += alt(MAS)
	d_t2_t2_t2_in = S.Task('d_t2_t2_t2_in', length=1, delay_cost=1)
	d_t2_t2_t2_in += alt(MAS_in)
	S += d_t2_t2_t2_in*MAS_in[0]<=d_t2_t2_t2*MAS[0]

	S += d_t2_t2_t2_in*MAS_in[1]<=d_t2_t2_t2*MAS[1]

	S += d_t2_t2_t2_in*MAS_in[2]<=d_t2_t2_t2*MAS[2]

	S += d_t2_t2_t2_in*MAS_in[3]<=d_t2_t2_t2*MAS[3]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	d_t2_t2_t2_mem0 += MAS_MEM[6]
	S += 98 < d_t2_t2_t2_mem0
	S += d_t2_t2_t2_mem0 <= d_t2_t2_t2

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	d_t2_t2_t2_mem1 += MAS_MEM[1]
	S += 99 < d_t2_t2_t2_mem1
	S += d_t2_t2_t2_mem1 <= d_t2_t2_t2

	d_t2_t31 = S.Task('d_t2_t31', length=2, delay_cost=1)
	d_t2_t31 += alt(MAS)
	d_t2_t31_in = S.Task('d_t2_t31_in', length=1, delay_cost=1)
	d_t2_t31_in += alt(MAS_in)
	S += d_t2_t31_in*MAS_in[0]<=d_t2_t31*MAS[0]

	S += d_t2_t31_in*MAS_in[1]<=d_t2_t31*MAS[1]

	S += d_t2_t31_in*MAS_in[2]<=d_t2_t31*MAS[2]

	S += d_t2_t31_in*MAS_in[3]<=d_t2_t31*MAS[3]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	d_t2_t31_mem0 += MM_MEM[0]
	S += 12 < d_t2_t31_mem0
	S += d_t2_t31_mem0 <= d_t2_t31

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	d_t2_t31_mem1 += MAS_MEM[3]
	S += 27 < d_t2_t31_mem1
	S += d_t2_t31_mem1 <= d_t2_t31

	d_t210 = S.Task('d_t210', length=2, delay_cost=1)
	d_t210 += alt(MAS)
	d_t210_in = S.Task('d_t210_in', length=1, delay_cost=1)
	d_t210_in += alt(MAS_in)
	S += d_t210_in*MAS_in[0]<=d_t210*MAS[0]

	S += d_t210_in*MAS_in[1]<=d_t210*MAS[1]

	S += d_t210_in*MAS_in[2]<=d_t210*MAS[2]

	S += d_t210_in*MAS_in[3]<=d_t210*MAS[3]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	d_t210_mem0 += MAS_MEM[2]
	S += 26 < d_t210_mem0
	S += d_t210_mem0 <= d_t210

	d_t210_mem1 = S.Task('d_t210_mem1', length=1, delay_cost=1)
	d_t210_mem1 += MAS_MEM[3]
	S += 26 < d_t210_mem1
	S += d_t210_mem1 <= d_t210

	d_t3_t00 = S.Task('d_t3_t00', length=2, delay_cost=1)
	d_t3_t00 += alt(MAS)
	d_t3_t00_in = S.Task('d_t3_t00_in', length=1, delay_cost=1)
	d_t3_t00_in += alt(MAS_in)
	S += d_t3_t00_in*MAS_in[0]<=d_t3_t00*MAS[0]

	S += d_t3_t00_in*MAS_in[1]<=d_t3_t00*MAS[1]

	S += d_t3_t00_in*MAS_in[2]<=d_t3_t00*MAS[2]

	S += d_t3_t00_in*MAS_in[3]<=d_t3_t00*MAS[3]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	d_t3_t00_mem0 += MAS_MEM[4]
	S += 9 < d_t3_t00_mem0
	S += d_t3_t00_mem0 <= d_t3_t00

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	d_t3_t00_mem1 += MAS_MEM[5]
	S += 22 < d_t3_t00_mem1
	S += d_t3_t00_mem1 <= d_t3_t00

	d_t3_t01 = S.Task('d_t3_t01', length=2, delay_cost=1)
	d_t3_t01 += alt(MAS)
	d_t3_t01_in = S.Task('d_t3_t01_in', length=1, delay_cost=1)
	d_t3_t01_in += alt(MAS_in)
	S += d_t3_t01_in*MAS_in[0]<=d_t3_t01*MAS[0]

	S += d_t3_t01_in*MAS_in[1]<=d_t3_t01*MAS[1]

	S += d_t3_t01_in*MAS_in[2]<=d_t3_t01*MAS[2]

	S += d_t3_t01_in*MAS_in[3]<=d_t3_t01*MAS[3]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	d_t3_t01_mem0 += MAS_MEM[6]
	S += 29 < d_t3_t01_mem0
	S += d_t3_t01_mem0 <= d_t3_t01

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	d_t3_t01_mem1 += MAS_MEM[1]
	S += 22 < d_t3_t01_mem1
	S += d_t3_t01_mem1 <= d_t3_t01

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=2, delay_cost=1)
	d_t3_t2_t3 += alt(MAS)
	d_t3_t2_t3_in = S.Task('d_t3_t2_t3_in', length=1, delay_cost=1)
	d_t3_t2_t3_in += alt(MAS_in)
	S += d_t3_t2_t3_in*MAS_in[0]<=d_t3_t2_t3*MAS[0]

	S += d_t3_t2_t3_in*MAS_in[1]<=d_t3_t2_t3*MAS[1]

	S += d_t3_t2_t3_in*MAS_in[2]<=d_t3_t2_t3*MAS[2]

	S += d_t3_t2_t3_in*MAS_in[3]<=d_t3_t2_t3*MAS[3]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	d_t3_t2_t3_mem0 += MAS_MEM[6]
	S += 21 < d_t3_t2_t3_mem0
	S += d_t3_t2_t3_mem0 <= d_t3_t2_t3

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	d_t3_t2_t3_mem1 += MAS_MEM[7]
	S += 31 < d_t3_t2_t3_mem1
	S += d_t3_t2_t3_mem1 <= d_t3_t2_t3

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=6, delay_cost=1)
	d_t3_t3_t4 += alt(MM)
	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	d_t3_t3_t4_in += alt(MM_in)
	S += d_t3_t3_t4_in*MM_in[0]<=d_t3_t3_t4*MM[0]
	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	d_t3_t3_t4_mem0 += MAS_MEM[4]
	S += 31 < d_t3_t3_t4_mem0
	S += d_t3_t3_t4_mem0 <= d_t3_t3_t4

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	d_t3_t3_t4_mem1 += MAS_MEM[3]
	S += 21 < d_t3_t3_t4_mem1
	S += d_t3_t3_t4_mem1 <= d_t3_t3_t4

	d_t3_t30 = S.Task('d_t3_t30', length=2, delay_cost=1)
	d_t3_t30 += alt(MAS)
	d_t3_t30_in = S.Task('d_t3_t30_in', length=1, delay_cost=1)
	d_t3_t30_in += alt(MAS_in)
	S += d_t3_t30_in*MAS_in[0]<=d_t3_t30*MAS[0]

	S += d_t3_t30_in*MAS_in[1]<=d_t3_t30*MAS[1]

	S += d_t3_t30_in*MAS_in[2]<=d_t3_t30*MAS[2]

	S += d_t3_t30_in*MAS_in[3]<=d_t3_t30*MAS[3]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	d_t3_t30_mem0 += MM_MEM[0]
	S += 27 < d_t3_t30_mem0
	S += d_t3_t30_mem0 <= d_t3_t30

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	d_t3_t30_mem1 += MM_MEM[1]
	S += 36 < d_t3_t30_mem1
	S += d_t3_t30_mem1 <= d_t3_t30

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=2, delay_cost=1)
	d_t3_t3_t5 += alt(MAS)
	d_t3_t3_t5_in = S.Task('d_t3_t3_t5_in', length=1, delay_cost=1)
	d_t3_t3_t5_in += alt(MAS_in)
	S += d_t3_t3_t5_in*MAS_in[0]<=d_t3_t3_t5*MAS[0]

	S += d_t3_t3_t5_in*MAS_in[1]<=d_t3_t3_t5*MAS[1]

	S += d_t3_t3_t5_in*MAS_in[2]<=d_t3_t3_t5*MAS[2]

	S += d_t3_t3_t5_in*MAS_in[3]<=d_t3_t3_t5*MAS[3]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	d_t3_t3_t5_mem0 += MM_MEM[0]
	S += 27 < d_t3_t3_t5_mem0
	S += d_t3_t3_t5_mem0 <= d_t3_t3_t5

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	d_t3_t3_t5_mem1 += MM_MEM[1]
	S += 36 < d_t3_t3_t5_mem1
	S += d_t3_t3_t5_mem1 <= d_t3_t3_t5

	d_t4_t00 = S.Task('d_t4_t00', length=2, delay_cost=1)
	d_t4_t00 += alt(MAS)
	d_t4_t00_in = S.Task('d_t4_t00_in', length=1, delay_cost=1)
	d_t4_t00_in += alt(MAS_in)
	S += d_t4_t00_in*MAS_in[0]<=d_t4_t00*MAS[0]

	S += d_t4_t00_in*MAS_in[1]<=d_t4_t00*MAS[1]

	S += d_t4_t00_in*MAS_in[2]<=d_t4_t00*MAS[2]

	S += d_t4_t00_in*MAS_in[3]<=d_t4_t00*MAS[3]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	d_t4_t00_mem0 += MAS_MEM[6]
	S += 24 < d_t4_t00_mem0
	S += d_t4_t00_mem0 <= d_t4_t00

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	d_t4_t00_mem1 += MAS_MEM[7]
	S += 48 < d_t4_t00_mem1
	S += d_t4_t00_mem1 <= d_t4_t00

	d_t4_t01 = S.Task('d_t4_t01', length=2, delay_cost=1)
	d_t4_t01 += alt(MAS)
	d_t4_t01_in = S.Task('d_t4_t01_in', length=1, delay_cost=1)
	d_t4_t01_in += alt(MAS_in)
	S += d_t4_t01_in*MAS_in[0]<=d_t4_t01*MAS[0]

	S += d_t4_t01_in*MAS_in[1]<=d_t4_t01*MAS[1]

	S += d_t4_t01_in*MAS_in[2]<=d_t4_t01*MAS[2]

	S += d_t4_t01_in*MAS_in[3]<=d_t4_t01*MAS[3]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	d_t4_t01_mem0 += MAS_MEM[0]
	S += 18 < d_t4_t01_mem0
	S += d_t4_t01_mem0 <= d_t4_t01

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	d_t4_t01_mem1 += MAS_MEM[5]
	S += 48 < d_t4_t01_mem1
	S += d_t4_t01_mem1 <= d_t4_t01

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=2, delay_cost=1)
	d_t4_t2_t3 += alt(MAS)
	d_t4_t2_t3_in = S.Task('d_t4_t2_t3_in', length=1, delay_cost=1)
	d_t4_t2_t3_in += alt(MAS_in)
	S += d_t4_t2_t3_in*MAS_in[0]<=d_t4_t2_t3*MAS[0]

	S += d_t4_t2_t3_in*MAS_in[1]<=d_t4_t2_t3*MAS[1]

	S += d_t4_t2_t3_in*MAS_in[2]<=d_t4_t2_t3*MAS[2]

	S += d_t4_t2_t3_in*MAS_in[3]<=d_t4_t2_t3*MAS[3]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	d_t4_t2_t3_mem0 += MAS_MEM[2]
	S += 49 < d_t4_t2_t3_mem0
	S += d_t4_t2_t3_mem0 <= d_t4_t2_t3

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	d_t4_t2_t3_mem1 += MAS_MEM[5]
	S += 42 < d_t4_t2_t3_mem1
	S += d_t4_t2_t3_mem1 <= d_t4_t2_t3

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=6, delay_cost=1)
	d_t4_t3_t4 += alt(MM)
	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	d_t4_t3_t4_in += alt(MM_in)
	S += d_t4_t3_t4_in*MM_in[0]<=d_t4_t3_t4*MM[0]
	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	d_t4_t3_t4_mem0 += MAS_MEM[4]
	S += 26 < d_t4_t3_t4_mem0
	S += d_t4_t3_t4_mem0 <= d_t4_t3_t4

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	d_t4_t3_t4_mem1 += MAS_MEM[1]
	S += 50 < d_t4_t3_t4_mem1
	S += d_t4_t3_t4_mem1 <= d_t4_t3_t4

	d_t4_t30 = S.Task('d_t4_t30', length=2, delay_cost=1)
	d_t4_t30 += alt(MAS)
	d_t4_t30_in = S.Task('d_t4_t30_in', length=1, delay_cost=1)
	d_t4_t30_in += alt(MAS_in)
	S += d_t4_t30_in*MAS_in[0]<=d_t4_t30*MAS[0]

	S += d_t4_t30_in*MAS_in[1]<=d_t4_t30*MAS[1]

	S += d_t4_t30_in*MAS_in[2]<=d_t4_t30*MAS[2]

	S += d_t4_t30_in*MAS_in[3]<=d_t4_t30*MAS[3]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	d_t4_t30_mem0 += MM_MEM[0]
	S += 55 < d_t4_t30_mem0
	S += d_t4_t30_mem0 <= d_t4_t30

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	d_t4_t30_mem1 += MM_MEM[1]
	S += 45 < d_t4_t30_mem1
	S += d_t4_t30_mem1 <= d_t4_t30

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=2, delay_cost=1)
	d_t4_t3_t5 += alt(MAS)
	d_t4_t3_t5_in = S.Task('d_t4_t3_t5_in', length=1, delay_cost=1)
	d_t4_t3_t5_in += alt(MAS_in)
	S += d_t4_t3_t5_in*MAS_in[0]<=d_t4_t3_t5*MAS[0]

	S += d_t4_t3_t5_in*MAS_in[1]<=d_t4_t3_t5*MAS[1]

	S += d_t4_t3_t5_in*MAS_in[2]<=d_t4_t3_t5*MAS[2]

	S += d_t4_t3_t5_in*MAS_in[3]<=d_t4_t3_t5*MAS[3]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	d_t4_t3_t5_mem0 += MM_MEM[0]
	S += 55 < d_t4_t3_t5_mem0
	S += d_t4_t3_t5_mem0 <= d_t4_t3_t5

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	d_t4_t3_t5_mem1 += MM_MEM[1]
	S += 45 < d_t4_t3_t5_mem1
	S += d_t4_t3_t5_mem1 <= d_t4_t3_t5

	d_t5_t00 = S.Task('d_t5_t00', length=2, delay_cost=1)
	d_t5_t00 += alt(MAS)
	d_t5_t00_in = S.Task('d_t5_t00_in', length=1, delay_cost=1)
	d_t5_t00_in += alt(MAS_in)
	S += d_t5_t00_in*MAS_in[0]<=d_t5_t00*MAS[0]

	S += d_t5_t00_in*MAS_in[1]<=d_t5_t00*MAS[1]

	S += d_t5_t00_in*MAS_in[2]<=d_t5_t00*MAS[2]

	S += d_t5_t00_in*MAS_in[3]<=d_t5_t00*MAS[3]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	d_t5_t00_mem0 += MAS_MEM[4]
	S += 53 < d_t5_t00_mem0
	S += d_t5_t00_mem0 <= d_t5_t00

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	d_t5_t00_mem1 += MAS_MEM[1]
	S += 56 < d_t5_t00_mem1
	S += d_t5_t00_mem1 <= d_t5_t00

	d_t5_t01 = S.Task('d_t5_t01', length=2, delay_cost=1)
	d_t5_t01 += alt(MAS)
	d_t5_t01_in = S.Task('d_t5_t01_in', length=1, delay_cost=1)
	d_t5_t01_in += alt(MAS_in)
	S += d_t5_t01_in*MAS_in[0]<=d_t5_t01*MAS[0]

	S += d_t5_t01_in*MAS_in[1]<=d_t5_t01*MAS[1]

	S += d_t5_t01_in*MAS_in[2]<=d_t5_t01*MAS[2]

	S += d_t5_t01_in*MAS_in[3]<=d_t5_t01*MAS[3]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	d_t5_t01_mem0 += MAS_MEM[4]
	S += 51 < d_t5_t01_mem0
	S += d_t5_t01_mem0 <= d_t5_t01

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	d_t5_t01_mem1 += MAS_MEM[5]
	S += 54 < d_t5_t01_mem1
	S += d_t5_t01_mem1 <= d_t5_t01

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=2, delay_cost=1)
	d_t5_t2_t3 += alt(MAS)
	d_t5_t2_t3_in = S.Task('d_t5_t2_t3_in', length=1, delay_cost=1)
	d_t5_t2_t3_in += alt(MAS_in)
	S += d_t5_t2_t3_in*MAS_in[0]<=d_t5_t2_t3*MAS[0]

	S += d_t5_t2_t3_in*MAS_in[1]<=d_t5_t2_t3*MAS[1]

	S += d_t5_t2_t3_in*MAS_in[2]<=d_t5_t2_t3*MAS[2]

	S += d_t5_t2_t3_in*MAS_in[3]<=d_t5_t2_t3*MAS[3]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	d_t5_t2_t3_mem0 += MAS_MEM[4]
	S += 56 < d_t5_t2_t3_mem0
	S += d_t5_t2_t3_mem0 <= d_t5_t2_t3

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	d_t5_t2_t3_mem1 += MAS_MEM[1]
	S += 57 < d_t5_t2_t3_mem1
	S += d_t5_t2_t3_mem1 <= d_t5_t2_t3

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=6, delay_cost=1)
	d_t5_t3_t4 += alt(MM)
	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	d_t5_t3_t4_in += alt(MM_in)
	S += d_t5_t3_t4_in*MM_in[0]<=d_t5_t3_t4*MM[0]
	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	d_t5_t3_t4_mem0 += MAS_MEM[6]
	S += 58 < d_t5_t3_t4_mem0
	S += d_t5_t3_t4_mem0 <= d_t5_t3_t4

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	d_t5_t3_t4_mem1 += MAS_MEM[5]
	S += 55 < d_t5_t3_t4_mem1
	S += d_t5_t3_t4_mem1 <= d_t5_t3_t4

	d_t5_t30 = S.Task('d_t5_t30', length=2, delay_cost=1)
	d_t5_t30 += alt(MAS)
	d_t5_t30_in = S.Task('d_t5_t30_in', length=1, delay_cost=1)
	d_t5_t30_in += alt(MAS_in)
	S += d_t5_t30_in*MAS_in[0]<=d_t5_t30*MAS[0]

	S += d_t5_t30_in*MAS_in[1]<=d_t5_t30*MAS[1]

	S += d_t5_t30_in*MAS_in[2]<=d_t5_t30*MAS[2]

	S += d_t5_t30_in*MAS_in[3]<=d_t5_t30*MAS[3]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	d_t5_t30_mem0 += MM_MEM[0]
	S += 59 < d_t5_t30_mem0
	S += d_t5_t30_mem0 <= d_t5_t30

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	d_t5_t30_mem1 += MM_MEM[1]
	S += 58 < d_t5_t30_mem1
	S += d_t5_t30_mem1 <= d_t5_t30

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=2, delay_cost=1)
	d_t5_t3_t5 += alt(MAS)
	d_t5_t3_t5_in = S.Task('d_t5_t3_t5_in', length=1, delay_cost=1)
	d_t5_t3_t5_in += alt(MAS_in)
	S += d_t5_t3_t5_in*MAS_in[0]<=d_t5_t3_t5*MAS[0]

	S += d_t5_t3_t5_in*MAS_in[1]<=d_t5_t3_t5*MAS[1]

	S += d_t5_t3_t5_in*MAS_in[2]<=d_t5_t3_t5*MAS[2]

	S += d_t5_t3_t5_in*MAS_in[3]<=d_t5_t3_t5*MAS[3]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	d_t5_t3_t5_mem0 += MM_MEM[0]
	S += 59 < d_t5_t3_t5_mem0
	S += d_t5_t3_t5_mem0 <= d_t5_t3_t5

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	d_t5_t3_t5_mem1 += MM_MEM[1]
	S += 58 < d_t5_t3_t5_mem1
	S += d_t5_t3_t5_mem1 <= d_t5_t3_t5

	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	c_t0_t01 += alt(MAS)
	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	c_t0_t01_in += alt(MAS_in)
	S += c_t0_t01_in*MAS_in[0]<=c_t0_t01*MAS[0]

	S += c_t0_t01_in*MAS_in[1]<=c_t0_t01*MAS[1]

	S += c_t0_t01_in*MAS_in[2]<=c_t0_t01*MAS[2]

	S += c_t0_t01_in*MAS_in[3]<=c_t0_t01*MAS[3]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	c_t0_t01_mem0 += MM_MEM[0]
	S += 53 < c_t0_t01_mem0
	S += c_t0_t01_mem0 <= c_t0_t01

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	c_t0_t01_mem1 += MAS_MEM[5]
	S += 67 < c_t0_t01_mem1
	S += c_t0_t01_mem1 <= c_t0_t01

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	c_t0_t11_in += alt(MAS_in)
	S += c_t0_t11_in*MAS_in[0]<=c_t0_t11*MAS[0]

	S += c_t0_t11_in*MAS_in[1]<=c_t0_t11*MAS[1]

	S += c_t0_t11_in*MAS_in[2]<=c_t0_t11*MAS[2]

	S += c_t0_t11_in*MAS_in[3]<=c_t0_t11*MAS[3]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MM_MEM[0]
	S += 56 < c_t0_t11_mem0
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAS_MEM[5]
	S += 66 < c_t0_t11_mem1
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=6, delay_cost=1)
	c_t0_t4_t4 += alt(MM)
	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	c_t0_t4_t4_in += alt(MM_in)
	S += c_t0_t4_t4_in*MM_in[0]<=c_t0_t4_t4*MM[0]
	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	c_t0_t4_t4_mem0 += MAS_MEM[6]
	S += 47 < c_t0_t4_t4_mem0
	S += c_t0_t4_t4_mem0 <= c_t0_t4_t4

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	c_t0_t4_t4_mem1 += MAS_MEM[3]
	S += 45 < c_t0_t4_t4_mem1
	S += c_t0_t4_t4_mem1 <= c_t0_t4_t4

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	c_t0_t40 += alt(MAS)
	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	c_t0_t40_in += alt(MAS_in)
	S += c_t0_t40_in*MAS_in[0]<=c_t0_t40*MAS[0]

	S += c_t0_t40_in*MAS_in[1]<=c_t0_t40*MAS[1]

	S += c_t0_t40_in*MAS_in[2]<=c_t0_t40*MAS[2]

	S += c_t0_t40_in*MAS_in[3]<=c_t0_t40*MAS[3]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	c_t0_t40_mem0 += MM_MEM[0]
	S += 47 < c_t0_t40_mem0
	S += c_t0_t40_mem0 <= c_t0_t40

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	c_t0_t40_mem1 += MM_MEM[1]
	S += 50 < c_t0_t40_mem1
	S += c_t0_t40_mem1 <= c_t0_t40

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=2, delay_cost=1)
	c_t0_t4_t5 += alt(MAS)
	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	c_t0_t4_t5_in += alt(MAS_in)
	S += c_t0_t4_t5_in*MAS_in[0]<=c_t0_t4_t5*MAS[0]

	S += c_t0_t4_t5_in*MAS_in[1]<=c_t0_t4_t5*MAS[1]

	S += c_t0_t4_t5_in*MAS_in[2]<=c_t0_t4_t5*MAS[2]

	S += c_t0_t4_t5_in*MAS_in[3]<=c_t0_t4_t5*MAS[3]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	c_t0_t4_t5_mem0 += MM_MEM[0]
	S += 47 < c_t0_t4_t5_mem0
	S += c_t0_t4_t5_mem0 <= c_t0_t4_t5

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	c_t0_t4_t5_mem1 += MM_MEM[1]
	S += 50 < c_t0_t4_t5_mem1
	S += c_t0_t4_t5_mem1 <= c_t0_t4_t5

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	c_t0_t50 += alt(MAS)
	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	c_t0_t50_in += alt(MAS_in)
	S += c_t0_t50_in*MAS_in[0]<=c_t0_t50*MAS[0]

	S += c_t0_t50_in*MAS_in[1]<=c_t0_t50*MAS[1]

	S += c_t0_t50_in*MAS_in[2]<=c_t0_t50*MAS[2]

	S += c_t0_t50_in*MAS_in[3]<=c_t0_t50*MAS[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	c_t0_t50_mem0 += MAS_MEM[2]
	S += 68 < c_t0_t50_mem0
	S += c_t0_t50_mem0 <= c_t0_t50

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	c_t0_t50_mem1 += MAS_MEM[5]
	S += 65 < c_t0_t50_mem1
	S += c_t0_t50_mem1 <= c_t0_t50

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	c_t1_t01 += alt(MAS)
	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	c_t1_t01_in += alt(MAS_in)
	S += c_t1_t01_in*MAS_in[0]<=c_t1_t01*MAS[0]

	S += c_t1_t01_in*MAS_in[1]<=c_t1_t01*MAS[1]

	S += c_t1_t01_in*MAS_in[2]<=c_t1_t01*MAS[2]

	S += c_t1_t01_in*MAS_in[3]<=c_t1_t01*MAS[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	c_t1_t01_mem0 += MM_MEM[0]
	S += 41 < c_t1_t01_mem0
	S += c_t1_t01_mem0 <= c_t1_t01

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	c_t1_t01_mem1 += MAS_MEM[5]
	S += 63 < c_t1_t01_mem1
	S += c_t1_t01_mem1 <= c_t1_t01

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	c_t1_t11_in += alt(MAS_in)
	S += c_t1_t11_in*MAS_in[0]<=c_t1_t11*MAS[0]

	S += c_t1_t11_in*MAS_in[1]<=c_t1_t11*MAS[1]

	S += c_t1_t11_in*MAS_in[2]<=c_t1_t11*MAS[2]

	S += c_t1_t11_in*MAS_in[3]<=c_t1_t11*MAS[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MM_MEM[0]
	S += 66 < c_t1_t11_mem0
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAS_MEM[3]
	S += 56 < c_t1_t11_mem1
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=6, delay_cost=1)
	c_t1_t4_t4 += alt(MM)
	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	c_t1_t4_t4_in += alt(MM_in)
	S += c_t1_t4_t4_in*MM_in[0]<=c_t1_t4_t4*MM[0]
	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	c_t1_t4_t4_mem0 += MAS_MEM[6]
	S += 56 < c_t1_t4_t4_mem0
	S += c_t1_t4_t4_mem0 <= c_t1_t4_t4

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	c_t1_t4_t4_mem1 += MAS_MEM[3]
	S += 44 < c_t1_t4_t4_mem1
	S += c_t1_t4_t4_mem1 <= c_t1_t4_t4

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	c_t1_t40 += alt(MAS)
	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	c_t1_t40_in += alt(MAS_in)
	S += c_t1_t40_in*MAS_in[0]<=c_t1_t40*MAS[0]

	S += c_t1_t40_in*MAS_in[1]<=c_t1_t40*MAS[1]

	S += c_t1_t40_in*MAS_in[2]<=c_t1_t40*MAS[2]

	S += c_t1_t40_in*MAS_in[3]<=c_t1_t40*MAS[3]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	c_t1_t40_mem0 += MM_MEM[0]
	S += 68 < c_t1_t40_mem0
	S += c_t1_t40_mem0 <= c_t1_t40

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	c_t1_t40_mem1 += MM_MEM[1]
	S += 40 < c_t1_t40_mem1
	S += c_t1_t40_mem1 <= c_t1_t40

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=2, delay_cost=1)
	c_t1_t4_t5 += alt(MAS)
	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	c_t1_t4_t5_in += alt(MAS_in)
	S += c_t1_t4_t5_in*MAS_in[0]<=c_t1_t4_t5*MAS[0]

	S += c_t1_t4_t5_in*MAS_in[1]<=c_t1_t4_t5*MAS[1]

	S += c_t1_t4_t5_in*MAS_in[2]<=c_t1_t4_t5*MAS[2]

	S += c_t1_t4_t5_in*MAS_in[3]<=c_t1_t4_t5*MAS[3]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	c_t1_t4_t5_mem0 += MM_MEM[0]
	S += 68 < c_t1_t4_t5_mem0
	S += c_t1_t4_t5_mem0 <= c_t1_t4_t5

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	c_t1_t4_t5_mem1 += MM_MEM[1]
	S += 40 < c_t1_t4_t5_mem1
	S += c_t1_t4_t5_mem1 <= c_t1_t4_t5

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	c_t1_t50 += alt(MAS)
	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	c_t1_t50_in += alt(MAS_in)
	S += c_t1_t50_in*MAS_in[0]<=c_t1_t50*MAS[0]

	S += c_t1_t50_in*MAS_in[1]<=c_t1_t50*MAS[1]

	S += c_t1_t50_in*MAS_in[2]<=c_t1_t50*MAS[2]

	S += c_t1_t50_in*MAS_in[3]<=c_t1_t50*MAS[3]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	c_t1_t50_mem0 += MAS_MEM[4]
	S += 64 < c_t1_t50_mem0
	S += c_t1_t50_mem0 <= c_t1_t50

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	c_t1_t50_mem1 += MAS_MEM[3]
	S += 57 < c_t1_t50_mem1
	S += c_t1_t50_mem1 <= c_t1_t50

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	c_t2_t01 += alt(MAS)
	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	c_t2_t01_in += alt(MAS_in)
	S += c_t2_t01_in*MAS_in[0]<=c_t2_t01*MAS[0]

	S += c_t2_t01_in*MAS_in[1]<=c_t2_t01*MAS[1]

	S += c_t2_t01_in*MAS_in[2]<=c_t2_t01*MAS[2]

	S += c_t2_t01_in*MAS_in[3]<=c_t2_t01*MAS[3]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	c_t2_t01_mem0 += MM_MEM[0]
	S += 97 < c_t2_t01_mem0
	S += c_t2_t01_mem0 <= c_t2_t01

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	c_t2_t01_mem1 += MAS_MEM[3]
	S += 72 < c_t2_t01_mem1
	S += c_t2_t01_mem1 <= c_t2_t01

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	c_t2_t11_in += alt(MAS_in)
	S += c_t2_t11_in*MAS_in[0]<=c_t2_t11*MAS[0]

	S += c_t2_t11_in*MAS_in[1]<=c_t2_t11*MAS[1]

	S += c_t2_t11_in*MAS_in[2]<=c_t2_t11*MAS[2]

	S += c_t2_t11_in*MAS_in[3]<=c_t2_t11*MAS[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MM_MEM[0]
	S += 96 < c_t2_t11_mem0
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAS_MEM[1]
	S += 96 < c_t2_t11_mem1
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=6, delay_cost=1)
	c_t2_t4_t4 += alt(MM)
	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	c_t2_t4_t4_in += alt(MM_in)
	S += c_t2_t4_t4_in*MM_in[0]<=c_t2_t4_t4*MM[0]
	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	c_t2_t4_t4_mem0 += MAS_MEM[0]
	S += 68 < c_t2_t4_t4_mem0
	S += c_t2_t4_t4_mem0 <= c_t2_t4_t4

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	c_t2_t4_t4_mem1 += MAS_MEM[5]
	S += 74 < c_t2_t4_t4_mem1
	S += c_t2_t4_t4_mem1 <= c_t2_t4_t4

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	c_t2_t40 += alt(MAS)
	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	c_t2_t40_in += alt(MAS_in)
	S += c_t2_t40_in*MAS_in[0]<=c_t2_t40*MAS[0]

	S += c_t2_t40_in*MAS_in[1]<=c_t2_t40*MAS[1]

	S += c_t2_t40_in*MAS_in[2]<=c_t2_t40*MAS[2]

	S += c_t2_t40_in*MAS_in[3]<=c_t2_t40*MAS[3]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	c_t2_t40_mem0 += MM_MEM[0]
	S += 75 < c_t2_t40_mem0
	S += c_t2_t40_mem0 <= c_t2_t40

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	c_t2_t40_mem1 += MM_MEM[1]
	S += 79 < c_t2_t40_mem1
	S += c_t2_t40_mem1 <= c_t2_t40

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=2, delay_cost=1)
	c_t2_t4_t5 += alt(MAS)
	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	c_t2_t4_t5_in += alt(MAS_in)
	S += c_t2_t4_t5_in*MAS_in[0]<=c_t2_t4_t5*MAS[0]

	S += c_t2_t4_t5_in*MAS_in[1]<=c_t2_t4_t5*MAS[1]

	S += c_t2_t4_t5_in*MAS_in[2]<=c_t2_t4_t5*MAS[2]

	S += c_t2_t4_t5_in*MAS_in[3]<=c_t2_t4_t5*MAS[3]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	c_t2_t4_t5_mem0 += MM_MEM[0]
	S += 75 < c_t2_t4_t5_mem0
	S += c_t2_t4_t5_mem0 <= c_t2_t4_t5

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	c_t2_t4_t5_mem1 += MM_MEM[1]
	S += 79 < c_t2_t4_t5_mem1
	S += c_t2_t4_t5_mem1 <= c_t2_t4_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS4/FP12_LADDERMUL/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

