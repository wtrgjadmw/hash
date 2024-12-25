from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 182
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 0
	c_ab_t0_t3_in += MAS_in[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 0
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 0
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 1
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 1
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 1
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 1
	c_ab_t0_t3 += MAS[1]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 2
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 2
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 2
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=11, delay_cost=1)
	S += c_ab_t0_t1 >= 2
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=11, delay_cost=1)
	S += c_ab_t0_t0 >= 3
	c_ab_t0_t0 += MM[0]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 3
	c_cc_a1_1_in += MAS_in[1]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 3
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 3
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 4
	c_cc_a1_1 += MAS[1]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 4
	c_cc_t11_in += MAS_in[4]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 4
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 4
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 5
	c_cc_t11 += MAS[4]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 5
	c_cc_t3_t1_in += MM_in[1]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 5
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 5
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 6
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 6
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 6
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=11, delay_cost=1)
	S += c_cc_t3_t1 >= 6
	c_cc_t3_t1 += MM[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=11, delay_cost=1)
	S += c_aa_t3_t1 >= 7
	c_aa_t3_t1 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 7
	c_ab_t1_t1_in += MM_in[1]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 7
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 7
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=11, delay_cost=1)
	S += c_ab_t1_t1 >= 8
	c_ab_t1_t1 += MM[1]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 8
	c_bb_t3_t0_in += MM_in[1]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 8
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 8
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 9
	c_ab_t0_t2_in += MAS_in[2]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 9
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 9
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=11, delay_cost=1)
	S += c_bb_t3_t0 >= 9
	c_bb_t3_t0 += MM[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 10
	c_aa_t3_t2_in += MAS_in[5]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 10
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 10
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 10
	c_ab_t0_t2 += MAS[2]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 11
	c_aa_t3_t2 += MAS[5]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 11
	c_cc_t3_t3_in += MAS_in[5]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 11
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 11
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 12
	c_bb_t3_t3_in += MAS_in[5]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 12
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 12
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 12
	c_cc_t3_t3 += MAS[5]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 13
	c_bb_t3_t3 += MAS[5]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 13
	c_cc_t3_t2_in += MAS_in[5]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 13
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 14
	c_cc_t10_in += MAS_in[4]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 14
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 14
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 14
	c_cc_t3_t2 += MAS[5]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 15
	c_aa_a1_0_in += MAS_in[5]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 15
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 15
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 15
	c_cc_t10 += MAS[4]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 16
	c_aa_a1_0 += MAS[5]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 16
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 16
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 16
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 17
	c_bb_a1_1_in += MAS_in[5]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 17
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 17
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=11, delay_cost=1)
	S += c_cc_t3_t0 >= 17
	c_cc_t3_t0 += MM[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 18
	c_bb_a1_1 += MAS[5]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 18
	c_bb_t11_in += MAS_in[4]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 18
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 18
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 19
	c_aa_a1_1_in += MAS_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 19
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 19
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 19
	c_bb_t11 += MAS[4]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 20
	c_aa_a1_1 += MAS[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 20
	c_aa_t3_t0_in += MM_in[1]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 20
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 20
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=11, delay_cost=1)
	S += c_aa_t3_t0 >= 21
	c_aa_t3_t0 += MM[1]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 21
	c_bb_t3_t1_in += MM_in[1]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 21
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 21
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 22
	c_bb_t10_in += MAS_in[5]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 22
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 22
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=11, delay_cost=1)
	S += c_bb_t3_t1 >= 22
	c_bb_t3_t1 += MM[1]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 23
	c_bb_t10 += MAS[5]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 23
	c_cc_a1_0_in += MAS_in[4]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 23
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 23
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 24
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 24
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 24
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 24
	c_cc_a1_0 += MAS[4]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 25
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 25
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 25
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 25
	c_bb_t3_t2 += MAS[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=11, delay_cost=1)
	S += c_ab_t1_t0 >= 26
	c_ab_t1_t0 += MM[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 26
	c_bb_a1_0_in += MAS_in[5]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 26
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 26
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 27
	c_aa_t3_t3_in += MAS_in[5]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 27
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 27
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 27
	c_bb_a1_0 += MAS[5]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 28
	c_aa_t11_in += MAS_in[5]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 28
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 28
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 28
	c_aa_t3_t3 += MAS[5]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 29
	c_aa_t10_in += MAS_in[5]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 29
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 29
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 29
	c_aa_t11 += MAS[5]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 30
	c_aa_t10 += MAS[5]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 30
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 30
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 30
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=11, delay_cost=1)
	S += c_ac_t0_t0 >= 31
	c_ac_t0_t0 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 31
	c_ac_t1_t0_in += MM_in[1]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 31
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 31
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=11, delay_cost=1)
	S += c_ac_t1_t0 >= 32
	c_ac_t1_t0 += MM[1]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 32
	c_bc_t0_t3_in += MAS_in[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 32
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 32
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 33
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 33
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 33
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	S += c_bc_t0_t3 >= 33
	c_bc_t0_t3 += MAS[2]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=11, delay_cost=1)
	S += c_ac_t0_t1 >= 34
	c_ac_t0_t1 += MM[0]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 34
	c_ac_t31_in += MAS_in[5]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 34
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 34
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	S += c_ac_t31 >= 35
	c_ac_t31 += MAS[5]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 35
	c_bc_t1_t3_in += MAS_in[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 35
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 35
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 36
	c_ac_t0_t3_in += MAS_in[2]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 36
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 36
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	S += c_bc_t1_t3 >= 36
	c_bc_t1_t3 += MAS[1]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	S += c_ac_t0_t3 >= 37
	c_ac_t0_t3 += MAS[2]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 37
	c_ac_t1_t1_in += MM_in[1]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 37
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 37
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=11, delay_cost=1)
	S += c_ac_t1_t1 >= 38
	c_ac_t1_t1 += MM[1]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 38
	c_bc_t1_t0_in += MM_in[1]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 38
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 38
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=11, delay_cost=1)
	S += c_bc_t1_t0 >= 39
	c_bc_t1_t0 += MM[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 39
	c_bc_t31_in += MAS_in[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 39
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 39
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 40
	c_ac_t21_in += MAS_in[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 40
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 40
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	S += c_bc_t31 >= 40
	c_bc_t31 += MAS[0]

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	S += c_ac_t21 >= 41
	c_ac_t21 += MAS[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 41
	c_bc_t0_t1_in += MM_in[1]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 41
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 41
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=11, delay_cost=1)
	S += c_bc_t0_t1 >= 42
	c_bc_t0_t1 += MM[1]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 42
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 42
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 42
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 43
	c_ac_t30_in += MAS_in[5]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 43
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 43
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=11, delay_cost=1)
	S += c_bc_t1_t1 >= 43
	c_bc_t1_t1 += MM[0]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 44
	c_ac_t0_t2_in += MAS_in[2]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 44
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 44
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	S += c_ac_t30 >= 44
	c_ac_t30 += MAS[5]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	S += c_ac_t0_t2 >= 45
	c_ac_t0_t2 += MAS[2]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 45
	c_bc_t0_t2_in += MAS_in[4]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 45
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 45
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	S += c_bc_t0_t2 >= 46
	c_bc_t0_t2 += MAS[4]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 46
	c_bc_t1_t2_in += MAS_in[4]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 46
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 46
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	S += c_bc_t1_t2 >= 47
	c_bc_t1_t2 += MAS[4]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 47
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 47
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 47
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 48
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 48
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 48
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	S += c_bc_t30 >= 48
	c_bc_t30 += MAS[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	S += c_ab_t1_t2 >= 49
	c_ab_t1_t2 += MAS[0]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 49
	c_ab_t31_in += MAS_in[2]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 49
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 49
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	S += c_ab_t31 >= 50
	c_ab_t31 += MAS[2]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 50
	c_ac_t20_in += MAS_in[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 50
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 50
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	S += c_ac_t20 >= 51
	c_ac_t20 += MAS[0]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 51
	c_bc_t21_in += MAS_in[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 51
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 51
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 52
	c_bc_t20_in += MAS_in[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 52
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 52
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	S += c_bc_t21 >= 52
	c_bc_t21 += MAS[3]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 53
	c_ac_t1_t3_in += MAS_in[2]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 53
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 53
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	S += c_bc_t20 >= 53
	c_bc_t20 += MAS[1]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 54
	c_ac_t1_t2_in += MAS_in[1]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 54
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 54
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	S += c_ac_t1_t3 >= 54
	c_ac_t1_t3 += MAS[2]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	S += c_ac_t1_t2 >= 55
	c_ac_t1_t2 += MAS[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 55
	c_bc_t0_t0_in += MM_in[1]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 55
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 55
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 56
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 56
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 56
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=11, delay_cost=1)
	S += c_bc_t0_t0 >= 56
	c_bc_t0_t0 += MM[1]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	S += c_ab_t1_t3 >= 57
	c_ab_t1_t3 += MAS[0]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 57
	c_ab_t30_in += MAS_in[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 57
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 57
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 58
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 58
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 58
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	S += c_ab_t30 >= 58
	c_ab_t30 += MAS[0]

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
	S += c_ab_t20 >= 59
	c_ab_t20 += MAS[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 59
	c_ab_t21_in += MAS_in[3]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 59
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 59
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	S += c_ab_t21 >= 60
	c_ab_t21 += MAS[3]


	# new tasks
	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=2, delay_cost=1)
	c_pbc_t0_t3 += alt(MAS)
	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	c_pbc_t0_t3_in += alt(MAS_in)
	S += c_pbc_t0_t3_in*MAS_in[0]<=c_pbc_t0_t3*MAS[0]

	S += c_pbc_t0_t3_in*MAS_in[1]<=c_pbc_t0_t3*MAS[1]

	S += c_pbc_t0_t3_in*MAS_in[2]<=c_pbc_t0_t3*MAS[2]

	S += c_pbc_t0_t3_in*MAS_in[3]<=c_pbc_t0_t3*MAS[3]

	S += c_pbc_t0_t3_in*MAS_in[4]<=c_pbc_t0_t3*MAS[4]

	S += c_pbc_t0_t3_in*MAS_in[5]<=c_pbc_t0_t3*MAS[5]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_pbc_t0_t3_mem0 <= c_pbc_t0_t3

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t0_t3_mem1 <= c_pbc_t0_t3

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=2, delay_cost=1)
	c_pbc_t1_t3 += alt(MAS)
	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	c_pbc_t1_t3_in += alt(MAS_in)
	S += c_pbc_t1_t3_in*MAS_in[0]<=c_pbc_t1_t3*MAS[0]

	S += c_pbc_t1_t3_in*MAS_in[1]<=c_pbc_t1_t3*MAS[1]

	S += c_pbc_t1_t3_in*MAS_in[2]<=c_pbc_t1_t3*MAS[2]

	S += c_pbc_t1_t3_in*MAS_in[3]<=c_pbc_t1_t3*MAS[3]

	S += c_pbc_t1_t3_in*MAS_in[4]<=c_pbc_t1_t3*MAS[4]

	S += c_pbc_t1_t3_in*MAS_in[5]<=c_pbc_t1_t3*MAS[5]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_pbc_t1_t3_mem0 <= c_pbc_t1_t3

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t1_t3_mem1 <= c_pbc_t1_t3

	c_pbc_t30 = S.Task('c_pbc_t30', length=2, delay_cost=1)
	c_pbc_t30 += alt(MAS)
	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	c_pbc_t30_in += alt(MAS_in)
	S += c_pbc_t30_in*MAS_in[0]<=c_pbc_t30*MAS[0]

	S += c_pbc_t30_in*MAS_in[1]<=c_pbc_t30*MAS[1]

	S += c_pbc_t30_in*MAS_in[2]<=c_pbc_t30*MAS[2]

	S += c_pbc_t30_in*MAS_in[3]<=c_pbc_t30*MAS[3]

	S += c_pbc_t30_in*MAS_in[4]<=c_pbc_t30*MAS[4]

	S += c_pbc_t30_in*MAS_in[5]<=c_pbc_t30*MAS[5]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	c_pbc_t30_mem0 += MAIN_MEM_r[0]
	S += c_pbc_t30_mem0 <= c_pbc_t30

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	c_pbc_t30_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t30_mem1 <= c_pbc_t30

	c_pbc_t31 = S.Task('c_pbc_t31', length=2, delay_cost=1)
	c_pbc_t31 += alt(MAS)
	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	c_pbc_t31_in += alt(MAS_in)
	S += c_pbc_t31_in*MAS_in[0]<=c_pbc_t31*MAS[0]

	S += c_pbc_t31_in*MAS_in[1]<=c_pbc_t31*MAS[1]

	S += c_pbc_t31_in*MAS_in[2]<=c_pbc_t31*MAS[2]

	S += c_pbc_t31_in*MAS_in[3]<=c_pbc_t31*MAS[3]

	S += c_pbc_t31_in*MAS_in[4]<=c_pbc_t31*MAS[4]

	S += c_pbc_t31_in*MAS_in[5]<=c_pbc_t31*MAS[5]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	c_pbc_t31_mem0 += MAIN_MEM_r[0]
	S += c_pbc_t31_mem0 <= c_pbc_t31

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	c_pbc_t31_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t31_mem1 <= c_pbc_t31

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=2, delay_cost=1)
	c_pcb_t0_t3 += alt(MAS)
	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	c_pcb_t0_t3_in += alt(MAS_in)
	S += c_pcb_t0_t3_in*MAS_in[0]<=c_pcb_t0_t3*MAS[0]

	S += c_pcb_t0_t3_in*MAS_in[1]<=c_pcb_t0_t3*MAS[1]

	S += c_pcb_t0_t3_in*MAS_in[2]<=c_pcb_t0_t3*MAS[2]

	S += c_pcb_t0_t3_in*MAS_in[3]<=c_pcb_t0_t3*MAS[3]

	S += c_pcb_t0_t3_in*MAS_in[4]<=c_pcb_t0_t3*MAS[4]

	S += c_pcb_t0_t3_in*MAS_in[5]<=c_pcb_t0_t3*MAS[5]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_pcb_t0_t3_mem0 <= c_pcb_t0_t3

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t0_t3_mem1 <= c_pcb_t0_t3

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=2, delay_cost=1)
	c_pcb_t1_t3 += alt(MAS)
	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	c_pcb_t1_t3_in += alt(MAS_in)
	S += c_pcb_t1_t3_in*MAS_in[0]<=c_pcb_t1_t3*MAS[0]

	S += c_pcb_t1_t3_in*MAS_in[1]<=c_pcb_t1_t3*MAS[1]

	S += c_pcb_t1_t3_in*MAS_in[2]<=c_pcb_t1_t3*MAS[2]

	S += c_pcb_t1_t3_in*MAS_in[3]<=c_pcb_t1_t3*MAS[3]

	S += c_pcb_t1_t3_in*MAS_in[4]<=c_pcb_t1_t3*MAS[4]

	S += c_pcb_t1_t3_in*MAS_in[5]<=c_pcb_t1_t3*MAS[5]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_pcb_t1_t3_mem0 <= c_pcb_t1_t3

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t1_t3_mem1 <= c_pcb_t1_t3

	c_pcb_t30 = S.Task('c_pcb_t30', length=2, delay_cost=1)
	c_pcb_t30 += alt(MAS)
	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	c_pcb_t30_in += alt(MAS_in)
	S += c_pcb_t30_in*MAS_in[0]<=c_pcb_t30*MAS[0]

	S += c_pcb_t30_in*MAS_in[1]<=c_pcb_t30*MAS[1]

	S += c_pcb_t30_in*MAS_in[2]<=c_pcb_t30*MAS[2]

	S += c_pcb_t30_in*MAS_in[3]<=c_pcb_t30*MAS[3]

	S += c_pcb_t30_in*MAS_in[4]<=c_pcb_t30*MAS[4]

	S += c_pcb_t30_in*MAS_in[5]<=c_pcb_t30*MAS[5]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	c_pcb_t30_mem0 += MAIN_MEM_r[0]
	S += c_pcb_t30_mem0 <= c_pcb_t30

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	c_pcb_t30_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t30_mem1 <= c_pcb_t30

	c_pcb_t31 = S.Task('c_pcb_t31', length=2, delay_cost=1)
	c_pcb_t31 += alt(MAS)
	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	c_pcb_t31_in += alt(MAS_in)
	S += c_pcb_t31_in*MAS_in[0]<=c_pcb_t31*MAS[0]

	S += c_pcb_t31_in*MAS_in[1]<=c_pcb_t31*MAS[1]

	S += c_pcb_t31_in*MAS_in[2]<=c_pcb_t31*MAS[2]

	S += c_pcb_t31_in*MAS_in[3]<=c_pcb_t31*MAS[3]

	S += c_pcb_t31_in*MAS_in[4]<=c_pcb_t31*MAS[4]

	S += c_pcb_t31_in*MAS_in[5]<=c_pcb_t31*MAS[5]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	c_pcb_t31_mem0 += MAIN_MEM_r[0]
	S += c_pcb_t31_mem0 <= c_pcb_t31

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	c_pcb_t31_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t31_mem1 <= c_pcb_t31

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=2, delay_cost=1)
	c_paa_t0_t3 += alt(MAS)
	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	c_paa_t0_t3_in += alt(MAS_in)
	S += c_paa_t0_t3_in*MAS_in[0]<=c_paa_t0_t3*MAS[0]

	S += c_paa_t0_t3_in*MAS_in[1]<=c_paa_t0_t3*MAS[1]

	S += c_paa_t0_t3_in*MAS_in[2]<=c_paa_t0_t3*MAS[2]

	S += c_paa_t0_t3_in*MAS_in[3]<=c_paa_t0_t3*MAS[3]

	S += c_paa_t0_t3_in*MAS_in[4]<=c_paa_t0_t3*MAS[4]

	S += c_paa_t0_t3_in*MAS_in[5]<=c_paa_t0_t3*MAS[5]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_paa_t0_t3_mem0 <= c_paa_t0_t3

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_paa_t0_t3_mem1 <= c_paa_t0_t3

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=2, delay_cost=1)
	c_paa_t1_t3 += alt(MAS)
	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	c_paa_t1_t3_in += alt(MAS_in)
	S += c_paa_t1_t3_in*MAS_in[0]<=c_paa_t1_t3*MAS[0]

	S += c_paa_t1_t3_in*MAS_in[1]<=c_paa_t1_t3*MAS[1]

	S += c_paa_t1_t3_in*MAS_in[2]<=c_paa_t1_t3*MAS[2]

	S += c_paa_t1_t3_in*MAS_in[3]<=c_paa_t1_t3*MAS[3]

	S += c_paa_t1_t3_in*MAS_in[4]<=c_paa_t1_t3*MAS[4]

	S += c_paa_t1_t3_in*MAS_in[5]<=c_paa_t1_t3*MAS[5]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_paa_t1_t3_mem0 <= c_paa_t1_t3

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_paa_t1_t3_mem1 <= c_paa_t1_t3

	c_paa_t30 = S.Task('c_paa_t30', length=2, delay_cost=1)
	c_paa_t30 += alt(MAS)
	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	c_paa_t30_in += alt(MAS_in)
	S += c_paa_t30_in*MAS_in[0]<=c_paa_t30*MAS[0]

	S += c_paa_t30_in*MAS_in[1]<=c_paa_t30*MAS[1]

	S += c_paa_t30_in*MAS_in[2]<=c_paa_t30*MAS[2]

	S += c_paa_t30_in*MAS_in[3]<=c_paa_t30*MAS[3]

	S += c_paa_t30_in*MAS_in[4]<=c_paa_t30*MAS[4]

	S += c_paa_t30_in*MAS_in[5]<=c_paa_t30*MAS[5]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	c_paa_t30_mem0 += MAIN_MEM_r[0]
	S += c_paa_t30_mem0 <= c_paa_t30

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	c_paa_t30_mem1 += MAIN_MEM_r[1]
	S += c_paa_t30_mem1 <= c_paa_t30

	c_paa_t31 = S.Task('c_paa_t31', length=2, delay_cost=1)
	c_paa_t31 += alt(MAS)
	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	c_paa_t31_in += alt(MAS_in)
	S += c_paa_t31_in*MAS_in[0]<=c_paa_t31*MAS[0]

	S += c_paa_t31_in*MAS_in[1]<=c_paa_t31*MAS[1]

	S += c_paa_t31_in*MAS_in[2]<=c_paa_t31*MAS[2]

	S += c_paa_t31_in*MAS_in[3]<=c_paa_t31*MAS[3]

	S += c_paa_t31_in*MAS_in[4]<=c_paa_t31*MAS[4]

	S += c_paa_t31_in*MAS_in[5]<=c_paa_t31*MAS[5]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	c_paa_t31_mem0 += MAIN_MEM_r[0]
	S += c_paa_t31_mem0 <= c_paa_t31

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	c_paa_t31_mem1 += MAIN_MEM_r[1]
	S += c_paa_t31_mem1 <= c_paa_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS6/FP12_INV_BEFORE_FPINV/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

