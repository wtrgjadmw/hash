from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 221
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=5)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 0
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 0
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 0
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=14, delay_cost=1)
	S += c_aa_t3_t1 >= 1
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 1
	c_aa_t3_t2_in += MAS_in[2]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 1
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 1
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=3, delay_cost=1)
	S += c_aa_t3_t2 >= 2
	c_aa_t3_t2 += MAS[2]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 2
	c_aa_t3_t3_in += MAS_in[2]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 2
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 2
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 3
	c_aa_t10_in += MAS_in[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 3
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 3
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=3, delay_cost=1)
	S += c_aa_t3_t3 >= 3
	c_aa_t3_t3 += MAS[2]

	c_aa_t10 = S.Task('c_aa_t10', length=3, delay_cost=1)
	S += c_aa_t10 >= 4
	c_aa_t10 += MAS[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 4
	c_cc_t10_in += MAS_in[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 4
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 4
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 5
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 5
	c_aa_t3_t4_mem0 += MAS_MEM[4]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 5
	c_aa_t3_t4_mem1 += MAS_MEM[5]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 5
	c_bb_t10_in += MAS_in[0]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 5
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 5
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=3, delay_cost=1)
	S += c_cc_t10 >= 5
	c_cc_t10 += MAS[0]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=14, delay_cost=1)
	S += c_aa_t3_t4 >= 6
	c_aa_t3_t4 += MM[0]

	c_bb_t10 = S.Task('c_bb_t10', length=3, delay_cost=1)
	S += c_bb_t10 >= 6
	c_bb_t10 += MAS[0]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 6
	c_cc_t3_t3_in += MAS_in[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 6
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 6
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 7
	c_aa_a1_0_in += MAS_in[1]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 7
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 7
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=3, delay_cost=1)
	S += c_cc_t3_t3 >= 7
	c_cc_t3_t3 += MAS[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=3, delay_cost=1)
	S += c_aa_a1_0 >= 8
	c_aa_a1_0 += MAS[1]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 8
	c_ab_t0_t2_in += MAS_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 8
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 8
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 9
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 9
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 9
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=3, delay_cost=1)
	S += c_ab_t0_t2 >= 9
	c_ab_t0_t2 += MAS[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=14, delay_cost=1)
	S += c_aa_t3_t0 >= 10
	c_aa_t3_t0 += MM[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 10
	c_cc_t11_in += MAS_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 10
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 10
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 11
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 11
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 11
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=3, delay_cost=1)
	S += c_cc_t11 >= 11
	c_cc_t11 += MAS[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 12
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 12
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 12
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=3, delay_cost=1)
	S += c_bb_t3_t2 >= 12
	c_bb_t3_t2 += MAS[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=14, delay_cost=1)
	S += c_ab_t0_t0 >= 13
	c_ab_t0_t0 += MM[0]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 13
	c_cc_a1_0_in += MAS_in[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 13
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 13
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 13
	c_cc_t2_t3_in += MAS_in[1]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 13
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 13
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 14
	c_aa_t11_in += MAS_in[4]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 14
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 14
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=3, delay_cost=1)
	S += c_cc_a1_0 >= 14
	c_cc_a1_0 += MAS[0]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=3, delay_cost=1)
	S += c_cc_t2_t3 >= 14
	c_cc_t2_t3 += MAS[1]

	c_aa_t11 = S.Task('c_aa_t11', length=3, delay_cost=1)
	S += c_aa_t11 >= 15
	c_aa_t11 += MAS[4]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 15
	c_bb_a1_1_in += MAS_in[4]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 15
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 15
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=3, delay_cost=1)
	S += c_bb_a1_1 >= 16
	c_bb_a1_1 += MAS[4]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 16
	c_bb_t11_in += MAS_in[3]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 16
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 16
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 17
	c_aa_t2_t3_in += MAS_in[2]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 17
	c_aa_t2_t3_mem0 += MAS_MEM[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 17
	c_aa_t2_t3_mem1 += MAS_MEM[9]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 17
	c_bb_a1_0_in += MAS_in[4]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 17
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 17
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=3, delay_cost=1)
	S += c_bb_t11 >= 17
	c_bb_t11 += MAS[3]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=3, delay_cost=1)
	S += c_aa_t2_t3 >= 18
	c_aa_t2_t3 += MAS[2]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=3, delay_cost=1)
	S += c_bb_a1_0 >= 18
	c_bb_a1_0 += MAS[4]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 18
	c_cc_a1_1_in += MAS_in[4]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 18
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 18
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 19
	c_aa_a1_1_in += MAS_in[2]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 19
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 19
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 19
	c_bb_t2_t3_in += MAS_in[3]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 19
	c_bb_t2_t3_mem0 += MAS_MEM[0]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 19
	c_bb_t2_t3_mem1 += MAS_MEM[7]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=3, delay_cost=1)
	S += c_cc_a1_1 >= 19
	c_cc_a1_1 += MAS[4]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=3, delay_cost=1)
	S += c_aa_a1_1 >= 20
	c_aa_a1_1 += MAS[2]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=3, delay_cost=1)
	S += c_bb_t2_t3 >= 20
	c_bb_t2_t3 += MAS[3]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 20
	c_bb_t3_t3_in += MAS_in[4]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 20
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 20
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 21
	c_ab_t0_t3_in += MAS_in[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 21
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 21
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=3, delay_cost=1)
	S += c_bb_t3_t3 >= 21
	c_bb_t3_t3 += MAS[4]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=3, delay_cost=1)
	S += c_ab_t0_t3 >= 22
	c_ab_t0_t3 += MAS[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 22
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 22
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 22
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 23
	c_aa_t3_t5_in += MAS_in[0]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 23
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 23
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=14, delay_cost=1)
	S += c_ab_t1_t1 >= 23
	c_ab_t1_t1 += MM[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 23
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 23
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 23
	c_bb_t3_t4_mem1 += MAS_MEM[9]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 23
	c_cc_t3_t2_in += MAS_in[4]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 23
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 23
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 24
	c_aa_t30_in += MAS_in[2]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 24
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 24
	c_aa_t30_mem1 += MM_MEM[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=3, delay_cost=1)
	S += c_aa_t3_t5 >= 24
	c_aa_t3_t5 += MAS[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 24
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 24
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 24
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=14, delay_cost=1)
	S += c_bb_t3_t4 >= 24
	c_bb_t3_t4 += MM[0]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=3, delay_cost=1)
	S += c_cc_t3_t2 >= 24
	c_cc_t3_t2 += MAS[4]

	c_aa_t30 = S.Task('c_aa_t30', length=3, delay_cost=1)
	S += c_aa_t30 >= 25
	c_aa_t30 += MAS[2]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=14, delay_cost=1)
	S += c_ab_t0_t1 >= 25
	c_ab_t0_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 25
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 25
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 25
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	S += c_aa_t31_in >= 26
	c_aa_t31_in += MAS_in[3]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 26
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 26
	c_aa_t31_mem1 += MAS_MEM[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=14, delay_cost=1)
	S += c_ab_t1_t0 >= 26
	c_ab_t1_t0 += MM[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 26
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 26
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 26
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	S += c_aa10_in >= 27
	c_aa10_in += MAS_in[2]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 27
	c_aa10_mem0 += MAS_MEM[4]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 27
	c_aa10_mem1 += MAS_MEM[5]

	c_aa_t31 = S.Task('c_aa_t31', length=3, delay_cost=1)
	S += c_aa_t31 >= 27
	c_aa_t31 += MAS[3]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 27
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 27
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 27
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=14, delay_cost=1)
	S += c_cc_t3_t1 >= 27
	c_cc_t3_t1 += MM[0]

	c_aa10 = S.Task('c_aa10', length=3, delay_cost=1)
	S += c_aa10 >= 28
	c_aa10 += MAS[2]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 28
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 28
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 28
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=14, delay_cost=1)
	S += c_cc_t3_t0 >= 28
	c_cc_t3_t0 += MM[0]

	c_aa_t40_in = S.Task('c_aa_t40_in', length=1, delay_cost=1)
	S += c_aa_t40_in >= 29
	c_aa_t40_in += MAS_in[0]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 29
	c_aa_t40_mem0 += MAS_MEM[4]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 29
	c_aa_t40_mem1 += MAS_MEM[7]

	c_aa_t41_in = S.Task('c_aa_t41_in', length=1, delay_cost=1)
	S += c_aa_t41_in >= 29
	c_aa_t41_in += MAS_in[3]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 29
	c_aa_t41_mem0 += MAS_MEM[6]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 29
	c_aa_t41_mem1 += MAS_MEM[5]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 29
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 29
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 29
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=14, delay_cost=1)
	S += c_bb_t3_t1 >= 29
	c_bb_t3_t1 += MM[0]

	c_aa11_in = S.Task('c_aa11_in', length=1, delay_cost=1)
	S += c_aa11_in >= 30
	c_aa11_in += MAS_in[3]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 30
	c_aa11_mem0 += MAS_MEM[6]

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	S += c_aa11_mem1 >= 30
	c_aa11_mem1 += MAS_MEM[7]

	c_aa_t40 = S.Task('c_aa_t40', length=3, delay_cost=1)
	S += c_aa_t40 >= 30
	c_aa_t40 += MAS[0]

	c_aa_t41 = S.Task('c_aa_t41', length=3, delay_cost=1)
	S += c_aa_t41 >= 30
	c_aa_t41 += MAS[3]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 30
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 30
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 30
	c_ab_t0_t4_mem1 += MAS_MEM[1]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 30
	c_ab_t21_in += MAS_in[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 30
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 30
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=14, delay_cost=1)
	S += c_bb_t3_t0 >= 30
	c_bb_t3_t0 += MM[0]

	c_aa11 = S.Task('c_aa11', length=3, delay_cost=1)
	S += c_aa11 >= 31
	c_aa11 += MAS[3]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=14, delay_cost=1)
	S += c_ab_t0_t4 >= 31
	c_ab_t0_t4 += MM[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 31
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 31
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 31
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t21 = S.Task('c_ab_t21', length=3, delay_cost=1)
	S += c_ab_t21 >= 31
	c_ab_t21 += MAS[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 31
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 31
	c_cc_t3_t4_mem0 += MAS_MEM[8]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 31
	c_cc_t3_t4_mem1 += MAS_MEM[1]

	c_ab_t20 = S.Task('c_ab_t20', length=3, delay_cost=1)
	S += c_ab_t20 >= 32
	c_ab_t20 += MAS[0]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 32
	c_ab_t30_in += MAS_in[4]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 32
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 32
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=14, delay_cost=1)
	S += c_cc_t3_t4 >= 32
	c_cc_t3_t4 += MM[0]

	c_ab_t30 = S.Task('c_ab_t30', length=3, delay_cost=1)
	S += c_ab_t30 >= 33
	c_ab_t30 += MAS[4]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 33
	c_ab_t31_in += MAS_in[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 33
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 33
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 34
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 34
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 34
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t31 = S.Task('c_ab_t31', length=3, delay_cost=1)
	S += c_ab_t31 >= 34
	c_ab_t31 += MAS[0]

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 34
	c_ab_t4_t2_in += MAS_in[3]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 34
	c_ab_t4_t2_mem0 += MAS_MEM[0]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 34
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=3, delay_cost=1)
	S += c_ab_t1_t3 >= 35
	c_ab_t1_t3 += MAS[0]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 35
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 35
	c_ab_t4_t0_mem0 += MAS_MEM[0]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 35
	c_ab_t4_t0_mem1 += MAS_MEM[9]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=3, delay_cost=1)
	S += c_ab_t4_t2 >= 35
	c_ab_t4_t2 += MAS[3]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 35
	c_bc_t1_t2_in += MAS_in[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 35
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 35
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=14, delay_cost=1)
	S += c_ab_t4_t0 >= 36
	c_ab_t4_t0 += MM[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 36
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 36
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 36
	c_ab_t4_t1_mem1 += MAS_MEM[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=3, delay_cost=1)
	S += c_bc_t1_t2 >= 36
	c_bc_t1_t2 += MAS[0]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 36
	c_bc_t20_in += MAS_in[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 36
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 36
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=14, delay_cost=1)
	S += c_ab_t4_t1 >= 37
	c_ab_t4_t1 += MM[0]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 37
	c_ab_t4_t3_in += MAS_in[3]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 37
	c_ab_t4_t3_mem0 += MAS_MEM[8]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 37
	c_ab_t4_t3_mem1 += MAS_MEM[1]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 37
	c_ac_t1_t2_in += MAS_in[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 37
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 37
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t20 = S.Task('c_bc_t20', length=3, delay_cost=1)
	S += c_bc_t20 >= 37
	c_bc_t20 += MAS[0]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 38
	c_ab_t00_in += MAS_in[3]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 38
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 38
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=3, delay_cost=1)
	S += c_ab_t4_t3 >= 38
	c_ab_t4_t3 += MAS[3]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=3, delay_cost=1)
	S += c_ac_t1_t2 >= 38
	c_ac_t1_t2 += MAS[0]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 38
	c_bc_t31_in += MAS_in[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 38
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 38
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t00 = S.Task('c_ab_t00', length=3, delay_cost=1)
	S += c_ab_t00 >= 39
	c_ab_t00 += MAS[3]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 39
	c_ab_t1_t5_in += MAS_in[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 39
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 39
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 39
	c_ac_t1_t3_in += MAS_in[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 39
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 39
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=3, delay_cost=1)
	S += c_bc_t31 >= 39
	c_bc_t31 += MAS[0]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 40
	c_ab_t10_in += MAS_in[3]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 40
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 40
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=3, delay_cost=1)
	S += c_ab_t1_t5 >= 40
	c_ab_t1_t5 += MAS[3]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 40
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 40
	c_ab_t4_t4_mem0 += MAS_MEM[6]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 40
	c_ab_t4_t4_mem1 += MAS_MEM[7]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=3, delay_cost=1)
	S += c_ac_t1_t3 >= 40
	c_ac_t1_t3 += MAS[0]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 40
	c_bc_t21_in += MAS_in[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 40
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 40
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=3, delay_cost=1)
	S += c_ab_t10 >= 41
	c_ab_t10 += MAS[3]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=14, delay_cost=1)
	S += c_ab_t4_t4 >= 41
	c_ab_t4_t4 += MM[0]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 41
	c_ac_t21_in += MAS_in[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 41
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 41
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t21 = S.Task('c_bc_t21', length=3, delay_cost=1)
	S += c_bc_t21 >= 41
	c_bc_t21 += MAS[0]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 41
	c_cc_t3_t5_in += MAS_in[3]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 41
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 41
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 42
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 42
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 42
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_ac_t21 = S.Task('c_ac_t21', length=3, delay_cost=1)
	S += c_ac_t21 >= 42
	c_ac_t21 += MAS[0]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 42
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 42
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 42
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 42
	c_cc_t30_in += MAS_in[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 42
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 42
	c_cc_t30_mem1 += MM_MEM[1]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=3, delay_cost=1)
	S += c_cc_t3_t5 >= 42
	c_cc_t3_t5 += MAS[3]

	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	S += c_ab_t50_in >= 43
	c_ab_t50_in += MAS_in[2]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 43
	c_ab_t50_mem0 += MAS_MEM[6]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 43
	c_ab_t50_mem1 += MAS_MEM[7]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 43
	c_ac_t0_t2_in += MAS_in[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 43
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 43
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=14, delay_cost=1)
	S += c_ac_t1_t4 >= 43
	c_ac_t1_t4 += MM[0]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 43
	c_bb_t3_t5_in += MAS_in[3]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 43
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 43
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=3, delay_cost=1)
	S += c_bc_t1_t3 >= 43
	c_bc_t1_t3 += MAS[0]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 43
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 43
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 43
	c_bc_t4_t1_mem1 += MAS_MEM[1]

	c_cc_t30 = S.Task('c_cc_t30', length=3, delay_cost=1)
	S += c_cc_t30 >= 43
	c_cc_t30 += MAS[1]

	c_ab_t50 = S.Task('c_ab_t50', length=3, delay_cost=1)
	S += c_ab_t50 >= 44
	c_ab_t50 += MAS[2]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=3, delay_cost=1)
	S += c_ac_t0_t2 >= 44
	c_ac_t0_t2 += MAS[0]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 44
	c_bb_t30_in += MAS_in[4]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 44
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 44
	c_bb_t30_mem1 += MM_MEM[1]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=3, delay_cost=1)
	S += c_bb_t3_t5 >= 44
	c_bb_t3_t5 += MAS[3]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 44
	c_bc_t0_t3_in += MAS_in[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 44
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 44
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=14, delay_cost=1)
	S += c_bc_t4_t1 >= 44
	c_bc_t4_t1 += MM[0]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 44
	c_bc_t4_t2_in += MAS_in[3]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 44
	c_bc_t4_t2_mem0 += MAS_MEM[0]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 44
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 45
	c_ab_t0_t5_in += MAS_in[0]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 45
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 45
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 45
	c_ac_t20_in += MAS_in[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 45
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 45
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bb_t30 = S.Task('c_bb_t30', length=3, delay_cost=1)
	S += c_bb_t30 >= 45
	c_bb_t30 += MAS[4]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=3, delay_cost=1)
	S += c_bc_t0_t3 >= 45
	c_bc_t0_t3 += MAS[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 45
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 45
	c_bc_t1_t4_mem0 += MAS_MEM[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 45
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=3, delay_cost=1)
	S += c_bc_t4_t2 >= 45
	c_bc_t4_t2 += MAS[3]

	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	S += c_cc10_in >= 45
	c_cc10_in += MAS_in[1]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 45
	c_cc10_mem0 += MAS_MEM[2]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 45
	c_cc10_mem1 += MAS_MEM[3]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=3, delay_cost=1)
	S += c_ab_t0_t5 >= 46
	c_ab_t0_t5 += MAS[0]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 46
	c_ab_t1_t2_in += MAS_in[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 46
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 46
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t20 = S.Task('c_ac_t20', length=3, delay_cost=1)
	S += c_ac_t20 >= 46
	c_ac_t20 += MAS[3]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=14, delay_cost=1)
	S += c_bc_t1_t4 >= 46
	c_bc_t1_t4 += MM[0]

	c_cc10 = S.Task('c_cc10', length=3, delay_cost=1)
	S += c_cc10 >= 46
	c_cc10 += MAS[1]

	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	S += c_cc_t31_in >= 46
	c_cc_t31_in += MAS_in[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 46
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 46
	c_cc_t31_mem1 += MAS_MEM[7]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=3, delay_cost=1)
	S += c_ab_t1_t2 >= 47
	c_ab_t1_t2 += MAS[1]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 47
	c_ac_t0_t3_in += MAS_in[0]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 47
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 47
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	S += c_bb10_in >= 47
	c_bb10_in += MAS_in[3]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 47
	c_bb10_mem0 += MAS_MEM[8]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 47
	c_bb10_mem1 += MAS_MEM[9]

	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	S += c_bb_t31_in >= 47
	c_bb_t31_in += MAS_in[1]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 47
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 47
	c_bb_t31_mem1 += MAS_MEM[7]

	c_cc_t31 = S.Task('c_cc_t31', length=3, delay_cost=1)
	S += c_cc_t31 >= 47
	c_cc_t31 += MAS[0]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=3, delay_cost=1)
	S += c_ac_t0_t3 >= 48
	c_ac_t0_t3 += MAS[0]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 48
	c_ac_t30_in += MAS_in[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 48
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 48
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 48
	c_ac_t4_t2_in += MAS_in[2]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 48
	c_ac_t4_t2_mem0 += MAS_MEM[6]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 48
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_bb10 = S.Task('c_bb10', length=3, delay_cost=1)
	S += c_bb10 >= 48
	c_bb10 += MAS[3]

	c_bb_t31 = S.Task('c_bb_t31', length=3, delay_cost=1)
	S += c_bb_t31 >= 48
	c_bb_t31 += MAS[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 49
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 49
	c_ab_t1_t4_mem0 += MAS_MEM[2]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 49
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_ac_t30 = S.Task('c_ac_t30', length=3, delay_cost=1)
	S += c_ac_t30 >= 49
	c_ac_t30 += MAS[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=3, delay_cost=1)
	S += c_ac_t4_t2 >= 49
	c_ac_t4_t2 += MAS[2]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 49
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 49
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 49
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t41_in = S.Task('c_cc_t41_in', length=1, delay_cost=1)
	S += c_cc_t41_in >= 49
	c_cc_t41_in += MAS_in[3]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 49
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 49
	c_cc_t41_mem1 += MAS_MEM[3]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=14, delay_cost=1)
	S += c_ab_t1_t4 >= 50
	c_ab_t1_t4 += MM[0]

	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	S += c_ab_t4_t5_in >= 50
	c_ab_t4_t5_in += MAS_in[4]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 50
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 50
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 50
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 50
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 50
	c_ac_t0_t4_mem1 += MAS_MEM[1]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 50
	c_ac_t31_in += MAS_in[3]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 50
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 50
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bb_t40_in = S.Task('c_bb_t40_in', length=1, delay_cost=1)
	S += c_bb_t40_in >= 50
	c_bb_t40_in += MAS_in[1]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 50
	c_bb_t40_mem0 += MAS_MEM[8]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 50
	c_bb_t40_mem1 += MAS_MEM[3]

	c_bb_t41_in = S.Task('c_bb_t41_in', length=1, delay_cost=1)
	S += c_bb_t41_in >= 50
	c_bb_t41_in += MAS_in[0]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 50
	c_bb_t41_mem0 += MAS_MEM[2]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 50
	c_bb_t41_mem1 += MAS_MEM[9]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=3, delay_cost=1)
	S += c_bc_t0_t2 >= 50
	c_bc_t0_t2 += MAS[0]

	c_cc_t41 = S.Task('c_cc_t41', length=3, delay_cost=1)
	S += c_cc_t41 >= 50
	c_cc_t41 += MAS[3]

	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	S += c_ab_t40_in >= 51
	c_ab_t40_in += MAS_in[4]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 51
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 51
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=3, delay_cost=1)
	S += c_ab_t4_t5 >= 51
	c_ab_t4_t5 += MAS[4]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=14, delay_cost=1)
	S += c_ac_t0_t4 >= 51
	c_ac_t0_t4 += MM[0]

	c_ac_t31 = S.Task('c_ac_t31', length=3, delay_cost=1)
	S += c_ac_t31 >= 51
	c_ac_t31 += MAS[3]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 51
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 51
	c_ac_t4_t0_mem0 += MAS_MEM[6]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 51
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_bb11_in = S.Task('c_bb11_in', length=1, delay_cost=1)
	S += c_bb11_in >= 51
	c_bb11_in += MAS_in[2]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 51
	c_bb11_mem0 += MAS_MEM[2]

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	S += c_bb11_mem1 >= 51
	c_bb11_mem1 += MAS_MEM[3]

	c_bb_t40 = S.Task('c_bb_t40', length=3, delay_cost=1)
	S += c_bb_t40 >= 51
	c_bb_t40 += MAS[1]

	c_bb_t41 = S.Task('c_bb_t41', length=3, delay_cost=1)
	S += c_bb_t41 >= 51
	c_bb_t41 += MAS[0]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 51
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 51
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 51
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	S += c_ab_t01_in >= 52
	c_ab_t01_in += MAS_in[3]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 52
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 52
	c_ab_t01_mem1 += MAS_MEM[1]

	c_ab_t40 = S.Task('c_ab_t40', length=3, delay_cost=1)
	S += c_ab_t40 >= 52
	c_ab_t40 += MAS[4]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=14, delay_cost=1)
	S += c_ac_t4_t0 >= 52
	c_ac_t4_t0 += MM[0]

	c_bb11 = S.Task('c_bb11', length=3, delay_cost=1)
	S += c_bb11 >= 52
	c_bb11 += MAS[2]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 52
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 52
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 52
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=3, delay_cost=1)
	S += c_bc_t30 >= 52
	c_bc_t30 += MAS[0]

	c_ab_t01 = S.Task('c_ab_t01', length=3, delay_cost=1)
	S += c_ab_t01 >= 53
	c_ab_t01 += MAS[3]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 53
	c_ac_t4_t3_in += MAS_in[3]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 53
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 53
	c_ac_t4_t3_mem1 += MAS_MEM[7]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 53
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 53
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 53
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=14, delay_cost=1)
	S += c_bc_t0_t1 >= 53
	c_bc_t0_t1 += MM[0]

	c_cc_t40_in = S.Task('c_cc_t40_in', length=1, delay_cost=1)
	S += c_cc_t40_in >= 53
	c_cc_t40_in += MAS_in[1]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 53
	c_cc_t40_mem0 += MAS_MEM[2]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 53
	c_cc_t40_mem1 += MAS_MEM[1]

	c_ab10_in = S.Task('c_ab10_in', length=1, delay_cost=1)
	S += c_ab10_in >= 54
	c_ab10_in += MAS_in[2]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 54
	c_ab10_mem0 += MAS_MEM[8]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 54
	c_ab10_mem1 += MAS_MEM[5]

	c_ab_t41_in = S.Task('c_ab_t41_in', length=1, delay_cost=1)
	S += c_ab_t41_in >= 54
	c_ab_t41_in += MAS_in[1]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 54
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 54
	c_ab_t41_mem1 += MAS_MEM[9]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 54
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 54
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 54
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=3, delay_cost=1)
	S += c_ac_t4_t3 >= 54
	c_ac_t4_t3 += MAS[3]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=14, delay_cost=1)
	S += c_bc_t0_t0 >= 54
	c_bc_t0_t0 += MM[0]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 54
	c_bc_t4_t3_in += MAS_in[3]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 54
	c_bc_t4_t3_mem0 += MAS_MEM[0]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 54
	c_bc_t4_t3_mem1 += MAS_MEM[1]

	c_cc_t40 = S.Task('c_cc_t40', length=3, delay_cost=1)
	S += c_cc_t40 >= 54
	c_cc_t40 += MAS[1]

	c_ab10 = S.Task('c_ab10', length=3, delay_cost=1)
	S += c_ab10 >= 55
	c_ab10 += MAS[2]

	c_ab_t41 = S.Task('c_ab_t41', length=3, delay_cost=1)
	S += c_ab_t41 >= 55
	c_ab_t41 += MAS[1]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 55
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 55
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 55
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=14, delay_cost=1)
	S += c_ac_t1_t1 >= 55
	c_ac_t1_t1 += MM[0]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=3, delay_cost=1)
	S += c_bc_t4_t3 >= 55
	c_bc_t4_t3 += MAS[3]

	c_cc11_in = S.Task('c_cc11_in', length=1, delay_cost=1)
	S += c_cc11_in >= 55
	c_cc11_in += MAS_in[4]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 55
	c_cc11_mem0 += MAS_MEM[0]

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	S += c_cc11_mem1 >= 55
	c_cc11_mem1 += MAS_MEM[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 56
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 56
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 56
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=14, delay_cost=1)
	S += c_ac_t1_t0 >= 56
	c_ac_t1_t0 += MM[0]

	c_cc11 = S.Task('c_cc11', length=3, delay_cost=1)
	S += c_cc11 >= 56
	c_cc11 += MAS[4]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 57
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 57
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 57
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=14, delay_cost=1)
	S += c_ac_t0_t1 >= 57
	c_ac_t0_t1 += MM[0]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=14, delay_cost=1)
	S += c_ac_t0_t0 >= 58
	c_ac_t0_t0 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 58
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 58
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 58
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 59
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 59
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 59
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=14, delay_cost=1)
	S += c_bc_t1_t1 >= 59
	c_bc_t1_t1 += MM[0]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 60
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 60
	c_bc_t0_t4_mem0 += MAS_MEM[0]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 60
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=14, delay_cost=1)
	S += c_bc_t1_t0 >= 60
	c_bc_t1_t0 += MM[0]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 60
	c_pbc_t30_in += MAS_in[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 60
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 60
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=14, delay_cost=1)
	S += c_bc_t0_t4 >= 61
	c_bc_t0_t4 += MM[0]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 61
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 61
	c_bc_t4_t0_mem0 += MAS_MEM[0]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 61
	c_bc_t4_t0_mem1 += MAS_MEM[1]

	c_pbc_t30 = S.Task('c_pbc_t30', length=3, delay_cost=1)
	S += c_pbc_t30 >= 61
	c_pbc_t30 += MAS[0]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 61
	c_pbc_t31_in += MAS_in[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 61
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 61
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 62
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 62
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 62
	c_ac_t4_t1_mem1 += MAS_MEM[7]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=14, delay_cost=1)
	S += c_bc_t4_t0 >= 62
	c_bc_t4_t0 += MM[0]

	c_pbc_t31 = S.Task('c_pbc_t31', length=3, delay_cost=1)
	S += c_pbc_t31 >= 62
	c_pbc_t31 += MAS[0]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 62
	c_pcb_t1_t3_in += MAS_in[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 62
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 62
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=14, delay_cost=1)
	S += c_ac_t4_t1 >= 63
	c_ac_t4_t1 += MM[0]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 63
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 63
	c_ac_t4_t4_mem0 += MAS_MEM[4]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 63
	c_ac_t4_t4_mem1 += MAS_MEM[7]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 63
	c_pbc_t0_t3_in += MAS_in[0]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 63
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 63
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=3, delay_cost=1)
	S += c_pcb_t1_t3 >= 63
	c_pcb_t1_t3 += MAS[0]

	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	S += c_ab_t11_in >= 64
	c_ab_t11_in += MAS_in[2]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 64
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 64
	c_ab_t11_mem1 += MAS_MEM[7]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=14, delay_cost=1)
	S += c_ac_t4_t4 >= 64
	c_ac_t4_t4 += MM[0]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=3, delay_cost=1)
	S += c_pbc_t0_t3 >= 64
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 64
	c_pbc_t4_t3_in += MAS_in[3]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 64
	c_pbc_t4_t3_mem0 += MAS_MEM[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 64
	c_pbc_t4_t3_mem1 += MAS_MEM[1]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 64
	c_pcb_t0_t3_in += MAS_in[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 64
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 64
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t11 = S.Task('c_ab_t11', length=3, delay_cost=1)
	S += c_ab_t11 >= 65
	c_ab_t11 += MAS[2]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 65
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 65
	c_bc_t4_t4_mem0 += MAS_MEM[6]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 65
	c_bc_t4_t4_mem1 += MAS_MEM[7]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 65
	c_pbc_t1_t3_in += MAS_in[0]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 65
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 65
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=3, delay_cost=1)
	S += c_pbc_t4_t3 >= 65
	c_pbc_t4_t3 += MAS[3]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=3, delay_cost=1)
	S += c_pcb_t0_t3 >= 65
	c_pcb_t0_t3 += MAS[0]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=14, delay_cost=1)
	S += c_bc_t4_t4 >= 66
	c_bc_t4_t4 += MM[0]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 66
	c_paa_t31_in += MAS_in[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 66
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=3, delay_cost=1)
	S += c_pbc_t1_t3 >= 66
	c_pbc_t1_t3 += MAS[0]

	c_ab_s01_in = S.Task('c_ab_s01_in', length=1, delay_cost=1)
	S += c_ab_s01_in >= 67
	c_ab_s01_in += MAS_in[2]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 67
	c_ab_s01_mem0 += MAS_MEM[4]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 67
	c_ab_s01_mem1 += MAS_MEM[7]

	c_ab_t51_in = S.Task('c_ab_t51_in', length=1, delay_cost=1)
	S += c_ab_t51_in >= 67
	c_ab_t51_in += MAS_in[0]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 67
	c_ab_t51_mem0 += MAS_MEM[6]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 67
	c_ab_t51_mem1 += MAS_MEM[5]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 67
	c_bc_t00_in += MAS_in[4]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 67
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 67
	c_bc_t00_mem1 += MM_MEM[1]

	c_paa_t31 = S.Task('c_paa_t31', length=3, delay_cost=1)
	S += c_paa_t31 >= 67
	c_paa_t31 += MAS[0]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 67
	c_pcb_t31_in += MAS_in[3]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 67
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 67
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_ab_s00_in = S.Task('c_ab_s00_in', length=1, delay_cost=1)
	S += c_ab_s00_in >= 68
	c_ab_s00_in += MAS_in[1]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 68
	c_ab_s00_mem0 += MAS_MEM[6]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 68
	c_ab_s00_mem1 += MAS_MEM[5]

	c_ab_s01 = S.Task('c_ab_s01', length=3, delay_cost=1)
	S += c_ab_s01 >= 68
	c_ab_s01 += MAS[2]

	c_ab_t51 = S.Task('c_ab_t51', length=3, delay_cost=1)
	S += c_ab_t51 >= 68
	c_ab_t51 += MAS[0]

	c_bc_t00 = S.Task('c_bc_t00', length=3, delay_cost=1)
	S += c_bc_t00 >= 68
	c_bc_t00 += MAS[4]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 68
	c_bc_t0_t5_in += MAS_in[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 68
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 68
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 68
	c_paa_t0_t3_in += MAS_in[2]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 68
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 68
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=3, delay_cost=1)
	S += c_pcb_t31 >= 68
	c_pcb_t31 += MAS[3]

	c_ab_s00 = S.Task('c_ab_s00', length=3, delay_cost=1)
	S += c_ab_s00 >= 69
	c_ab_s00 += MAS[1]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 69
	c_ac_t10_in += MAS_in[1]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 69
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 69
	c_ac_t10_mem1 += MM_MEM[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=3, delay_cost=1)
	S += c_bc_t0_t5 >= 69
	c_bc_t0_t5 += MAS[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=3, delay_cost=1)
	S += c_paa_t0_t3 >= 69
	c_paa_t0_t3 += MAS[2]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 69
	c_pcb_t30_in += MAS_in[2]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 69
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 69
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t10 = S.Task('c_ac_t10', length=3, delay_cost=1)
	S += c_ac_t10 >= 70
	c_ac_t10 += MAS[1]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 70
	c_ac_t1_t5_in += MAS_in[3]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 70
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 70
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 70
	c_paa_t1_t3_in += MAS_in[2]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 70
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 70
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=3, delay_cost=1)
	S += c_pcb_t30 >= 70
	c_pcb_t30 += MAS[2]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 71
	c_ac_t00_in += MAS_in[1]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 71
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 71
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=3, delay_cost=1)
	S += c_ac_t1_t5 >= 71
	c_ac_t1_t5 += MAS[3]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=3, delay_cost=1)
	S += c_paa_t1_t3 >= 71
	c_paa_t1_t3 += MAS[2]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 71
	c_paa_t30_in += MAS_in[3]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 71
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 71
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 72
	c_aa_t00_in += MAS_in[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 72
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 72
	c_aa_t00_mem1 += MAS_MEM[3]

	c_ac_t00 = S.Task('c_ac_t00', length=3, delay_cost=1)
	S += c_ac_t00 >= 72
	c_ac_t00 += MAS[1]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 72
	c_ac_t0_t5_in += MAS_in[3]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 72
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 72
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_paa_t30 = S.Task('c_paa_t30', length=3, delay_cost=1)
	S += c_paa_t30 >= 72
	c_paa_t30 += MAS[3]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 72
	c_pcb_t4_t3_in += MAS_in[2]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 72
	c_pcb_t4_t3_mem0 += MAS_MEM[4]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 72
	c_pcb_t4_t3_mem1 += MAS_MEM[7]

	c_aa_t00 = S.Task('c_aa_t00', length=3, delay_cost=1)
	S += c_aa_t00 >= 73
	c_aa_t00 += MAS[0]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 73
	c_aa_t01_in += MAS_in[2]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 73
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 73
	c_aa_t01_mem1 += MAS_MEM[5]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=3, delay_cost=1)
	S += c_ac_t0_t5 >= 73
	c_ac_t0_t5 += MAS[3]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 73
	c_bc_t10_in += MAS_in[3]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 73
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 73
	c_bc_t10_mem1 += MM_MEM[1]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=3, delay_cost=1)
	S += c_pcb_t4_t3 >= 73
	c_pcb_t4_t3 += MAS[2]

	c_aa_t01 = S.Task('c_aa_t01', length=3, delay_cost=1)
	S += c_aa_t01 >= 74
	c_aa_t01 += MAS[2]

	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	S += c_ac_t50_in >= 74
	c_ac_t50_in += MAS_in[3]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 74
	c_ac_t50_mem0 += MAS_MEM[2]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 74
	c_ac_t50_mem1 += MAS_MEM[3]

	c_bc_t10 = S.Task('c_bc_t10', length=3, delay_cost=1)
	S += c_bc_t10 >= 74
	c_bc_t10 += MAS[3]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 74
	c_bc_t1_t5_in += MAS_in[2]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 74
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 74
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 74
	c_cc_t01_in += MAS_in[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 74
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 74
	c_cc_t01_mem1 += MAS_MEM[9]

	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	S += c_paa_t4_t3_in >= 74
	c_paa_t4_t3_in += MAS_in[1]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 74
	c_paa_t4_t3_mem0 += MAS_MEM[6]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 74
	c_paa_t4_t3_mem1 += MAS_MEM[1]

	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	S += c_ac_t01_in >= 75
	c_ac_t01_in += MAS_in[1]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 75
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 75
	c_ac_t01_mem1 += MAS_MEM[7]

	c_ac_t50 = S.Task('c_ac_t50', length=3, delay_cost=1)
	S += c_ac_t50 >= 75
	c_ac_t50 += MAS[3]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=3, delay_cost=1)
	S += c_bc_t1_t5 >= 75
	c_bc_t1_t5 += MAS[2]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 75
	c_cc_t00_in += MAS_in[0]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 75
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 75
	c_cc_t00_mem1 += MAS_MEM[1]

	c_cc_t01 = S.Task('c_cc_t01', length=3, delay_cost=1)
	S += c_cc_t01 >= 75
	c_cc_t01 += MAS[0]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=3, delay_cost=1)
	S += c_paa_t4_t3 >= 75
	c_paa_t4_t3 += MAS[1]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 76
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 76
	c_aa_t2_t0_mem0 += MAS_MEM[0]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 76
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_ac_t01 = S.Task('c_ac_t01', length=3, delay_cost=1)
	S += c_ac_t01 >= 76
	c_ac_t01 += MAS[1]

	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	S += c_ac_t4_t5_in >= 76
	c_ac_t4_t5_in += MAS_in[3]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 76
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 76
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 76
	c_bb_t00_in += MAS_in[4]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 76
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 76
	c_bb_t00_mem1 += MAS_MEM[9]

	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	S += c_bc_t50_in >= 76
	c_bc_t50_in += MAS_in[1]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 76
	c_bc_t50_mem0 += MAS_MEM[8]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 76
	c_bc_t50_mem1 += MAS_MEM[7]

	c_cc_t00 = S.Task('c_cc_t00', length=3, delay_cost=1)
	S += c_cc_t00 >= 76
	c_cc_t00 += MAS[0]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=14, delay_cost=1)
	S += c_aa_t2_t0 >= 77
	c_aa_t2_t0 += MM[0]

	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	S += c_ac_t11_in >= 77
	c_ac_t11_in += MAS_in[3]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 77
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 77
	c_ac_t11_mem1 += MAS_MEM[7]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=3, delay_cost=1)
	S += c_ac_t4_t5 >= 77
	c_ac_t4_t5 += MAS[3]

	c_bb_t00 = S.Task('c_bb_t00', length=3, delay_cost=1)
	S += c_bb_t00 >= 77
	c_bb_t00 += MAS[4]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 77
	c_bb_t01_in += MAS_in[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 77
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 77
	c_bb_t01_mem1 += MAS_MEM[9]

	c_bc_t50 = S.Task('c_bc_t50', length=3, delay_cost=1)
	S += c_bc_t50 >= 77
	c_bc_t50 += MAS[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 77
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 77
	c_cc_t2_t1_mem0 += MAS_MEM[0]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 77
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 78
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 78
	c_aa_t2_t1_mem0 += MAS_MEM[4]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 78
	c_aa_t2_t1_mem1 += MAS_MEM[9]

	c_ac_t11 = S.Task('c_ac_t11', length=3, delay_cost=1)
	S += c_ac_t11 >= 78
	c_ac_t11 += MAS[3]

	c_bb_t01 = S.Task('c_bb_t01', length=3, delay_cost=1)
	S += c_bb_t01 >= 78
	c_bb_t01 += MAS[1]

	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	S += c_bc_t40_in >= 78
	c_bc_t40_in += MAS_in[2]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 78
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 78
	c_bc_t40_mem1 += MM_MEM[1]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=14, delay_cost=1)
	S += c_cc_t2_t1 >= 78
	c_cc_t2_t1 += MM[0]

	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	S += c_cc_t2_t2_in >= 78
	c_cc_t2_t2_in += MAS_in[3]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 78
	c_cc_t2_t2_mem0 += MAS_MEM[0]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 78
	c_cc_t2_t2_mem1 += MAS_MEM[1]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=14, delay_cost=1)
	S += c_aa_t2_t1 >= 79
	c_aa_t2_t1 += MM[0]

	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	S += c_aa_t2_t2_in >= 79
	c_aa_t2_t2_in += MAS_in[0]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 79
	c_aa_t2_t2_mem0 += MAS_MEM[0]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 79
	c_aa_t2_t2_mem1 += MAS_MEM[5]

	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	S += c_ac_t40_in >= 79
	c_ac_t40_in += MAS_in[1]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 79
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 79
	c_ac_t40_mem1 += MM_MEM[1]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 79
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 79
	c_bb_t2_t0_mem0 += MAS_MEM[8]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 79
	c_bb_t2_t0_mem1 += MAS_MEM[1]

	c_bc_t40 = S.Task('c_bc_t40', length=3, delay_cost=1)
	S += c_bc_t40 >= 79
	c_bc_t40 += MAS[2]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=3, delay_cost=1)
	S += c_cc_t2_t2 >= 79
	c_cc_t2_t2 += MAS[3]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=3, delay_cost=1)
	S += c_aa_t2_t2 >= 80
	c_aa_t2_t2 += MAS[0]

	c_ac_s00_in = S.Task('c_ac_s00_in', length=1, delay_cost=1)
	S += c_ac_s00_in >= 80
	c_ac_s00_in += MAS_in[1]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 80
	c_ac_s00_mem0 += MAS_MEM[2]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 80
	c_ac_s00_mem1 += MAS_MEM[7]

	c_ac_t40 = S.Task('c_ac_t40', length=3, delay_cost=1)
	S += c_ac_t40 >= 80
	c_ac_t40 += MAS[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=14, delay_cost=1)
	S += c_bb_t2_t0 >= 80
	c_bb_t2_t0 += MM[0]

	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	S += c_bb_t2_t2_in >= 80
	c_bb_t2_t2_in += MAS_in[3]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 80
	c_bb_t2_t2_mem0 += MAS_MEM[8]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 80
	c_bb_t2_t2_mem1 += MAS_MEM[3]

	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	S += c_bc_t4_t5_in >= 80
	c_bc_t4_t5_in += MAS_in[2]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 80
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 80
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 80
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 80
	c_cc_t2_t0_mem0 += MAS_MEM[0]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 80
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_ac_s00 = S.Task('c_ac_s00', length=3, delay_cost=1)
	S += c_ac_s00 >= 81
	c_ac_s00 += MAS[1]

	c_ac_s01_in = S.Task('c_ac_s01_in', length=1, delay_cost=1)
	S += c_ac_s01_in >= 81
	c_ac_s01_in += MAS_in[3]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 81
	c_ac_s01_mem0 += MAS_MEM[6]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 81
	c_ac_s01_mem1 += MAS_MEM[3]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 81
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 81
	c_bb_t2_t1_mem0 += MAS_MEM[2]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 81
	c_bb_t2_t1_mem1 += MAS_MEM[7]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=3, delay_cost=1)
	S += c_bb_t2_t2 >= 81
	c_bb_t2_t2 += MAS[3]

	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	S += c_bc_t11_in >= 81
	c_bc_t11_in += MAS_in[1]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 81
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 81
	c_bc_t11_mem1 += MAS_MEM[5]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=3, delay_cost=1)
	S += c_bc_t4_t5 >= 81
	c_bc_t4_t5 += MAS[2]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=14, delay_cost=1)
	S += c_cc_t2_t0 >= 81
	c_cc_t2_t0 += MM[0]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 82
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 82
	c_aa_t2_t4_mem0 += MAS_MEM[0]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 82
	c_aa_t2_t4_mem1 += MAS_MEM[5]

	c_ac10_in = S.Task('c_ac10_in', length=1, delay_cost=1)
	S += c_ac10_in >= 82
	c_ac10_in += MAS_in[3]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 82
	c_ac10_mem0 += MAS_MEM[2]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 82
	c_ac10_mem1 += MAS_MEM[7]

	c_ac_s01 = S.Task('c_ac_s01', length=3, delay_cost=1)
	S += c_ac_s01 >= 82
	c_ac_s01 += MAS[3]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=14, delay_cost=1)
	S += c_bb_t2_t1 >= 82
	c_bb_t2_t1 += MM[0]

	c_bc10_in = S.Task('c_bc10_in', length=1, delay_cost=1)
	S += c_bc10_in >= 82
	c_bc10_in += MAS_in[0]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 82
	c_bc10_mem0 += MAS_MEM[4]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 82
	c_bc10_mem1 += MAS_MEM[3]

	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	S += c_bc_t01_in >= 82
	c_bc_t01_in += MAS_in[1]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 82
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 82
	c_bc_t01_mem1 += MAS_MEM[1]

	c_bc_t11 = S.Task('c_bc_t11', length=3, delay_cost=1)
	S += c_bc_t11 >= 82
	c_bc_t11 += MAS[1]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=14, delay_cost=1)
	S += c_aa_t2_t4 >= 83
	c_aa_t2_t4 += MM[0]

	c_ac10 = S.Task('c_ac10', length=3, delay_cost=1)
	S += c_ac10 >= 83
	c_ac10 += MAS[3]

	c_ac_t51_in = S.Task('c_ac_t51_in', length=1, delay_cost=1)
	S += c_ac_t51_in >= 83
	c_ac_t51_in += MAS_in[2]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 83
	c_ac_t51_mem0 += MAS_MEM[2]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 83
	c_ac_t51_mem1 += MAS_MEM[7]

	c_bc10 = S.Task('c_bc10', length=3, delay_cost=1)
	S += c_bc10 >= 83
	c_bc10 += MAS[0]

	c_bc_t01 = S.Task('c_bc_t01', length=3, delay_cost=1)
	S += c_bc_t01 >= 83
	c_bc_t01 += MAS[1]

	c_bc_t41_in = S.Task('c_bc_t41_in', length=1, delay_cost=1)
	S += c_bc_t41_in >= 83
	c_bc_t41_in += MAS_in[3]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 83
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 83
	c_bc_t41_mem1 += MAS_MEM[5]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 83
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 83
	c_cc_t2_t4_mem0 += MAS_MEM[6]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 83
	c_cc_t2_t4_mem1 += MAS_MEM[3]

	c_ac_t51 = S.Task('c_ac_t51', length=3, delay_cost=1)
	S += c_ac_t51 >= 84
	c_ac_t51 += MAS[2]

	c_bc_s00_in = S.Task('c_bc_s00_in', length=1, delay_cost=1)
	S += c_bc_s00_in >= 84
	c_bc_s00_in += MAS_in[2]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 84
	c_bc_s00_mem0 += MAS_MEM[6]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 84
	c_bc_s00_mem1 += MAS_MEM[3]

	c_bc_s01_in = S.Task('c_bc_s01_in', length=1, delay_cost=1)
	S += c_bc_s01_in >= 84
	c_bc_s01_in += MAS_in[3]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 84
	c_bc_s01_mem0 += MAS_MEM[2]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 84
	c_bc_s01_mem1 += MAS_MEM[7]

	c_bc_t41 = S.Task('c_bc_t41', length=3, delay_cost=1)
	S += c_bc_t41 >= 84
	c_bc_t41 += MAS[3]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=14, delay_cost=1)
	S += c_cc_t2_t4 >= 84
	c_cc_t2_t4 += MM[0]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 85
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 85
	c_bb_t2_t4_mem0 += MAS_MEM[6]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 85
	c_bb_t2_t4_mem1 += MAS_MEM[7]

	c_bc_s00 = S.Task('c_bc_s00', length=3, delay_cost=1)
	S += c_bc_s00 >= 85
	c_bc_s00 += MAS[2]

	c_bc_s01 = S.Task('c_bc_s01', length=3, delay_cost=1)
	S += c_bc_s01 >= 85
	c_bc_s01 += MAS[3]

	c_bc_t51_in = S.Task('c_bc_t51_in', length=1, delay_cost=1)
	S += c_bc_t51_in >= 85
	c_bc_t51_in += MAS_in[3]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 85
	c_bc_t51_mem0 += MAS_MEM[2]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 85
	c_bc_t51_mem1 += MAS_MEM[3]

	c_ac_t41_in = S.Task('c_ac_t41_in', length=1, delay_cost=1)
	S += c_ac_t41_in >= 86
	c_ac_t41_in += MAS_in[1]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 86
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 86
	c_ac_t41_mem1 += MAS_MEM[7]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=14, delay_cost=1)
	S += c_bb_t2_t4 >= 86
	c_bb_t2_t4 += MM[0]

	c_bc_t51 = S.Task('c_bc_t51', length=3, delay_cost=1)
	S += c_bc_t51 >= 86
	c_bc_t51 += MAS[3]

	c_ac_t41 = S.Task('c_ac_t41', length=3, delay_cost=1)
	S += c_ac_t41 >= 87
	c_ac_t41 += MAS[1]

	c_aa_t20_in = S.Task('c_aa_t20_in', length=1, delay_cost=1)
	S += c_aa_t20_in >= 92
	c_aa_t20_in += MAS_in[4]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 92
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 92
	c_aa_t20_mem1 += MM_MEM[1]

	c_aa_t20 = S.Task('c_aa_t20', length=3, delay_cost=1)
	S += c_aa_t20 >= 93
	c_aa_t20 += MAS[4]

	c_aa_t2_t5_in = S.Task('c_aa_t2_t5_in', length=1, delay_cost=1)
	S += c_aa_t2_t5_in >= 93
	c_aa_t2_t5_in += MAS_in[4]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 93
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 93
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=3, delay_cost=1)
	S += c_aa_t2_t5 >= 94
	c_aa_t2_t5 += MAS[4]

	c_cc_t20_in = S.Task('c_cc_t20_in', length=1, delay_cost=1)
	S += c_cc_t20_in >= 94
	c_cc_t20_in += MAS_in[1]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 94
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 94
	c_cc_t20_mem1 += MM_MEM[1]

	c_bb_t20_in = S.Task('c_bb_t20_in', length=1, delay_cost=1)
	S += c_bb_t20_in >= 95
	c_bb_t20_in += MAS_in[4]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 95
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 95
	c_bb_t20_mem1 += MM_MEM[1]

	c_cc_t20 = S.Task('c_cc_t20', length=3, delay_cost=1)
	S += c_cc_t20 >= 95
	c_cc_t20 += MAS[1]

	c_bb_t20 = S.Task('c_bb_t20', length=3, delay_cost=1)
	S += c_bb_t20 >= 96
	c_bb_t20 += MAS[4]

	c_bb_t2_t5_in = S.Task('c_bb_t2_t5_in', length=1, delay_cost=1)
	S += c_bb_t2_t5_in >= 96
	c_bb_t2_t5_in += MAS_in[4]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 96
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 96
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=3, delay_cost=1)
	S += c_bb_t2_t5 >= 97
	c_bb_t2_t5 += MAS[4]

	c_cc_t2_t5_in = S.Task('c_cc_t2_t5_in', length=1, delay_cost=1)
	S += c_cc_t2_t5_in >= 97
	c_cc_t2_t5_in += MAS_in[1]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 97
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 97
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=3, delay_cost=1)
	S += c_cc_t2_t5 >= 98
	c_cc_t2_t5 += MAS[1]


	# new tasks
	c_aa_t21 = S.Task('c_aa_t21', length=3, delay_cost=1)
	c_aa_t21 += alt(MAS)
	c_aa_t21_in = S.Task('c_aa_t21_in', length=1, delay_cost=1)
	c_aa_t21_in += alt(MAS_in)
	S += c_aa_t21_in*MAS_in[0]<=c_aa_t21*MAS[0]

	S += c_aa_t21_in*MAS_in[1]<=c_aa_t21*MAS[1]

	S += c_aa_t21_in*MAS_in[2]<=c_aa_t21*MAS[2]

	S += c_aa_t21_in*MAS_in[3]<=c_aa_t21*MAS[3]

	S += c_aa_t21_in*MAS_in[4]<=c_aa_t21*MAS[4]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	c_aa_t21_mem0 += MM_MEM[0]
	S += 96 < c_aa_t21_mem0
	S += c_aa_t21_mem0 <= c_aa_t21

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	c_aa_t21_mem1 += MAS_MEM[9]
	S += 96 < c_aa_t21_mem1
	S += c_aa_t21_mem1 <= c_aa_t21

	c_aa_t50 = S.Task('c_aa_t50', length=3, delay_cost=1)
	c_aa_t50 += alt(MAS)
	c_aa_t50_in = S.Task('c_aa_t50_in', length=1, delay_cost=1)
	c_aa_t50_in += alt(MAS_in)
	S += c_aa_t50_in*MAS_in[0]<=c_aa_t50*MAS[0]

	S += c_aa_t50_in*MAS_in[1]<=c_aa_t50*MAS[1]

	S += c_aa_t50_in*MAS_in[2]<=c_aa_t50*MAS[2]

	S += c_aa_t50_in*MAS_in[3]<=c_aa_t50*MAS[3]

	S += c_aa_t50_in*MAS_in[4]<=c_aa_t50*MAS[4]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	c_aa_t50_mem0 += MAS_MEM[4]
	S += 27 < c_aa_t50_mem0
	S += c_aa_t50_mem0 <= c_aa_t50

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	c_aa_t50_mem1 += MAS_MEM[1]
	S += 32 < c_aa_t50_mem1
	S += c_aa_t50_mem1 <= c_aa_t50

	c_aa_t51 = S.Task('c_aa_t51', length=3, delay_cost=1)
	c_aa_t51 += alt(MAS)
	c_aa_t51_in = S.Task('c_aa_t51_in', length=1, delay_cost=1)
	c_aa_t51_in += alt(MAS_in)
	S += c_aa_t51_in*MAS_in[0]<=c_aa_t51*MAS[0]

	S += c_aa_t51_in*MAS_in[1]<=c_aa_t51*MAS[1]

	S += c_aa_t51_in*MAS_in[2]<=c_aa_t51*MAS[2]

	S += c_aa_t51_in*MAS_in[3]<=c_aa_t51*MAS[3]

	S += c_aa_t51_in*MAS_in[4]<=c_aa_t51*MAS[4]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	c_aa_t51_mem0 += MAS_MEM[6]
	S += 29 < c_aa_t51_mem0
	S += c_aa_t51_mem0 <= c_aa_t51

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	c_aa_t51_mem1 += MAS_MEM[7]
	S += 32 < c_aa_t51_mem1
	S += c_aa_t51_mem1 <= c_aa_t51

	c_bb_t21 = S.Task('c_bb_t21', length=3, delay_cost=1)
	c_bb_t21 += alt(MAS)
	c_bb_t21_in = S.Task('c_bb_t21_in', length=1, delay_cost=1)
	c_bb_t21_in += alt(MAS_in)
	S += c_bb_t21_in*MAS_in[0]<=c_bb_t21*MAS[0]

	S += c_bb_t21_in*MAS_in[1]<=c_bb_t21*MAS[1]

	S += c_bb_t21_in*MAS_in[2]<=c_bb_t21*MAS[2]

	S += c_bb_t21_in*MAS_in[3]<=c_bb_t21*MAS[3]

	S += c_bb_t21_in*MAS_in[4]<=c_bb_t21*MAS[4]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	c_bb_t21_mem0 += MM_MEM[0]
	S += 99 < c_bb_t21_mem0
	S += c_bb_t21_mem0 <= c_bb_t21

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	c_bb_t21_mem1 += MAS_MEM[9]
	S += 99 < c_bb_t21_mem1
	S += c_bb_t21_mem1 <= c_bb_t21

	c_bb_t50 = S.Task('c_bb_t50', length=3, delay_cost=1)
	c_bb_t50 += alt(MAS)
	c_bb_t50_in = S.Task('c_bb_t50_in', length=1, delay_cost=1)
	c_bb_t50_in += alt(MAS_in)
	S += c_bb_t50_in*MAS_in[0]<=c_bb_t50*MAS[0]

	S += c_bb_t50_in*MAS_in[1]<=c_bb_t50*MAS[1]

	S += c_bb_t50_in*MAS_in[2]<=c_bb_t50*MAS[2]

	S += c_bb_t50_in*MAS_in[3]<=c_bb_t50*MAS[3]

	S += c_bb_t50_in*MAS_in[4]<=c_bb_t50*MAS[4]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	c_bb_t50_mem0 += MAS_MEM[8]
	S += 47 < c_bb_t50_mem0
	S += c_bb_t50_mem0 <= c_bb_t50

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	c_bb_t50_mem1 += MAS_MEM[3]
	S += 53 < c_bb_t50_mem1
	S += c_bb_t50_mem1 <= c_bb_t50

	c_bb_t51 = S.Task('c_bb_t51', length=3, delay_cost=1)
	c_bb_t51 += alt(MAS)
	c_bb_t51_in = S.Task('c_bb_t51_in', length=1, delay_cost=1)
	c_bb_t51_in += alt(MAS_in)
	S += c_bb_t51_in*MAS_in[0]<=c_bb_t51*MAS[0]

	S += c_bb_t51_in*MAS_in[1]<=c_bb_t51*MAS[1]

	S += c_bb_t51_in*MAS_in[2]<=c_bb_t51*MAS[2]

	S += c_bb_t51_in*MAS_in[3]<=c_bb_t51*MAS[3]

	S += c_bb_t51_in*MAS_in[4]<=c_bb_t51*MAS[4]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	c_bb_t51_mem0 += MAS_MEM[2]
	S += 50 < c_bb_t51_mem0
	S += c_bb_t51_mem0 <= c_bb_t51

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	c_bb_t51_mem1 += MAS_MEM[1]
	S += 53 < c_bb_t51_mem1
	S += c_bb_t51_mem1 <= c_bb_t51

	c_cc_t21 = S.Task('c_cc_t21', length=3, delay_cost=1)
	c_cc_t21 += alt(MAS)
	c_cc_t21_in = S.Task('c_cc_t21_in', length=1, delay_cost=1)
	c_cc_t21_in += alt(MAS_in)
	S += c_cc_t21_in*MAS_in[0]<=c_cc_t21*MAS[0]

	S += c_cc_t21_in*MAS_in[1]<=c_cc_t21*MAS[1]

	S += c_cc_t21_in*MAS_in[2]<=c_cc_t21*MAS[2]

	S += c_cc_t21_in*MAS_in[3]<=c_cc_t21*MAS[3]

	S += c_cc_t21_in*MAS_in[4]<=c_cc_t21*MAS[4]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	c_cc_t21_mem0 += MM_MEM[0]
	S += 97 < c_cc_t21_mem0
	S += c_cc_t21_mem0 <= c_cc_t21

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	c_cc_t21_mem1 += MAS_MEM[3]
	S += 100 < c_cc_t21_mem1
	S += c_cc_t21_mem1 <= c_cc_t21

	c_cc_t50 = S.Task('c_cc_t50', length=3, delay_cost=1)
	c_cc_t50 += alt(MAS)
	c_cc_t50_in = S.Task('c_cc_t50_in', length=1, delay_cost=1)
	c_cc_t50_in += alt(MAS_in)
	S += c_cc_t50_in*MAS_in[0]<=c_cc_t50*MAS[0]

	S += c_cc_t50_in*MAS_in[1]<=c_cc_t50*MAS[1]

	S += c_cc_t50_in*MAS_in[2]<=c_cc_t50*MAS[2]

	S += c_cc_t50_in*MAS_in[3]<=c_cc_t50*MAS[3]

	S += c_cc_t50_in*MAS_in[4]<=c_cc_t50*MAS[4]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	c_cc_t50_mem0 += MAS_MEM[2]
	S += 45 < c_cc_t50_mem0
	S += c_cc_t50_mem0 <= c_cc_t50

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	c_cc_t50_mem1 += MAS_MEM[3]
	S += 56 < c_cc_t50_mem1
	S += c_cc_t50_mem1 <= c_cc_t50

	c_cc_t51 = S.Task('c_cc_t51', length=3, delay_cost=1)
	c_cc_t51 += alt(MAS)
	c_cc_t51_in = S.Task('c_cc_t51_in', length=1, delay_cost=1)
	c_cc_t51_in += alt(MAS_in)
	S += c_cc_t51_in*MAS_in[0]<=c_cc_t51*MAS[0]

	S += c_cc_t51_in*MAS_in[1]<=c_cc_t51*MAS[1]

	S += c_cc_t51_in*MAS_in[2]<=c_cc_t51*MAS[2]

	S += c_cc_t51_in*MAS_in[3]<=c_cc_t51*MAS[3]

	S += c_cc_t51_in*MAS_in[4]<=c_cc_t51*MAS[4]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	c_cc_t51_mem0 += MAS_MEM[0]
	S += 49 < c_cc_t51_mem0
	S += c_cc_t51_mem0 <= c_cc_t51

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	c_cc_t51_mem1 += MAS_MEM[7]
	S += 52 < c_cc_t51_mem1
	S += c_cc_t51_mem1 <= c_cc_t51

	c_ab00 = S.Task('c_ab00', length=3, delay_cost=1)
	c_ab00 += alt(MAS)
	c_ab00_in = S.Task('c_ab00_in', length=1, delay_cost=1)
	c_ab00_in += alt(MAS_in)
	S += c_ab00_in*MAS_in[0]<=c_ab00*MAS[0]

	S += c_ab00_in*MAS_in[1]<=c_ab00*MAS[1]

	S += c_ab00_in*MAS_in[2]<=c_ab00*MAS[2]

	S += c_ab00_in*MAS_in[3]<=c_ab00*MAS[3]

	S += c_ab00_in*MAS_in[4]<=c_ab00*MAS[4]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	c_ab00_mem0 += MAS_MEM[6]
	S += 41 < c_ab00_mem0
	S += c_ab00_mem0 <= c_ab00

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	c_ab00_mem1 += MAS_MEM[3]
	S += 71 < c_ab00_mem1
	S += c_ab00_mem1 <= c_ab00

	c_ab01 = S.Task('c_ab01', length=3, delay_cost=1)
	c_ab01 += alt(MAS)
	c_ab01_in = S.Task('c_ab01_in', length=1, delay_cost=1)
	c_ab01_in += alt(MAS_in)
	S += c_ab01_in*MAS_in[0]<=c_ab01*MAS[0]

	S += c_ab01_in*MAS_in[1]<=c_ab01*MAS[1]

	S += c_ab01_in*MAS_in[2]<=c_ab01*MAS[2]

	S += c_ab01_in*MAS_in[3]<=c_ab01*MAS[3]

	S += c_ab01_in*MAS_in[4]<=c_ab01*MAS[4]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	c_ab01_mem0 += MAS_MEM[6]
	S += 55 < c_ab01_mem0
	S += c_ab01_mem0 <= c_ab01

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	c_ab01_mem1 += MAS_MEM[5]
	S += 70 < c_ab01_mem1
	S += c_ab01_mem1 <= c_ab01

	c_ab11 = S.Task('c_ab11', length=3, delay_cost=1)
	c_ab11 += alt(MAS)
	c_ab11_in = S.Task('c_ab11_in', length=1, delay_cost=1)
	c_ab11_in += alt(MAS_in)
	S += c_ab11_in*MAS_in[0]<=c_ab11*MAS[0]

	S += c_ab11_in*MAS_in[1]<=c_ab11*MAS[1]

	S += c_ab11_in*MAS_in[2]<=c_ab11*MAS[2]

	S += c_ab11_in*MAS_in[3]<=c_ab11*MAS[3]

	S += c_ab11_in*MAS_in[4]<=c_ab11*MAS[4]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	c_ab11_mem0 += MAS_MEM[2]
	S += 57 < c_ab11_mem0
	S += c_ab11_mem0 <= c_ab11

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	c_ab11_mem1 += MAS_MEM[1]
	S += 70 < c_ab11_mem1
	S += c_ab11_mem1 <= c_ab11

	c_bc00 = S.Task('c_bc00', length=3, delay_cost=1)
	c_bc00 += alt(MAS)
	c_bc00_in = S.Task('c_bc00_in', length=1, delay_cost=1)
	c_bc00_in += alt(MAS_in)
	S += c_bc00_in*MAS_in[0]<=c_bc00*MAS[0]

	S += c_bc00_in*MAS_in[1]<=c_bc00*MAS[1]

	S += c_bc00_in*MAS_in[2]<=c_bc00*MAS[2]

	S += c_bc00_in*MAS_in[3]<=c_bc00*MAS[3]

	S += c_bc00_in*MAS_in[4]<=c_bc00*MAS[4]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	c_bc00_mem0 += MAS_MEM[8]
	S += 70 < c_bc00_mem0
	S += c_bc00_mem0 <= c_bc00

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	c_bc00_mem1 += MAS_MEM[5]
	S += 87 < c_bc00_mem1
	S += c_bc00_mem1 <= c_bc00

	c_bc01 = S.Task('c_bc01', length=3, delay_cost=1)
	c_bc01 += alt(MAS)
	c_bc01_in = S.Task('c_bc01_in', length=1, delay_cost=1)
	c_bc01_in += alt(MAS_in)
	S += c_bc01_in*MAS_in[0]<=c_bc01*MAS[0]

	S += c_bc01_in*MAS_in[1]<=c_bc01*MAS[1]

	S += c_bc01_in*MAS_in[2]<=c_bc01*MAS[2]

	S += c_bc01_in*MAS_in[3]<=c_bc01*MAS[3]

	S += c_bc01_in*MAS_in[4]<=c_bc01*MAS[4]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	c_bc01_mem0 += MAS_MEM[2]
	S += 85 < c_bc01_mem0
	S += c_bc01_mem0 <= c_bc01

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	c_bc01_mem1 += MAS_MEM[7]
	S += 87 < c_bc01_mem1
	S += c_bc01_mem1 <= c_bc01

	c_bc11 = S.Task('c_bc11', length=3, delay_cost=1)
	c_bc11 += alt(MAS)
	c_bc11_in = S.Task('c_bc11_in', length=1, delay_cost=1)
	c_bc11_in += alt(MAS_in)
	S += c_bc11_in*MAS_in[0]<=c_bc11*MAS[0]

	S += c_bc11_in*MAS_in[1]<=c_bc11*MAS[1]

	S += c_bc11_in*MAS_in[2]<=c_bc11*MAS[2]

	S += c_bc11_in*MAS_in[3]<=c_bc11*MAS[3]

	S += c_bc11_in*MAS_in[4]<=c_bc11*MAS[4]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	c_bc11_mem0 += MAS_MEM[6]
	S += 86 < c_bc11_mem0
	S += c_bc11_mem0 <= c_bc11

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	c_bc11_mem1 += MAS_MEM[7]
	S += 88 < c_bc11_mem1
	S += c_bc11_mem1 <= c_bc11

	c_ac00 = S.Task('c_ac00', length=3, delay_cost=1)
	c_ac00 += alt(MAS)
	c_ac00_in = S.Task('c_ac00_in', length=1, delay_cost=1)
	c_ac00_in += alt(MAS_in)
	S += c_ac00_in*MAS_in[0]<=c_ac00*MAS[0]

	S += c_ac00_in*MAS_in[1]<=c_ac00*MAS[1]

	S += c_ac00_in*MAS_in[2]<=c_ac00*MAS[2]

	S += c_ac00_in*MAS_in[3]<=c_ac00*MAS[3]

	S += c_ac00_in*MAS_in[4]<=c_ac00*MAS[4]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	c_ac00_mem0 += MAS_MEM[2]
	S += 74 < c_ac00_mem0
	S += c_ac00_mem0 <= c_ac00

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	c_ac00_mem1 += MAS_MEM[3]
	S += 83 < c_ac00_mem1
	S += c_ac00_mem1 <= c_ac00

	c_ac01 = S.Task('c_ac01', length=3, delay_cost=1)
	c_ac01 += alt(MAS)
	c_ac01_in = S.Task('c_ac01_in', length=1, delay_cost=1)
	c_ac01_in += alt(MAS_in)
	S += c_ac01_in*MAS_in[0]<=c_ac01*MAS[0]

	S += c_ac01_in*MAS_in[1]<=c_ac01*MAS[1]

	S += c_ac01_in*MAS_in[2]<=c_ac01*MAS[2]

	S += c_ac01_in*MAS_in[3]<=c_ac01*MAS[3]

	S += c_ac01_in*MAS_in[4]<=c_ac01*MAS[4]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	c_ac01_mem0 += MAS_MEM[2]
	S += 78 < c_ac01_mem0
	S += c_ac01_mem0 <= c_ac01

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	c_ac01_mem1 += MAS_MEM[7]
	S += 84 < c_ac01_mem1
	S += c_ac01_mem1 <= c_ac01

	c_ac11 = S.Task('c_ac11', length=3, delay_cost=1)
	c_ac11 += alt(MAS)
	c_ac11_in = S.Task('c_ac11_in', length=1, delay_cost=1)
	c_ac11_in += alt(MAS_in)
	S += c_ac11_in*MAS_in[0]<=c_ac11*MAS[0]

	S += c_ac11_in*MAS_in[1]<=c_ac11*MAS[1]

	S += c_ac11_in*MAS_in[2]<=c_ac11*MAS[2]

	S += c_ac11_in*MAS_in[3]<=c_ac11*MAS[3]

	S += c_ac11_in*MAS_in[4]<=c_ac11*MAS[4]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	c_ac11_mem0 += MAS_MEM[2]
	S += 89 < c_ac11_mem0
	S += c_ac11_mem0 <= c_ac11

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	c_ac11_mem1 += MAS_MEM[5]
	S += 86 < c_ac11_mem1
	S += c_ac11_mem1 <= c_ac11

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=3, delay_cost=1)
	c_ccxi_y1_0 += alt(MAS)
	c_ccxi_y1_0_in = S.Task('c_ccxi_y1_0_in', length=1, delay_cost=1)
	c_ccxi_y1_0_in += alt(MAS_in)
	S += c_ccxi_y1_0_in*MAS_in[0]<=c_ccxi_y1_0*MAS[0]

	S += c_ccxi_y1_0_in*MAS_in[1]<=c_ccxi_y1_0*MAS[1]

	S += c_ccxi_y1_0_in*MAS_in[2]<=c_ccxi_y1_0*MAS[2]

	S += c_ccxi_y1_0_in*MAS_in[3]<=c_ccxi_y1_0*MAS[3]

	S += c_ccxi_y1_0_in*MAS_in[4]<=c_ccxi_y1_0*MAS[4]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	c_ccxi_y1_0_mem0 += MAS_MEM[2]
	S += 48 < c_ccxi_y1_0_mem0
	S += c_ccxi_y1_0_mem0 <= c_ccxi_y1_0

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	c_ccxi_y1_0_mem1 += MAS_MEM[9]
	S += 58 < c_ccxi_y1_0_mem1
	S += c_ccxi_y1_0_mem1 <= c_ccxi_y1_0

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=3, delay_cost=1)
	c_ccxi_y1_1 += alt(MAS)
	c_ccxi_y1_1_in = S.Task('c_ccxi_y1_1_in', length=1, delay_cost=1)
	c_ccxi_y1_1_in += alt(MAS_in)
	S += c_ccxi_y1_1_in*MAS_in[0]<=c_ccxi_y1_1*MAS[0]

	S += c_ccxi_y1_1_in*MAS_in[1]<=c_ccxi_y1_1*MAS[1]

	S += c_ccxi_y1_1_in*MAS_in[2]<=c_ccxi_y1_1*MAS[2]

	S += c_ccxi_y1_1_in*MAS_in[3]<=c_ccxi_y1_1*MAS[3]

	S += c_ccxi_y1_1_in*MAS_in[4]<=c_ccxi_y1_1*MAS[4]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	c_ccxi_y1_1_mem0 += MAS_MEM[8]
	S += 58 < c_ccxi_y1_1_mem0
	S += c_ccxi_y1_1_mem0 <= c_ccxi_y1_1

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	c_ccxi_y1_1_mem1 += MAS_MEM[3]
	S += 48 < c_ccxi_y1_1_mem1
	S += c_ccxi_y1_1_mem1 <= c_ccxi_y1_1

	c_pc10 = S.Task('c_pc10', length=3, delay_cost=1)
	c_pc10 += alt(MAS)
	c_pc10_in = S.Task('c_pc10_in', length=1, delay_cost=1)
	c_pc10_in += alt(MAS_in)
	S += c_pc10_in*MAS_in[0]<=c_pc10*MAS[0]

	S += c_pc10_in*MAS_in[1]<=c_pc10*MAS[1]

	S += c_pc10_in*MAS_in[2]<=c_pc10*MAS[2]

	S += c_pc10_in*MAS_in[3]<=c_pc10*MAS[3]

	S += c_pc10_in*MAS_in[4]<=c_pc10*MAS[4]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	c_pc10_mem0 += MAS_MEM[6]
	S += 50 < c_pc10_mem0
	S += c_pc10_mem0 <= c_pc10

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	c_pc10_mem1 += MAS_MEM[7]
	S += 85 < c_pc10_mem1
	S += c_pc10_mem1 <= c_pc10

	c_aa00 = S.Task('c_aa00', length=3, delay_cost=1)
	c_aa00 += alt(MAS)
	c_aa00_in = S.Task('c_aa00_in', length=1, delay_cost=1)
	c_aa00_in += alt(MAS_in)
	S += c_aa00_in*MAS_in[0]<=c_aa00*MAS[0]

	S += c_aa00_in*MAS_in[1]<=c_aa00*MAS[1]

	S += c_aa00_in*MAS_in[2]<=c_aa00*MAS[2]

	S += c_aa00_in*MAS_in[3]<=c_aa00*MAS[3]

	S += c_aa00_in*MAS_in[4]<=c_aa00*MAS[4]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	c_aa00_mem0 += MAS_MEM[8]
	S += 95 < c_aa00_mem0
	S += c_aa00_mem0 <= c_aa00

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	c_aa00_mem1 += alt(MAS_MEM)
	S += (c_aa_t50*MAS[0])-1 < c_aa00_mem1*MAS_MEM[1]
	S += (c_aa_t50*MAS[1])-1 < c_aa00_mem1*MAS_MEM[3]
	S += (c_aa_t50*MAS[2])-1 < c_aa00_mem1*MAS_MEM[5]
	S += (c_aa_t50*MAS[3])-1 < c_aa00_mem1*MAS_MEM[7]
	S += (c_aa_t50*MAS[4])-1 < c_aa00_mem1*MAS_MEM[9]
	S += c_aa00_mem1 <= c_aa00

	c_aa01 = S.Task('c_aa01', length=3, delay_cost=1)
	c_aa01 += alt(MAS)
	c_aa01_in = S.Task('c_aa01_in', length=1, delay_cost=1)
	c_aa01_in += alt(MAS_in)
	S += c_aa01_in*MAS_in[0]<=c_aa01*MAS[0]

	S += c_aa01_in*MAS_in[1]<=c_aa01*MAS[1]

	S += c_aa01_in*MAS_in[2]<=c_aa01*MAS[2]

	S += c_aa01_in*MAS_in[3]<=c_aa01*MAS[3]

	S += c_aa01_in*MAS_in[4]<=c_aa01*MAS[4]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	c_aa01_mem0 += alt(MAS_MEM)
	S += (c_aa_t21*MAS[0])-1 < c_aa01_mem0*MAS_MEM[0]
	S += (c_aa_t21*MAS[1])-1 < c_aa01_mem0*MAS_MEM[2]
	S += (c_aa_t21*MAS[2])-1 < c_aa01_mem0*MAS_MEM[4]
	S += (c_aa_t21*MAS[3])-1 < c_aa01_mem0*MAS_MEM[6]
	S += (c_aa_t21*MAS[4])-1 < c_aa01_mem0*MAS_MEM[8]
	S += c_aa01_mem0 <= c_aa01

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	c_aa01_mem1 += alt(MAS_MEM)
	S += (c_aa_t51*MAS[0])-1 < c_aa01_mem1*MAS_MEM[1]
	S += (c_aa_t51*MAS[1])-1 < c_aa01_mem1*MAS_MEM[3]
	S += (c_aa_t51*MAS[2])-1 < c_aa01_mem1*MAS_MEM[5]
	S += (c_aa_t51*MAS[3])-1 < c_aa01_mem1*MAS_MEM[7]
	S += (c_aa_t51*MAS[4])-1 < c_aa01_mem1*MAS_MEM[9]
	S += c_aa01_mem1 <= c_aa01

	c_bb00 = S.Task('c_bb00', length=3, delay_cost=1)
	c_bb00 += alt(MAS)
	c_bb00_in = S.Task('c_bb00_in', length=1, delay_cost=1)
	c_bb00_in += alt(MAS_in)
	S += c_bb00_in*MAS_in[0]<=c_bb00*MAS[0]

	S += c_bb00_in*MAS_in[1]<=c_bb00*MAS[1]

	S += c_bb00_in*MAS_in[2]<=c_bb00*MAS[2]

	S += c_bb00_in*MAS_in[3]<=c_bb00*MAS[3]

	S += c_bb00_in*MAS_in[4]<=c_bb00*MAS[4]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	c_bb00_mem0 += MAS_MEM[8]
	S += 98 < c_bb00_mem0
	S += c_bb00_mem0 <= c_bb00

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	c_bb00_mem1 += alt(MAS_MEM)
	S += (c_bb_t50*MAS[0])-1 < c_bb00_mem1*MAS_MEM[1]
	S += (c_bb_t50*MAS[1])-1 < c_bb00_mem1*MAS_MEM[3]
	S += (c_bb_t50*MAS[2])-1 < c_bb00_mem1*MAS_MEM[5]
	S += (c_bb_t50*MAS[3])-1 < c_bb00_mem1*MAS_MEM[7]
	S += (c_bb_t50*MAS[4])-1 < c_bb00_mem1*MAS_MEM[9]
	S += c_bb00_mem1 <= c_bb00

	c_bb01 = S.Task('c_bb01', length=3, delay_cost=1)
	c_bb01 += alt(MAS)
	c_bb01_in = S.Task('c_bb01_in', length=1, delay_cost=1)
	c_bb01_in += alt(MAS_in)
	S += c_bb01_in*MAS_in[0]<=c_bb01*MAS[0]

	S += c_bb01_in*MAS_in[1]<=c_bb01*MAS[1]

	S += c_bb01_in*MAS_in[2]<=c_bb01*MAS[2]

	S += c_bb01_in*MAS_in[3]<=c_bb01*MAS[3]

	S += c_bb01_in*MAS_in[4]<=c_bb01*MAS[4]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	c_bb01_mem0 += alt(MAS_MEM)
	S += (c_bb_t21*MAS[0])-1 < c_bb01_mem0*MAS_MEM[0]
	S += (c_bb_t21*MAS[1])-1 < c_bb01_mem0*MAS_MEM[2]
	S += (c_bb_t21*MAS[2])-1 < c_bb01_mem0*MAS_MEM[4]
	S += (c_bb_t21*MAS[3])-1 < c_bb01_mem0*MAS_MEM[6]
	S += (c_bb_t21*MAS[4])-1 < c_bb01_mem0*MAS_MEM[8]
	S += c_bb01_mem0 <= c_bb01

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	c_bb01_mem1 += alt(MAS_MEM)
	S += (c_bb_t51*MAS[0])-1 < c_bb01_mem1*MAS_MEM[1]
	S += (c_bb_t51*MAS[1])-1 < c_bb01_mem1*MAS_MEM[3]
	S += (c_bb_t51*MAS[2])-1 < c_bb01_mem1*MAS_MEM[5]
	S += (c_bb_t51*MAS[3])-1 < c_bb01_mem1*MAS_MEM[7]
	S += (c_bb_t51*MAS[4])-1 < c_bb01_mem1*MAS_MEM[9]
	S += c_bb01_mem1 <= c_bb01

	c_cc00 = S.Task('c_cc00', length=3, delay_cost=1)
	c_cc00 += alt(MAS)
	c_cc00_in = S.Task('c_cc00_in', length=1, delay_cost=1)
	c_cc00_in += alt(MAS_in)
	S += c_cc00_in*MAS_in[0]<=c_cc00*MAS[0]

	S += c_cc00_in*MAS_in[1]<=c_cc00*MAS[1]

	S += c_cc00_in*MAS_in[2]<=c_cc00*MAS[2]

	S += c_cc00_in*MAS_in[3]<=c_cc00*MAS[3]

	S += c_cc00_in*MAS_in[4]<=c_cc00*MAS[4]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	c_cc00_mem0 += MAS_MEM[2]
	S += 97 < c_cc00_mem0
	S += c_cc00_mem0 <= c_cc00

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	c_cc00_mem1 += alt(MAS_MEM)
	S += (c_cc_t50*MAS[0])-1 < c_cc00_mem1*MAS_MEM[1]
	S += (c_cc_t50*MAS[1])-1 < c_cc00_mem1*MAS_MEM[3]
	S += (c_cc_t50*MAS[2])-1 < c_cc00_mem1*MAS_MEM[5]
	S += (c_cc_t50*MAS[3])-1 < c_cc00_mem1*MAS_MEM[7]
	S += (c_cc_t50*MAS[4])-1 < c_cc00_mem1*MAS_MEM[9]
	S += c_cc00_mem1 <= c_cc00

	c_cc01 = S.Task('c_cc01', length=3, delay_cost=1)
	c_cc01 += alt(MAS)
	c_cc01_in = S.Task('c_cc01_in', length=1, delay_cost=1)
	c_cc01_in += alt(MAS_in)
	S += c_cc01_in*MAS_in[0]<=c_cc01*MAS[0]

	S += c_cc01_in*MAS_in[1]<=c_cc01*MAS[1]

	S += c_cc01_in*MAS_in[2]<=c_cc01*MAS[2]

	S += c_cc01_in*MAS_in[3]<=c_cc01*MAS[3]

	S += c_cc01_in*MAS_in[4]<=c_cc01*MAS[4]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	c_cc01_mem0 += alt(MAS_MEM)
	S += (c_cc_t21*MAS[0])-1 < c_cc01_mem0*MAS_MEM[0]
	S += (c_cc_t21*MAS[1])-1 < c_cc01_mem0*MAS_MEM[2]
	S += (c_cc_t21*MAS[2])-1 < c_cc01_mem0*MAS_MEM[4]
	S += (c_cc_t21*MAS[3])-1 < c_cc01_mem0*MAS_MEM[6]
	S += (c_cc_t21*MAS[4])-1 < c_cc01_mem0*MAS_MEM[8]
	S += c_cc01_mem0 <= c_cc01

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	c_cc01_mem1 += alt(MAS_MEM)
	S += (c_cc_t51*MAS[0])-1 < c_cc01_mem1*MAS_MEM[1]
	S += (c_cc_t51*MAS[1])-1 < c_cc01_mem1*MAS_MEM[3]
	S += (c_cc_t51*MAS[2])-1 < c_cc01_mem1*MAS_MEM[5]
	S += (c_cc_t51*MAS[3])-1 < c_cc01_mem1*MAS_MEM[7]
	S += (c_cc_t51*MAS[4])-1 < c_cc01_mem1*MAS_MEM[9]
	S += c_cc01_mem1 <= c_cc01

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=3, delay_cost=1)
	c_bcxi_y1_0 += alt(MAS)
	c_bcxi_y1_0_in = S.Task('c_bcxi_y1_0_in', length=1, delay_cost=1)
	c_bcxi_y1_0_in += alt(MAS_in)
	S += c_bcxi_y1_0_in*MAS_in[0]<=c_bcxi_y1_0*MAS[0]

	S += c_bcxi_y1_0_in*MAS_in[1]<=c_bcxi_y1_0*MAS[1]

	S += c_bcxi_y1_0_in*MAS_in[2]<=c_bcxi_y1_0*MAS[2]

	S += c_bcxi_y1_0_in*MAS_in[3]<=c_bcxi_y1_0*MAS[3]

	S += c_bcxi_y1_0_in*MAS_in[4]<=c_bcxi_y1_0*MAS[4]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	c_bcxi_y1_0_mem0 += MAS_MEM[0]
	S += 85 < c_bcxi_y1_0_mem0
	S += c_bcxi_y1_0_mem0 <= c_bcxi_y1_0

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	c_bcxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_0_mem1*MAS_MEM[1]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_0_mem1*MAS_MEM[3]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_0_mem1*MAS_MEM[5]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_0_mem1*MAS_MEM[7]
	S += (c_bc11*MAS[4])-1 < c_bcxi_y1_0_mem1*MAS_MEM[9]
	S += c_bcxi_y1_0_mem1 <= c_bcxi_y1_0

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=3, delay_cost=1)
	c_bcxi_y1_1 += alt(MAS)
	c_bcxi_y1_1_in = S.Task('c_bcxi_y1_1_in', length=1, delay_cost=1)
	c_bcxi_y1_1_in += alt(MAS_in)
	S += c_bcxi_y1_1_in*MAS_in[0]<=c_bcxi_y1_1*MAS[0]

	S += c_bcxi_y1_1_in*MAS_in[1]<=c_bcxi_y1_1*MAS[1]

	S += c_bcxi_y1_1_in*MAS_in[2]<=c_bcxi_y1_1*MAS[2]

	S += c_bcxi_y1_1_in*MAS_in[3]<=c_bcxi_y1_1*MAS[3]

	S += c_bcxi_y1_1_in*MAS_in[4]<=c_bcxi_y1_1*MAS[4]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	c_bcxi_y1_1_mem0 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_1_mem0*MAS_MEM[0]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_1_mem0*MAS_MEM[2]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_1_mem0*MAS_MEM[4]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_1_mem0*MAS_MEM[6]
	S += (c_bc11*MAS[4])-1 < c_bcxi_y1_1_mem0*MAS_MEM[8]
	S += c_bcxi_y1_1_mem0 <= c_bcxi_y1_1

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	c_bcxi_y1_1_mem1 += MAS_MEM[1]
	S += 85 < c_bcxi_y1_1_mem1
	S += c_bcxi_y1_1_mem1 <= c_bcxi_y1_1

	c_pa10 = S.Task('c_pa10', length=3, delay_cost=1)
	c_pa10 += alt(MAS)
	c_pa10_in = S.Task('c_pa10_in', length=1, delay_cost=1)
	c_pa10_in += alt(MAS_in)
	S += c_pa10_in*MAS_in[0]<=c_pa10*MAS[0]

	S += c_pa10_in*MAS_in[1]<=c_pa10*MAS[1]

	S += c_pa10_in*MAS_in[2]<=c_pa10*MAS[2]

	S += c_pa10_in*MAS_in[3]<=c_pa10*MAS[3]

	S += c_pa10_in*MAS_in[4]<=c_pa10*MAS[4]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	c_pa10_mem0 += MAS_MEM[4]
	S += 30 < c_pa10_mem0
	S += c_pa10_mem0 <= c_pa10

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	c_pa10_mem1 += alt(MAS_MEM)
	S += (c_bc00*MAS[0])-1 < c_pa10_mem1*MAS_MEM[1]
	S += (c_bc00*MAS[1])-1 < c_pa10_mem1*MAS_MEM[3]
	S += (c_bc00*MAS[2])-1 < c_pa10_mem1*MAS_MEM[5]
	S += (c_bc00*MAS[3])-1 < c_pa10_mem1*MAS_MEM[7]
	S += (c_bc00*MAS[4])-1 < c_pa10_mem1*MAS_MEM[9]
	S += c_pa10_mem1 <= c_pa10

	c_pa11 = S.Task('c_pa11', length=3, delay_cost=1)
	c_pa11 += alt(MAS)
	c_pa11_in = S.Task('c_pa11_in', length=1, delay_cost=1)
	c_pa11_in += alt(MAS_in)
	S += c_pa11_in*MAS_in[0]<=c_pa11*MAS[0]

	S += c_pa11_in*MAS_in[1]<=c_pa11*MAS[1]

	S += c_pa11_in*MAS_in[2]<=c_pa11*MAS[2]

	S += c_pa11_in*MAS_in[3]<=c_pa11*MAS[3]

	S += c_pa11_in*MAS_in[4]<=c_pa11*MAS[4]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	c_pa11_mem0 += MAS_MEM[6]
	S += 33 < c_pa11_mem0
	S += c_pa11_mem0 <= c_pa11

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	c_pa11_mem1 += alt(MAS_MEM)
	S += (c_bc01*MAS[0])-1 < c_pa11_mem1*MAS_MEM[1]
	S += (c_bc01*MAS[1])-1 < c_pa11_mem1*MAS_MEM[3]
	S += (c_bc01*MAS[2])-1 < c_pa11_mem1*MAS_MEM[5]
	S += (c_bc01*MAS[3])-1 < c_pa11_mem1*MAS_MEM[7]
	S += (c_bc01*MAS[4])-1 < c_pa11_mem1*MAS_MEM[9]
	S += c_pa11_mem1 <= c_pa11

	c_pb00 = S.Task('c_pb00', length=3, delay_cost=1)
	c_pb00 += alt(MAS)
	c_pb00_in = S.Task('c_pb00_in', length=1, delay_cost=1)
	c_pb00_in += alt(MAS_in)
	S += c_pb00_in*MAS_in[0]<=c_pb00*MAS[0]

	S += c_pb00_in*MAS_in[1]<=c_pb00*MAS[1]

	S += c_pb00_in*MAS_in[2]<=c_pb00*MAS[2]

	S += c_pb00_in*MAS_in[3]<=c_pb00*MAS[3]

	S += c_pb00_in*MAS_in[4]<=c_pb00*MAS[4]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	c_pb00_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_0*MAS[0])-1 < c_pb00_mem0*MAS_MEM[0]
	S += (c_ccxi_y1_0*MAS[1])-1 < c_pb00_mem0*MAS_MEM[2]
	S += (c_ccxi_y1_0*MAS[2])-1 < c_pb00_mem0*MAS_MEM[4]
	S += (c_ccxi_y1_0*MAS[3])-1 < c_pb00_mem0*MAS_MEM[6]
	S += (c_ccxi_y1_0*MAS[4])-1 < c_pb00_mem0*MAS_MEM[8]
	S += c_pb00_mem0 <= c_pb00

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	c_pb00_mem1 += alt(MAS_MEM)
	S += (c_ab00*MAS[0])-1 < c_pb00_mem1*MAS_MEM[1]
	S += (c_ab00*MAS[1])-1 < c_pb00_mem1*MAS_MEM[3]
	S += (c_ab00*MAS[2])-1 < c_pb00_mem1*MAS_MEM[5]
	S += (c_ab00*MAS[3])-1 < c_pb00_mem1*MAS_MEM[7]
	S += (c_ab00*MAS[4])-1 < c_pb00_mem1*MAS_MEM[9]
	S += c_pb00_mem1 <= c_pb00

	c_pb01 = S.Task('c_pb01', length=3, delay_cost=1)
	c_pb01 += alt(MAS)
	c_pb01_in = S.Task('c_pb01_in', length=1, delay_cost=1)
	c_pb01_in += alt(MAS_in)
	S += c_pb01_in*MAS_in[0]<=c_pb01*MAS[0]

	S += c_pb01_in*MAS_in[1]<=c_pb01*MAS[1]

	S += c_pb01_in*MAS_in[2]<=c_pb01*MAS[2]

	S += c_pb01_in*MAS_in[3]<=c_pb01*MAS[3]

	S += c_pb01_in*MAS_in[4]<=c_pb01*MAS[4]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	c_pb01_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_1*MAS[0])-1 < c_pb01_mem0*MAS_MEM[0]
	S += (c_ccxi_y1_1*MAS[1])-1 < c_pb01_mem0*MAS_MEM[2]
	S += (c_ccxi_y1_1*MAS[2])-1 < c_pb01_mem0*MAS_MEM[4]
	S += (c_ccxi_y1_1*MAS[3])-1 < c_pb01_mem0*MAS_MEM[6]
	S += (c_ccxi_y1_1*MAS[4])-1 < c_pb01_mem0*MAS_MEM[8]
	S += c_pb01_mem0 <= c_pb01

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	c_pb01_mem1 += alt(MAS_MEM)
	S += (c_ab01*MAS[0])-1 < c_pb01_mem1*MAS_MEM[1]
	S += (c_ab01*MAS[1])-1 < c_pb01_mem1*MAS_MEM[3]
	S += (c_ab01*MAS[2])-1 < c_pb01_mem1*MAS_MEM[5]
	S += (c_ab01*MAS[3])-1 < c_pb01_mem1*MAS_MEM[7]
	S += (c_ab01*MAS[4])-1 < c_pb01_mem1*MAS_MEM[9]
	S += c_pb01_mem1 <= c_pb01

	c_pc11 = S.Task('c_pc11', length=3, delay_cost=1)
	c_pc11 += alt(MAS)
	c_pc11_in = S.Task('c_pc11_in', length=1, delay_cost=1)
	c_pc11_in += alt(MAS_in)
	S += c_pc11_in*MAS_in[0]<=c_pc11*MAS[0]

	S += c_pc11_in*MAS_in[1]<=c_pc11*MAS[1]

	S += c_pc11_in*MAS_in[2]<=c_pc11*MAS[2]

	S += c_pc11_in*MAS_in[3]<=c_pc11*MAS[3]

	S += c_pc11_in*MAS_in[4]<=c_pc11*MAS[4]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	c_pc11_mem0 += MAS_MEM[4]
	S += 54 < c_pc11_mem0
	S += c_pc11_mem0 <= c_pc11

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	c_pc11_mem1 += alt(MAS_MEM)
	S += (c_ac11*MAS[0])-1 < c_pc11_mem1*MAS_MEM[1]
	S += (c_ac11*MAS[1])-1 < c_pc11_mem1*MAS_MEM[3]
	S += (c_ac11*MAS[2])-1 < c_pc11_mem1*MAS_MEM[5]
	S += (c_ac11*MAS[3])-1 < c_pc11_mem1*MAS_MEM[7]
	S += (c_ac11*MAS[4])-1 < c_pc11_mem1*MAS_MEM[9]
	S += c_pc11_mem1 <= c_pc11

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=14, delay_cost=1)
	c_pcb_t1_t0 += alt(MM)
	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	c_pcb_t1_t0_in += alt(MM_in)
	S += c_pcb_t1_t0_in*MM_in[0]<=c_pcb_t1_t0*MM[0]
	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	c_pcb_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t0_mem0*MAS_MEM[0]
	S += (c_pc10*MAS[1])-1 < c_pcb_t1_t0_mem0*MAS_MEM[2]
	S += (c_pc10*MAS[2])-1 < c_pcb_t1_t0_mem0*MAS_MEM[4]
	S += (c_pc10*MAS[3])-1 < c_pcb_t1_t0_mem0*MAS_MEM[6]
	S += (c_pc10*MAS[4])-1 < c_pcb_t1_t0_mem0*MAS_MEM[8]
	S += c_pcb_t1_t0_mem0 <= c_pcb_t1_t0

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t1_t0_mem1 <= c_pcb_t1_t0

	c_pa00 = S.Task('c_pa00', length=3, delay_cost=1)
	c_pa00 += alt(MAS)
	c_pa00_in = S.Task('c_pa00_in', length=1, delay_cost=1)
	c_pa00_in += alt(MAS_in)
	S += c_pa00_in*MAS_in[0]<=c_pa00*MAS[0]

	S += c_pa00_in*MAS_in[1]<=c_pa00*MAS[1]

	S += c_pa00_in*MAS_in[2]<=c_pa00*MAS[2]

	S += c_pa00_in*MAS_in[3]<=c_pa00*MAS[3]

	S += c_pa00_in*MAS_in[4]<=c_pa00*MAS[4]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	c_pa00_mem0 += alt(MAS_MEM)
	S += (c_aa00*MAS[0])-1 < c_pa00_mem0*MAS_MEM[0]
	S += (c_aa00*MAS[1])-1 < c_pa00_mem0*MAS_MEM[2]
	S += (c_aa00*MAS[2])-1 < c_pa00_mem0*MAS_MEM[4]
	S += (c_aa00*MAS[3])-1 < c_pa00_mem0*MAS_MEM[6]
	S += (c_aa00*MAS[4])-1 < c_pa00_mem0*MAS_MEM[8]
	S += c_pa00_mem0 <= c_pa00

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	c_pa00_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_0*MAS[0])-1 < c_pa00_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_0*MAS[1])-1 < c_pa00_mem1*MAS_MEM[3]
	S += (c_bcxi_y1_0*MAS[2])-1 < c_pa00_mem1*MAS_MEM[5]
	S += (c_bcxi_y1_0*MAS[3])-1 < c_pa00_mem1*MAS_MEM[7]
	S += (c_bcxi_y1_0*MAS[4])-1 < c_pa00_mem1*MAS_MEM[9]
	S += c_pa00_mem1 <= c_pa00

	c_pa01 = S.Task('c_pa01', length=3, delay_cost=1)
	c_pa01 += alt(MAS)
	c_pa01_in = S.Task('c_pa01_in', length=1, delay_cost=1)
	c_pa01_in += alt(MAS_in)
	S += c_pa01_in*MAS_in[0]<=c_pa01*MAS[0]

	S += c_pa01_in*MAS_in[1]<=c_pa01*MAS[1]

	S += c_pa01_in*MAS_in[2]<=c_pa01*MAS[2]

	S += c_pa01_in*MAS_in[3]<=c_pa01*MAS[3]

	S += c_pa01_in*MAS_in[4]<=c_pa01*MAS[4]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	c_pa01_mem0 += alt(MAS_MEM)
	S += (c_aa01*MAS[0])-1 < c_pa01_mem0*MAS_MEM[0]
	S += (c_aa01*MAS[1])-1 < c_pa01_mem0*MAS_MEM[2]
	S += (c_aa01*MAS[2])-1 < c_pa01_mem0*MAS_MEM[4]
	S += (c_aa01*MAS[3])-1 < c_pa01_mem0*MAS_MEM[6]
	S += (c_aa01*MAS[4])-1 < c_pa01_mem0*MAS_MEM[8]
	S += c_pa01_mem0 <= c_pa01

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	c_pa01_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_1*MAS[0])-1 < c_pa01_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_1*MAS[1])-1 < c_pa01_mem1*MAS_MEM[3]
	S += (c_bcxi_y1_1*MAS[2])-1 < c_pa01_mem1*MAS_MEM[5]
	S += (c_bcxi_y1_1*MAS[3])-1 < c_pa01_mem1*MAS_MEM[7]
	S += (c_bcxi_y1_1*MAS[4])-1 < c_pa01_mem1*MAS_MEM[9]
	S += c_pa01_mem1 <= c_pa01

	c_pb10 = S.Task('c_pb10', length=3, delay_cost=1)
	c_pb10 += alt(MAS)
	c_pb10_in = S.Task('c_pb10_in', length=1, delay_cost=1)
	c_pb10_in += alt(MAS_in)
	S += c_pb10_in*MAS_in[0]<=c_pb10*MAS[0]

	S += c_pb10_in*MAS_in[1]<=c_pb10*MAS[1]

	S += c_pb10_in*MAS_in[2]<=c_pb10*MAS[2]

	S += c_pb10_in*MAS_in[3]<=c_pb10*MAS[3]

	S += c_pb10_in*MAS_in[4]<=c_pb10*MAS[4]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	c_pb10_mem0 += alt(MAS_MEM)
	S += (c_cc00*MAS[0])-1 < c_pb10_mem0*MAS_MEM[0]
	S += (c_cc00*MAS[1])-1 < c_pb10_mem0*MAS_MEM[2]
	S += (c_cc00*MAS[2])-1 < c_pb10_mem0*MAS_MEM[4]
	S += (c_cc00*MAS[3])-1 < c_pb10_mem0*MAS_MEM[6]
	S += (c_cc00*MAS[4])-1 < c_pb10_mem0*MAS_MEM[8]
	S += c_pb10_mem0 <= c_pb10

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	c_pb10_mem1 += MAS_MEM[5]
	S += 57 < c_pb10_mem1
	S += c_pb10_mem1 <= c_pb10

	c_pb11 = S.Task('c_pb11', length=3, delay_cost=1)
	c_pb11 += alt(MAS)
	c_pb11_in = S.Task('c_pb11_in', length=1, delay_cost=1)
	c_pb11_in += alt(MAS_in)
	S += c_pb11_in*MAS_in[0]<=c_pb11*MAS[0]

	S += c_pb11_in*MAS_in[1]<=c_pb11*MAS[1]

	S += c_pb11_in*MAS_in[2]<=c_pb11*MAS[2]

	S += c_pb11_in*MAS_in[3]<=c_pb11*MAS[3]

	S += c_pb11_in*MAS_in[4]<=c_pb11*MAS[4]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	c_pb11_mem0 += alt(MAS_MEM)
	S += (c_cc01*MAS[0])-1 < c_pb11_mem0*MAS_MEM[0]
	S += (c_cc01*MAS[1])-1 < c_pb11_mem0*MAS_MEM[2]
	S += (c_cc01*MAS[2])-1 < c_pb11_mem0*MAS_MEM[4]
	S += (c_cc01*MAS[3])-1 < c_pb11_mem0*MAS_MEM[6]
	S += (c_cc01*MAS[4])-1 < c_pb11_mem0*MAS_MEM[8]
	S += c_pb11_mem0 <= c_pb11

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	c_pb11_mem1 += alt(MAS_MEM)
	S += (c_ab11*MAS[0])-1 < c_pb11_mem1*MAS_MEM[1]
	S += (c_ab11*MAS[1])-1 < c_pb11_mem1*MAS_MEM[3]
	S += (c_ab11*MAS[2])-1 < c_pb11_mem1*MAS_MEM[5]
	S += (c_ab11*MAS[3])-1 < c_pb11_mem1*MAS_MEM[7]
	S += (c_ab11*MAS[4])-1 < c_pb11_mem1*MAS_MEM[9]
	S += c_pb11_mem1 <= c_pb11

	c_pc00 = S.Task('c_pc00', length=3, delay_cost=1)
	c_pc00 += alt(MAS)
	c_pc00_in = S.Task('c_pc00_in', length=1, delay_cost=1)
	c_pc00_in += alt(MAS_in)
	S += c_pc00_in*MAS_in[0]<=c_pc00*MAS[0]

	S += c_pc00_in*MAS_in[1]<=c_pc00*MAS[1]

	S += c_pc00_in*MAS_in[2]<=c_pc00*MAS[2]

	S += c_pc00_in*MAS_in[3]<=c_pc00*MAS[3]

	S += c_pc00_in*MAS_in[4]<=c_pc00*MAS[4]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	c_pc00_mem0 += alt(MAS_MEM)
	S += (c_bb00*MAS[0])-1 < c_pc00_mem0*MAS_MEM[0]
	S += (c_bb00*MAS[1])-1 < c_pc00_mem0*MAS_MEM[2]
	S += (c_bb00*MAS[2])-1 < c_pc00_mem0*MAS_MEM[4]
	S += (c_bb00*MAS[3])-1 < c_pc00_mem0*MAS_MEM[6]
	S += (c_bb00*MAS[4])-1 < c_pc00_mem0*MAS_MEM[8]
	S += c_pc00_mem0 <= c_pc00

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	c_pc00_mem1 += alt(MAS_MEM)
	S += (c_ac00*MAS[0])-1 < c_pc00_mem1*MAS_MEM[1]
	S += (c_ac00*MAS[1])-1 < c_pc00_mem1*MAS_MEM[3]
	S += (c_ac00*MAS[2])-1 < c_pc00_mem1*MAS_MEM[5]
	S += (c_ac00*MAS[3])-1 < c_pc00_mem1*MAS_MEM[7]
	S += (c_ac00*MAS[4])-1 < c_pc00_mem1*MAS_MEM[9]
	S += c_pc00_mem1 <= c_pc00

	c_pc01 = S.Task('c_pc01', length=3, delay_cost=1)
	c_pc01 += alt(MAS)
	c_pc01_in = S.Task('c_pc01_in', length=1, delay_cost=1)
	c_pc01_in += alt(MAS_in)
	S += c_pc01_in*MAS_in[0]<=c_pc01*MAS[0]

	S += c_pc01_in*MAS_in[1]<=c_pc01*MAS[1]

	S += c_pc01_in*MAS_in[2]<=c_pc01*MAS[2]

	S += c_pc01_in*MAS_in[3]<=c_pc01*MAS[3]

	S += c_pc01_in*MAS_in[4]<=c_pc01*MAS[4]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	c_pc01_mem0 += alt(MAS_MEM)
	S += (c_bb01*MAS[0])-1 < c_pc01_mem0*MAS_MEM[0]
	S += (c_bb01*MAS[1])-1 < c_pc01_mem0*MAS_MEM[2]
	S += (c_bb01*MAS[2])-1 < c_pc01_mem0*MAS_MEM[4]
	S += (c_bb01*MAS[3])-1 < c_pc01_mem0*MAS_MEM[6]
	S += (c_bb01*MAS[4])-1 < c_pc01_mem0*MAS_MEM[8]
	S += c_pc01_mem0 <= c_pc01

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	c_pc01_mem1 += alt(MAS_MEM)
	S += (c_ac01*MAS[0])-1 < c_pc01_mem1*MAS_MEM[1]
	S += (c_ac01*MAS[1])-1 < c_pc01_mem1*MAS_MEM[3]
	S += (c_ac01*MAS[2])-1 < c_pc01_mem1*MAS_MEM[5]
	S += (c_ac01*MAS[3])-1 < c_pc01_mem1*MAS_MEM[7]
	S += (c_ac01*MAS[4])-1 < c_pc01_mem1*MAS_MEM[9]
	S += c_pc01_mem1 <= c_pc01

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=14, delay_cost=1)
	c_pbc_t0_t0 += alt(MM)
	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	c_pbc_t0_t0_in += alt(MM_in)
	S += c_pbc_t0_t0_in*MM_in[0]<=c_pbc_t0_t0*MM[0]
	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	c_pbc_t0_t0_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t0_mem0*MAS_MEM[0]
	S += (c_pb00*MAS[1])-1 < c_pbc_t0_t0_mem0*MAS_MEM[2]
	S += (c_pb00*MAS[2])-1 < c_pbc_t0_t0_mem0*MAS_MEM[4]
	S += (c_pb00*MAS[3])-1 < c_pbc_t0_t0_mem0*MAS_MEM[6]
	S += (c_pb00*MAS[4])-1 < c_pbc_t0_t0_mem0*MAS_MEM[8]
	S += c_pbc_t0_t0_mem0 <= c_pbc_t0_t0

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t0_t0_mem1 <= c_pbc_t0_t0

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=14, delay_cost=1)
	c_pbc_t0_t1 += alt(MM)
	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	c_pbc_t0_t1_in += alt(MM_in)
	S += c_pbc_t0_t1_in*MM_in[0]<=c_pbc_t0_t1*MM[0]
	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	c_pbc_t0_t1_mem0 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t1_mem0*MAS_MEM[0]
	S += (c_pb01*MAS[1])-1 < c_pbc_t0_t1_mem0*MAS_MEM[2]
	S += (c_pb01*MAS[2])-1 < c_pbc_t0_t1_mem0*MAS_MEM[4]
	S += (c_pb01*MAS[3])-1 < c_pbc_t0_t1_mem0*MAS_MEM[6]
	S += (c_pb01*MAS[4])-1 < c_pbc_t0_t1_mem0*MAS_MEM[8]
	S += c_pbc_t0_t1_mem0 <= c_pbc_t0_t1

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t0_t1_mem1 <= c_pbc_t0_t1

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=3, delay_cost=1)
	c_pbc_t0_t2 += alt(MAS)
	c_pbc_t0_t2_in = S.Task('c_pbc_t0_t2_in', length=1, delay_cost=1)
	c_pbc_t0_t2_in += alt(MAS_in)
	S += c_pbc_t0_t2_in*MAS_in[0]<=c_pbc_t0_t2*MAS[0]

	S += c_pbc_t0_t2_in*MAS_in[1]<=c_pbc_t0_t2*MAS[1]

	S += c_pbc_t0_t2_in*MAS_in[2]<=c_pbc_t0_t2*MAS[2]

	S += c_pbc_t0_t2_in*MAS_in[3]<=c_pbc_t0_t2*MAS[3]

	S += c_pbc_t0_t2_in*MAS_in[4]<=c_pbc_t0_t2*MAS[4]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	c_pbc_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t2_mem0*MAS_MEM[0]
	S += (c_pb00*MAS[1])-1 < c_pbc_t0_t2_mem0*MAS_MEM[2]
	S += (c_pb00*MAS[2])-1 < c_pbc_t0_t2_mem0*MAS_MEM[4]
	S += (c_pb00*MAS[3])-1 < c_pbc_t0_t2_mem0*MAS_MEM[6]
	S += (c_pb00*MAS[4])-1 < c_pbc_t0_t2_mem0*MAS_MEM[8]
	S += c_pbc_t0_t2_mem0 <= c_pbc_t0_t2

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	c_pbc_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t2_mem1*MAS_MEM[1]
	S += (c_pb01*MAS[1])-1 < c_pbc_t0_t2_mem1*MAS_MEM[3]
	S += (c_pb01*MAS[2])-1 < c_pbc_t0_t2_mem1*MAS_MEM[5]
	S += (c_pb01*MAS[3])-1 < c_pbc_t0_t2_mem1*MAS_MEM[7]
	S += (c_pb01*MAS[4])-1 < c_pbc_t0_t2_mem1*MAS_MEM[9]
	S += c_pbc_t0_t2_mem1 <= c_pbc_t0_t2

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=14, delay_cost=1)
	c_pcb_t1_t1 += alt(MM)
	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	c_pcb_t1_t1_in += alt(MM_in)
	S += c_pcb_t1_t1_in*MM_in[0]<=c_pcb_t1_t1*MM[0]
	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	c_pcb_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t1_mem0*MAS_MEM[0]
	S += (c_pc11*MAS[1])-1 < c_pcb_t1_t1_mem0*MAS_MEM[2]
	S += (c_pc11*MAS[2])-1 < c_pcb_t1_t1_mem0*MAS_MEM[4]
	S += (c_pc11*MAS[3])-1 < c_pcb_t1_t1_mem0*MAS_MEM[6]
	S += (c_pc11*MAS[4])-1 < c_pcb_t1_t1_mem0*MAS_MEM[8]
	S += c_pcb_t1_t1_mem0 <= c_pcb_t1_t1

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t1_t1_mem1 <= c_pcb_t1_t1

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=3, delay_cost=1)
	c_pcb_t1_t2 += alt(MAS)
	c_pcb_t1_t2_in = S.Task('c_pcb_t1_t2_in', length=1, delay_cost=1)
	c_pcb_t1_t2_in += alt(MAS_in)
	S += c_pcb_t1_t2_in*MAS_in[0]<=c_pcb_t1_t2*MAS[0]

	S += c_pcb_t1_t2_in*MAS_in[1]<=c_pcb_t1_t2*MAS[1]

	S += c_pcb_t1_t2_in*MAS_in[2]<=c_pcb_t1_t2*MAS[2]

	S += c_pcb_t1_t2_in*MAS_in[3]<=c_pcb_t1_t2*MAS[3]

	S += c_pcb_t1_t2_in*MAS_in[4]<=c_pcb_t1_t2*MAS[4]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	c_pcb_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t2_mem0*MAS_MEM[0]
	S += (c_pc10*MAS[1])-1 < c_pcb_t1_t2_mem0*MAS_MEM[2]
	S += (c_pc10*MAS[2])-1 < c_pcb_t1_t2_mem0*MAS_MEM[4]
	S += (c_pc10*MAS[3])-1 < c_pcb_t1_t2_mem0*MAS_MEM[6]
	S += (c_pc10*MAS[4])-1 < c_pcb_t1_t2_mem0*MAS_MEM[8]
	S += c_pcb_t1_t2_mem0 <= c_pcb_t1_t2

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	c_pcb_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t2_mem1*MAS_MEM[1]
	S += (c_pc11*MAS[1])-1 < c_pcb_t1_t2_mem1*MAS_MEM[3]
	S += (c_pc11*MAS[2])-1 < c_pcb_t1_t2_mem1*MAS_MEM[5]
	S += (c_pc11*MAS[3])-1 < c_pcb_t1_t2_mem1*MAS_MEM[7]
	S += (c_pc11*MAS[4])-1 < c_pcb_t1_t2_mem1*MAS_MEM[9]
	S += c_pcb_t1_t2_mem1 <= c_pcb_t1_t2

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=14, delay_cost=1)
	c_paa_t1_t0 += alt(MM)
	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	c_paa_t1_t0_in += alt(MM_in)
	S += c_paa_t1_t0_in*MM_in[0]<=c_paa_t1_t0*MM[0]
	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	c_paa_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t0_mem0*MAS_MEM[0]
	S += (c_pa10*MAS[1])-1 < c_paa_t1_t0_mem0*MAS_MEM[2]
	S += (c_pa10*MAS[2])-1 < c_paa_t1_t0_mem0*MAS_MEM[4]
	S += (c_pa10*MAS[3])-1 < c_paa_t1_t0_mem0*MAS_MEM[6]
	S += (c_pa10*MAS[4])-1 < c_paa_t1_t0_mem0*MAS_MEM[8]
	S += c_paa_t1_t0_mem0 <= c_paa_t1_t0

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_paa_t1_t0_mem1 <= c_paa_t1_t0

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=14, delay_cost=1)
	c_paa_t1_t1 += alt(MM)
	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	c_paa_t1_t1_in += alt(MM_in)
	S += c_paa_t1_t1_in*MM_in[0]<=c_paa_t1_t1*MM[0]
	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	c_paa_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t1_mem0*MAS_MEM[0]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t1_mem0*MAS_MEM[2]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t1_mem0*MAS_MEM[4]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t1_mem0*MAS_MEM[6]
	S += (c_pa11*MAS[4])-1 < c_paa_t1_t1_mem0*MAS_MEM[8]
	S += c_paa_t1_t1_mem0 <= c_paa_t1_t1

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_paa_t1_t1_mem1 <= c_paa_t1_t1

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=3, delay_cost=1)
	c_paa_t1_t2 += alt(MAS)
	c_paa_t1_t2_in = S.Task('c_paa_t1_t2_in', length=1, delay_cost=1)
	c_paa_t1_t2_in += alt(MAS_in)
	S += c_paa_t1_t2_in*MAS_in[0]<=c_paa_t1_t2*MAS[0]

	S += c_paa_t1_t2_in*MAS_in[1]<=c_paa_t1_t2*MAS[1]

	S += c_paa_t1_t2_in*MAS_in[2]<=c_paa_t1_t2*MAS[2]

	S += c_paa_t1_t2_in*MAS_in[3]<=c_paa_t1_t2*MAS[3]

	S += c_paa_t1_t2_in*MAS_in[4]<=c_paa_t1_t2*MAS[4]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	c_paa_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t2_mem0*MAS_MEM[0]
	S += (c_pa10*MAS[1])-1 < c_paa_t1_t2_mem0*MAS_MEM[2]
	S += (c_pa10*MAS[2])-1 < c_paa_t1_t2_mem0*MAS_MEM[4]
	S += (c_pa10*MAS[3])-1 < c_paa_t1_t2_mem0*MAS_MEM[6]
	S += (c_pa10*MAS[4])-1 < c_paa_t1_t2_mem0*MAS_MEM[8]
	S += c_paa_t1_t2_mem0 <= c_paa_t1_t2

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	c_paa_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t2_mem1*MAS_MEM[1]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t2_mem1*MAS_MEM[3]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t2_mem1*MAS_MEM[5]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t2_mem1*MAS_MEM[7]
	S += (c_pa11*MAS[4])-1 < c_paa_t1_t2_mem1*MAS_MEM[9]
	S += c_paa_t1_t2_mem1 <= c_paa_t1_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS5/FP12_INV_BEFORE_FPINV/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

