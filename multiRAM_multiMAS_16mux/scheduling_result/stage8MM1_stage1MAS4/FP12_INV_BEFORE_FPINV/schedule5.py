from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 202
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 0
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 0
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 0
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=8, delay_cost=1)
	S += c_cc_t3_t0 >= 1
	c_cc_t3_t0 += MM[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 1
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 1
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 1
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 2
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 2
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 2
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=8, delay_cost=1)
	S += c_cc_t3_t1 >= 2
	c_cc_t3_t1 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 3
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 3
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 3
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=8, delay_cost=1)
	S += c_bb_t3_t1 >= 3
	c_bb_t3_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 4
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 4
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 4
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=8, delay_cost=1)
	S += c_ab_t1_t1 >= 4
	c_ab_t1_t1 += MM[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 5
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 5
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 5
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=8, delay_cost=1)
	S += c_ab_t1_t0 >= 5
	c_ab_t1_t0 += MM[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=8, delay_cost=1)
	S += c_ab_t0_t1 >= 6
	c_ab_t0_t1 += MM[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 6
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 6
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 6
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 7
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 7
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 7
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=8, delay_cost=1)
	S += c_bb_t3_t0 >= 7
	c_bb_t3_t0 += MM[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 8
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 8
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 8
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=8, delay_cost=1)
	S += c_ab_t0_t0 >= 8
	c_ab_t0_t0 += MM[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 9
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 9
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 9
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=8, delay_cost=1)
	S += c_aa_t3_t1 >= 9
	c_aa_t3_t1 += MM[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 9
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 9
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=8, delay_cost=1)
	S += c_aa_t3_t0 >= 10
	c_aa_t3_t0 += MM[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 10
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 10
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 10
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 10
	c_cc_t30_mem1 += MM_MEM[1]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 10
	c_cc_t3_t5 += MAS[3]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 11
	c_ab_t0_t3 += MAS[3]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 11
	c_cc10_mem0 += MAS_MEM[0]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 11
	c_cc10_mem1 += MAS_MEM[1]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 11
	c_cc_t30 += MAS[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 11
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 11
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 12
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 12
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 12
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 12
	c_ab_t10_mem1 += MM_MEM[1]

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	S += c_cc10 >= 12
	c_cc10 += MAS[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 12
	c_cc_t3_t3 += MAS[0]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 13
	c_aa_t10 += MAS[1]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 13
	c_ab_t10 += MAS[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 13
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 13
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 13
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 14
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 14
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 14
	c_ab_t1_t5 += MAS[3]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 14
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 14
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 14
	c_cc_t3_t2 += MAS[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 14
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 14
	c_cc_t3_t4_mem0 += MAS_MEM[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 14
	c_cc_t3_t4_mem1 += MAS_MEM[1]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 15
	c_aa_t3_t2 += MAS[2]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 15
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 15
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 15
	c_bb_t3_t5 += MAS[3]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 15
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 15
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=8, delay_cost=1)
	S += c_cc_t3_t4 >= 15
	c_cc_t3_t4 += MM[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 16
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 16
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 16
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 16
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 16
	c_ab_t0_t5 += MAS[1]

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 16
	c_cc_t10 += MAS[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 17
	c_aa_a1_0 += MAS[2]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 17
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 17
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 17
	c_ab_t00 += MAS[1]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 17
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 17
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 17
	c_ab_t50_mem0 += MAS_MEM[2]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 17
	c_ab_t50_mem1 += MAS_MEM[7]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 18
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 18
	c_aa_t30_mem1 += MM_MEM[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 18
	c_aa_t3_t5 += MAS[2]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 18
	c_ab_t0_t2 += MAS[0]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 18
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 18
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 18
	c_ab_t0_t4_mem1 += MAS_MEM[7]

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	S += c_ab_t50 >= 18
	c_ab_t50 += MAS[1]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 18
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 18
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 19
	c_aa10_mem0 += MAS_MEM[2]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 19
	c_aa10_mem1 += MAS_MEM[3]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 19
	c_aa_t30 += MAS[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 19
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 19
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=8, delay_cost=1)
	S += c_ab_t0_t4 >= 19
	c_ab_t0_t4 += MM[0]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 19
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 19
	c_bb_t30_mem1 += MM_MEM[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 19
	c_cc_a1_1 += MAS[0]

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	S += c_aa10 >= 20
	c_aa10 += MAS[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 20
	c_aa_t3_t3 += MAS[2]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 20
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 20
	c_aa_t3_t4_mem0 += MAS_MEM[4]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 20
	c_aa_t3_t4_mem1 += MAS_MEM[5]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 20
	c_bb10_mem0 += MAS_MEM[2]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 20
	c_bb10_mem1 += MAS_MEM[3]

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 20
	c_bb_t30 += MAS[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 20
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 20
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 21
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 21
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=8, delay_cost=1)
	S += c_aa_t3_t4 >= 21
	c_aa_t3_t4 += MM[0]

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	S += c_bb10 >= 21
	c_bb10 += MAS[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 21
	c_cc_a1_0 += MAS[0]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 22
	c_aa_t11 += MAS[2]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 22
	c_aa_t2_t3_mem0 += MAS_MEM[2]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 22
	c_aa_t2_t3_mem1 += MAS_MEM[5]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 22
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 22
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 22
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 22
	c_cc_t31_mem1 += MAS_MEM[7]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 23
	c_aa_t2_t3 += MAS[1]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 23
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 23
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 23
	c_cc_t11 += MAS[0]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 23
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 23
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	S += c_cc_t31 >= 23
	c_cc_t31 += MAS[3]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 24
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 24
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 24
	c_bb_a1_1 += MAS[2]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 24
	c_cc_t2_t3 += MAS[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 25
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 25
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 25
	c_bb_a1_0 += MAS[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 26
	c_aa_a1_1 += MAS[2]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 26
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 26
	c_ab_t01_mem1 += MAS_MEM[3]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 26
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 26
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	S += c_ab_t01 >= 27
	c_ab_t01 += MAS[1]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 27
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 27
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 27
	c_bb_t3_t3 += MAS[3]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 28
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 28
	c_aa_t31_mem1 += MAS_MEM[5]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 28
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 28
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 28
	c_bb_t3_t2 += MAS[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 28
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 28
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 28
	c_bb_t3_t4_mem1 += MAS_MEM[7]

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	S += c_aa_t31 >= 29
	c_aa_t31 += MAS[0]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 29
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 29
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 29
	c_bb_t11 += MAS[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=8, delay_cost=1)
	S += c_bb_t3_t4 >= 29
	c_bb_t3_t4 += MM[0]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 30
	c_bb_t10 += MAS[3]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 30
	c_bb_t2_t3_mem0 += MAS_MEM[6]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 30
	c_bb_t2_t3_mem1 += MAS_MEM[3]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 30
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 30
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 30
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 31
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 31
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 31
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 31
	c_bb_t2_t3 += MAS[0]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=8, delay_cost=1)
	S += c_bc_t1_t0 >= 31
	c_bc_t1_t0 += MM[0]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=8, delay_cost=1)
	S += c_ac_t1_t1 >= 32
	c_ac_t1_t1 += MM[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 32
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 32
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 32
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=8, delay_cost=1)
	S += c_bc_t0_t1 >= 33
	c_bc_t0_t1 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 33
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 33
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 33
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 34
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 34
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 34
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=8, delay_cost=1)
	S += c_bc_t1_t1 >= 34
	c_bc_t1_t1 += MM[0]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=8, delay_cost=1)
	S += c_ac_t1_t0 >= 35
	c_ac_t1_t0 += MM[0]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 35
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 35
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 35
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 36
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 36
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 36
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 36
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 36
	c_bb_t31_mem1 += MAS_MEM[7]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=8, delay_cost=1)
	S += c_bc_t0_t0 >= 36
	c_bc_t0_t0 += MM[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 37
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 37
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 37
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=8, delay_cost=1)
	S += c_ac_t0_t1 >= 37
	c_ac_t0_t1 += MM[0]

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	S += c_bb_t31 >= 37
	c_bb_t31 += MAS[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 38
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 38
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=8, delay_cost=1)
	S += c_ac_t0_t0 >= 38
	c_ac_t0_t0 += MM[0]

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 39
	c_ab_t31 += MAS[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 39
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 39
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 40
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 40
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 40
	c_ac_t20 += MAS[0]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 41
	c_ab_t30 += MAS[3]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 41
	c_ab_t4_t3_mem0 += MAS_MEM[6]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 41
	c_ab_t4_t3_mem1 += MAS_MEM[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 41
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 41
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 41
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 41
	c_bc_t10_mem1 += MM_MEM[1]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 42
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 42
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 42
	c_ab_t4_t3 += MAS[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 42
	c_ac_t1_t3 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 42
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 42
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 42
	c_bc_t10 += MAS[2]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 43
	c_ab_t1_t3 += MAS[1]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 43
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 43
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 43
	c_ac_t1_t5 += MAS[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 43
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 43
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 44
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 44
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 44
	c_ac_t0_t3 += MAS[2]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 44
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 44
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 44
	c_bc_t0_t5 += MAS[0]

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 45
	c_ab_t20 += MAS[3]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 45
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 45
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 45
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 45
	c_ab_t4_t0_mem0 += MAS_MEM[6]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 45
	c_ab_t4_t0_mem1 += MAS_MEM[7]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 45
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 45
	c_ac_t10_mem1 += MM_MEM[1]

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 45
	c_bc_t00 += MAS[1]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 45
	c_bc_t50_mem0 += MAS_MEM[2]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 45
	c_bc_t50_mem1 += MAS_MEM[5]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 46
	c_ab_t21 += MAS[0]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=8, delay_cost=1)
	S += c_ab_t4_t0 >= 46
	c_ab_t4_t0 += MM[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 46
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 46
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 46
	c_ab_t4_t1_mem1 += MAS_MEM[1]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 46
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 46
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 46
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 46
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 46
	c_ac_t10 += MAS[2]

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	S += c_bc_t50 >= 46
	c_bc_t50 += MAS[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=8, delay_cost=1)
	S += c_ab_t4_t1 >= 47
	c_ab_t4_t1 += MM[0]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 47
	c_ab_t4_t2_mem0 += MAS_MEM[6]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 47
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 47
	c_ac_t00 += MAS[2]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 47
	c_ac_t0_t2 += MAS[0]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 47
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 47
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 47
	c_ac_t0_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 47
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 47
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 47
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 47
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 48
	c_ab_t4_t2 += MAS[3]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 48
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 48
	c_ab_t4_t4_mem0 += MAS_MEM[6]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 48
	c_ab_t4_t4_mem1 += MAS_MEM[3]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=8, delay_cost=1)
	S += c_ac_t0_t4 >= 48
	c_ac_t0_t4 += MM[0]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 48
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 48
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 48
	c_ac_t50_mem0 += MAS_MEM[4]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 48
	c_ac_t50_mem1 += MAS_MEM[5]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 48
	c_bc_t1_t5 += MAS[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 48
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 48
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 48
	c_bc_t30 += MAS[1]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=8, delay_cost=1)
	S += c_ab_t4_t4 >= 49
	c_ab_t4_t4 += MM[0]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 49
	c_ac_t0_t5 += MAS[1]

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	S += c_ac_t50 >= 49
	c_ac_t50 += MAS[2]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 49
	c_bc_t21 += MAS[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 49
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 49
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 50
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 50
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 50
	c_bc_t31 += MAS[3]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 50
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 50
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 50
	c_bc_t4_t1_mem1 += MAS_MEM[7]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 51
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 51
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 51
	c_ac_t21 += MAS[3]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 51
	c_ac_t4_t2_mem0 += MAS_MEM[0]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 51
	c_ac_t4_t2_mem1 += MAS_MEM[7]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=8, delay_cost=1)
	S += c_bc_t4_t1 >= 51
	c_bc_t4_t1 += MM[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 52
	c_ac_t1_t2 += MAS[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 52
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 52
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 52
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 52
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 52
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 52
	c_ac_t4_t2 += MAS[2]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 52
	c_bc_t4_t3_mem0 += MAS_MEM[2]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 52
	c_bc_t4_t3_mem1 += MAS_MEM[7]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=8, delay_cost=1)
	S += c_ac_t1_t4 >= 53
	c_ac_t1_t4 += MM[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 53
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 53
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 53
	c_ac_t31 += MAS[2]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 53
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 53
	c_ac_t4_t1_mem0 += MAS_MEM[6]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 53
	c_ac_t4_t1_mem1 += MAS_MEM[5]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 53
	c_bc_t4_t3 += MAS[3]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 54
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 54
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 54
	c_ac_t30 += MAS[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 54
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 54
	c_ac_t4_t0_mem0 += MAS_MEM[0]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 54
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=8, delay_cost=1)
	S += c_ac_t4_t1 >= 54
	c_ac_t4_t1 += MM[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 54
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 54
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 55
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 55
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 55
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 55
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	S += c_ab_t4_t5 >= 55
	c_ab_t4_t5 += MAS[0]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=8, delay_cost=1)
	S += c_ac_t4_t0 >= 55
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 55
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 55
	c_ac_t4_t3_mem1 += MAS_MEM[5]

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 55
	c_bc_t20 += MAS[2]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 55
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 55
	c_bc_t4_t0_mem0 += MAS_MEM[4]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 55
	c_bc_t4_t0_mem1 += MAS_MEM[3]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 56
	c_ab_t1_t2 += MAS[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 56
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 56
	c_ab_t1_t4_mem0 += MAS_MEM[2]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 56
	c_ab_t1_t4_mem1 += MAS_MEM[3]

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	S += c_ab_t40 >= 56
	c_ab_t40 += MAS[0]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 56
	c_ac_t4_t3 += MAS[3]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 56
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 56
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=8, delay_cost=1)
	S += c_bc_t4_t0 >= 56
	c_bc_t4_t0 += MM[0]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 56
	c_bc_t4_t2_mem0 += MAS_MEM[4]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 56
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=8, delay_cost=1)
	S += c_ab_t1_t4 >= 57
	c_ab_t1_t4 += MM[0]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 57
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 57
	c_ac_t01_mem1 += MAS_MEM[3]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 57
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 57
	c_ac_t4_t4_mem0 += MAS_MEM[4]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 57
	c_ac_t4_t4_mem1 += MAS_MEM[7]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 57
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 57
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 57
	c_bc_t1_t3 += MAS[3]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 57
	c_bc_t4_t2 += MAS[0]

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	S += c_ac_t01 >= 58
	c_ac_t01 += MAS[1]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=8, delay_cost=1)
	S += c_ac_t4_t4 >= 58
	c_ac_t4_t4 += MM[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 58
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 58
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 58
	c_bc_t1_t2 += MAS[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 58
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 58
	c_bc_t1_t4_mem0 += MAS_MEM[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 58
	c_bc_t1_t4_mem1 += MAS_MEM[7]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 59
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 59
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 59
	c_bc_t0_t3 += MAS[0]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=8, delay_cost=1)
	S += c_bc_t1_t4 >= 59
	c_bc_t1_t4 += MM[0]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 59
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 59
	c_bc_t4_t4_mem0 += MAS_MEM[0]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 59
	c_bc_t4_t4_mem1 += MAS_MEM[7]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 60
	c_bc_t0_t2 += MAS[1]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 60
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 60
	c_bc_t0_t4_mem0 += MAS_MEM[2]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 60
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=8, delay_cost=1)
	S += c_bc_t4_t4 >= 60
	c_bc_t4_t4 += MM[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 60
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 60
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 61
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 61
	c_ac_t11_mem1 += MAS_MEM[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=8, delay_cost=1)
	S += c_bc_t0_t4 >= 61
	c_bc_t0_t4 += MM[0]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 61
	c_pcb_t1_t3 += MAS[2]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 61
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 61
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	S += c_ac_t11 >= 62
	c_ac_t11 += MAS[1]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 62
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 62
	c_ac_t40_mem1 += MM_MEM[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 62
	c_pcb_t30 += MAS[3]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 62
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 62
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	S += c_ac_t40 >= 63
	c_ac_t40 += MAS[0]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 63
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 63
	c_bc_t40_mem1 += MM_MEM[1]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 63
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 63
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 63
	c_pcb_t31 += MAS[3]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 63
	c_pcb_t4_t3_mem0 += MAS_MEM[6]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 63
	c_pcb_t4_t3_mem1 += MAS_MEM[7]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 64
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 64
	c_ab_t11_mem1 += MAS_MEM[7]

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	S += c_bc_t40 >= 64
	c_bc_t40 += MAS[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 64
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 64
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 64
	c_pcb_t0_t3 += MAS[1]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 64
	c_pcb_t4_t3 += MAS[3]

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	S += c_ab_t11 >= 65
	c_ab_t11 += MAS[2]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 65
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 65
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 65
	c_paa_t0_t3 += MAS[1]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 65
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 65
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 66
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 66
	c_bc_t11_mem1 += MAS_MEM[1]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	S += c_bc_t4_t5 >= 66
	c_bc_t4_t5 += MAS[3]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 66
	c_paa_t1_t3 += MAS[1]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 66
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 66
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 67
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 67
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	S += c_bc_t11 >= 67
	c_bc_t11 += MAS[1]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 67
	c_paa_t30 += MAS[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 67
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 67
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	S += c_ac_t4_t5 >= 68
	c_ac_t4_t5 += MAS[1]

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 68
	c_paa_t31 += MAS[0]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 68
	c_paa_t4_t3_mem0 += MAS_MEM[0]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 68
	c_paa_t4_t3_mem1 += MAS_MEM[1]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 68
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 68
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 69
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 69
	c_bc_t01_mem1 += MAS_MEM[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 69
	c_paa_t4_t3 += MAS[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 69
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 69
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 69
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	S += c_bc_t01 >= 70
	c_bc_t01 += MAS[1]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 70
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 70
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 70
	c_pbc_t31 += MAS[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 71
	c_pbc_t1_t3 += MAS[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 71
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 71
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 72
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 72
	c_aa_t00_mem1 += MAS_MEM[5]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 72
	c_pbc_t30 += MAS[3]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 72
	c_pbc_t4_t3_mem0 += MAS_MEM[6]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 72
	c_pbc_t4_t3_mem1 += MAS_MEM[1]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 73
	c_aa_t00 += MAS[3]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 73
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 73
	c_aa_t2_t0_mem0 += MAS_MEM[6]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 73
	c_aa_t2_t0_mem1 += MAS_MEM[3]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 73
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 73
	c_bb_t01_mem1 += MAS_MEM[5]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 73
	c_pbc_t4_t3 += MAS[0]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=8, delay_cost=1)
	S += c_aa_t2_t0 >= 74
	c_aa_t2_t0 += MM[0]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 74
	c_bb_t01 += MAS[2]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 74
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 74
	c_bb_t2_t1_mem0 += MAS_MEM[4]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 74
	c_bb_t2_t1_mem1 += MAS_MEM[3]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 74
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 74
	c_cc_t00_mem1 += MAS_MEM[1]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 75
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 75
	c_bb_t00_mem1 += MAS_MEM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=8, delay_cost=1)
	S += c_bb_t2_t1 >= 75
	c_bb_t2_t1 += MM[0]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 75
	c_cc_t00 += MAS[0]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 76
	c_bb_t00 += MAS[0]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 76
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 76
	c_bb_t2_t0_mem0 += MAS_MEM[0]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 76
	c_bb_t2_t0_mem1 += MAS_MEM[7]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 76
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 76
	c_cc_t01_mem1 += MAS_MEM[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 77
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 77
	c_aa_t01_mem1 += MAS_MEM[5]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=8, delay_cost=1)
	S += c_bb_t2_t0 >= 77
	c_bb_t2_t0 += MM[0]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 77
	c_cc_t01 += MAS[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 77
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 77
	c_cc_t2_t1_mem0 += MAS_MEM[2]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 77
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 77
	c_cc_t2_t2_mem0 += MAS_MEM[0]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 77
	c_cc_t2_t2_mem1 += MAS_MEM[3]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 78
	c_aa_t01 += MAS[1]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 78
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 78
	c_aa_t2_t1_mem0 += MAS_MEM[2]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 78
	c_aa_t2_t1_mem1 += MAS_MEM[5]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 78
	c_aa_t2_t2_mem0 += MAS_MEM[6]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 78
	c_aa_t2_t2_mem1 += MAS_MEM[3]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=8, delay_cost=1)
	S += c_cc_t2_t1 >= 78
	c_cc_t2_t1 += MM[0]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	S += c_cc_t2_t2 >= 78
	c_cc_t2_t2 += MAS[2]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=8, delay_cost=1)
	S += c_aa_t2_t1 >= 79
	c_aa_t2_t1 += MM[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	S += c_aa_t2_t2 >= 79
	c_aa_t2_t2 += MAS[0]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 79
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 79
	c_cc_t2_t0_mem0 += MAS_MEM[0]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 79
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 80
	c_bb_t2_t2_mem0 += MAS_MEM[0]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 80
	c_bb_t2_t2_mem1 += MAS_MEM[5]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=8, delay_cost=1)
	S += c_cc_t2_t0 >= 80
	c_cc_t2_t0 += MM[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	S += c_bb_t2_t2 >= 81
	c_bb_t2_t2 += MAS[0]


	# new tasks
	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=8, delay_cost=1)
	c_aa_t2_t4 += alt(MM)
	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	c_aa_t2_t4_in += alt(MM_in)
	S += c_aa_t2_t4_in*MM_in[0]<=c_aa_t2_t4*MM[0]
	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	c_aa_t2_t4_mem0 += MAS_MEM[0]
	S += 79 < c_aa_t2_t4_mem0
	S += c_aa_t2_t4_mem0 <= c_aa_t2_t4

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	c_aa_t2_t4_mem1 += MAS_MEM[3]
	S += 23 < c_aa_t2_t4_mem1
	S += c_aa_t2_t4_mem1 <= c_aa_t2_t4

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	c_aa_t20 += alt(MAS)
	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	c_aa_t20_mem0 += MM_MEM[0]
	S += 81 < c_aa_t20_mem0
	S += c_aa_t20_mem0 <= c_aa_t20

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	c_aa_t20_mem1 += MM_MEM[1]
	S += 86 < c_aa_t20_mem1
	S += c_aa_t20_mem1 <= c_aa_t20

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	c_aa_t2_t5 += alt(MAS)
	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	c_aa_t2_t5_mem0 += MM_MEM[0]
	S += 81 < c_aa_t2_t5_mem0
	S += c_aa_t2_t5_mem0 <= c_aa_t2_t5

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	c_aa_t2_t5_mem1 += MM_MEM[1]
	S += 86 < c_aa_t2_t5_mem1
	S += c_aa_t2_t5_mem1 <= c_aa_t2_t5

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	c_aa_t40 += alt(MAS)
	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	c_aa_t40_mem0 += MAS_MEM[2]
	S += 19 < c_aa_t40_mem0
	S += c_aa_t40_mem0 <= c_aa_t40

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	c_aa_t40_mem1 += MAS_MEM[1]
	S += 29 < c_aa_t40_mem1
	S += c_aa_t40_mem1 <= c_aa_t40

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	c_aa_t41 += alt(MAS)
	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	c_aa_t41_mem0 += MAS_MEM[0]
	S += 29 < c_aa_t41_mem0
	S += c_aa_t41_mem0 <= c_aa_t41

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	c_aa_t41_mem1 += MAS_MEM[3]
	S += 19 < c_aa_t41_mem1
	S += c_aa_t41_mem1 <= c_aa_t41

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	c_aa11 += alt(MAS)
	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	c_aa11_mem0 += MAS_MEM[0]
	S += 29 < c_aa11_mem0
	S += c_aa11_mem0 <= c_aa11

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	c_aa11_mem1 += MAS_MEM[1]
	S += 29 < c_aa11_mem1
	S += c_aa11_mem1 <= c_aa11

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=8, delay_cost=1)
	c_bb_t2_t4 += alt(MM)
	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	c_bb_t2_t4_in += alt(MM_in)
	S += c_bb_t2_t4_in*MM_in[0]<=c_bb_t2_t4*MM[0]
	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	c_bb_t2_t4_mem0 += MAS_MEM[0]
	S += 81 < c_bb_t2_t4_mem0
	S += c_bb_t2_t4_mem0 <= c_bb_t2_t4

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	c_bb_t2_t4_mem1 += MAS_MEM[1]
	S += 31 < c_bb_t2_t4_mem1
	S += c_bb_t2_t4_mem1 <= c_bb_t2_t4

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	c_bb_t20 += alt(MAS)
	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	c_bb_t20_mem0 += MM_MEM[0]
	S += 84 < c_bb_t20_mem0
	S += c_bb_t20_mem0 <= c_bb_t20

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	c_bb_t20_mem1 += MM_MEM[1]
	S += 82 < c_bb_t20_mem1
	S += c_bb_t20_mem1 <= c_bb_t20

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	c_bb_t2_t5 += alt(MAS)
	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	c_bb_t2_t5_mem0 += MM_MEM[0]
	S += 84 < c_bb_t2_t5_mem0
	S += c_bb_t2_t5_mem0 <= c_bb_t2_t5

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	c_bb_t2_t5_mem1 += MM_MEM[1]
	S += 82 < c_bb_t2_t5_mem1
	S += c_bb_t2_t5_mem1 <= c_bb_t2_t5

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	c_bb_t40 += alt(MAS)
	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	c_bb_t40_mem0 += MAS_MEM[2]
	S += 20 < c_bb_t40_mem0
	S += c_bb_t40_mem0 <= c_bb_t40

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	c_bb_t40_mem1 += MAS_MEM[1]
	S += 37 < c_bb_t40_mem1
	S += c_bb_t40_mem1 <= c_bb_t40

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	c_bb_t41 += alt(MAS)
	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	c_bb_t41_mem0 += MAS_MEM[0]
	S += 37 < c_bb_t41_mem0
	S += c_bb_t41_mem0 <= c_bb_t41

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	c_bb_t41_mem1 += MAS_MEM[3]
	S += 20 < c_bb_t41_mem1
	S += c_bb_t41_mem1 <= c_bb_t41

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	c_bb11 += alt(MAS)
	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	c_bb11_mem0 += MAS_MEM[0]
	S += 37 < c_bb11_mem0
	S += c_bb11_mem0 <= c_bb11

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	c_bb11_mem1 += MAS_MEM[1]
	S += 37 < c_bb11_mem1
	S += c_bb11_mem1 <= c_bb11

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=8, delay_cost=1)
	c_cc_t2_t4 += alt(MM)
	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	c_cc_t2_t4_in += alt(MM_in)
	S += c_cc_t2_t4_in*MM_in[0]<=c_cc_t2_t4*MM[0]
	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	c_cc_t2_t4_mem0 += MAS_MEM[4]
	S += 78 < c_cc_t2_t4_mem0
	S += c_cc_t2_t4_mem0 <= c_cc_t2_t4

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	c_cc_t2_t4_mem1 += MAS_MEM[1]
	S += 24 < c_cc_t2_t4_mem1
	S += c_cc_t2_t4_mem1 <= c_cc_t2_t4

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	c_cc_t20 += alt(MAS)
	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	c_cc_t20_mem0 += MM_MEM[0]
	S += 87 < c_cc_t20_mem0
	S += c_cc_t20_mem0 <= c_cc_t20

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	c_cc_t20_mem1 += MM_MEM[1]
	S += 85 < c_cc_t20_mem1
	S += c_cc_t20_mem1 <= c_cc_t20

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	c_cc_t2_t5 += alt(MAS)
	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	c_cc_t2_t5_mem0 += MM_MEM[0]
	S += 87 < c_cc_t2_t5_mem0
	S += c_cc_t2_t5_mem0 <= c_cc_t2_t5

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	c_cc_t2_t5_mem1 += MM_MEM[1]
	S += 85 < c_cc_t2_t5_mem1
	S += c_cc_t2_t5_mem1 <= c_cc_t2_t5

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	c_cc_t40 += alt(MAS)
	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	c_cc_t40_mem0 += MAS_MEM[0]
	S += 11 < c_cc_t40_mem0
	S += c_cc_t40_mem0 <= c_cc_t40

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	c_cc_t40_mem1 += MAS_MEM[7]
	S += 23 < c_cc_t40_mem1
	S += c_cc_t40_mem1 <= c_cc_t40

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	c_cc_t41 += alt(MAS)
	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	c_cc_t41_mem0 += MAS_MEM[6]
	S += 23 < c_cc_t41_mem0
	S += c_cc_t41_mem0 <= c_cc_t41

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	c_cc_t41_mem1 += MAS_MEM[1]
	S += 11 < c_cc_t41_mem1
	S += c_cc_t41_mem1 <= c_cc_t41

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	c_cc11 += alt(MAS)
	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	c_cc11_mem0 += MAS_MEM[6]
	S += 23 < c_cc11_mem0
	S += c_cc11_mem0 <= c_cc11

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	c_cc11_mem1 += MAS_MEM[7]
	S += 23 < c_cc11_mem1
	S += c_cc11_mem1 <= c_cc11

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	c_ab_t41 += alt(MAS)
	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	c_ab_t41_mem0 += MM_MEM[0]
	S += 56 < c_ab_t41_mem0
	S += c_ab_t41_mem0 <= c_ab_t41

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	c_ab_t41_mem1 += MAS_MEM[1]
	S += 55 < c_ab_t41_mem1
	S += c_ab_t41_mem1 <= c_ab_t41

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	c_ab_s00 += alt(MAS)
	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	c_ab_s00_mem0 += MAS_MEM[6]
	S += 13 < c_ab_s00_mem0
	S += c_ab_s00_mem0 <= c_ab_s00

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	c_ab_s00_mem1 += MAS_MEM[5]
	S += 65 < c_ab_s00_mem1
	S += c_ab_s00_mem1 <= c_ab_s00

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	c_ab_s01 += alt(MAS)
	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	c_ab_s01_mem0 += MAS_MEM[4]
	S += 65 < c_ab_s01_mem0
	S += c_ab_s01_mem0 <= c_ab_s01

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	c_ab_s01_mem1 += MAS_MEM[7]
	S += 13 < c_ab_s01_mem1
	S += c_ab_s01_mem1 <= c_ab_s01

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	c_ab_t51 += alt(MAS)
	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	c_ab_t51_mem0 += MAS_MEM[2]
	S += 27 < c_ab_t51_mem0
	S += c_ab_t51_mem0 <= c_ab_t51

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	c_ab_t51_mem1 += MAS_MEM[5]
	S += 65 < c_ab_t51_mem1
	S += c_ab_t51_mem1 <= c_ab_t51

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	c_ab10 += alt(MAS)
	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	c_ab10_mem0 += MAS_MEM[0]
	S += 56 < c_ab10_mem0
	S += c_ab10_mem0 <= c_ab10

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	c_ab10_mem1 += MAS_MEM[3]
	S += 18 < c_ab10_mem1
	S += c_ab10_mem1 <= c_ab10

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	c_bc_t41 += alt(MAS)
	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	c_bc_t41_mem0 += MM_MEM[0]
	S += 67 < c_bc_t41_mem0
	S += c_bc_t41_mem0 <= c_bc_t41

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	c_bc_t41_mem1 += MAS_MEM[7]
	S += 66 < c_bc_t41_mem1
	S += c_bc_t41_mem1 <= c_bc_t41

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	c_bc_s00 += alt(MAS)
	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	c_bc_s00_mem0 += MAS_MEM[4]
	S += 42 < c_bc_s00_mem0
	S += c_bc_s00_mem0 <= c_bc_s00

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	c_bc_s00_mem1 += MAS_MEM[3]
	S += 67 < c_bc_s00_mem1
	S += c_bc_s00_mem1 <= c_bc_s00

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	c_bc_s01 += alt(MAS)
	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	c_bc_s01_mem0 += MAS_MEM[2]
	S += 67 < c_bc_s01_mem0
	S += c_bc_s01_mem0 <= c_bc_s01

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	c_bc_s01_mem1 += MAS_MEM[5]
	S += 42 < c_bc_s01_mem1
	S += c_bc_s01_mem1 <= c_bc_s01

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	c_bc_t51 += alt(MAS)
	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	c_bc_t51_mem0 += MAS_MEM[2]
	S += 70 < c_bc_t51_mem0
	S += c_bc_t51_mem0 <= c_bc_t51

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	c_bc_t51_mem1 += MAS_MEM[3]
	S += 67 < c_bc_t51_mem1
	S += c_bc_t51_mem1 <= c_bc_t51

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	c_bc10 += alt(MAS)
	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	c_bc10_mem0 += MAS_MEM[0]
	S += 64 < c_bc10_mem0
	S += c_bc10_mem0 <= c_bc10

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	c_bc10_mem1 += MAS_MEM[3]
	S += 46 < c_bc10_mem1
	S += c_bc10_mem1 <= c_bc10

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	c_ac_t41 += alt(MAS)
	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	c_ac_t41_mem0 += MM_MEM[0]
	S += 65 < c_ac_t41_mem0
	S += c_ac_t41_mem0 <= c_ac_t41

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	c_ac_t41_mem1 += MAS_MEM[3]
	S += 68 < c_ac_t41_mem1
	S += c_ac_t41_mem1 <= c_ac_t41

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	c_ac_s00 += alt(MAS)
	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	c_ac_s00_mem0 += MAS_MEM[4]
	S += 46 < c_ac_s00_mem0
	S += c_ac_s00_mem0 <= c_ac_s00

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	c_ac_s00_mem1 += MAS_MEM[3]
	S += 62 < c_ac_s00_mem1
	S += c_ac_s00_mem1 <= c_ac_s00

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	c_ac_s01 += alt(MAS)
	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	c_ac_s01_mem0 += MAS_MEM[2]
	S += 62 < c_ac_s01_mem0
	S += c_ac_s01_mem0 <= c_ac_s01

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	c_ac_s01_mem1 += MAS_MEM[5]
	S += 46 < c_ac_s01_mem1
	S += c_ac_s01_mem1 <= c_ac_s01

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	c_ac_t51 += alt(MAS)
	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	c_ac_t51_mem0 += MAS_MEM[2]
	S += 58 < c_ac_t51_mem0
	S += c_ac_t51_mem0 <= c_ac_t51

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	c_ac_t51_mem1 += MAS_MEM[3]
	S += 62 < c_ac_t51_mem1
	S += c_ac_t51_mem1 <= c_ac_t51

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	c_ac10 += alt(MAS)
	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	c_ac10_mem0 += MAS_MEM[0]
	S += 63 < c_ac10_mem0
	S += c_ac10_mem0 <= c_ac10

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	c_ac10_mem1 += MAS_MEM[5]
	S += 49 < c_ac10_mem1
	S += c_ac10_mem1 <= c_ac10

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS4/FP12_INV_BEFORE_FPINV/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

