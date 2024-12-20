from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 0
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 0
	c_ab_t1_t1_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 0
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 1
	c_aa_a1_0 += MAS[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 1
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=6, delay_cost=1)
	S += c_ab_t1_t1 >= 1
	c_ab_t1_t1 += MM[0]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 1
	c_bb_t10 += MAS[1]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 1
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 1
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 1
	c_cc_t11 += MAS[3]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 1
	c_cc_t3_t2 += MAS[2]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 2
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 2
	c_aa_t3_t0_in += MM_in[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=6, delay_cost=1)
	S += c_ab_t0_t0 >= 2
	c_ab_t0_t0 += MM[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 2
	c_ab_t0_t2 += MAS[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 2
	c_bb_a1_0 += MAS[2]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 2
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 2
	c_cc_a1_0 += MAS[3]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 2
	c_cc_a1_1 += MAS[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 3
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 3
	c_aa_t11 += MAS[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=6, delay_cost=1)
	S += c_aa_t3_t0 >= 3
	c_aa_t3_t0 += MM[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 3
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 3
	c_ab_t1_t0_in += MM_in[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 3
	c_bb_a1_1 += MAS[3]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 3
	c_bb_t3_t2 += MAS[2]

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 3
	c_cc_t10 += MAS[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 4
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 4
	c_aa_t3_t2 += MAS[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=6, delay_cost=1)
	S += c_ab_t1_t0 >= 4
	c_ab_t1_t0 += MM[0]

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 4
	c_bb_t11 += MAS[2]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 4
	c_bb_t3_t3 += MAS[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 4
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 4
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 4
	c_cc_t3_t3 += MAS[3]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 5
	c_aa_a1_1 += MAS[1]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 5
	c_aa_t10 += MAS[2]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=6, delay_cost=1)
	S += c_aa_t3_t1 >= 5
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 5
	c_aa_t3_t3 += MAS[0]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 5
	c_ab_t0_t3 += MAS[3]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 5
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 5
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 5
	c_cc_t3_t1_in += MM_in[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 6
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 6
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 6
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=6, delay_cost=1)
	S += c_cc_t3_t1 >= 6
	c_cc_t3_t1 += MM[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 7
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=6, delay_cost=1)
	S += c_bb_t3_t0 >= 7
	c_bb_t3_t0 += MM[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 7
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 7
	c_cc_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 8
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 8
	c_ab_t0_t1_in += MM_in[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 8
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=6, delay_cost=1)
	S += c_cc_t3_t0 >= 8
	c_cc_t3_t0 += MM[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=6, delay_cost=1)
	S += c_ab_t0_t1 >= 9
	c_ab_t0_t1 += MM[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 9
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 9
	c_bb_t3_t1_in += MM_in[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 9
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 10
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 10
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=6, delay_cost=1)
	S += c_bb_t3_t1 >= 10
	c_bb_t3_t1 += MM[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 11
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 11
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 12
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 12
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 13
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 13
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 14
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 14
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 15
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 15
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 16
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 16
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 17
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 17
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 18
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 18
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 19
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 19
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 20
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 20
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 21
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 21
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 22
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 22
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 23
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 23
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 24
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 24
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 25
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 25
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 26
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 26
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 27
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 27
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 28
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 28
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 29
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 29
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	c_ab_t1_t2 += alt(MAS)

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]
	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]
	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	c_ab_t1_t3 += alt(MAS)

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]
	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]
	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	c_ab_t20 += alt(MAS)

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	c_ab_t20_mem0 += MAIN_MEM_r[0]
	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	c_ab_t20_mem1 += MAIN_MEM_r[1]
	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	c_ab_t21 += alt(MAS)

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	c_ab_t21_mem0 += MAIN_MEM_r[0]
	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	c_ab_t21_mem1 += MAIN_MEM_r[1]
	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	c_ab_t30 += alt(MAS)

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	c_ab_t30_mem0 += MAIN_MEM_r[0]
	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	c_ab_t30_mem1 += MAIN_MEM_r[1]
	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	c_ab_t31 += alt(MAS)

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	c_ab_t31_mem0 += MAIN_MEM_r[0]
	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	c_ab_t31_mem1 += MAIN_MEM_r[1]
	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	c_bc_t0_t0_in += alt(MM_in)
	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=6, delay_cost=1)
	c_bc_t0_t0 += alt(MM)
	S += c_bc_t0_t0>=c_bc_t0_t0_in

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]
	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]
	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	c_bc_t0_t1_in += alt(MM_in)
	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=6, delay_cost=1)
	c_bc_t0_t1 += alt(MM)
	S += c_bc_t0_t1>=c_bc_t0_t1_in

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]
	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]
	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	c_bc_t0_t2 += alt(MAS)

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]
	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]
	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	c_bc_t0_t3 += alt(MAS)

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]
	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]
	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	c_bc_t1_t0_in += alt(MM_in)
	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=6, delay_cost=1)
	c_bc_t1_t0 += alt(MM)
	S += c_bc_t1_t0>=c_bc_t1_t0_in

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]
	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]
	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	c_bc_t1_t1_in += alt(MM_in)
	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=6, delay_cost=1)
	c_bc_t1_t1 += alt(MM)
	S += c_bc_t1_t1>=c_bc_t1_t1_in

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]
	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]
	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	c_bc_t1_t2 += alt(MAS)

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]
	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]
	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	c_bc_t1_t3 += alt(MAS)

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]
	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]
	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	c_bc_t20 += alt(MAS)

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	c_bc_t20_mem0 += MAIN_MEM_r[0]
	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	c_bc_t20_mem1 += MAIN_MEM_r[1]
	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	c_bc_t21 += alt(MAS)

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	c_bc_t21_mem0 += MAIN_MEM_r[0]
	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	c_bc_t21_mem1 += MAIN_MEM_r[1]
	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	c_bc_t30 += alt(MAS)

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	c_bc_t30_mem0 += MAIN_MEM_r[0]
	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	c_bc_t30_mem1 += MAIN_MEM_r[1]
	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	c_bc_t31 += alt(MAS)

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	c_bc_t31_mem0 += MAIN_MEM_r[0]
	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	c_bc_t31_mem1 += MAIN_MEM_r[1]
	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	c_ac_t0_t0_in += alt(MM_in)
	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=6, delay_cost=1)
	c_ac_t0_t0 += alt(MM)
	S += c_ac_t0_t0>=c_ac_t0_t0_in

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]
	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]
	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	c_ac_t0_t1_in += alt(MM_in)
	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=6, delay_cost=1)
	c_ac_t0_t1 += alt(MM)
	S += c_ac_t0_t1>=c_ac_t0_t1_in

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]
	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]
	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	c_ac_t0_t2 += alt(MAS)

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]
	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]
	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	c_ac_t0_t3 += alt(MAS)

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]
	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]
	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	c_ac_t1_t0_in += alt(MM_in)
	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=6, delay_cost=1)
	c_ac_t1_t0 += alt(MM)
	S += c_ac_t1_t0>=c_ac_t1_t0_in

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]
	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]
	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	c_ac_t1_t1_in += alt(MM_in)
	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=6, delay_cost=1)
	c_ac_t1_t1 += alt(MM)
	S += c_ac_t1_t1>=c_ac_t1_t1_in

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]
	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]
	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	c_ac_t1_t2 += alt(MAS)

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]
	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]
	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	c_ac_t1_t3 += alt(MAS)

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]
	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]
	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	c_ac_t20 += alt(MAS)

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	c_ac_t20_mem0 += MAIN_MEM_r[0]
	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	c_ac_t20_mem1 += MAIN_MEM_r[1]
	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	c_ac_t21 += alt(MAS)

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	c_ac_t21_mem0 += MAIN_MEM_r[0]
	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	c_ac_t21_mem1 += MAIN_MEM_r[1]
	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	c_ac_t30 += alt(MAS)

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	c_ac_t30_mem0 += MAIN_MEM_r[0]
	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	c_ac_t30_mem1 += MAIN_MEM_r[1]
	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	c_ac_t31 += alt(MAS)

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	c_ac_t31_mem0 += MAIN_MEM_r[0]
	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	c_ac_t31_mem1 += MAIN_MEM_r[1]
	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/FP12_INV_BEFORE_FPINV/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

