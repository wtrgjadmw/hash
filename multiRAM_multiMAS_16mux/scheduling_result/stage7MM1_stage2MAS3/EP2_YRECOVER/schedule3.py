from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 197
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=3)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=3, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=6)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	r13_t3_in = S.Task('r13_t3_in', length=1, delay_cost=1)
	S += r13_t3_in >= 0
	r13_t3_in += MAS_in[1]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 0
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 0
	r13_t3_mem1 += MAIN_MEM_r[1]

	r13_t3 = S.Task('r13_t3', length=2, delay_cost=1)
	S += r13_t3 >= 1
	r13_t3 += MAS[1]

	r1_t3_in = S.Task('r1_t3_in', length=1, delay_cost=1)
	S += r1_t3_in >= 1
	r1_t3_in += MAS_in[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 1
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 1
	r1_t3_mem1 += MAIN_MEM_r[1]

	r1_t3 = S.Task('r1_t3', length=2, delay_cost=1)
	S += r1_t3 >= 2
	r1_t3 += MAS[0]

	r4_t2_in = S.Task('r4_t2_in', length=1, delay_cost=1)
	S += r4_t2_in >= 2
	r4_t2_in += MAS_in[2]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 2
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 2
	r4_t2_mem1 += MAIN_MEM_r[1]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 3
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 3
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 3
	r12_t1_mem1 += MAIN_MEM_r[1]

	r4_t2 = S.Task('r4_t2', length=2, delay_cost=1)
	S += r4_t2 >= 3
	r4_t2 += MAS[2]

	r12_t1 = S.Task('r12_t1', length=7, delay_cost=1)
	S += r12_t1 >= 4
	r12_t1 += MM[0]

	r6_t2_in = S.Task('r6_t2_in', length=1, delay_cost=1)
	S += r6_t2_in >= 4
	r6_t2_in += MAS_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 4
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 4
	r6_t2_mem1 += MAIN_MEM_r[1]

	r5_t3_in = S.Task('r5_t3_in', length=1, delay_cost=1)
	S += r5_t3_in >= 5
	r5_t3_in += MAS_in[2]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 5
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 5
	r5_t3_mem1 += MAIN_MEM_r[1]

	r6_t2 = S.Task('r6_t2', length=2, delay_cost=1)
	S += r6_t2 >= 5
	r6_t2 += MAS[0]

	r1_t2_in = S.Task('r1_t2_in', length=1, delay_cost=1)
	S += r1_t2_in >= 6
	r1_t2_in += MAS_in[2]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 6
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 6
	r1_t2_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=2, delay_cost=1)
	S += r5_t3 >= 6
	r5_t3 += MAS[2]

	r1_t2 = S.Task('r1_t2', length=2, delay_cost=1)
	S += r1_t2 >= 7
	r1_t2 += MAS[2]

	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 7
	r6_t1_in += MM_in[0]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 7
	r6_t1_mem0 += MAIN_MEM_r[0]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 7
	r6_t1_mem1 += MAIN_MEM_r[1]

	r12_t2_in = S.Task('r12_t2_in', length=1, delay_cost=1)
	S += r12_t2_in >= 8
	r12_t2_in += MAS_in[2]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 8
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 8
	r12_t2_mem1 += MAIN_MEM_r[1]

	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	S += r1_t4_in >= 8
	r1_t4_in += MM_in[0]

	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	S += r1_t4_mem0 >= 8
	r1_t4_mem0 += MAS_MEM[4]

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	S += r1_t4_mem1 >= 8
	r1_t4_mem1 += MAS_MEM[1]

	r6_t1 = S.Task('r6_t1', length=7, delay_cost=1)
	S += r6_t1 >= 8
	r6_t1 += MM[0]

	r12_t2 = S.Task('r12_t2', length=2, delay_cost=1)
	S += r12_t2 >= 9
	r12_t2 += MAS[2]

	r1_t4 = S.Task('r1_t4', length=7, delay_cost=1)
	S += r1_t4 >= 9
	r1_t4 += MM[0]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 9
	r5_t0_in += MM_in[0]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 9
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 9
	r5_t0_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=7, delay_cost=1)
	S += r5_t0 >= 10
	r5_t0 += MM[0]

	r6_t3_in = S.Task('r6_t3_in', length=1, delay_cost=1)
	S += r6_t3_in >= 10
	r6_t3_in += MAS_in[2]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 10
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 10
	r6_t3_mem1 += MAIN_MEM_r[1]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 11
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 11
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 11
	r4_t1_mem1 += MAIN_MEM_r[1]

	r6_t3 = S.Task('r6_t3', length=2, delay_cost=1)
	S += r6_t3 >= 11
	r6_t3 += MAS[2]

	r13_t2_in = S.Task('r13_t2_in', length=1, delay_cost=1)
	S += r13_t2_in >= 12
	r13_t2_in += MAS_in[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 12
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 12
	r13_t2_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=7, delay_cost=1)
	S += r4_t1 >= 12
	r4_t1 += MM[0]

	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	S += r6_t4_in >= 12
	r6_t4_in += MM_in[0]

	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	S += r6_t4_mem0 >= 12
	r6_t4_mem0 += MAS_MEM[0]

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	S += r6_t4_mem1 >= 12
	r6_t4_mem1 += MAS_MEM[5]

	r13_t2 = S.Task('r13_t2', length=2, delay_cost=1)
	S += r13_t2 >= 13
	r13_t2 += MAS[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 13
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 13
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 13
	r4_t0_mem1 += MAIN_MEM_r[1]

	r6_t4 = S.Task('r6_t4', length=7, delay_cost=1)
	S += r6_t4 >= 13
	r6_t4 += MM[0]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 14
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 14
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 14
	r3_t1_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=7, delay_cost=1)
	S += r4_t0 >= 14
	r4_t0 += MM[0]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 15
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 15
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 15
	r3_t0_mem1 += MAIN_MEM_r[1]

	r3_t1 = S.Task('r3_t1', length=7, delay_cost=1)
	S += r3_t1 >= 15
	r3_t1 += MM[0]

	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	S += r13_t4_in >= 16
	r13_t4_in += MM_in[0]

	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	S += r13_t4_mem0 >= 16
	r13_t4_mem0 += MAS_MEM[0]

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	S += r13_t4_mem1 >= 16
	r13_t4_mem1 += MAS_MEM[3]

	r3_t0 = S.Task('r3_t0', length=7, delay_cost=1)
	S += r3_t0 >= 16
	r3_t0 += MM[0]

	r9_t2_in = S.Task('r9_t2_in', length=1, delay_cost=1)
	S += r9_t2_in >= 16
	r9_t2_in += MAS_in[0]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 16
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 16
	r9_t2_mem1 += MAIN_MEM_r[1]

	r13_t4 = S.Task('r13_t4', length=7, delay_cost=1)
	S += r13_t4 >= 17
	r13_t4 += MM[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 17
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 17
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 17
	r5_t1_mem1 += MAIN_MEM_r[1]

	r9_t2 = S.Task('r9_t2', length=2, delay_cost=1)
	S += r9_t2 >= 17
	r9_t2 += MAS[0]

	r12_t3_in = S.Task('r12_t3_in', length=1, delay_cost=1)
	S += r12_t3_in >= 18
	r12_t3_in += MAS_in[0]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 18
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 18
	r12_t3_mem1 += MAIN_MEM_r[1]

	r5_t1 = S.Task('r5_t1', length=7, delay_cost=1)
	S += r5_t1 >= 18
	r5_t1 += MM[0]

	r12_t3 = S.Task('r12_t3', length=2, delay_cost=1)
	S += r12_t3 >= 19
	r12_t3 += MAS[0]

	r3_t2_in = S.Task('r3_t2_in', length=1, delay_cost=1)
	S += r3_t2_in >= 19
	r3_t2_in += MAS_in[2]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 19
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 19
	r3_t2_mem1 += MAIN_MEM_r[1]

	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	S += r12_t4_in >= 20
	r12_t4_in += MM_in[0]

	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	S += r12_t4_mem0 >= 20
	r12_t4_mem0 += MAS_MEM[4]

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	S += r12_t4_mem1 >= 20
	r12_t4_mem1 += MAS_MEM[1]

	r3_t2 = S.Task('r3_t2', length=2, delay_cost=1)
	S += r3_t2 >= 20
	r3_t2 += MAS[2]

	r40_in = S.Task('r40_in', length=1, delay_cost=1)
	S += r40_in >= 20
	r40_in += MAS_in[0]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	S += r40_mem0 >= 20
	r40_mem0 += MM_MEM[0]

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	S += r40_mem1 >= 20
	r40_mem1 += MM_MEM[1]

	r5_t2_in = S.Task('r5_t2_in', length=1, delay_cost=1)
	S += r5_t2_in >= 20
	r5_t2_in += MAS_in[1]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 20
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 20
	r5_t2_mem1 += MAIN_MEM_r[1]

	r12_t4 = S.Task('r12_t4', length=7, delay_cost=1)
	S += r12_t4 >= 21
	r12_t4 += MM[0]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 21
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 21
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 21
	r1_t1_mem1 += MAIN_MEM_r[1]

	r40 = S.Task('r40', length=2, delay_cost=1)
	S += r40 >= 21
	r40 += MAS[0]

	r4_t5_in = S.Task('r4_t5_in', length=1, delay_cost=1)
	S += r4_t5_in >= 21
	r4_t5_in += MAS_in[1]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	S += r4_t5_mem0 >= 21
	r4_t5_mem0 += MM_MEM[0]

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	S += r4_t5_mem1 >= 21
	r4_t5_mem1 += MM_MEM[1]

	r5_t2 = S.Task('r5_t2', length=2, delay_cost=1)
	S += r5_t2 >= 21
	r5_t2 += MAS[1]

	r1_t1 = S.Task('r1_t1', length=7, delay_cost=1)
	S += r1_t1 >= 22
	r1_t1 += MM[0]

	r3_t5_in = S.Task('r3_t5_in', length=1, delay_cost=1)
	S += r3_t5_in >= 22
	r3_t5_in += MAS_in[1]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	S += r3_t5_mem0 >= 22
	r3_t5_mem0 += MM_MEM[0]

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	S += r3_t5_mem1 >= 22
	r3_t5_mem1 += MM_MEM[1]

	r4_t3_in = S.Task('r4_t3_in', length=1, delay_cost=1)
	S += r4_t3_in >= 22
	r4_t3_in += MAS_in[0]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 22
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 22
	r4_t3_mem1 += MAIN_MEM_r[1]

	r4_t5 = S.Task('r4_t5', length=2, delay_cost=1)
	S += r4_t5 >= 22
	r4_t5 += MAS[1]

	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	S += r5_t4_in >= 22
	r5_t4_in += MM_in[0]

	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	S += r5_t4_mem0 >= 22
	r5_t4_mem0 += MAS_MEM[2]

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	S += r5_t4_mem1 >= 22
	r5_t4_mem1 += MAS_MEM[5]

	r30_in = S.Task('r30_in', length=1, delay_cost=1)
	S += r30_in >= 23
	r30_in += MAS_in[0]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	S += r30_mem0 >= 23
	r30_mem0 += MM_MEM[0]

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	S += r30_mem1 >= 23
	r30_mem1 += MM_MEM[1]

	r3_t3_in = S.Task('r3_t3_in', length=1, delay_cost=1)
	S += r3_t3_in >= 23
	r3_t3_in += MAS_in[1]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 23
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 23
	r3_t3_mem1 += MAIN_MEM_r[1]

	r3_t5 = S.Task('r3_t5', length=2, delay_cost=1)
	S += r3_t5 >= 23
	r3_t5 += MAS[1]

	r4_t3 = S.Task('r4_t3', length=2, delay_cost=1)
	S += r4_t3 >= 23
	r4_t3 += MAS[0]

	r5_t4 = S.Task('r5_t4', length=7, delay_cost=1)
	S += r5_t4 >= 23
	r5_t4 += MM[0]

	r16_t3_in = S.Task('r16_t3_in', length=1, delay_cost=1)
	S += r16_t3_in >= 24
	r16_t3_in += MAS_in[0]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 24
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 24
	r16_t3_mem1 += MAIN_MEM_r[1]

	r30 = S.Task('r30', length=2, delay_cost=1)
	S += r30 >= 24
	r30 += MAS[0]

	r3_t3 = S.Task('r3_t3', length=2, delay_cost=1)
	S += r3_t3 >= 24
	r3_t3 += MAS[1]

	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	S += r4_t4_in >= 24
	r4_t4_in += MM_in[0]

	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	S += r4_t4_mem0 >= 24
	r4_t4_mem0 += MAS_MEM[4]

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	S += r4_t4_mem1 >= 24
	r4_t4_mem1 += MAS_MEM[1]

	r50_in = S.Task('r50_in', length=1, delay_cost=1)
	S += r50_in >= 24
	r50_in += MAS_in[1]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	S += r50_mem0 >= 24
	r50_mem0 += MM_MEM[0]

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	S += r50_mem1 >= 24
	r50_mem1 += MM_MEM[1]

	r16_t3 = S.Task('r16_t3', length=2, delay_cost=1)
	S += r16_t3 >= 25
	r16_t3 += MAS[0]

	r4_t4 = S.Task('r4_t4', length=7, delay_cost=1)
	S += r4_t4 >= 25
	r4_t4 += MM[0]

	r50 = S.Task('r50', length=2, delay_cost=1)
	S += r50 >= 25
	r50 += MAS[1]

	r5_t5_in = S.Task('r5_t5_in', length=1, delay_cost=1)
	S += r5_t5_in >= 25
	r5_t5_in += MAS_in[0]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	S += r5_t5_mem0 >= 25
	r5_t5_mem0 += MM_MEM[0]

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	S += r5_t5_mem1 >= 25
	r5_t5_mem1 += MM_MEM[1]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 25
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 25
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 25
	r6_t0_mem1 += MAIN_MEM_r[1]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 26
	r1_t0_in += MM_in[0]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 26
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 26
	r1_t0_mem1 += MAIN_MEM_r[1]

	r5_t5 = S.Task('r5_t5', length=2, delay_cost=1)
	S += r5_t5 >= 26
	r5_t5 += MAS[0]

	r6_t0 = S.Task('r6_t0', length=7, delay_cost=1)
	S += r6_t0 >= 26
	r6_t0 += MM[0]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 27
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 27
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 27
	r13_t1_mem1 += MAIN_MEM_r[1]

	r1_t0 = S.Task('r1_t0', length=7, delay_cost=1)
	S += r1_t0 >= 27
	r1_t0 += MM[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 28
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 28
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 28
	r13_t0_mem1 += MAIN_MEM_r[1]

	r13_t1 = S.Task('r13_t1', length=7, delay_cost=1)
	S += r13_t1 >= 28
	r13_t1 += MM[0]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 29
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 29
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 29
	r12_t0_mem1 += MAIN_MEM_r[1]

	r13_t0 = S.Task('r13_t0', length=7, delay_cost=1)
	S += r13_t0 >= 29
	r13_t0 += MM[0]

	r51_in = S.Task('r51_in', length=1, delay_cost=1)
	S += r51_in >= 29
	r51_in += MAS_in[0]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	S += r51_mem0 >= 29
	r51_mem0 += MM_MEM[0]

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	S += r51_mem1 >= 29
	r51_mem1 += MAS_MEM[1]

	r100_in = S.Task('r100_in', length=1, delay_cost=1)
	S += r100_in >= 30
	r100_in += MAS_in[0]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	S += r100_mem0 >= 30
	r100_mem0 += MAIN_MEM_r[0]

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	S += r100_mem1 >= 30
	r100_mem1 += MAS_MEM[1]

	r12_t0 = S.Task('r12_t0', length=7, delay_cost=1)
	S += r12_t0 >= 30
	r12_t0 += MM[0]

	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	S += r3_t4_in >= 30
	r3_t4_in += MM_in[0]

	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	S += r3_t4_mem0 >= 30
	r3_t4_mem0 += MAS_MEM[4]

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	S += r3_t4_mem1 >= 30
	r3_t4_mem1 += MAS_MEM[3]

	r51 = S.Task('r51', length=2, delay_cost=1)
	S += r51 >= 30
	r51 += MAS[0]

	r100 = S.Task('r100', length=2, delay_cost=1)
	S += r100 >= 31
	r100 += MAS[0]

	r3_t4 = S.Task('r3_t4', length=7, delay_cost=1)
	S += r3_t4 >= 31
	r3_t4 += MM[0]

	r41_in = S.Task('r41_in', length=1, delay_cost=1)
	S += r41_in >= 31
	r41_in += MAS_in[0]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	S += r41_mem0 >= 31
	r41_mem0 += MM_MEM[0]

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	S += r41_mem1 >= 31
	r41_mem1 += MAS_MEM[3]

	r80_in = S.Task('r80_in', length=1, delay_cost=1)
	S += r80_in >= 31
	r80_in += MAS_in[1]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	S += r80_mem0 >= 31
	r80_mem0 += MAIN_MEM_r[0]

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	S += r80_mem1 >= 31
	r80_mem1 += MAS_MEM[1]

	r41 = S.Task('r41', length=2, delay_cost=1)
	S += r41 >= 32
	r41 += MAS[0]

	r60_in = S.Task('r60_in', length=1, delay_cost=1)
	S += r60_in >= 32
	r60_in += MAS_in[2]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	S += r60_mem0 >= 32
	r60_mem0 += MM_MEM[0]

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	S += r60_mem1 >= 32
	r60_mem1 += MM_MEM[1]

	r80 = S.Task('r80', length=2, delay_cost=1)
	S += r80 >= 32
	r80 += MAS[1]

	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	S += r10_in >= 33
	r10_in += MAS_in[0]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	S += r10_mem0 >= 33
	r10_mem0 += MM_MEM[0]

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	S += r10_mem1 >= 33
	r10_mem1 += MM_MEM[1]

	r60 = S.Task('r60', length=2, delay_cost=1)
	S += r60 >= 33
	r60 += MAS[2]

	r81_in = S.Task('r81_in', length=1, delay_cost=1)
	S += r81_in >= 33
	r81_in += MAS_in[2]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	S += r81_mem0 >= 33
	r81_mem0 += MAIN_MEM_r[0]

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	S += r81_mem1 >= 33
	r81_mem1 += MAS_MEM[1]

	r10 = S.Task('r10', length=2, delay_cost=1)
	S += r10 >= 34
	r10 += MAS[0]

	r101_in = S.Task('r101_in', length=1, delay_cost=1)
	S += r101_in >= 34
	r101_in += MAS_in[1]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	S += r101_mem0 >= 34
	r101_mem0 += MAIN_MEM_r[0]

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	S += r101_mem1 >= 34
	r101_mem1 += MAS_MEM[1]

	r1_t5_in = S.Task('r1_t5_in', length=1, delay_cost=1)
	S += r1_t5_in >= 34
	r1_t5_in += MAS_in[0]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	S += r1_t5_mem0 >= 34
	r1_t5_mem0 += MM_MEM[0]

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	S += r1_t5_mem1 >= 34
	r1_t5_mem1 += MM_MEM[1]

	r70_in = S.Task('r70_in', length=1, delay_cost=1)
	S += r70_in >= 34
	r70_in += MAS_in[2]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	S += r70_mem0 >= 34
	r70_mem0 += MAS_MEM[2]

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	S += r70_mem1 >= 34
	r70_mem1 += MAS_MEM[5]

	r81 = S.Task('r81', length=2, delay_cost=1)
	S += r81 >= 34
	r81 += MAS[2]

	r101 = S.Task('r101', length=2, delay_cost=1)
	S += r101 >= 35
	r101 += MAS[1]

	r130_in = S.Task('r130_in', length=1, delay_cost=1)
	S += r130_in >= 35
	r130_in += MAS_in[0]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	S += r130_mem0 >= 35
	r130_mem0 += MM_MEM[0]

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	S += r130_mem1 >= 35
	r130_mem1 += MM_MEM[1]

	r15_t2_in = S.Task('r15_t2_in', length=1, delay_cost=1)
	S += r15_t2_in >= 35
	r15_t2_in += MAS_in[1]

	r15_t2_mem0 = S.Task('r15_t2_mem0', length=1, delay_cost=1)
	S += r15_t2_mem0 >= 35
	r15_t2_mem0 += MAS_MEM[2]

	r15_t2_mem1 = S.Task('r15_t2_mem1', length=1, delay_cost=1)
	S += r15_t2_mem1 >= 35
	r15_t2_mem1 += MAS_MEM[5]

	r1_t5 = S.Task('r1_t5', length=2, delay_cost=1)
	S += r1_t5 >= 35
	r1_t5 += MAS[0]

	r20_in = S.Task('r20_in', length=1, delay_cost=1)
	S += r20_in >= 35
	r20_in += MAS_in[2]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	S += r20_mem0 >= 35
	r20_mem0 += MAS_MEM[0]

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	S += r20_mem1 >= 35
	r20_mem1 += MAS_MEM[1]

	r70 = S.Task('r70', length=2, delay_cost=1)
	S += r70 >= 35
	r70 += MAS[2]

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	S += r11_in >= 36
	r11_in += MAS_in[1]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	S += r11_mem0 >= 36
	r11_mem0 += MM_MEM[0]

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	S += r11_mem1 >= 36
	r11_mem1 += MAS_MEM[1]

	r11_t1_in = S.Task('r11_t1_in', length=1, delay_cost=1)
	S += r11_t1_in >= 36
	r11_t1_in += MAS_in[2]

	r11_t1_mem0 = S.Task('r11_t1_mem0', length=1, delay_cost=1)
	S += r11_t1_mem0 >= 36
	r11_t1_mem0 += MAS_MEM[0]

	r11_t1_mem1 = S.Task('r11_t1_mem1', length=1, delay_cost=1)
	S += r11_t1_mem1 >= 36
	r11_t1_mem1 += MAS_MEM[3]

	r130 = S.Task('r130', length=2, delay_cost=1)
	S += r130 >= 36
	r130 += MAS[0]

	r15_t2 = S.Task('r15_t2', length=2, delay_cost=1)
	S += r15_t2 >= 36
	r15_t2 += MAS[1]

	r20 = S.Task('r20', length=2, delay_cost=1)
	S += r20 >= 36
	r20 += MAS[2]

	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	S += r9_t0_in >= 36
	r9_t0_in += MM_in[0]

	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	S += r9_t0_mem0 >= 36
	r9_t0_mem0 += MAIN_MEM_r[0]

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	S += r9_t0_mem1 >= 36
	r9_t0_mem1 += MAS_MEM[5]

	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	S += Z_new_t0_in >= 37
	Z_new_t0_in += MM_in[0]

	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	S += Z_new_t0_mem0 >= 37
	Z_new_t0_mem0 += MAS_MEM[4]

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	S += Z_new_t0_mem1 >= 37
	Z_new_t0_mem1 += MAS_MEM[1]

	r11 = S.Task('r11', length=2, delay_cost=1)
	S += r11 >= 37
	r11 += MAS[1]

	r11_t1 = S.Task('r11_t1', length=2, delay_cost=1)
	S += r11_t1 >= 37
	r11_t1 += MAS[2]

	r31_in = S.Task('r31_in', length=1, delay_cost=1)
	S += r31_in >= 37
	r31_in += MAS_in[0]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	S += r31_mem0 >= 37
	r31_mem0 += MM_MEM[0]

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	S += r31_mem1 >= 37
	r31_mem1 += MAS_MEM[3]

	r9_t0 = S.Task('r9_t0', length=7, delay_cost=1)
	S += r9_t0 >= 37
	r9_t0 += MM[0]

	Z_new_t0 = S.Task('Z_new_t0', length=7, delay_cost=1)
	S += Z_new_t0 >= 38
	Z_new_t0 += MM[0]

	r13_t5_in = S.Task('r13_t5_in', length=1, delay_cost=1)
	S += r13_t5_in >= 38
	r13_t5_in += MAS_in[0]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	S += r13_t5_mem0 >= 38
	r13_t5_mem0 += MM_MEM[0]

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	S += r13_t5_mem1 >= 38
	r13_t5_mem1 += MM_MEM[1]

	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	S += r14_t0_in >= 38
	r14_t0_in += MM_in[0]

	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	S += r14_t0_mem0 >= 38
	r14_t0_mem0 += MAS_MEM[4]

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	S += r14_t0_mem1 >= 38
	r14_t0_mem1 += MAS_MEM[1]

	r21_in = S.Task('r21_in', length=1, delay_cost=1)
	S += r21_in >= 38
	r21_in += MAS_in[1]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	S += r21_mem0 >= 38
	r21_mem0 += MAS_MEM[2]

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	S += r21_mem1 >= 38
	r21_mem1 += MAS_MEM[3]

	r31 = S.Task('r31', length=2, delay_cost=1)
	S += r31 >= 38
	r31 += MAS[0]

	r120_in = S.Task('r120_in', length=1, delay_cost=1)
	S += r120_in >= 39
	r120_in += MAS_in[1]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	S += r120_mem0 >= 39
	r120_mem0 += MM_MEM[0]

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	S += r120_mem1 >= 39
	r120_mem1 += MM_MEM[1]

	r13_t5 = S.Task('r13_t5', length=2, delay_cost=1)
	S += r13_t5 >= 39
	r13_t5 += MAS[0]

	r14_t0 = S.Task('r14_t0', length=7, delay_cost=1)
	S += r14_t0 >= 39
	r14_t0 += MM[0]

	r14_t3_in = S.Task('r14_t3_in', length=1, delay_cost=1)
	S += r14_t3_in >= 39
	r14_t3_in += MAS_in[2]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	S += r14_t3_mem0 >= 39
	r14_t3_mem0 += MAS_MEM[0]

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	S += r14_t3_mem1 >= 39
	r14_t3_mem1 += MAS_MEM[1]

	r21 = S.Task('r21', length=2, delay_cost=1)
	S += r21 >= 39
	r21 += MAS[1]

	r11_t0_in = S.Task('r11_t0_in', length=1, delay_cost=1)
	S += r11_t0_in >= 40
	r11_t0_in += MAS_in[1]

	r11_t0_mem0 = S.Task('r11_t0_mem0', length=1, delay_cost=1)
	S += r11_t0_mem0 >= 40
	r11_t0_mem0 += MAS_MEM[0]

	r11_t0_mem1 = S.Task('r11_t0_mem1', length=1, delay_cost=1)
	S += r11_t0_mem1 >= 40
	r11_t0_mem1 += MAS_MEM[3]

	r120 = S.Task('r120', length=2, delay_cost=1)
	S += r120 >= 40
	r120 += MAS[1]

	r131_in = S.Task('r131_in', length=1, delay_cost=1)
	S += r131_in >= 40
	r131_in += MAS_in[0]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	S += r131_mem0 >= 40
	r131_mem0 += MM_MEM[0]

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	S += r131_mem1 >= 40
	r131_mem1 += MAS_MEM[1]

	r14_t3 = S.Task('r14_t3', length=2, delay_cost=1)
	S += r14_t3 >= 40
	r14_t3 += MAS[2]

	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	S += X_new_t0_in >= 41
	X_new_t0_in += MM_in[0]

	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	S += X_new_t0_mem0 >= 41
	X_new_t0_mem0 += MAS_MEM[4]

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	S += X_new_t0_mem1 >= 41
	X_new_t0_mem1 += MAS_MEM[3]

	r11_t0 = S.Task('r11_t0', length=2, delay_cost=1)
	S += r11_t0 >= 41
	r11_t0 += MAS[1]

	r131 = S.Task('r131', length=2, delay_cost=1)
	S += r131 >= 41
	r131 += MAS[0]

	r6_t5_in = S.Task('r6_t5_in', length=1, delay_cost=1)
	S += r6_t5_in >= 41
	r6_t5_in += MAS_in[0]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	S += r6_t5_mem0 >= 41
	r6_t5_mem0 += MM_MEM[0]

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	S += r6_t5_mem1 >= 41
	r6_t5_mem1 += MM_MEM[1]

	X_new_t0 = S.Task('X_new_t0', length=7, delay_cost=1)
	S += X_new_t0 >= 42
	X_new_t0 += MM[0]

	Z_new_t2_in = S.Task('Z_new_t2_in', length=1, delay_cost=1)
	S += Z_new_t2_in >= 42
	Z_new_t2_in += MAS_in[1]

	Z_new_t2_mem0 = S.Task('Z_new_t2_mem0', length=1, delay_cost=1)
	S += Z_new_t2_mem0 >= 42
	Z_new_t2_mem0 += MAS_MEM[4]

	Z_new_t2_mem1 = S.Task('Z_new_t2_mem1', length=1, delay_cost=1)
	S += Z_new_t2_mem1 >= 42
	Z_new_t2_mem1 += MAS_MEM[3]

	Z_new_t3_in = S.Task('Z_new_t3_in', length=1, delay_cost=1)
	S += Z_new_t3_in >= 42
	Z_new_t3_in += MAS_in[2]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	S += Z_new_t3_mem0 >= 42
	Z_new_t3_mem0 += MAS_MEM[0]

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	S += Z_new_t3_mem1 >= 42
	Z_new_t3_mem1 += MAS_MEM[1]

	r11_t2_in = S.Task('r11_t2_in', length=1, delay_cost=1)
	S += r11_t2_in >= 42
	r11_t2_in += MM_in[0]

	r11_t2_mem0 = S.Task('r11_t2_mem0', length=1, delay_cost=1)
	S += r11_t2_mem0 >= 42
	r11_t2_mem0 += MAS_MEM[2]

	r11_t2_mem1 = S.Task('r11_t2_mem1', length=1, delay_cost=1)
	S += r11_t2_mem1 >= 42
	r11_t2_mem1 += MAS_MEM[5]

	r12_t5_in = S.Task('r12_t5_in', length=1, delay_cost=1)
	S += r12_t5_in >= 42
	r12_t5_in += MAS_in[0]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	S += r12_t5_mem0 >= 42
	r12_t5_mem0 += MM_MEM[0]

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	S += r12_t5_mem1 >= 42
	r12_t5_mem1 += MM_MEM[1]

	r6_t5 = S.Task('r6_t5', length=2, delay_cost=1)
	S += r6_t5 >= 42
	r6_t5 += MAS[0]

	Z_new_t2 = S.Task('Z_new_t2', length=2, delay_cost=1)
	S += Z_new_t2 >= 43
	Z_new_t2 += MAS[1]

	Z_new_t3 = S.Task('Z_new_t3', length=2, delay_cost=1)
	S += Z_new_t3 >= 43
	Z_new_t3 += MAS[2]

	r11_t2 = S.Task('r11_t2', length=7, delay_cost=1)
	S += r11_t2 >= 43
	r11_t2 += MM[0]

	r11_t3_in = S.Task('r11_t3_in', length=1, delay_cost=1)
	S += r11_t3_in >= 43
	r11_t3_in += MM_in[0]

	r11_t3_mem0 = S.Task('r11_t3_mem0', length=1, delay_cost=1)
	S += r11_t3_mem0 >= 43
	r11_t3_mem0 += MAS_MEM[0]

	r11_t3_mem1 = S.Task('r11_t3_mem1', length=1, delay_cost=1)
	S += r11_t3_mem1 >= 43
	r11_t3_mem1 += MAS_MEM[3]

	r12_t5 = S.Task('r12_t5', length=2, delay_cost=1)
	S += r12_t5 >= 43
	r12_t5 += MAS[0]

	r61_in = S.Task('r61_in', length=1, delay_cost=1)
	S += r61_in >= 43
	r61_in += MAS_in[2]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	S += r61_mem0 >= 43
	r61_mem0 += MM_MEM[0]

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	S += r61_mem1 >= 43
	r61_mem1 += MAS_MEM[1]

	Z_new_t4_in = S.Task('Z_new_t4_in', length=1, delay_cost=1)
	S += Z_new_t4_in >= 44
	Z_new_t4_in += MM_in[0]

	Z_new_t4_mem0 = S.Task('Z_new_t4_mem0', length=1, delay_cost=1)
	S += Z_new_t4_mem0 >= 44
	Z_new_t4_mem0 += MAS_MEM[2]

	Z_new_t4_mem1 = S.Task('Z_new_t4_mem1', length=1, delay_cost=1)
	S += Z_new_t4_mem1 >= 44
	Z_new_t4_mem1 += MAS_MEM[5]

	r11_t3 = S.Task('r11_t3', length=7, delay_cost=1)
	S += r11_t3 >= 44
	r11_t3 += MM[0]

	r121_in = S.Task('r121_in', length=1, delay_cost=1)
	S += r121_in >= 44
	r121_in += MAS_in[0]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	S += r121_mem0 >= 44
	r121_mem0 += MM_MEM[0]

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	S += r121_mem1 >= 44
	r121_mem1 += MAS_MEM[1]

	r14_t2_in = S.Task('r14_t2_in', length=1, delay_cost=1)
	S += r14_t2_in >= 44
	r14_t2_in += MAS_in[2]

	r14_t2_mem0 = S.Task('r14_t2_mem0', length=1, delay_cost=1)
	S += r14_t2_mem0 >= 44
	r14_t2_mem0 += MAS_MEM[4]

	r14_t2_mem1 = S.Task('r14_t2_mem1', length=1, delay_cost=1)
	S += r14_t2_mem1 >= 44
	r14_t2_mem1 += MAS_MEM[3]

	r61 = S.Task('r61', length=2, delay_cost=1)
	S += r61 >= 44
	r61 += MAS[2]

	X_new_t2_in = S.Task('X_new_t2_in', length=1, delay_cost=1)
	S += X_new_t2_in >= 45
	X_new_t2_in += MAS_in[0]

	X_new_t2_mem0 = S.Task('X_new_t2_mem0', length=1, delay_cost=1)
	S += X_new_t2_mem0 >= 45
	X_new_t2_mem0 += MAS_MEM[4]

	X_new_t2_mem1 = S.Task('X_new_t2_mem1', length=1, delay_cost=1)
	S += X_new_t2_mem1 >= 45
	X_new_t2_mem1 += MAS_MEM[3]

	Z_new_t1_in = S.Task('Z_new_t1_in', length=1, delay_cost=1)
	S += Z_new_t1_in >= 45
	Z_new_t1_in += MM_in[0]

	Z_new_t1_mem0 = S.Task('Z_new_t1_mem0', length=1, delay_cost=1)
	S += Z_new_t1_mem0 >= 45
	Z_new_t1_mem0 += MAS_MEM[2]

	Z_new_t1_mem1 = S.Task('Z_new_t1_mem1', length=1, delay_cost=1)
	S += Z_new_t1_mem1 >= 45
	Z_new_t1_mem1 += MAS_MEM[1]

	Z_new_t4 = S.Task('Z_new_t4', length=7, delay_cost=1)
	S += Z_new_t4 >= 45
	Z_new_t4 += MM[0]

	r121 = S.Task('r121', length=2, delay_cost=1)
	S += r121 >= 45
	r121 += MAS[0]

	r14_t2 = S.Task('r14_t2', length=2, delay_cost=1)
	S += r14_t2 >= 45
	r14_t2 += MAS[2]

	r71_in = S.Task('r71_in', length=1, delay_cost=1)
	S += r71_in >= 45
	r71_in += MAS_in[1]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	S += r71_mem0 >= 45
	r71_mem0 += MAS_MEM[0]

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	S += r71_mem1 >= 45
	r71_mem1 += MAS_MEM[5]

	X_new_t2 = S.Task('X_new_t2', length=2, delay_cost=1)
	S += X_new_t2 >= 46
	X_new_t2 += MAS[0]

	X_new_t3_in = S.Task('X_new_t3_in', length=1, delay_cost=1)
	S += X_new_t3_in >= 46
	X_new_t3_in += MAS_in[0]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	S += X_new_t3_mem0 >= 46
	X_new_t3_mem0 += MAS_MEM[2]

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	S += X_new_t3_mem1 >= 46
	X_new_t3_mem1 += MAS_MEM[1]

	Z_new_t1 = S.Task('Z_new_t1', length=7, delay_cost=1)
	S += Z_new_t1 >= 46
	Z_new_t1 += MM[0]

	r14_t4_in = S.Task('r14_t4_in', length=1, delay_cost=1)
	S += r14_t4_in >= 46
	r14_t4_in += MM_in[0]

	r14_t4_mem0 = S.Task('r14_t4_mem0', length=1, delay_cost=1)
	S += r14_t4_mem0 >= 46
	r14_t4_mem0 += MAS_MEM[4]

	r14_t4_mem1 = S.Task('r14_t4_mem1', length=1, delay_cost=1)
	S += r14_t4_mem1 >= 46
	r14_t4_mem1 += MAS_MEM[5]

	r71 = S.Task('r71', length=2, delay_cost=1)
	S += r71 >= 46
	r71 += MAS[1]

	X_new_t1_in = S.Task('X_new_t1_in', length=1, delay_cost=1)
	S += X_new_t1_in >= 47
	X_new_t1_in += MM_in[0]

	X_new_t1_mem0 = S.Task('X_new_t1_mem0', length=1, delay_cost=1)
	S += X_new_t1_mem0 >= 47
	X_new_t1_mem0 += MAS_MEM[2]

	X_new_t1_mem1 = S.Task('X_new_t1_mem1', length=1, delay_cost=1)
	S += X_new_t1_mem1 >= 47
	X_new_t1_mem1 += MAS_MEM[1]

	X_new_t3 = S.Task('X_new_t3', length=2, delay_cost=1)
	S += X_new_t3 >= 47
	X_new_t3 += MAS[0]

	r14_t4 = S.Task('r14_t4', length=7, delay_cost=1)
	S += r14_t4 >= 47
	r14_t4 += MM[0]

	r9_t3_in = S.Task('r9_t3_in', length=1, delay_cost=1)
	S += r9_t3_in >= 47
	r9_t3_in += MAS_in[0]

	r9_t3_mem0 = S.Task('r9_t3_mem0', length=1, delay_cost=1)
	S += r9_t3_mem0 >= 47
	r9_t3_mem0 += MAS_MEM[4]

	r9_t3_mem1 = S.Task('r9_t3_mem1', length=1, delay_cost=1)
	S += r9_t3_mem1 >= 47
	r9_t3_mem1 += MAS_MEM[3]

	X_new_t1 = S.Task('X_new_t1', length=7, delay_cost=1)
	S += X_new_t1 >= 48
	X_new_t1 += MM[0]

	r9_t1_in = S.Task('r9_t1_in', length=1, delay_cost=1)
	S += r9_t1_in >= 48
	r9_t1_in += MM_in[0]

	r9_t1_mem0 = S.Task('r9_t1_mem0', length=1, delay_cost=1)
	S += r9_t1_mem0 >= 48
	r9_t1_mem0 += MAIN_MEM_r[0]

	r9_t1_mem1 = S.Task('r9_t1_mem1', length=1, delay_cost=1)
	S += r9_t1_mem1 >= 48
	r9_t1_mem1 += MAS_MEM[3]

	r9_t3 = S.Task('r9_t3', length=2, delay_cost=1)
	S += r9_t3 >= 48
	r9_t3 += MAS[0]

	r14_t1_in = S.Task('r14_t1_in', length=1, delay_cost=1)
	S += r14_t1_in >= 49
	r14_t1_in += MM_in[0]

	r14_t1_mem0 = S.Task('r14_t1_mem0', length=1, delay_cost=1)
	S += r14_t1_mem0 >= 49
	r14_t1_mem0 += MAS_MEM[2]

	r14_t1_mem1 = S.Task('r14_t1_mem1', length=1, delay_cost=1)
	S += r14_t1_mem1 >= 49
	r14_t1_mem1 += MAS_MEM[1]

	r9_t1 = S.Task('r9_t1', length=7, delay_cost=1)
	S += r9_t1 >= 49
	r9_t1 += MM[0]

	r11_t5_in = S.Task('r11_t5_in', length=1, delay_cost=1)
	S += r11_t5_in >= 50
	r11_t5_in += MAS_in[0]

	r11_t5_mem0 = S.Task('r11_t5_mem0', length=1, delay_cost=1)
	S += r11_t5_mem0 >= 50
	r11_t5_mem0 += MM_MEM[0]

	r11_t5_mem1 = S.Task('r11_t5_mem1', length=1, delay_cost=1)
	S += r11_t5_mem1 >= 50
	r11_t5_mem1 += MM_MEM[1]

	r14_t1 = S.Task('r14_t1', length=7, delay_cost=1)
	S += r14_t1 >= 50
	r14_t1 += MM[0]

	r9_t4_in = S.Task('r9_t4_in', length=1, delay_cost=1)
	S += r9_t4_in >= 50
	r9_t4_in += MM_in[0]

	r9_t4_mem0 = S.Task('r9_t4_mem0', length=1, delay_cost=1)
	S += r9_t4_mem0 >= 50
	r9_t4_mem0 += MAS_MEM[0]

	r9_t4_mem1 = S.Task('r9_t4_mem1', length=1, delay_cost=1)
	S += r9_t4_mem1 >= 50
	r9_t4_mem1 += MAS_MEM[1]

	X_new_t4_in = S.Task('X_new_t4_in', length=1, delay_cost=1)
	S += X_new_t4_in >= 51
	X_new_t4_in += MM_in[0]

	X_new_t4_mem0 = S.Task('X_new_t4_mem0', length=1, delay_cost=1)
	S += X_new_t4_mem0 >= 51
	X_new_t4_mem0 += MAS_MEM[0]

	X_new_t4_mem1 = S.Task('X_new_t4_mem1', length=1, delay_cost=1)
	S += X_new_t4_mem1 >= 51
	X_new_t4_mem1 += MAS_MEM[1]

	r111_in = S.Task('r111_in', length=1, delay_cost=1)
	S += r111_in >= 51
	r111_in += MAS_in[1]

	r111_mem0 = S.Task('r111_mem0', length=1, delay_cost=1)
	S += r111_mem0 >= 51
	r111_mem0 += MM_MEM[0]

	r111_mem1 = S.Task('r111_mem1', length=1, delay_cost=1)
	S += r111_mem1 >= 51
	r111_mem1 += MM_MEM[1]

	r11_t5 = S.Task('r11_t5', length=2, delay_cost=1)
	S += r11_t5 >= 51
	r11_t5 += MAS[0]

	r9_t4 = S.Task('r9_t4', length=7, delay_cost=1)
	S += r9_t4 >= 51
	r9_t4 += MM[0]

	X_new_t4 = S.Task('X_new_t4', length=7, delay_cost=1)
	S += X_new_t4 >= 52
	X_new_t4 += MM[0]

	r110_in = S.Task('r110_in', length=1, delay_cost=1)
	S += r110_in >= 52
	r110_in += MAS_in[0]

	r110_mem0 = S.Task('r110_mem0', length=1, delay_cost=1)
	S += r110_mem0 >= 52
	r110_mem0 += MM_MEM[0]

	r110_mem1 = S.Task('r110_mem1', length=1, delay_cost=1)
	S += r110_mem1 >= 52
	r110_mem1 += MAS_MEM[1]

	r111 = S.Task('r111', length=2, delay_cost=1)
	S += r111 >= 52
	r111 += MAS[1]

	Z_new0_in = S.Task('Z_new0_in', length=1, delay_cost=1)
	S += Z_new0_in >= 53
	Z_new0_in += MAS_in[2]

	Z_new0_mem0 = S.Task('Z_new0_mem0', length=1, delay_cost=1)
	S += Z_new0_mem0 >= 53
	Z_new0_mem0 += MM_MEM[0]

	Z_new0_mem1 = S.Task('Z_new0_mem1', length=1, delay_cost=1)
	S += Z_new0_mem1 >= 53
	Z_new0_mem1 += MM_MEM[1]

	r110 = S.Task('r110', length=2, delay_cost=1)
	S += r110 >= 53
	r110 += MAS[0]

	r16_t1_in = S.Task('r16_t1_in', length=1, delay_cost=1)
	S += r16_t1_in >= 53
	r16_t1_in += MM_in[0]

	r16_t1_mem0 = S.Task('r16_t1_mem0', length=1, delay_cost=1)
	S += r16_t1_mem0 >= 53
	r16_t1_mem0 += MAS_MEM[2]

	r16_t1_mem1 = S.Task('r16_t1_mem1', length=1, delay_cost=1)
	S += r16_t1_mem1 >= 53
	r16_t1_mem1 += MAIN_MEM_r[1]

	X_new0_in = S.Task('X_new0_in', length=1, delay_cost=1)
	S += X_new0_in >= 54
	X_new0_in += MAS_in[0]

	X_new0_mem0 = S.Task('X_new0_mem0', length=1, delay_cost=1)
	S += X_new0_mem0 >= 54
	X_new0_mem0 += MM_MEM[0]

	X_new0_mem1 = S.Task('X_new0_mem1', length=1, delay_cost=1)
	S += X_new0_mem1 >= 54
	X_new0_mem1 += MM_MEM[1]

	Z_new0 = S.Task('Z_new0', length=2, delay_cost=1)
	S += Z_new0 >= 54
	Z_new0 += MAS[2]

	r16_t1 = S.Task('r16_t1', length=7, delay_cost=1)
	S += r16_t1 >= 54
	r16_t1 += MM[0]

	r16_t2_in = S.Task('r16_t2_in', length=1, delay_cost=1)
	S += r16_t2_in >= 54
	r16_t2_in += MAS_in[2]

	r16_t2_mem0 = S.Task('r16_t2_mem0', length=1, delay_cost=1)
	S += r16_t2_mem0 >= 54
	r16_t2_mem0 += MAS_MEM[0]

	r16_t2_mem1 = S.Task('r16_t2_mem1', length=1, delay_cost=1)
	S += r16_t2_mem1 >= 54
	r16_t2_mem1 += MAS_MEM[3]

	X_new0 = S.Task('X_new0', length=2, delay_cost=1)
	S += X_new0 >= 55
	X_new0 += MAS[0]

	r16_t0_in = S.Task('r16_t0_in', length=1, delay_cost=1)
	S += r16_t0_in >= 55
	r16_t0_in += MM_in[0]

	r16_t0_mem0 = S.Task('r16_t0_mem0', length=1, delay_cost=1)
	S += r16_t0_mem0 >= 55
	r16_t0_mem0 += MAS_MEM[0]

	r16_t0_mem1 = S.Task('r16_t0_mem1', length=1, delay_cost=1)
	S += r16_t0_mem1 >= 55
	r16_t0_mem1 += MAIN_MEM_r[1]

	r16_t2 = S.Task('r16_t2', length=2, delay_cost=1)
	S += r16_t2 >= 55
	r16_t2 += MAS[2]

	r9_t5_in = S.Task('r9_t5_in', length=1, delay_cost=1)
	S += r9_t5_in >= 55
	r9_t5_in += MAS_in[0]

	r9_t5_mem0 = S.Task('r9_t5_mem0', length=1, delay_cost=1)
	S += r9_t5_mem0 >= 55
	r9_t5_mem0 += MM_MEM[0]

	r9_t5_mem1 = S.Task('r9_t5_mem1', length=1, delay_cost=1)
	S += r9_t5_mem1 >= 55
	r9_t5_mem1 += MM_MEM[1]

	Z_new0_w = S.Task('Z_new0_w', length=1, delay_cost=1)
	S += Z_new0_w >= 56
	Z_new0_w += MAIN_MEM_w

	r16_t0 = S.Task('r16_t0', length=7, delay_cost=1)
	S += r16_t0 >= 56
	r16_t0 += MM[0]

	r16_t4_in = S.Task('r16_t4_in', length=1, delay_cost=1)
	S += r16_t4_in >= 56
	r16_t4_in += MM_in[0]

	r16_t4_mem0 = S.Task('r16_t4_mem0', length=1, delay_cost=1)
	S += r16_t4_mem0 >= 56
	r16_t4_mem0 += MAS_MEM[4]

	r16_t4_mem1 = S.Task('r16_t4_mem1', length=1, delay_cost=1)
	S += r16_t4_mem1 >= 56
	r16_t4_mem1 += MAS_MEM[1]

	r9_t5 = S.Task('r9_t5', length=2, delay_cost=1)
	S += r9_t5 >= 56
	r9_t5 += MAS[0]

	X_new0_w = S.Task('X_new0_w', length=1, delay_cost=1)
	S += X_new0_w >= 57
	X_new0_w += MAIN_MEM_w

	r16_t4 = S.Task('r16_t4', length=7, delay_cost=1)
	S += r16_t4 >= 57
	r16_t4 += MM[0]

	X_new_t5_in = S.Task('X_new_t5_in', length=1, delay_cost=1)
	S += X_new_t5_in >= 58
	X_new_t5_in += MAS_in[1]

	X_new_t5_mem0 = S.Task('X_new_t5_mem0', length=1, delay_cost=1)
	S += X_new_t5_mem0 >= 58
	X_new_t5_mem0 += MM_MEM[0]

	X_new_t5_mem1 = S.Task('X_new_t5_mem1', length=1, delay_cost=1)
	S += X_new_t5_mem1 >= 58
	X_new_t5_mem1 += MM_MEM[1]

	r15_t0_in = S.Task('r15_t0_in', length=1, delay_cost=1)
	S += r15_t0_in >= 58
	r15_t0_in += MM_in[0]

	r15_t0_mem0 = S.Task('r15_t0_mem0', length=1, delay_cost=1)
	S += r15_t0_mem0 >= 58
	r15_t0_mem0 += MAS_MEM[2]

	r15_t0_mem1 = S.Task('r15_t0_mem1', length=1, delay_cost=1)
	S += r15_t0_mem1 >= 58
	r15_t0_mem1 += MAS_MEM[1]

	X_new_t5 = S.Task('X_new_t5', length=2, delay_cost=1)
	S += X_new_t5 >= 59
	X_new_t5 += MAS[1]

	Z_new_t5_in = S.Task('Z_new_t5_in', length=1, delay_cost=1)
	S += Z_new_t5_in >= 59
	Z_new_t5_in += MAS_in[2]

	Z_new_t5_mem0 = S.Task('Z_new_t5_mem0', length=1, delay_cost=1)
	S += Z_new_t5_mem0 >= 59
	Z_new_t5_mem0 += MM_MEM[0]

	Z_new_t5_mem1 = S.Task('Z_new_t5_mem1', length=1, delay_cost=1)
	S += Z_new_t5_mem1 >= 59
	Z_new_t5_mem1 += MM_MEM[1]

	r15_t0 = S.Task('r15_t0', length=7, delay_cost=1)
	S += r15_t0 >= 59
	r15_t0 += MM[0]

	r15_t1_in = S.Task('r15_t1_in', length=1, delay_cost=1)
	S += r15_t1_in >= 59
	r15_t1_in += MM_in[0]

	r15_t1_mem0 = S.Task('r15_t1_mem0', length=1, delay_cost=1)
	S += r15_t1_mem0 >= 59
	r15_t1_mem0 += MAS_MEM[4]

	r15_t1_mem1 = S.Task('r15_t1_mem1', length=1, delay_cost=1)
	S += r15_t1_mem1 >= 59
	r15_t1_mem1 += MAS_MEM[5]

	X_new1_in = S.Task('X_new1_in', length=1, delay_cost=1)
	S += X_new1_in >= 60
	X_new1_in += MAS_in[0]

	X_new1_mem0 = S.Task('X_new1_mem0', length=1, delay_cost=1)
	S += X_new1_mem0 >= 60
	X_new1_mem0 += MM_MEM[0]

	X_new1_mem1 = S.Task('X_new1_mem1', length=1, delay_cost=1)
	S += X_new1_mem1 >= 60
	X_new1_mem1 += MAS_MEM[3]

	Z_new_t5 = S.Task('Z_new_t5', length=2, delay_cost=1)
	S += Z_new_t5 >= 60
	Z_new_t5 += MAS[2]

	r15_t1 = S.Task('r15_t1', length=7, delay_cost=1)
	S += r15_t1 >= 60
	r15_t1 += MM[0]

	X_new1 = S.Task('X_new1', length=2, delay_cost=1)
	S += X_new1 >= 61
	X_new1 += MAS[0]

	Z_new1_in = S.Task('Z_new1_in', length=1, delay_cost=1)
	S += Z_new1_in >= 61
	Z_new1_in += MAS_in[2]

	Z_new1_mem0 = S.Task('Z_new1_mem0', length=1, delay_cost=1)
	S += Z_new1_mem0 >= 61
	Z_new1_mem0 += MM_MEM[0]

	Z_new1_mem1 = S.Task('Z_new1_mem1', length=1, delay_cost=1)
	S += Z_new1_mem1 >= 61
	Z_new1_mem1 += MAS_MEM[5]

	Z_new1 = S.Task('Z_new1', length=2, delay_cost=1)
	S += Z_new1 >= 62
	Z_new1 += MAS[2]

	r140_in = S.Task('r140_in', length=1, delay_cost=1)
	S += r140_in >= 62
	r140_in += MAS_in[2]

	r140_mem0 = S.Task('r140_mem0', length=1, delay_cost=1)
	S += r140_mem0 >= 62
	r140_mem0 += MM_MEM[0]

	r140_mem1 = S.Task('r140_mem1', length=1, delay_cost=1)
	S += r140_mem1 >= 62
	r140_mem1 += MM_MEM[1]

	r15_t4_in = S.Task('r15_t4_in', length=1, delay_cost=1)
	S += r15_t4_in >= 62
	r15_t4_in += MM_in[0]

	r15_t4_mem0 = S.Task('r15_t4_mem0', length=1, delay_cost=1)
	S += r15_t4_mem0 >= 62
	r15_t4_mem0 += MAS_MEM[2]

	r15_t4_mem1 = S.Task('r15_t4_mem1', length=1, delay_cost=1)
	S += r15_t4_mem1 >= 62
	r15_t4_mem1 += MAS_MEM[5]

	X_new1_w = S.Task('X_new1_w', length=1, delay_cost=1)
	S += X_new1_w >= 63
	X_new1_w += MAIN_MEM_w

	r140 = S.Task('r140', length=2, delay_cost=1)
	S += r140 >= 63
	r140 += MAS[2]

	r14_t5_in = S.Task('r14_t5_in', length=1, delay_cost=1)
	S += r14_t5_in >= 63
	r14_t5_in += MAS_in[0]

	r14_t5_mem0 = S.Task('r14_t5_mem0', length=1, delay_cost=1)
	S += r14_t5_mem0 >= 63
	r14_t5_mem0 += MM_MEM[0]

	r14_t5_mem1 = S.Task('r14_t5_mem1', length=1, delay_cost=1)
	S += r14_t5_mem1 >= 63
	r14_t5_mem1 += MM_MEM[1]

	r15_t4 = S.Task('r15_t4', length=7, delay_cost=1)
	S += r15_t4 >= 63
	r15_t4 += MM[0]

	Z_new1_w = S.Task('Z_new1_w', length=1, delay_cost=1)
	S += Z_new1_w >= 64
	Z_new1_w += MAIN_MEM_w

	r14_t5 = S.Task('r14_t5', length=2, delay_cost=1)
	S += r14_t5 >= 64
	r14_t5 += MAS[0]

	r160_in = S.Task('r160_in', length=1, delay_cost=1)
	S += r160_in >= 64
	r160_in += MAS_in[2]

	r160_mem0 = S.Task('r160_mem0', length=1, delay_cost=1)
	S += r160_mem0 >= 64
	r160_mem0 += MM_MEM[0]

	r160_mem1 = S.Task('r160_mem1', length=1, delay_cost=1)
	S += r160_mem1 >= 64
	r160_mem1 += MM_MEM[1]

	r141_in = S.Task('r141_in', length=1, delay_cost=1)
	S += r141_in >= 65
	r141_in += MAS_in[2]

	r141_mem0 = S.Task('r141_mem0', length=1, delay_cost=1)
	S += r141_mem0 >= 65
	r141_mem0 += MM_MEM[0]

	r141_mem1 = S.Task('r141_mem1', length=1, delay_cost=1)
	S += r141_mem1 >= 65
	r141_mem1 += MAS_MEM[1]

	r160 = S.Task('r160', length=2, delay_cost=1)
	S += r160 >= 65
	r160 += MAS[2]

	r141 = S.Task('r141', length=2, delay_cost=1)
	S += r141 >= 66
	r141 += MAS[2]

	r150_in = S.Task('r150_in', length=1, delay_cost=1)
	S += r150_in >= 66
	r150_in += MAS_in[1]

	r150_mem0 = S.Task('r150_mem0', length=1, delay_cost=1)
	S += r150_mem0 >= 66
	r150_mem0 += MM_MEM[0]

	r150_mem1 = S.Task('r150_mem1', length=1, delay_cost=1)
	S += r150_mem1 >= 66
	r150_mem1 += MM_MEM[1]

	r150 = S.Task('r150', length=2, delay_cost=1)
	S += r150 >= 67
	r150 += MAS[1]

	r15_t5_in = S.Task('r15_t5_in', length=1, delay_cost=1)
	S += r15_t5_in >= 67
	r15_t5_in += MAS_in[0]

	r15_t5_mem0 = S.Task('r15_t5_mem0', length=1, delay_cost=1)
	S += r15_t5_mem0 >= 67
	r15_t5_mem0 += MM_MEM[0]

	r15_t5_mem1 = S.Task('r15_t5_mem1', length=1, delay_cost=1)
	S += r15_t5_mem1 >= 67
	r15_t5_mem1 += MM_MEM[1]

	r15_t5 = S.Task('r15_t5', length=2, delay_cost=1)
	S += r15_t5 >= 68
	r15_t5 += MAS[0]

	r16_t5_in = S.Task('r16_t5_in', length=1, delay_cost=1)
	S += r16_t5_in >= 68
	r16_t5_in += MAS_in[0]

	r16_t5_mem0 = S.Task('r16_t5_mem0', length=1, delay_cost=1)
	S += r16_t5_mem0 >= 68
	r16_t5_mem0 += MM_MEM[0]

	r16_t5_mem1 = S.Task('r16_t5_mem1', length=1, delay_cost=1)
	S += r16_t5_mem1 >= 68
	r16_t5_mem1 += MM_MEM[1]

	r170_in = S.Task('r170_in', length=1, delay_cost=1)
	S += r170_in >= 68
	r170_in += MAS_in[1]

	r170_mem0 = S.Task('r170_mem0', length=1, delay_cost=1)
	S += r170_mem0 >= 68
	r170_mem0 += MAS_MEM[4]

	r170_mem1 = S.Task('r170_mem1', length=1, delay_cost=1)
	S += r170_mem1 >= 68
	r170_mem1 += MAS_MEM[3]

	r151_in = S.Task('r151_in', length=1, delay_cost=1)
	S += r151_in >= 69
	r151_in += MAS_in[2]

	r151_mem0 = S.Task('r151_mem0', length=1, delay_cost=1)
	S += r151_mem0 >= 69
	r151_mem0 += MM_MEM[0]

	r151_mem1 = S.Task('r151_mem1', length=1, delay_cost=1)
	S += r151_mem1 >= 69
	r151_mem1 += MAS_MEM[1]

	r16_t5 = S.Task('r16_t5', length=2, delay_cost=1)
	S += r16_t5 >= 69
	r16_t5 += MAS[0]

	r170 = S.Task('r170', length=2, delay_cost=1)
	S += r170 >= 69
	r170 += MAS[1]

	Y_new0_in = S.Task('Y_new0_in', length=1, delay_cost=1)
	S += Y_new0_in >= 70
	Y_new0_in += MAS_in[1]

	Y_new0_mem0 = S.Task('Y_new0_mem0', length=1, delay_cost=1)
	S += Y_new0_mem0 >= 70
	Y_new0_mem0 += MAS_MEM[2]

	Y_new0_mem1 = S.Task('Y_new0_mem1', length=1, delay_cost=1)
	S += Y_new0_mem1 >= 70
	Y_new0_mem1 += MAS_MEM[5]

	r151 = S.Task('r151', length=2, delay_cost=1)
	S += r151 >= 70
	r151 += MAS[2]

	r161_in = S.Task('r161_in', length=1, delay_cost=1)
	S += r161_in >= 70
	r161_in += MAS_in[0]

	r161_mem0 = S.Task('r161_mem0', length=1, delay_cost=1)
	S += r161_mem0 >= 70
	r161_mem0 += MM_MEM[0]

	r161_mem1 = S.Task('r161_mem1', length=1, delay_cost=1)
	S += r161_mem1 >= 70
	r161_mem1 += MAS_MEM[1]

	Y_new0 = S.Task('Y_new0', length=2, delay_cost=1)
	S += Y_new0 >= 71
	Y_new0 += MAS[1]

	r161 = S.Task('r161', length=2, delay_cost=1)
	S += r161 >= 71
	r161 += MAS[0]

	r171_in = S.Task('r171_in', length=1, delay_cost=1)
	S += r171_in >= 71
	r171_in += MAS_in[0]

	r171_mem0 = S.Task('r171_mem0', length=1, delay_cost=1)
	S += r171_mem0 >= 71
	r171_mem0 += MAS_MEM[4]

	r171_mem1 = S.Task('r171_mem1', length=1, delay_cost=1)
	S += r171_mem1 >= 71
	r171_mem1 += MAS_MEM[5]

	r171 = S.Task('r171', length=2, delay_cost=1)
	S += r171 >= 72
	r171 += MAS[0]

	Y_new0_w = S.Task('Y_new0_w', length=1, delay_cost=1)
	S += Y_new0_w >= 73
	Y_new0_w += MAIN_MEM_w

	Y_new1_in = S.Task('Y_new1_in', length=1, delay_cost=1)
	S += Y_new1_in >= 73
	Y_new1_in += MAS_in[0]

	Y_new1_mem0 = S.Task('Y_new1_mem0', length=1, delay_cost=1)
	S += Y_new1_mem0 >= 73
	Y_new1_mem0 += MAS_MEM[0]

	Y_new1_mem1 = S.Task('Y_new1_mem1', length=1, delay_cost=1)
	S += Y_new1_mem1 >= 73
	Y_new1_mem1 += MAS_MEM[1]

	Y_new1 = S.Task('Y_new1', length=2, delay_cost=1)
	S += Y_new1 >= 74
	Y_new1 += MAS[0]

	Y_new1_w = S.Task('Y_new1_w', length=1, delay_cost=1)
	S += Y_new1_w >= 76
	Y_new1_w += MAIN_MEM_w


	# new tasks
	r90 = S.Task('r90', length=2, delay_cost=1)
	r90 += alt(MAS)
	r90_in = S.Task('r90_in', length=1, delay_cost=1)
	r90_in += alt(MAS_in)
	S += r90_in*MAS_in[0]<=r90*MAS[0]

	S += r90_in*MAS_in[1]<=r90*MAS[1]

	S += r90_in*MAS_in[2]<=r90*MAS[2]

	S += r90<59

	r90_mem0 = S.Task('r90_mem0', length=1, delay_cost=1)
	r90_mem0 += MM_MEM[0]
	S += 43 < r90_mem0
	S += r90_mem0 <= r90

	r90_mem1 = S.Task('r90_mem1', length=1, delay_cost=1)
	r90_mem1 += MM_MEM[1]
	S += 55 < r90_mem1
	S += r90_mem1 <= r90

	r91 = S.Task('r91', length=2, delay_cost=1)
	r91 += alt(MAS)
	r91_in = S.Task('r91_in', length=1, delay_cost=1)
	r91_in += alt(MAS_in)
	S += r91_in*MAS_in[0]<=r91*MAS[0]

	S += r91_in*MAS_in[1]<=r91*MAS[1]

	S += r91_in*MAS_in[2]<=r91*MAS[2]

	S += r91<60

	r91_mem0 = S.Task('r91_mem0', length=1, delay_cost=1)
	r91_mem0 += MM_MEM[0]
	S += 57 < r91_mem0
	S += r91_mem0 <= r91

	r91_mem1 = S.Task('r91_mem1', length=1, delay_cost=1)
	r91_mem1 += MAS_MEM[1]
	S += 57 < r91_mem1
	S += r91_mem1 <= r91

	r15_t3 = S.Task('r15_t3', length=2, delay_cost=1)
	r15_t3 += alt(MAS)
	r15_t3_in = S.Task('r15_t3_in', length=1, delay_cost=1)
	r15_t3_in += alt(MAS_in)
	S += r15_t3_in*MAS_in[0]<=r15_t3*MAS[0]

	S += r15_t3_in*MAS_in[1]<=r15_t3*MAS[1]

	S += r15_t3_in*MAS_in[2]<=r15_t3*MAS[2]

	S += r15_t3<63

	r15_t3_mem0 = S.Task('r15_t3_mem0', length=1, delay_cost=1)
	r15_t3_mem0 += alt(MAS_MEM)
	S += (r90*MAS[0])-1 < r15_t3_mem0*MAS_MEM[0]
	S += (r90*MAS[1])-1 < r15_t3_mem0*MAS_MEM[2]
	S += (r90*MAS[2])-1 < r15_t3_mem0*MAS_MEM[4]
	S += r15_t3_mem0 <= r15_t3

	r15_t3_mem1 = S.Task('r15_t3_mem1', length=1, delay_cost=1)
	r15_t3_mem1 += alt(MAS_MEM)
	S += (r91*MAS[0])-1 < r15_t3_mem1*MAS_MEM[1]
	S += (r91*MAS[1])-1 < r15_t3_mem1*MAS_MEM[3]
	S += (r91*MAS[2])-1 < r15_t3_mem1*MAS_MEM[5]
	S += r15_t3_mem1 <= r15_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage2MAS3/EP2_YRECOVER/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 4))

	return solution

