from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 208
	S = Scenario("schedule15", horizon=horizon)

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
	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 0
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 0
	d_t1_t3_t1_in += MM_in[0]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 0
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=1, delay_cost=1)
	S += d_t0_a1_0 >= 1
	d_t0_a1_0 += MAS[3]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 1
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 1
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=6, delay_cost=1)
	S += d_t1_t3_t1 >= 1
	d_t1_t3_t1 += MM[0]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=1, delay_cost=1)
	S += d_t1_t3_t3 >= 1
	d_t1_t3_t3 += MAS[2]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 1
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=1, delay_cost=1)
	S += d_t2_a1_0 >= 1
	d_t2_a1_0 += MAS[0]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=1, delay_cost=1)
	S += d_t2_t3_t3 >= 1
	d_t2_t3_t3 += MAS[1]

	d_t0_t11 = S.Task('d_t0_t11', length=1, delay_cost=1)
	S += d_t0_t11 >= 2
	d_t0_t11 += MAS[1]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 2
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=6, delay_cost=1)
	S += d_t0_t3_t1 >= 2
	d_t0_t3_t1 += MM[0]

	d_t1_t10 = S.Task('d_t1_t10', length=1, delay_cost=1)
	S += d_t1_t10 >= 2
	d_t1_t10 += MAS[3]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 2
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=1, delay_cost=1)
	S += d_t2_a1_1 >= 2
	d_t2_a1_1 += MAS[2]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 2
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t4000 = S.Task('d_t4000', length=1, delay_cost=1)
	S += d_t4000 >= 2
	d_t4000 += MAS[0]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=1, delay_cost=1)
	S += d_t0_a1_1 >= 3
	d_t0_a1_1 += MAS[0]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=6, delay_cost=1)
	S += d_t0_t3_t0 >= 3
	d_t0_t3_t0 += MM[0]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=1, delay_cost=1)
	S += d_t0_t3_t3 >= 3
	d_t0_t3_t3 += MAS[1]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 3
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 3
	d_t2_t3_t0_in += MM_in[0]

	d_t3000 = S.Task('d_t3000', length=1, delay_cost=1)
	S += d_t3000 >= 3
	d_t3000 += MAS[3]

	d_t4001 = S.Task('d_t4001', length=1, delay_cost=1)
	S += d_t4001 >= 3
	d_t4001 += MAS[2]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 3
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t0_t10 = S.Task('d_t0_t10', length=1, delay_cost=1)
	S += d_t0_t10 >= 4
	d_t0_t10 += MAS[0]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=1, delay_cost=1)
	S += d_t0_t3_t2 >= 4
	d_t0_t3_t2 += MAS[1]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 4
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 4
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=1, delay_cost=1)
	S += d_t2_t10 >= 4
	d_t2_t10 += MAS[2]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=6, delay_cost=1)
	S += d_t2_t3_t0 >= 4
	d_t2_t3_t0 += MM[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 4
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t3001 = S.Task('d_t3001', length=1, delay_cost=1)
	S += d_t3001 >= 4
	d_t3001 += MAS[3]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 5
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=1, delay_cost=1)
	S += d_t1_a1_0 >= 5
	d_t1_a1_0 += MAS[1]

	d_t1_t11 = S.Task('d_t1_t11', length=1, delay_cost=1)
	S += d_t1_t11 >= 5
	d_t1_t11 += MAS[0]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=6, delay_cost=1)
	S += d_t1_t3_t0 >= 5
	d_t1_t3_t0 += MM[0]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 5
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=1, delay_cost=1)
	S += d_t2_t3_t2 >= 5
	d_t2_t3_t2 += MAS[3]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 5
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=1, delay_cost=1)
	S += d_t3011 >= 5
	d_t3011 += MAS[2]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 6
	c_t0_t1_t0_in += MM_in[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 6
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=1, delay_cost=1)
	S += d_t1_a1_1 >= 6
	d_t1_a1_1 += MAS[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=1, delay_cost=1)
	S += d_t1_t3_t2 >= 6
	d_t1_t3_t2 += MAS[1]

	d_t2_t11 = S.Task('d_t2_t11', length=1, delay_cost=1)
	S += d_t2_t11 >= 6
	d_t2_t11 += MAS[3]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=6, delay_cost=1)
	S += d_t2_t3_t1 >= 6
	d_t2_t3_t1 += MM[0]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 6
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t3010 = S.Task('d_t3010', length=1, delay_cost=1)
	S += d_t3010 >= 6
	d_t3010 += MAS[2]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 7
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=6, delay_cost=1)
	S += c_t0_t1_t0 >= 7
	c_t0_t1_t0 += MM[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 7
	c_t0_t21 += MAS[3]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 7
	c_t1_t30 += MAS[2]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 7
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 7
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t5000 = S.Task('d_t5000', length=1, delay_cost=1)
	S += d_t5000 >= 7
	d_t5000 += MAS[0]

	d_t5001 = S.Task('d_t5001', length=1, delay_cost=1)
	S += d_t5001 >= 7
	d_t5001 += MAS[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=6, delay_cost=1)
	S += c_t0_t0_t1 >= 8
	c_t0_t0_t1 += MM[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 8
	c_t1_t0_t2 += MAS[2]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 8
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 8
	c_t1_t1_t2 += MAS[0]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 8
	c_t1_t21 += MAS[3]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 8
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 8
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t4010 = S.Task('d_t4010', length=1, delay_cost=1)
	S += d_t4010 >= 8
	d_t4010 += MAS[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 9
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 9
	c_t0_t0_t3 += MAS[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 9
	c_t1_t0_t3 += MAS[3]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=6, delay_cost=1)
	S += c_t1_t1_t0 >= 9
	c_t1_t1_t0 += MM[0]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 9
	c_t1_t20 += MAS[2]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 9
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 9
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t5011 = S.Task('d_t5011', length=1, delay_cost=1)
	S += d_t5011 >= 9
	d_t5011 += MAS[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=6, delay_cost=1)
	S += c_t0_t0_t0 >= 10
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 10
	c_t0_t0_t2 += MAS[2]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 10
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 10
	c_t0_t1_t2 += MAS[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 10
	c_t0_t1_t3 += MAS[3]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 10
	c_t0_t20 += MAS[1]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 10
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 10
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=6, delay_cost=1)
	S += c_t0_t1_t1 >= 11
	c_t0_t1_t1 += MM[0]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 11
	c_t0_t30 += MAS[2]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 11
	c_t0_t31 += MAS[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 11
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 11
	c_t1_t31 += MAS[3]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 11
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 11
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t4011 = S.Task('d_t4011', length=1, delay_cost=1)
	S += d_t4011 >= 11
	d_t4011 += MAS[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 12
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=6, delay_cost=1)
	S += c_t1_t1_t1 >= 12
	c_t1_t1_t1 += MM[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 12
	c_t1_t1_t3 += MAS[1]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 12
	c_t4001 += MAS[3]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 12
	c_t5000 += MAS[0]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 12
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=1, delay_cost=1)
	S += d_t5010 >= 12
	d_t5010 += MAS[2]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 13
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=6, delay_cost=1)
	S += c_t1_t0_t1 >= 13
	c_t1_t0_t1 += MM[0]

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	S += c_t2_t20 >= 13
	c_t2_t20 += MAS[2]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 13
	c_t3010 += MAS[0]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 13
	c_t3011 += MAS[1]

	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	S += c_t4110 >= 13
	c_t4110 += MAS[3]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 13
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 13
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=6, delay_cost=1)
	S += c_t1_t0_t0 >= 14
	c_t1_t0_t0 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 14
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	S += c_t2_t1_t3 >= 14
	c_t2_t1_t3 += MAS[0]

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 14
	c_t2_t30 += MAS[3]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 14
	c_t3001 += MAS[1]

	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	S += c_t3111 >= 14
	c_t3111 += MAS[2]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 14
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 14
	d_t3001_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=6, delay_cost=1)
	S += c_t2_t0_t0 >= 15
	c_t2_t0_t0 += MM[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 15
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	S += c_t2_t31 >= 15
	c_t2_t31 += MAS[3]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 15
	c_t4000 += MAS[1]

	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	S += c_t4111 >= 15
	c_t4111 += MAS[0]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 15
	c_t5001 += MAS[2]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 15
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 15
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	S += c_t2_t0_t3 >= 16
	c_t2_t0_t3 += MAS[3]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=6, delay_cost=1)
	S += c_t2_t1_t0 >= 16
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 16
	c_t2_t1_t1_in += MM_in[0]

	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	S += c_t3101 >= 16
	c_t3101 += MAS[0]

	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	S += c_t3110 >= 16
	c_t3110 += MAS[1]

	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	S += c_t4100 >= 16
	c_t4100 += MAS[2]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 16
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 16
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 17
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	S += c_t2_t0_t2 >= 17
	c_t2_t0_t2 += MAS[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=6, delay_cost=1)
	S += c_t2_t1_t1 >= 17
	c_t2_t1_t1 += MM[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	S += c_t2_t1_t2 >= 17
	c_t2_t1_t2 += MAS[3]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 17
	c_t3000 += MAS[2]

	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	S += c_t3100 >= 17
	c_t3100 += MAS[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 17
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 17
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=6, delay_cost=1)
	S += c_t2_t0_t1 >= 18
	c_t2_t0_t1 += MM[0]

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	S += c_t2_t21 >= 18
	c_t2_t21 += MAS[2]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 18
	c_t4010 += MAS[1]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 18
	c_t4011 += MAS[0]

	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	S += c_t4101 >= 18
	c_t4101 += MAS[3]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 18
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 18
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 18
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 18
	d_t1_t3_t4_mem0 += MAS_MEM[2]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 18
	d_t1_t3_t4_mem1 += MAS_MEM[5]

	c_t5100 = S.Task('c_t5100', length=1, delay_cost=1)
	S += c_t5100 >= 19
	c_t5100 += MAS[1]

	c_t5101 = S.Task('c_t5101', length=1, delay_cost=1)
	S += c_t5101 >= 19
	c_t5101 += MAS[2]

	c_t5110 = S.Task('c_t5110', length=1, delay_cost=1)
	S += c_t5110 >= 19
	c_t5110 += MAS[0]

	c_t5111 = S.Task('c_t5111', length=1, delay_cost=1)
	S += c_t5111 >= 19
	c_t5111 += MAS[3]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 19
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 19
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 19
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=6, delay_cost=1)
	S += d_t1_t3_t4 >= 19
	d_t1_t3_t4 += MM[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 19
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 19
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 19
	d_t3_t3_t0_mem0 += MAS_MEM[6]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 19
	d_t3_t3_t0_mem1 += MAS_MEM[5]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 19
	d_t4_a1_0_mem0 += MAS_MEM[2]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 19
	d_t4_a1_0_mem1 += MAS_MEM[3]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 20
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 20
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 20
	c_t5010 += MAS[3]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 20
	c_t5011 += MAS[0]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=1, delay_cost=1)
	S += d_t0_t3_t5 >= 20
	d_t0_t3_t5 += MAS[2]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 20
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 20
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 20
	d_t2_t2_t3_mem0 += MAS_MEM[4]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 20
	d_t2_t2_t3_mem1 += MAS_MEM[7]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 20
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 20
	d_t2_t3_t4_mem0 += MAS_MEM[6]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 20
	d_t2_t3_t4_mem1 += MAS_MEM[3]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=6, delay_cost=1)
	S += d_t3_t3_t0 >= 20
	d_t3_t3_t0 += MM[0]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=1, delay_cost=1)
	S += d_t4_a1_0 >= 20
	d_t4_a1_0 += MAS[1]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 20
	d_t5_a1_1_mem0 += MAS_MEM[0]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 20
	d_t5_a1_1_mem1 += MAS_MEM[5]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 20
	d_t5_t11_mem0 += MAS_MEM[2]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 20
	d_t5_t11_mem1 += MAS_MEM[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 21
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 21
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 21
	c_t0_t1_t4_mem1 += MAS_MEM[7]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=1, delay_cost=1)
	S += c_t0_t1_t5 >= 21
	c_t0_t1_t5 += MAS[1]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 21
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 21
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 21
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=1, delay_cost=1)
	S += d_t2_t2_t3 >= 21
	d_t2_t2_t3 += MAS[2]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 21
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=6, delay_cost=1)
	S += d_t2_t3_t4 >= 21
	d_t2_t3_t4 += MM[0]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 21
	d_t3_t11_mem0 += MAS_MEM[6]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 21
	d_t3_t11_mem1 += MAS_MEM[5]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 21
	d_t4_a1_1_mem0 += MAS_MEM[2]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 21
	d_t4_a1_1_mem1 += MAS_MEM[3]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 21
	d_t5_a1_0_mem0 += MAS_MEM[4]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 21
	d_t5_a1_0_mem1 += MAS_MEM[1]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=1, delay_cost=1)
	S += d_t5_a1_1 >= 21
	d_t5_a1_1 += MAS[0]

	d_t5_t11 = S.Task('d_t5_t11', length=1, delay_cost=1)
	S += d_t5_t11 >= 21
	d_t5_t11 += MAS[3]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 22
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 22
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=6, delay_cost=1)
	S += c_t0_t1_t4 >= 22
	c_t0_t1_t4 += MM[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 22
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 22
	d_t0_t2_t3_mem0 += MAS_MEM[0]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 22
	d_t0_t2_t3_mem1 += MAS_MEM[3]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=1, delay_cost=1)
	S += d_t1_t3_t5 >= 22
	d_t1_t3_t5 += MAS[3]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 22
	d_t3_a1_1_mem0 += MAS_MEM[4]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 22
	d_t3_a1_1_mem1 += MAS_MEM[5]

	d_t3_t11 = S.Task('d_t3_t11', length=1, delay_cost=1)
	S += d_t3_t11 >= 22
	d_t3_t11 += MAS[2]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 22
	d_t3_t3_t2_mem0 += MAS_MEM[6]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 22
	d_t3_t3_t2_mem1 += MAS_MEM[7]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 22
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=1, delay_cost=1)
	S += d_t4_a1_1 >= 22
	d_t4_a1_1 += MAS[1]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=1, delay_cost=1)
	S += d_t5_a1_0 >= 22
	d_t5_a1_0 += MAS[0]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 22
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 22
	d_t5_t3_t1_mem0 += MAS_MEM[2]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 22
	d_t5_t3_t1_mem1 += MAS_MEM[1]

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	S += c_t0_t00 >= 23
	c_t0_t00 += MAS[1]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 23
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 23
	d_t0_t00_mem1 += MAS_MEM[7]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=1, delay_cost=1)
	S += d_t0_t2_t3 >= 23
	d_t0_t2_t3 += MAS[2]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 23
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 23
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 23
	d_t2_t30_mem1 += MM_MEM[1]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=1, delay_cost=1)
	S += d_t3_a1_1 >= 23
	d_t3_a1_1 += MAS[3]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=1, delay_cost=1)
	S += d_t3_t3_t2 >= 23
	d_t3_t3_t2 += MAS[0]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 23
	d_t4_t3_t3_mem0 += MAS_MEM[2]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 23
	d_t4_t3_t3_mem1 += MAS_MEM[3]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 23
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 23
	d_t5_t3_t0_mem0 += MAS_MEM[0]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 23
	d_t5_t3_t0_mem1 += MAS_MEM[5]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=6, delay_cost=1)
	S += d_t5_t3_t1 >= 23
	d_t5_t3_t1 += MM[0]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 23
	d_t5_t3_t3_mem0 += MAS_MEM[4]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 23
	d_t5_t3_t3_mem1 += MAS_MEM[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 24
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 24
	c_t0_t4_t1_mem0 += MAS_MEM[6]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 24
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 24
	c_t4_t0_t2_mem0 += MAS_MEM[2]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 24
	c_t4_t0_t2_mem1 += MAS_MEM[7]

	d_t0_t00 = S.Task('d_t0_t00', length=1, delay_cost=1)
	S += d_t0_t00 >= 24
	d_t0_t00 += MAS[2]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 24
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 24
	d_t0_t30_mem1 += MM_MEM[1]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 24
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t30 = S.Task('d_t2_t30', length=1, delay_cost=1)
	S += d_t2_t30 >= 24
	d_t2_t30 += MAS[1]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 24
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 24
	d_t3_a1_0_mem0 += MAS_MEM[4]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 24
	d_t3_a1_0_mem1 += MAS_MEM[5]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 24
	d_t4_t10_mem0 += MAS_MEM[0]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 24
	d_t4_t10_mem1 += MAS_MEM[3]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=1, delay_cost=1)
	S += d_t4_t3_t3 >= 24
	d_t4_t3_t3 += MAS[0]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=6, delay_cost=1)
	S += d_t5_t3_t0 >= 24
	d_t5_t3_t0 += MM[0]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=1, delay_cost=1)
	S += d_t5_t3_t3 >= 24
	d_t5_t3_t3 += MAS[3]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 25
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 25
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=6, delay_cost=1)
	S += c_t0_t4_t1 >= 25
	c_t0_t4_t1 += MM[0]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 25
	c_t0_t4_t2_mem0 += MAS_MEM[2]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 25
	c_t0_t4_t2_mem1 += MAS_MEM[7]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=1, delay_cost=1)
	S += c_t4_t0_t2 >= 25
	c_t4_t0_t2 += MAS[2]

	d_t0_t30 = S.Task('d_t0_t30', length=1, delay_cost=1)
	S += d_t0_t30 >= 25
	d_t0_t30 += MAS[1]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 25
	d_t1_t2_t3_mem0 += MAS_MEM[6]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 25
	d_t1_t2_t3_mem1 += MAS_MEM[1]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 25
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 25
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=1, delay_cost=1)
	S += d_t3_a1_0 >= 25
	d_t3_a1_0 += MAS[0]

	d_t4_t10 = S.Task('d_t4_t10', length=1, delay_cost=1)
	S += d_t4_t10 >= 25
	d_t4_t10 += MAS[3]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 25
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 25
	d_t4_t3_t1_mem0 += MAS_MEM[4]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 25
	d_t4_t3_t1_mem1 += MAS_MEM[3]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 25
	d_t4_t3_t2_mem0 += MAS_MEM[0]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 25
	d_t4_t3_t2_mem1 += MAS_MEM[5]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=1, delay_cost=1)
	S += c_t0_t0_t5 >= 26
	c_t0_t0_t5 += MAS[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 26
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 26
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=1, delay_cost=1)
	S += c_t0_t4_t2 >= 26
	c_t0_t4_t2 += MAS[3]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 26
	c_t1_t4_t2_mem0 += MAS_MEM[4]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 26
	c_t1_t4_t2_mem1 += MAS_MEM[7]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 26
	d_t0_t01_mem1 += MAS_MEM[1]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 26
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 26
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 26
	d_t0_t3_t4_in += MM_in[0]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 26
	d_t0_t3_t4_mem0 += MAS_MEM[2]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 26
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=1, delay_cost=1)
	S += d_t1_t2_t3 >= 26
	d_t1_t2_t3 += MAS[0]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 26
	d_t3_t10_mem0 += MAS_MEM[6]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 26
	d_t3_t10_mem1 += MAS_MEM[5]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=6, delay_cost=1)
	S += d_t4_t3_t1 >= 26
	d_t4_t3_t1 += MM[0]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=1, delay_cost=1)
	S += d_t4_t3_t2 >= 26
	d_t4_t3_t2 += MAS[2]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 27
	c_t0_t10 += MAS[2]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=1, delay_cost=1)
	S += c_t1_t4_t2 >= 27
	c_t1_t4_t2 += MAS[1]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 27
	c_t2_t4_t3_mem0 += MAS_MEM[6]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 27
	c_t2_t4_t3_mem1 += MAS_MEM[7]

	d_t0_t01 = S.Task('d_t0_t01', length=1, delay_cost=1)
	S += d_t0_t01 >= 27
	d_t0_t01 += MAS[0]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=6, delay_cost=1)
	S += d_t0_t3_t4 >= 27
	d_t0_t3_t4 += MM[0]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 27
	d_t1_t01_mem1 += MAS_MEM[1]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 27
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 27
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 27
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 27
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t3_t10 = S.Task('d_t3_t10', length=1, delay_cost=1)
	S += d_t3_t10 >= 27
	d_t3_t10 += MAS[3]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 27
	d_t3_t3_t3_mem0 += MAS_MEM[4]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 27
	d_t3_t3_t3_mem1 += MAS_MEM[5]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 27
	d_t4_t3_t0_in += MM_in[0]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 27
	d_t4_t3_t0_mem0 += MAS_MEM[0]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 27
	d_t4_t3_t0_mem1 += MAS_MEM[3]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 28
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 28
	c_t0_t0_t4_mem0 += MAS_MEM[4]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 28
	c_t0_t0_t4_mem1 += MAS_MEM[3]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=1, delay_cost=1)
	S += c_t2_t4_t3 >= 28
	c_t2_t4_t3 += MAS[2]

	d_t1_t01 = S.Task('d_t1_t01', length=1, delay_cost=1)
	S += d_t1_t01 >= 28
	d_t1_t01 += MAS[0]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 28
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 28
	d_t1_t30_mem1 += MM_MEM[1]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 28
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 28
	d_t2_t00_mem1 += MAS_MEM[1]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 28
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=1, delay_cost=1)
	S += d_t2_t3_t5 >= 28
	d_t2_t3_t5 += MAS[1]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	S += d_t3_t01_mem0 >= 28
	d_t3_t01_mem0 += MAS_MEM[6]

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	S += d_t3_t01_mem1 >= 28
	d_t3_t01_mem1 += MAS_MEM[7]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=1, delay_cost=1)
	S += d_t3_t3_t3 >= 28
	d_t3_t3_t3 += MAS[3]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=6, delay_cost=1)
	S += d_t4_t3_t0 >= 28
	d_t4_t3_t0 += MM[0]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 28
	d_t5_t10_mem0 += MAS_MEM[0]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 28
	d_t5_t10_mem1 += MAS_MEM[5]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=6, delay_cost=1)
	S += c_t0_t0_t4 >= 29
	c_t0_t0_t4 += MM[0]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 29
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 29
	c_t2_t00_mem1 += MM_MEM[1]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 29
	c_t3_t0_t3_mem0 += MAS_MEM[0]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 29
	c_t3_t0_t3_mem1 += MAS_MEM[1]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	S += d_t010_mem0 >= 29
	d_t010_mem0 += MAS_MEM[2]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 29
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 29
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t30 = S.Task('d_t1_t30', length=1, delay_cost=1)
	S += d_t1_t30 >= 29
	d_t1_t30 += MAS[2]

	d_t2_t00 = S.Task('d_t2_t00', length=1, delay_cost=1)
	S += d_t2_t00 >= 29
	d_t2_t00 += MAS[1]

	d_t3_t01 = S.Task('d_t3_t01', length=1, delay_cost=1)
	S += d_t3_t01 >= 29
	d_t3_t01 += MAS[0]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 29
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 29
	d_t3_t3_t1_mem0 += MAS_MEM[6]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 29
	d_t3_t3_t1_mem1 += MAS_MEM[5]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 29
	d_t4_t11_mem0 += MAS_MEM[4]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 29
	d_t4_t11_mem1 += MAS_MEM[3]

	d_t5_t10 = S.Task('d_t5_t10', length=1, delay_cost=1)
	S += d_t5_t10 >= 29
	d_t5_t10 += MAS[3]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 30
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 30
	c_t0_t4_t0_mem0 += MAS_MEM[2]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 30
	c_t0_t4_t0_mem1 += MAS_MEM[5]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 30
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 30
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 30
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	S += c_t2_t00 >= 30
	c_t2_t00 += MAS[3]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=1, delay_cost=1)
	S += c_t3_t0_t3 >= 30
	c_t3_t0_t3 += MAS[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 30
	c_t4_t30_mem0 += MAS_MEM[4]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 30
	c_t4_t30_mem1 += MAS_MEM[7]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 30
	c_t4_t31_mem0 += MAS_MEM[6]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 30
	c_t4_t31_mem1 += MAS_MEM[1]

	d_t010 = S.Task('d_t010', length=1, delay_cost=1)
	S += d_t010 >= 30
	d_t010 += MAS[0]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=6, delay_cost=1)
	S += d_t3_t3_t1 >= 30
	d_t3_t3_t1 += MM[0]

	d_t4_t11 = S.Task('d_t4_t11', length=1, delay_cost=1)
	S += d_t4_t11 >= 30
	d_t4_t11 += MAS[2]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 30
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 30
	d_t5_t3_t2_mem0 += MAS_MEM[0]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 30
	d_t5_t3_t2_mem1 += MAS_MEM[3]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 31
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=6, delay_cost=1)
	S += c_t0_t4_t0 >= 31
	c_t0_t4_t0 += MM[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 31
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 31
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 31
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=1, delay_cost=1)
	S += c_t1_t1_t5 >= 31
	c_t1_t1_t5 += MAS[0]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 31
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 31
	c_t2_t0_t4_mem0 += MAS_MEM[2]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 31
	c_t2_t0_t4_mem1 += MAS_MEM[7]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 31
	c_t3_t20_mem0 += MAS_MEM[4]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 31
	c_t3_t20_mem1 += MAS_MEM[1]

	c_t4_t30 = S.Task('c_t4_t30', length=1, delay_cost=1)
	S += c_t4_t30 >= 31
	c_t4_t30 += MAS[1]

	c_t4_t31 = S.Task('c_t4_t31', length=1, delay_cost=1)
	S += c_t4_t31 >= 31
	c_t4_t31 += MAS[2]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 31
	d_t1_t00_mem1 += MAS_MEM[3]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 31
	d_t2_t01_mem1 += MAS_MEM[5]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=1, delay_cost=1)
	S += d_t5_t3_t2 >= 31
	d_t5_t3_t2 += MAS[3]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 32
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=1, delay_cost=1)
	S += c_t1_t0_t5 >= 32
	c_t1_t0_t5 += MAS[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 32
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 32
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 32
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 32
	c_t1_t4_t3_mem0 += MAS_MEM[4]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 32
	c_t1_t4_t3_mem1 += MAS_MEM[7]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=6, delay_cost=1)
	S += c_t2_t0_t4 >= 32
	c_t2_t0_t4 += MM[0]

	c_t3_t20 = S.Task('c_t3_t20', length=1, delay_cost=1)
	S += c_t3_t20 >= 32
	c_t3_t20 += MAS[2]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 32
	c_t4_t21_mem0 += MAS_MEM[6]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 32
	c_t4_t21_mem1 += MAS_MEM[1]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 32
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 32
	c_t5_t0_t0_mem0 += MAS_MEM[0]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 32
	c_t5_t0_t0_mem1 += MAS_MEM[3]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 32
	c_t5_t0_t3_mem0 += MAS_MEM[2]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 32
	c_t5_t0_t3_mem1 += MAS_MEM[5]

	d_t1_t00 = S.Task('d_t1_t00', length=1, delay_cost=1)
	S += d_t1_t00 >= 32
	d_t1_t00 += MAS[0]

	d_t2_t01 = S.Task('d_t2_t01', length=1, delay_cost=1)
	S += d_t2_t01 >= 32
	d_t2_t01 += MAS[1]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 33
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 33
	c_t0_t4_t3_mem0 += MAS_MEM[4]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 33
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 33
	c_t1_t10 += MAS[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 33
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 33
	c_t1_t4_t1_mem0 += MAS_MEM[6]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 33
	c_t1_t4_t1_mem1 += MAS_MEM[7]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=1, delay_cost=1)
	S += c_t1_t4_t3 >= 33
	c_t1_t4_t3 += MAS[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 33
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 33
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 33
	c_t3_t1_t3_mem0 += MAS_MEM[2]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 33
	c_t3_t1_t3_mem1 += MAS_MEM[5]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 33
	c_t3_t30_mem0 += MAS_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 33
	c_t3_t30_mem1 += MAS_MEM[3]

	c_t4_t21 = S.Task('c_t4_t21', length=1, delay_cost=1)
	S += c_t4_t21 >= 33
	c_t4_t21 += MAS[2]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=6, delay_cost=1)
	S += c_t5_t0_t0 >= 33
	c_t5_t0_t0 += MM[0]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=1, delay_cost=1)
	S += c_t5_t0_t3 >= 33
	c_t5_t0_t3 += MAS[3]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 33
	d_t5001_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=1, delay_cost=1)
	S += c_t0_t4_t3 >= 34
	c_t0_t4_t3 += MAS[1]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 34
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 34
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=6, delay_cost=1)
	S += c_t1_t4_t1 >= 34
	c_t1_t4_t1 += MM[0]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=1, delay_cost=1)
	S += c_t2_t0_t5 >= 34
	c_t2_t0_t5 += MAS[3]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 34
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 34
	c_t2_t1_t4_mem0 += MAS_MEM[6]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 34
	c_t2_t1_t4_mem1 += MAS_MEM[1]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 34
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 34
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=1, delay_cost=1)
	S += c_t3_t1_t3 >= 34
	c_t3_t1_t3 += MAS[0]

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	S += c_t3_t30 >= 34
	c_t3_t30 += MAS[2]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 34
	c_t4_t0_t3_mem0 += MAS_MEM[4]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 34
	c_t4_t0_t3_mem1 += MAS_MEM[7]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 34
	c_t4_t20_mem0 += MAS_MEM[2]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 34
	c_t4_t20_mem1 += MAS_MEM[3]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 34
	c_t5_t0_t2_mem0 += MAS_MEM[0]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 34
	c_t5_t0_t2_mem1 += MAS_MEM[5]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 35
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 35
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 35
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 35
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=6, delay_cost=1)
	S += c_t2_t1_t4 >= 35
	c_t2_t1_t4 += MM[0]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=1, delay_cost=1)
	S += c_t2_t1_t5 >= 35
	c_t2_t1_t5 += MAS[2]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 35
	c_t2_t4_t2_mem0 += MAS_MEM[4]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 35
	c_t2_t4_t2_mem1 += MAS_MEM[5]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 35
	c_t3_t1_t2_mem0 += MAS_MEM[0]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 35
	c_t3_t1_t2_mem1 += MAS_MEM[3]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 35
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 35
	c_t4_t0_t1_mem0 += MAS_MEM[6]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 35
	c_t4_t0_t1_mem1 += MAS_MEM[7]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=1, delay_cost=1)
	S += c_t4_t0_t3 >= 35
	c_t4_t0_t3 += MAS[1]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 35
	c_t4_t1_t2_mem0 += MAS_MEM[2]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 35
	c_t4_t1_t2_mem1 += MAS_MEM[1]

	c_t4_t20 = S.Task('c_t4_t20', length=1, delay_cost=1)
	S += c_t4_t20 >= 35
	c_t4_t20 += MAS[0]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=1, delay_cost=1)
	S += c_t5_t0_t2 >= 35
	c_t5_t0_t2 += MAS[3]

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	S += c_t1_t00 >= 36
	c_t1_t00 += MAS[3]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 36
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 36
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 36
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 36
	c_t2_t4_t1_mem0 += MAS_MEM[4]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 36
	c_t2_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=1, delay_cost=1)
	S += c_t2_t4_t2 >= 36
	c_t2_t4_t2 += MAS[2]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=1, delay_cost=1)
	S += c_t3_t1_t2 >= 36
	c_t3_t1_t2 += MAS[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 36
	c_t3_t21_mem0 += MAS_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 36
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 36
	c_t3_t31_mem0 += MAS_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 36
	c_t3_t31_mem1 += MAS_MEM[5]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=6, delay_cost=1)
	S += c_t4_t0_t1 >= 36
	c_t4_t0_t1 += MM[0]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=1, delay_cost=1)
	S += c_t4_t1_t2 >= 36
	c_t4_t1_t2 += MAS[0]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 36
	c_t4_t1_t3_mem0 += MAS_MEM[6]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 36
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 36
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 36
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 37
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 37
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 37
	c_t2_t10 += MAS[3]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=6, delay_cost=1)
	S += c_t2_t4_t1 >= 37
	c_t2_t4_t1 += MM[0]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 37
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 37
	c_t3_t0_t1_mem0 += MAS_MEM[2]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 37
	c_t3_t0_t1_mem1 += MAS_MEM[1]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 37
	c_t3_t0_t2_mem0 += MAS_MEM[4]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 37
	c_t3_t0_t2_mem1 += MAS_MEM[3]

	c_t3_t21 = S.Task('c_t3_t21', length=1, delay_cost=1)
	S += c_t3_t21 >= 37
	c_t3_t21 += MAS[1]

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	S += c_t3_t31 >= 37
	c_t3_t31 += MAS[2]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=1, delay_cost=1)
	S += c_t4_t1_t3 >= 37
	c_t4_t1_t3 += MAS[0]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 37
	c_t5_t20_mem0 += MAS_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 37
	c_t5_t20_mem1 += MAS_MEM[7]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem0 >= 37
	d_t4_t2_t3_mem0 += MAS_MEM[6]

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem1 >= 37
	d_t4_t2_t3_mem1 += MAS_MEM[5]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem0 >= 37
	d_t5_t3_t5_mem0 += MM_MEM[0]

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem1 >= 37
	d_t5_t3_t5_mem1 += MM_MEM[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 38
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 38
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=6, delay_cost=1)
	S += c_t3_t0_t1 >= 38
	c_t3_t0_t1 += MM[0]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=1, delay_cost=1)
	S += c_t3_t0_t2 >= 38
	c_t3_t0_t2 += MAS[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 38
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 38
	c_t4_t1_t0_mem0 += MAS_MEM[2]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 38
	c_t4_t1_t0_mem1 += MAS_MEM[7]

	c_t5_t20 = S.Task('c_t5_t20', length=1, delay_cost=1)
	S += c_t5_t20 >= 38
	c_t5_t20 += MAS[2]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 38
	c_t5_t21_mem0 += MAS_MEM[4]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 38
	c_t5_t21_mem1 += MAS_MEM[1]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem0 >= 38
	d_t3_t2_t3_mem0 += MAS_MEM[6]

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem1 >= 38
	d_t3_t2_t3_mem1 += MAS_MEM[5]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	S += d_t4_t00_mem0 >= 38
	d_t4_t00_mem0 += MAS_MEM[0]

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	S += d_t4_t00_mem1 >= 38
	d_t4_t00_mem1 += MAS_MEM[3]

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=1, delay_cost=1)
	S += d_t4_t2_t3 >= 38
	d_t4_t2_t3 += MAS[1]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem0 >= 38
	d_t4_t3_t5_mem0 += MM_MEM[0]

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem1 >= 38
	d_t4_t3_t5_mem1 += MM_MEM[1]

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=1, delay_cost=1)
	S += d_t5_t3_t5 >= 38
	d_t5_t3_t5 += MAS[3]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 39
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 39
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 39
	c_t0_t11_mem0 += MM_MEM[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 39
	c_t0_t11_mem1 += MAS_MEM[3]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 39
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 39
	c_t1_t4_t0_mem0 += MAS_MEM[4]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 39
	c_t1_t4_t0_mem1 += MAS_MEM[5]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=6, delay_cost=1)
	S += c_t4_t1_t0 >= 39
	c_t4_t1_t0 += MM[0]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 39
	c_t5_t1_t3_mem0 += MAS_MEM[0]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 39
	c_t5_t1_t3_mem1 += MAS_MEM[7]

	c_t5_t21 = S.Task('c_t5_t21', length=1, delay_cost=1)
	S += c_t5_t21 >= 39
	c_t5_t21 += MAS[3]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 39
	c_t5_t30_mem0 += MAS_MEM[2]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 39
	c_t5_t30_mem1 += MAS_MEM[1]

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=1, delay_cost=1)
	S += d_t3_t2_t3 >= 39
	d_t3_t2_t3 += MAS[2]

	d_t4_t00 = S.Task('d_t4_t00', length=1, delay_cost=1)
	S += d_t4_t00 >= 39
	d_t4_t00 += MAS[0]

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=1, delay_cost=1)
	S += d_t4_t3_t5 >= 39
	d_t4_t3_t5 += MAS[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 40
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 40
	c_t0_t01_mem1 += MAS_MEM[3]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 40
	c_t0_t11 += MAS[3]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 40
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 40
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=6, delay_cost=1)
	S += c_t1_t4_t0 >= 40
	c_t1_t4_t0 += MM[0]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 40
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 40
	c_t4_t0_t0_mem0 += MAS_MEM[2]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 40
	c_t4_t0_t0_mem1 += MAS_MEM[5]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 40
	c_t5_t1_t2_mem0 += MAS_MEM[6]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 40
	c_t5_t1_t2_mem1 += MAS_MEM[1]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=1, delay_cost=1)
	S += c_t5_t1_t3 >= 40
	c_t5_t1_t3 += MAS[1]

	c_t5_t30 = S.Task('c_t5_t30', length=1, delay_cost=1)
	S += c_t5_t30 >= 40
	c_t5_t30 += MAS[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 40
	c_t5_t31_mem0 += MAS_MEM[4]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 40
	c_t5_t31_mem1 += MAS_MEM[7]

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	S += c_t0_t01 >= 41
	c_t0_t01 += MAS[2]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 41
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 41
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 41
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 41
	c_t0_t50_mem0 += MAS_MEM[2]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 41
	c_t0_t50_mem1 += MAS_MEM[5]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 41
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 41
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 41
	c_t1_t0_t4_mem0 += MAS_MEM[4]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 41
	c_t1_t0_t4_mem1 += MAS_MEM[7]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=6, delay_cost=1)
	S += c_t4_t0_t0 >= 41
	c_t4_t0_t0 += MM[0]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=1, delay_cost=1)
	S += c_t5_t1_t2 >= 41
	c_t5_t1_t2 += MAS[3]

	c_t5_t31 = S.Task('c_t5_t31', length=1, delay_cost=1)
	S += c_t5_t31 >= 41
	c_t5_t31 += MAS[1]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem0 >= 41
	d_t1_t2_t2_mem0 += MAS_MEM[0]

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem1 >= 41
	d_t1_t2_t2_mem1 += MAS_MEM[1]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=1, delay_cost=1)
	S += c_t0_t4_t5 >= 42
	c_t0_t4_t5 += MAS[0]

	c_t0_t50 = S.Task('c_t0_t50', length=1, delay_cost=1)
	S += c_t0_t50 >= 42
	c_t0_t50 += MAS[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=6, delay_cost=1)
	S += c_t1_t0_t4 >= 42
	c_t1_t0_t4 += MM[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 42
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 42
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 42
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 42
	c_t3_t1_t1_mem0 += MAS_MEM[2]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 42
	c_t3_t1_t1_mem1 += MAS_MEM[5]

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=1, delay_cost=1)
	S += d_t1_t2_t2 >= 42
	d_t1_t2_t2 += MAS[3]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	S += d_t3_t30_mem0 >= 42
	d_t3_t30_mem0 += MM_MEM[0]

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	S += d_t3_t30_mem1 >= 42
	d_t3_t30_mem1 += MM_MEM[1]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	S += d_t4_t01_mem0 >= 42
	d_t4_t01_mem0 += MAS_MEM[4]

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	S += d_t4_t01_mem1 >= 42
	d_t4_t01_mem1 += MAS_MEM[3]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	S += d_t5_t00_mem0 >= 42
	d_t5_t00_mem0 += MAS_MEM[0]

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	S += d_t5_t00_mem1 >= 42
	d_t5_t00_mem1 += MAS_MEM[1]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem0 >= 42
	d_t5_t2_t3_mem0 += MAS_MEM[6]

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem1 >= 42
	d_t5_t2_t3_mem1 += MAS_MEM[7]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 43
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 43
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 43
	c_t2_t01_mem1 += MAS_MEM[7]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 43
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 43
	c_t3_t0_t0_mem0 += MAS_MEM[4]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 43
	c_t3_t0_t0_mem1 += MAS_MEM[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=6, delay_cost=1)
	S += c_t3_t1_t1 >= 43
	c_t3_t1_t1 += MM[0]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 43
	c_t4_t4_t2_mem0 += MAS_MEM[0]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 43
	c_t4_t4_t2_mem1 += MAS_MEM[5]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem0 >= 43
	d_t2_t2_t2_mem0 += MAS_MEM[2]

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem1 >= 43
	d_t2_t2_t2_mem1 += MAS_MEM[3]

	d_t310_mem0 = S.Task('d_t310_mem0', length=1, delay_cost=1)
	S += d_t310_mem0 >= 43
	d_t310_mem0 += MAS_MEM[6]

	d_t3_t30 = S.Task('d_t3_t30', length=1, delay_cost=1)
	S += d_t3_t30 >= 43
	d_t3_t30 += MAS[3]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 43
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4_t01 = S.Task('d_t4_t01', length=1, delay_cost=1)
	S += d_t4_t01 >= 43
	d_t4_t01 += MAS[2]

	d_t5_t00 = S.Task('d_t5_t00', length=1, delay_cost=1)
	S += d_t5_t00 >= 43
	d_t5_t00 += MAS[1]

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=1, delay_cost=1)
	S += d_t5_t2_t3 >= 43
	d_t5_t2_t3 += MAS[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 44
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 44
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	S += c_t2_t01 >= 44
	c_t2_t01 += MAS[0]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=6, delay_cost=1)
	S += c_t3_t0_t0 >= 44
	c_t3_t0_t0 += MM[0]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=1, delay_cost=1)
	S += c_t4_t4_t2 >= 44
	c_t4_t4_t2 += MAS[1]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 44
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 44
	c_t5_t0_t1_mem0 += MAS_MEM[4]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 44
	c_t5_t0_t1_mem1 += MAS_MEM[5]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 44
	c_t5_t4_t3_mem0 += MAS_MEM[0]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 44
	c_t5_t4_t3_mem1 += MAS_MEM[3]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	S += d_t210_mem0 >= 44
	d_t210_mem0 += MAS_MEM[2]

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=1, delay_cost=1)
	S += d_t2_t2_t2 >= 44
	d_t2_t2_t2 += MAS[2]

	d_t310 = S.Task('d_t310', length=1, delay_cost=1)
	S += d_t310 >= 44
	d_t310 += MAS[3]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	S += d_t3_t00_mem0 >= 44
	d_t3_t00_mem0 += MAS_MEM[6]

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	S += d_t3_t00_mem1 >= 44
	d_t3_t00_mem1 += MAS_MEM[1]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem0 >= 44
	d_t3_t3_t5_mem0 += MM_MEM[0]

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem1 >= 44
	d_t3_t3_t5_mem1 += MM_MEM[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 45
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 45
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 45
	c_t2_t4_t0_mem0 += MAS_MEM[4]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 45
	c_t2_t4_t0_mem1 += MAS_MEM[7]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=6, delay_cost=1)
	S += c_t5_t0_t1 >= 45
	c_t5_t0_t1 += MM[0]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=1, delay_cost=1)
	S += c_t5_t4_t3 >= 45
	c_t5_t4_t3 += MAS[2]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	S += d_t0_t31_mem0 >= 45
	d_t0_t31_mem0 += MM_MEM[0]

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	S += d_t0_t31_mem1 >= 45
	d_t0_t31_mem1 += MAS_MEM[5]

	d_t210 = S.Task('d_t210', length=1, delay_cost=1)
	S += d_t210 >= 45
	d_t210 += MAS[1]

	d_t3_t00 = S.Task('d_t3_t00', length=1, delay_cost=1)
	S += d_t3_t00 >= 45
	d_t3_t00 += MAS[0]

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=1, delay_cost=1)
	S += d_t3_t3_t5 >= 45
	d_t3_t3_t5 += MAS[3]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 45
	d_t4011_mem1 += MAIN_MEM_r[1]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	S += d_t5_t01_mem0 >= 45
	d_t5_t01_mem0 += MAS_MEM[2]

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	S += d_t5_t01_mem1 >= 45
	d_t5_t01_mem1 += MAS_MEM[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 46
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 46
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 46
	c_t0_t40_mem1 += MM_MEM[1]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 46
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 46
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 46
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 46
	c_t1_t1_t4_mem1 += MAS_MEM[3]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 46
	c_t1_t50_mem0 += MAS_MEM[6]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 46
	c_t1_t50_mem1 += MAS_MEM[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=6, delay_cost=1)
	S += c_t2_t4_t0 >= 46
	c_t2_t4_t0 += MM[0]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 46
	c_t4_t4_t3_mem0 += MAS_MEM[2]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 46
	c_t4_t4_t3_mem1 += MAS_MEM[5]

	d_t0_t31 = S.Task('d_t0_t31', length=1, delay_cost=1)
	S += d_t0_t31 >= 46
	d_t0_t31 += MAS[2]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	S += d_t110_mem0 >= 46
	d_t110_mem0 += MAS_MEM[4]

	d_t5_t01 = S.Task('d_t5_t01', length=1, delay_cost=1)
	S += d_t5_t01 >= 46
	d_t5_t01 += MAS[0]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	S += c_t0_s01_mem0 >= 47
	c_t0_s01_mem0 += MAS_MEM[6]

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	S += c_t0_s01_mem1 >= 47
	c_t0_s01_mem1 += MAS_MEM[5]

	c_t0_t40 = S.Task('c_t0_t40', length=1, delay_cost=1)
	S += c_t0_t40 >= 47
	c_t0_t40 += MAS[1]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 47
	c_t1_t01_mem0 += MM_MEM[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 47
	c_t1_t01_mem1 += MAS_MEM[7]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 47
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=6, delay_cost=1)
	S += c_t1_t1_t4 >= 47
	c_t1_t1_t4 += MM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 47
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t50 = S.Task('c_t1_t50', length=1, delay_cost=1)
	S += c_t1_t50 >= 47
	c_t1_t50 += MAS[0]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 47
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 47
	c_t3_t1_t0_mem0 += MAS_MEM[0]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 47
	c_t3_t1_t0_mem1 += MAS_MEM[3]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=1, delay_cost=1)
	S += c_t4_t4_t3 >= 47
	c_t4_t4_t3 += MAS[3]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem0 >= 47
	d_t0_t2_t2_mem0 += MAS_MEM[4]

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem1 >= 47
	d_t0_t2_t2_mem1 += MAS_MEM[1]

	d_t110 = S.Task('d_t110', length=1, delay_cost=1)
	S += d_t110 >= 47
	d_t110 += MAS[2]

	c_t0_s01 = S.Task('c_t0_s01', length=1, delay_cost=1)
	S += c_t0_s01 >= 48
	c_t0_s01 += MAS[3]

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	S += c_t1_t01 >= 48
	c_t1_t01 += MAS[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 48
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 48
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 48
	c_t1_t40_mem1 += MM_MEM[1]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 48
	c_t2_t50_mem0 += MAS_MEM[6]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 48
	c_t2_t50_mem1 += MAS_MEM[7]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=6, delay_cost=1)
	S += c_t3_t1_t0 >= 48
	c_t3_t1_t0 += MM[0]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 48
	c_t3_t4_t2_mem0 += MAS_MEM[4]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 48
	c_t3_t4_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 48
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 48
	c_t4_t1_t1_mem0 += MAS_MEM[0]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 48
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=1, delay_cost=1)
	S += d_t0_t2_t2 >= 48
	d_t0_t2_t2 += MAS[2]

	d_t0_t40_mem0 = S.Task('d_t0_t40_mem0', length=1, delay_cost=1)
	S += d_t0_t40_mem0 >= 48
	d_t0_t40_mem0 += MAS_MEM[2]

	d_t0_t40_mem1 = S.Task('d_t0_t40_mem1', length=1, delay_cost=1)
	S += d_t0_t40_mem1 >= 48
	d_t0_t40_mem1 += MAS_MEM[5]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 48
	d_t5010_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 49
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 49
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t40 = S.Task('c_t1_t40', length=1, delay_cost=1)
	S += c_t1_t40 >= 49
	c_t1_t40 += MAS[2]

	c_t2_t50 = S.Task('c_t2_t50', length=1, delay_cost=1)
	S += c_t2_t50 >= 49
	c_t2_t50 += MAS[3]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=1, delay_cost=1)
	S += c_t3_t4_t2 >= 49
	c_t3_t4_t2 += MAS[0]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 49
	c_t3_t4_t3_mem0 += MAS_MEM[4]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 49
	c_t3_t4_t3_mem1 += MAS_MEM[5]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=6, delay_cost=1)
	S += c_t4_t1_t1 >= 49
	c_t4_t1_t1 += MM[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 49
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 49
	c_t5_t1_t1_mem0 += MAS_MEM[0]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 49
	c_t5_t1_t1_mem1 += MAS_MEM[7]

	d_t0_t40 = S.Task('d_t0_t40', length=1, delay_cost=1)
	S += d_t0_t40 >= 49
	d_t0_t40 += MAS[1]

	d_t5_t2_t2_mem0 = S.Task('d_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem0 >= 49
	d_t5_t2_t2_mem0 += MAS_MEM[2]

	d_t5_t2_t2_mem1 = S.Task('d_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem1 >= 49
	d_t5_t2_t2_mem1 += MAS_MEM[1]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	S += d_t5_t30_mem0 >= 49
	d_t5_t30_mem0 += MM_MEM[0]

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	S += d_t5_t30_mem1 >= 49
	d_t5_t30_mem1 += MM_MEM[1]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 50
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 50
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=1, delay_cost=1)
	S += c_t3_t4_t3 >= 50
	c_t3_t4_t3 += MAS[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 50
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 50
	c_t5_t1_t0_mem0 += MAS_MEM[6]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 50
	c_t5_t1_t0_mem1 += MAS_MEM[1]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=6, delay_cost=1)
	S += c_t5_t1_t1 >= 50
	c_t5_t1_t1 += MM[0]

	d_s1010_mem0 = S.Task('d_s1010_mem0', length=1, delay_cost=1)
	S += d_s1010_mem0 >= 50
	d_s1010_mem0 += MAS_MEM[4]

	d_s1010_mem1 = S.Task('d_s1010_mem1', length=1, delay_cost=1)
	S += d_s1010_mem1 >= 50
	d_s1010_mem1 += MAS_MEM[3]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	S += d_t1_t31_mem0 >= 50
	d_t1_t31_mem0 += MM_MEM[0]

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	S += d_t1_t31_mem1 >= 50
	d_t1_t31_mem1 += MAS_MEM[7]

	d_t4_t2_t2_mem0 = S.Task('d_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem0 >= 50
	d_t4_t2_t2_mem0 += MAS_MEM[0]

	d_t4_t2_t2_mem1 = S.Task('d_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem1 >= 50
	d_t4_t2_t2_mem1 += MAS_MEM[5]

	d_t510_mem0 = S.Task('d_t510_mem0', length=1, delay_cost=1)
	S += d_t510_mem0 >= 50
	d_t510_mem0 += MAS_MEM[2]

	d_t5_t2_t2 = S.Task('d_t5_t2_t2', length=1, delay_cost=1)
	S += d_t5_t2_t2 >= 50
	d_t5_t2_t2 += MAS[3]

	d_t5_t30 = S.Task('d_t5_t30', length=1, delay_cost=1)
	S += d_t5_t30 >= 50
	d_t5_t30 += MAS[1]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 51
	c_t010_mem0 += MAS_MEM[2]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 51
	c_t010_mem1 += MAS_MEM[3]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 51
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 51
	c_t110_mem0 += MAS_MEM[4]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 51
	c_t110_mem1 += MAS_MEM[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 51
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 51
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 51
	c_t2_t40_mem1 += MM_MEM[1]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=6, delay_cost=1)
	S += c_t5_t1_t0 >= 51
	c_t5_t1_t0 += MM[0]

	d_s0010_mem0 = S.Task('d_s0010_mem0', length=1, delay_cost=1)
	S += d_s0010_mem0 >= 51
	d_s0010_mem0 += MAS_MEM[0]

	d_s0010_mem1 = S.Task('d_s0010_mem1', length=1, delay_cost=1)
	S += d_s0010_mem1 >= 51
	d_s0010_mem1 += MAS_MEM[5]

	d_s1010 = S.Task('d_s1010', length=1, delay_cost=1)
	S += d_s1010 >= 51
	d_s1010 += MAS[1]

	d_t1_t31 = S.Task('d_t1_t31', length=1, delay_cost=1)
	S += d_t1_t31 >= 51
	d_t1_t31 += MAS[3]

	d_t4_t2_t2 = S.Task('d_t4_t2_t2', length=1, delay_cost=1)
	S += d_t4_t2_t2 >= 51
	d_t4_t2_t2 += MAS[2]

	d_t510 = S.Task('d_t510', length=1, delay_cost=1)
	S += d_t510 >= 51
	d_t510 += MAS[0]

	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	S += d_t5_t3_t4_in >= 51
	d_t5_t3_t4_in += MM_in[0]

	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem0 >= 51
	d_t5_t3_t4_mem0 += MAS_MEM[6]

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem1 >= 51
	d_t5_t3_t4_mem1 += MAS_MEM[7]

	c_t010 = S.Task('c_t010', length=1, delay_cost=1)
	S += c_t010 >= 52
	c_t010 += MAS[2]

	c_t110 = S.Task('c_t110', length=1, delay_cost=1)
	S += c_t110 >= 52
	c_t110 += MAS[3]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 52
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t40 = S.Task('c_t2_t40', length=1, delay_cost=1)
	S += c_t2_t40 >= 52
	c_t2_t40 += MAS[1]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 52
	c_t5_t4_t2_mem0 += MAS_MEM[4]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 52
	c_t5_t4_t2_mem1 += MAS_MEM[7]

	d_s0010 = S.Task('d_s0010', length=1, delay_cost=1)
	S += d_s0010 >= 52
	d_s0010 += MAS[0]

	d_t111_mem0 = S.Task('d_t111_mem0', length=1, delay_cost=1)
	S += d_t111_mem0 >= 52
	d_t111_mem0 += MAS_MEM[6]

	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	S += d_t2_t2_t0_in >= 52
	d_t2_t2_t0_in += MM_in[0]

	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem0 >= 52
	d_t2_t2_t0_mem0 += MAS_MEM[2]

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem1 >= 52
	d_t2_t2_t0_mem1 += MAS_MEM[5]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	S += d_t2_t31_mem0 >= 52
	d_t2_t31_mem0 += MM_MEM[0]

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	S += d_t2_t31_mem1 >= 52
	d_t2_t31_mem1 += MAS_MEM[3]

	d_t3_t2_t2_mem0 = S.Task('d_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem0 >= 52
	d_t3_t2_t2_mem0 += MAS_MEM[0]

	d_t3_t2_t2_mem1 = S.Task('d_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem1 >= 52
	d_t3_t2_t2_mem1 += MAS_MEM[1]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 52
	d_t5001_mem1 += MAIN_MEM_r[1]

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=6, delay_cost=1)
	S += d_t5_t3_t4 >= 52
	d_t5_t3_t4 += MM[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 53
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 53
	c_t0_t51_mem0 += MAS_MEM[4]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 53
	c_t0_t51_mem1 += MAS_MEM[7]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=1, delay_cost=1)
	S += c_t5_t4_t2 >= 53
	c_t5_t4_t2 += MAS[3]

	d_t111 = S.Task('d_t111', length=1, delay_cost=1)
	S += d_t111 >= 53
	d_t111 += MAS[0]

	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	S += d_t1_t2_t1_in >= 53
	d_t1_t2_t1_in += MM_in[0]

	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem0 >= 53
	d_t1_t2_t1_mem0 += MAS_MEM[0]

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem1 >= 53
	d_t1_t2_t1_mem1 += MAS_MEM[1]

	d_t1_t41_mem0 = S.Task('d_t1_t41_mem0', length=1, delay_cost=1)
	S += d_t1_t41_mem0 >= 53
	d_t1_t41_mem0 += MAS_MEM[6]

	d_t1_t41_mem1 = S.Task('d_t1_t41_mem1', length=1, delay_cost=1)
	S += d_t1_t41_mem1 >= 53
	d_t1_t41_mem1 += MAS_MEM[5]

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=6, delay_cost=1)
	S += d_t2_t2_t0 >= 53
	d_t2_t2_t0 += MM[0]

	d_t2_t31 = S.Task('d_t2_t31', length=1, delay_cost=1)
	S += d_t2_t31 >= 53
	d_t2_t31 += MAS[1]

	d_t2_t40_mem0 = S.Task('d_t2_t40_mem0', length=1, delay_cost=1)
	S += d_t2_t40_mem0 >= 53
	d_t2_t40_mem0 += MAS_MEM[2]

	d_t2_t40_mem1 = S.Task('d_t2_t40_mem1', length=1, delay_cost=1)
	S += d_t2_t40_mem1 >= 53
	d_t2_t40_mem1 += MAS_MEM[3]

	d_t3_t2_t2 = S.Task('d_t3_t2_t2', length=1, delay_cost=1)
	S += d_t3_t2_t2 >= 53
	d_t3_t2_t2 += MAS[2]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	S += d_t4_t30_mem0 >= 53
	d_t4_t30_mem0 += MM_MEM[0]

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	S += d_t4_t30_mem1 >= 53
	d_t4_t30_mem1 += MM_MEM[1]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 53
	d_t5000_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 54
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 54
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 54
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 54
	c_t0_t4_t4_mem0 += MAS_MEM[6]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 54
	c_t0_t4_t4_mem1 += MAS_MEM[3]

	c_t0_t51 = S.Task('c_t0_t51', length=1, delay_cost=1)
	S += c_t0_t51 >= 54
	c_t0_t51 += MAS[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 54
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 54
	c_t2_t11_mem1 += MAS_MEM[5]

	d_s2010_mem0 = S.Task('d_s2010_mem0', length=1, delay_cost=1)
	S += d_s2010_mem0 >= 54
	d_s2010_mem0 += MAS_MEM[2]

	d_s2010_mem1 = S.Task('d_s2010_mem1', length=1, delay_cost=1)
	S += d_s2010_mem1 >= 54
	d_s2010_mem1 += MAS_MEM[1]

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=6, delay_cost=1)
	S += d_t1_t2_t1 >= 54
	d_t1_t2_t1 += MM[0]

	d_t1_t40_mem0 = S.Task('d_t1_t40_mem0', length=1, delay_cost=1)
	S += d_t1_t40_mem0 >= 54
	d_t1_t40_mem0 += MAS_MEM[4]

	d_t1_t40_mem1 = S.Task('d_t1_t40_mem1', length=1, delay_cost=1)
	S += d_t1_t40_mem1 >= 54
	d_t1_t40_mem1 += MAS_MEM[7]

	d_t1_t41 = S.Task('d_t1_t41', length=1, delay_cost=1)
	S += d_t1_t41 >= 54
	d_t1_t41 += MAS[3]

	d_t2_t40 = S.Task('d_t2_t40', length=1, delay_cost=1)
	S += d_t2_t40 >= 54
	d_t2_t40 += MAS[0]

	d_t4_t30 = S.Task('d_t4_t30', length=1, delay_cost=1)
	S += d_t4_t30 >= 54
	d_t4_t30 += MAS[2]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 55
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=6, delay_cost=1)
	S += c_t0_t4_t4 >= 55
	c_t0_t4_t4 += MM[0]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 55
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 55
	c_t1_t11_mem1 += MAS_MEM[1]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 55
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 55
	c_t2_t11 += MAS[2]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 55
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 55
	c_t2_t4_t4_mem0 += MAS_MEM[4]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 55
	c_t2_t4_t4_mem1 += MAS_MEM[5]

	d_s2010 = S.Task('d_s2010', length=1, delay_cost=1)
	S += d_s2010 >= 55
	d_s2010 += MAS[0]

	d_t1_t40 = S.Task('d_t1_t40', length=1, delay_cost=1)
	S += d_t1_t40 >= 55
	d_t1_t40 += MAS[3]

	d_t1_t51_mem0 = S.Task('d_t1_t51_mem0', length=1, delay_cost=1)
	S += d_t1_t51_mem0 >= 55
	d_t1_t51_mem0 += MAS_MEM[6]

	d_t1_t51_mem1 = S.Task('d_t1_t51_mem1', length=1, delay_cost=1)
	S += d_t1_t51_mem1 >= 55
	d_t1_t51_mem1 += MAS_MEM[7]

	d_t2_t41_mem0 = S.Task('d_t2_t41_mem0', length=1, delay_cost=1)
	S += d_t2_t41_mem0 >= 55
	d_t2_t41_mem0 += MAS_MEM[2]

	d_t2_t41_mem1 = S.Task('d_t2_t41_mem1', length=1, delay_cost=1)
	S += d_t2_t41_mem1 >= 55
	d_t2_t41_mem1 += MAS_MEM[3]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 56
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	S += c_t1_s01_mem0 >= 56
	c_t1_s01_mem0 += MAS_MEM[6]

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	S += c_t1_s01_mem1 >= 56
	c_t1_s01_mem1 += MAS_MEM[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 56
	c_t1_t11 += MAS[3]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 56
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 56
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=6, delay_cost=1)
	S += c_t2_t4_t4 >= 56
	c_t2_t4_t4 += MM[0]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 56
	c_t2_t51_mem0 += MAS_MEM[0]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 56
	c_t2_t51_mem1 += MAS_MEM[5]

	d_t0_t41_mem0 = S.Task('d_t0_t41_mem0', length=1, delay_cost=1)
	S += d_t0_t41_mem0 >= 56
	d_t0_t41_mem0 += MAS_MEM[4]

	d_t0_t41_mem1 = S.Task('d_t0_t41_mem1', length=1, delay_cost=1)
	S += d_t0_t41_mem1 >= 56
	d_t0_t41_mem1 += MAS_MEM[3]

	d_t1_t51 = S.Task('d_t1_t51', length=1, delay_cost=1)
	S += d_t1_t51 >= 56
	d_t1_t51 += MAS[1]

	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	S += d_t2_t2_t1_in >= 56
	d_t2_t2_t1_in += MM_in[0]

	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem0 >= 56
	d_t2_t2_t1_mem0 += MAS_MEM[2]

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem1 >= 56
	d_t2_t2_t1_mem1 += MAS_MEM[7]

	d_t2_t41 = S.Task('d_t2_t41', length=1, delay_cost=1)
	S += d_t2_t41 >= 56
	d_t2_t41 += MAS[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 56
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	S += c_t0_s00_mem0 >= 57
	c_t0_s00_mem0 += MAS_MEM[4]

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	S += c_t0_s00_mem1 >= 57
	c_t0_s00_mem1 += MAS_MEM[7]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 57
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_s01 = S.Task('c_t1_s01', length=1, delay_cost=1)
	S += c_t1_s01 >= 57
	c_t1_s01 += MAS[2]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 57
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 57
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 57
	c_t1_t4_t4_mem0 += MAS_MEM[2]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 57
	c_t1_t4_t4_mem1 += MAS_MEM[3]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=1, delay_cost=1)
	S += c_t1_t4_t5 >= 57
	c_t1_t4_t5 += MAS[0]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	S += c_t2_s00_mem0 >= 57
	c_t2_s00_mem0 += MAS_MEM[6]

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	S += c_t2_s00_mem1 >= 57
	c_t2_s00_mem1 += MAS_MEM[5]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 57
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 57
	c_t2_t4_t5_mem1 += MM_MEM[1]

	c_t2_t51 = S.Task('c_t2_t51', length=1, delay_cost=1)
	S += c_t2_t51 >= 57
	c_t2_t51 += MAS[1]

	d_s210_mem0 = S.Task('d_s210_mem0', length=1, delay_cost=1)
	S += d_s210_mem0 >= 57
	d_s210_mem0 += MAS_MEM[0]

	d_s210_mem1 = S.Task('d_s210_mem1', length=1, delay_cost=1)
	S += d_s210_mem1 >= 57
	d_s210_mem1 += MAS_MEM[1]

	d_t0_t41 = S.Task('d_t0_t41', length=1, delay_cost=1)
	S += d_t0_t41 >= 57
	d_t0_t41 += MAS[3]

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=6, delay_cost=1)
	S += d_t2_t2_t1 >= 57
	d_t2_t2_t1 += MM[0]

	c_t0_s00 = S.Task('c_t0_s00', length=1, delay_cost=1)
	S += c_t0_s00 >= 58
	c_t0_s00 += MAS[3]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=6, delay_cost=1)
	S += c_t1_t4_t4 >= 58
	c_t1_t4_t4 += MM[0]

	c_t2_s00 = S.Task('c_t2_s00', length=1, delay_cost=1)
	S += c_t2_s00 >= 58
	c_t2_s00 += MAS[1]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=1, delay_cost=1)
	S += c_t2_t4_t5 >= 58
	c_t2_t4_t5 += MAS[2]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 58
	c_t3_t00_mem0 += MM_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 58
	c_t3_t00_mem1 += MM_MEM[1]

	d_s010_mem0 = S.Task('d_s010_mem0', length=1, delay_cost=1)
	S += d_s010_mem0 >= 58
	d_s010_mem0 += MAS_MEM[6]

	d_s010_mem1 = S.Task('d_s010_mem1', length=1, delay_cost=1)
	S += d_s010_mem1 >= 58
	d_s010_mem1 += MAS_MEM[1]

	d_s210 = S.Task('d_s210', length=1, delay_cost=1)
	S += d_s210 >= 58
	d_s210 += MAS[0]

	d_t011_mem0 = S.Task('d_t011_mem0', length=1, delay_cost=1)
	S += d_t011_mem0 >= 58
	d_t011_mem0 += MAS_MEM[4]

	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	S += d_t1_t2_t0_in >= 58
	d_t1_t2_t0_in += MM_in[0]

	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem0 >= 58
	d_t1_t2_t0_mem0 += MAS_MEM[0]

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem1 >= 58
	d_t1_t2_t0_mem1 += MAS_MEM[7]

	d_t211_mem0 = S.Task('d_t211_mem0', length=1, delay_cost=1)
	S += d_t211_mem0 >= 58
	d_t211_mem0 += MAS_MEM[2]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 58
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 58
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 59
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 59
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3_t00 = S.Task('c_t3_t00', length=1, delay_cost=1)
	S += c_t3_t00 >= 59
	c_t3_t00 += MAS[0]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 59
	c_t3_t0_t5_mem0 += MM_MEM[0]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 59
	c_t3_t0_t5_mem1 += MM_MEM[1]

	d_s010 = S.Task('d_s010', length=1, delay_cost=1)
	S += d_s010 >= 59
	d_s010 += MAS[1]

	d_t011 = S.Task('d_t011', length=1, delay_cost=1)
	S += d_t011 >= 59
	d_t011 += MAS[2]

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=6, delay_cost=1)
	S += d_t1_t2_t0 >= 59
	d_t1_t2_t0 += MM[0]

	d_t211 = S.Task('d_t211', length=1, delay_cost=1)
	S += d_t211 >= 59
	d_t211 += MAS[3]

	d_t2_t51_mem0 = S.Task('d_t2_t51_mem0', length=1, delay_cost=1)
	S += d_t2_t51_mem0 >= 59
	d_t2_t51_mem0 += MAS_MEM[2]

	d_t2_t51_mem1 = S.Task('d_t2_t51_mem1', length=1, delay_cost=1)
	S += d_t2_t51_mem1 >= 59
	d_t2_t51_mem1 += MAS_MEM[1]

	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	S += d_t3_t3_t4_in >= 59
	d_t3_t3_t4_in += MM_in[0]

	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem0 >= 59
	d_t3_t3_t4_mem0 += MAS_MEM[0]

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem1 >= 59
	d_t3_t3_t4_mem1 += MAS_MEM[7]

	d_t410_mem0 = S.Task('d_t410_mem0', length=1, delay_cost=1)
	S += d_t410_mem0 >= 59
	d_t410_mem0 += MAS_MEM[4]

	d_t6_y1_1_mem0 = S.Task('d_t6_y1_1_mem0', length=1, delay_cost=1)
	S += d_t6_y1_1_mem0 >= 59
	d_t6_y1_1_mem0 += MAS_MEM[6]

	d_t6_y1_1_mem1 = S.Task('d_t6_y1_1_mem1', length=1, delay_cost=1)
	S += d_t6_y1_1_mem1 >= 59
	d_t6_y1_1_mem1 += MAS_MEM[3]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	S += c_t1_s00_mem0 >= 60
	c_t1_s00_mem0 += MAS_MEM[0]

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	S += c_t1_s00_mem1 >= 60
	c_t1_s00_mem1 += MAS_MEM[7]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 60
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 60
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=1, delay_cost=1)
	S += c_t3_t0_t5 >= 60
	c_t3_t0_t5 += MAS[0]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 60
	c_t3_t10_mem0 += MM_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 60
	c_t3_t10_mem1 += MM_MEM[1]

	d_s1110_mem0 = S.Task('d_s1110_mem0', length=1, delay_cost=1)
	S += d_s1110_mem0 >= 60
	d_s1110_mem0 += MAS_MEM[2]

	d_s1110_mem1 = S.Task('d_s1110_mem1', length=1, delay_cost=1)
	S += d_s1110_mem1 >= 60
	d_s1110_mem1 += MAS_MEM[3]

	d_s2011_mem0 = S.Task('d_s2011_mem0', length=1, delay_cost=1)
	S += d_s2011_mem0 >= 60
	d_s2011_mem0 += MAS_MEM[6]

	d_s2011_mem1 = S.Task('d_s2011_mem1', length=1, delay_cost=1)
	S += d_s2011_mem1 >= 60
	d_s2011_mem1 += MAS_MEM[5]

	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	S += d_t0_t2_t0_in >= 60
	d_t0_t2_t0_in += MM_in[0]

	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem0 >= 60
	d_t0_t2_t0_mem0 += MAS_MEM[4]

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem1 >= 60
	d_t0_t2_t0_mem1 += MAS_MEM[1]

	d_t2_t51 = S.Task('d_t2_t51', length=1, delay_cost=1)
	S += d_t2_t51 >= 60
	d_t2_t51 += MAS[2]

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=6, delay_cost=1)
	S += d_t3_t3_t4 >= 60
	d_t3_t3_t4 += MM[0]

	d_t410 = S.Task('d_t410', length=1, delay_cost=1)
	S += d_t410 >= 60
	d_t410 += MAS[1]

	d_t6_y1_1 = S.Task('d_t6_y1_1', length=1, delay_cost=1)
	S += d_t6_y1_1 >= 60
	d_t6_y1_1 += MAS[3]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 61
	c_t100_mem0 += MAS_MEM[6]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 61
	c_t100_mem1 += MAS_MEM[3]

	c_t1_s00 = S.Task('c_t1_s00', length=1, delay_cost=1)
	S += c_t1_s00 >= 61
	c_t1_s00 += MAS[1]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 61
	c_t1_t51_mem0 += MAS_MEM[0]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 61
	c_t1_t51_mem1 += MAS_MEM[7]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 61
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	S += c_t3_t10 >= 61
	c_t3_t10 += MAS[0]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 61
	c_t3_t1_t5_mem0 += MM_MEM[0]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 61
	c_t3_t1_t5_mem1 += MM_MEM[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 61
	c_t4011_mem0 += MAIN_MEM_r[0]

	d_s1110 = S.Task('d_s1110', length=1, delay_cost=1)
	S += d_s1110 >= 61
	d_s1110 += MAS[2]

	d_s2011 = S.Task('d_s2011', length=1, delay_cost=1)
	S += d_s2011 >= 61
	d_s2011 += MAS[3]

	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=6, delay_cost=1)
	S += d_t0_t2_t0 >= 61
	d_t0_t2_t0 += MM[0]

	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	S += d_t4_t3_t4_in >= 61
	d_t4_t3_t4_in += MM_in[0]

	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem0 >= 61
	d_t4_t3_t4_mem0 += MAS_MEM[4]

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem1 >= 61
	d_t4_t3_t4_mem1 += MAS_MEM[1]

	c_t100 = S.Task('c_t100', length=1, delay_cost=1)
	S += c_t100 >= 62
	c_t100 += MAS[3]

	c_t1_t51 = S.Task('c_t1_t51', length=1, delay_cost=1)
	S += c_t1_t51 >= 62
	c_t1_t51 += MAS[1]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	S += c_t2_s01_mem0 >= 62
	c_t2_s01_mem0 += MAS_MEM[4]

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	S += c_t2_s01_mem1 >= 62
	c_t2_s01_mem1 += MAS_MEM[7]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 62
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=1, delay_cost=1)
	S += c_t3_t1_t5 >= 62
	c_t3_t1_t5 += MAS[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 62
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 62
	c_t4_t00_mem0 += MM_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 62
	c_t4_t00_mem1 += MM_MEM[1]

	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	S += d_t0_t2_t1_in >= 62
	d_t0_t2_t1_in += MM_in[0]

	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem0 >= 62
	d_t0_t2_t1_mem0 += MAS_MEM[0]

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem1 >= 62
	d_t0_t2_t1_mem1 += MAS_MEM[3]

	d_t2_t50_mem0 = S.Task('d_t2_t50_mem0', length=1, delay_cost=1)
	S += d_t2_t50_mem0 >= 62
	d_t2_t50_mem0 += MAS_MEM[2]

	d_t2_t50_mem1 = S.Task('d_t2_t50_mem1', length=1, delay_cost=1)
	S += d_t2_t50_mem1 >= 62
	d_t2_t50_mem1 += MAS_MEM[1]

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=6, delay_cost=1)
	S += d_t4_t3_t4 >= 62
	d_t4_t3_t4 += MM[0]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 63
	c_t101_mem0 += MAS_MEM[0]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 63
	c_t101_mem1 += MAS_MEM[5]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 63
	c_t200_mem0 += MAS_MEM[6]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 63
	c_t200_mem1 += MAS_MEM[3]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 63
	c_t210_mem0 += MAS_MEM[2]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 63
	c_t210_mem1 += MAS_MEM[7]

	c_t2_s01 = S.Task('c_t2_s01', length=1, delay_cost=1)
	S += c_t2_s01 >= 63
	c_t2_s01 += MAS[3]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 63
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 63
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4_t00 = S.Task('c_t4_t00', length=1, delay_cost=1)
	S += c_t4_t00 >= 63
	c_t4_t00 += MAS[0]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 63
	c_t4_t0_t5_mem0 += MM_MEM[0]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 63
	c_t4_t0_t5_mem1 += MM_MEM[1]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 63
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 63
	c_t5_t4_t0_mem0 += MAS_MEM[4]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 63
	c_t5_t4_t0_mem1 += MAS_MEM[1]

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=6, delay_cost=1)
	S += d_t0_t2_t1 >= 63
	d_t0_t2_t1 += MM[0]

	d_t2_t50 = S.Task('d_t2_t50', length=1, delay_cost=1)
	S += d_t2_t50 >= 63
	d_t2_t50 += MAS[2]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 64
	c_t001_mem0 += MAS_MEM[4]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 64
	c_t001_mem1 += MAS_MEM[7]

	c_t101 = S.Task('c_t101', length=1, delay_cost=1)
	S += c_t101 >= 64
	c_t101 += MAS[2]

	c_t200 = S.Task('c_t200', length=1, delay_cost=1)
	S += c_t200 >= 64
	c_t200 += MAS[3]

	c_t210 = S.Task('c_t210', length=1, delay_cost=1)
	S += c_t210 >= 64
	c_t210 += MAS[1]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 64
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 64
	c_t3_t50_mem0 += MAS_MEM[0]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 64
	c_t3_t50_mem1 += MAS_MEM[1]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=1, delay_cost=1)
	S += c_t4_t0_t5 >= 64
	c_t4_t0_t5 += MAS[0]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 64
	c_t4_t10_mem0 += MM_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 64
	c_t4_t10_mem1 += MM_MEM[1]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 64
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 64
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 64
	c_t5_t1_t4_mem0 += MAS_MEM[6]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 64
	c_t5_t1_t4_mem1 += MAS_MEM[3]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=6, delay_cost=1)
	S += c_t5_t4_t0 >= 64
	c_t5_t4_t0 += MM[0]

	c_t8010_mem0 = S.Task('c_t8010_mem0', length=1, delay_cost=1)
	S += c_t8010_mem0 >= 64
	c_t8010_mem0 += MAS_MEM[2]

	c_t8010_mem1 = S.Task('c_t8010_mem1', length=1, delay_cost=1)
	S += c_t8010_mem1 >= 64
	c_t8010_mem1 += MAS_MEM[5]

	c_t001 = S.Task('c_t001', length=1, delay_cost=1)
	S += c_t001 >= 65
	c_t001 += MAS[2]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 65
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 65
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3_t50 = S.Task('c_t3_t50', length=1, delay_cost=1)
	S += c_t3_t50 >= 65
	c_t3_t50 += MAS[1]

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	S += c_t4_t10 >= 65
	c_t4_t10 += MAS[0]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 65
	c_t4_t1_t5_mem0 += MM_MEM[0]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 65
	c_t4_t1_t5_mem1 += MM_MEM[1]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 65
	c_t4_t50_mem0 += MAS_MEM[0]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 65
	c_t4_t50_mem1 += MAS_MEM[1]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 65
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 65
	c_t5_t0_t4_mem0 += MAS_MEM[6]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 65
	c_t5_t0_t4_mem1 += MAS_MEM[7]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=6, delay_cost=1)
	S += c_t5_t1_t4 >= 65
	c_t5_t1_t4 += MM[0]

	c_t6001_mem0 = S.Task('c_t6001_mem0', length=1, delay_cost=1)
	S += c_t6001_mem0 >= 65
	c_t6001_mem0 += MAS_MEM[4]

	c_t6001_mem1 = S.Task('c_t6001_mem1', length=1, delay_cost=1)
	S += c_t6001_mem1 >= 65
	c_t6001_mem1 += MAS_MEM[5]

	c_t8010 = S.Task('c_t8010', length=1, delay_cost=1)
	S += c_t8010 >= 65
	c_t8010 += MAS[3]

	d_t0_t50_mem0 = S.Task('d_t0_t50_mem0', length=1, delay_cost=1)
	S += d_t0_t50_mem0 >= 65
	d_t0_t50_mem0 += MAS_MEM[2]

	d_t0_t50_mem1 = S.Task('d_t0_t50_mem1', length=1, delay_cost=1)
	S += d_t0_t50_mem1 >= 65
	d_t0_t50_mem1 += MAS_MEM[3]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 66
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 66
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=1, delay_cost=1)
	S += c_t4_t1_t5 >= 66
	c_t4_t1_t5 += MAS[0]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 66
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 66
	c_t4_t4_t1_mem0 += MAS_MEM[4]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 66
	c_t4_t4_t1_mem1 += MAS_MEM[5]

	c_t4_t50 = S.Task('c_t4_t50', length=1, delay_cost=1)
	S += c_t4_t50 >= 66
	c_t4_t50 += MAS[1]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 66
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 66
	c_t5_t00_mem1 += MM_MEM[1]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=6, delay_cost=1)
	S += c_t5_t0_t4 >= 66
	c_t5_t0_t4 += MM[0]

	c_t6001 = S.Task('c_t6001', length=1, delay_cost=1)
	S += c_t6001 >= 66
	c_t6001 += MAS[2]

	c_t7010_mem0 = S.Task('c_t7010_mem0', length=1, delay_cost=1)
	S += c_t7010_mem0 >= 66
	c_t7010_mem0 += MAS_MEM[6]

	c_t7010_mem1 = S.Task('c_t7010_mem1', length=1, delay_cost=1)
	S += c_t7010_mem1 >= 66
	c_t7010_mem1 += MAS_MEM[3]

	d_s1011_mem0 = S.Task('d_s1011_mem0', length=1, delay_cost=1)
	S += d_s1011_mem0 >= 66
	d_s1011_mem0 += MAS_MEM[0]

	d_s1011_mem1 = S.Task('d_s1011_mem1', length=1, delay_cost=1)
	S += d_s1011_mem1 >= 66
	d_s1011_mem1 += MAS_MEM[7]

	d_t0_t50 = S.Task('d_t0_t50', length=1, delay_cost=1)
	S += d_t0_t50 >= 66
	d_t0_t50 += MAS[3]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 67
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 67
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 67
	c_t4_t4_t0_in += MM_in[0]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 67
	c_t4_t4_t0_mem0 += MAS_MEM[0]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 67
	c_t4_t4_t0_mem1 += MAS_MEM[3]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=6, delay_cost=1)
	S += c_t4_t4_t1 >= 67
	c_t4_t4_t1 += MM[0]

	c_t5_t00 = S.Task('c_t5_t00', length=1, delay_cost=1)
	S += c_t5_t00 >= 67
	c_t5_t00 += MAS[0]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 67
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 67
	c_t5_t0_t5_mem1 += MM_MEM[1]

	c_t7010 = S.Task('c_t7010', length=1, delay_cost=1)
	S += c_t7010 >= 67
	c_t7010 += MAS[1]

	d_s0011_mem0 = S.Task('d_s0011_mem0', length=1, delay_cost=1)
	S += d_s0011_mem0 >= 67
	d_s0011_mem0 += MAS_MEM[4]

	d_s0011_mem1 = S.Task('d_s0011_mem1', length=1, delay_cost=1)
	S += d_s0011_mem1 >= 67
	d_s0011_mem1 += MAS_MEM[1]

	d_s1011 = S.Task('d_s1011', length=1, delay_cost=1)
	S += d_s1011 >= 67
	d_s1011 += MAS[3]

	d_t6_y1_0_mem0 = S.Task('d_t6_y1_0_mem0', length=1, delay_cost=1)
	S += d_t6_y1_0_mem0 >= 67
	d_t6_y1_0_mem0 += MAS_MEM[2]

	d_t6_y1_0_mem1 = S.Task('d_t6_y1_0_mem1', length=1, delay_cost=1)
	S += d_t6_y1_0_mem1 >= 67
	d_t6_y1_0_mem1 += MAS_MEM[7]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 68
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 68
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 68
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 68
	c_t4_t1_t4_mem0 += MAS_MEM[0]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 68
	c_t4_t1_t4_mem1 += MAS_MEM[1]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=6, delay_cost=1)
	S += c_t4_t4_t0 >= 68
	c_t4_t4_t0 += MM[0]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=1, delay_cost=1)
	S += c_t5_t0_t5 >= 68
	c_t5_t0_t5 += MAS[0]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 68
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 68
	c_t5_t10_mem1 += MM_MEM[1]

	d_s0011 = S.Task('d_s0011', length=1, delay_cost=1)
	S += d_s0011 >= 68
	d_s0011 += MAS[1]

	d_t0_t51_mem0 = S.Task('d_t0_t51_mem0', length=1, delay_cost=1)
	S += d_t0_t51_mem0 >= 68
	d_t0_t51_mem0 += MAS_MEM[4]

	d_t0_t51_mem1 = S.Task('d_t0_t51_mem1', length=1, delay_cost=1)
	S += d_t0_t51_mem1 >= 68
	d_t0_t51_mem1 += MAS_MEM[7]

	d_t6_y1_0 = S.Task('d_t6_y1_0', length=1, delay_cost=1)
	S += d_t6_y1_0 >= 68
	d_t6_y1_0 += MAS[3]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 69
	c_t000_mem0 += MAS_MEM[2]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 69
	c_t000_mem1 += MAS_MEM[7]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 69
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 69
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 69
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 69
	c_t4_t0_t4_mem0 += MAS_MEM[4]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 69
	c_t4_t0_t4_mem1 += MAS_MEM[3]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=6, delay_cost=1)
	S += c_t4_t1_t4 >= 69
	c_t4_t1_t4 += MM[0]

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	S += c_t5_t10 >= 69
	c_t5_t10 += MAS[0]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 69
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 69
	c_t5_t1_t5_mem1 += MM_MEM[1]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 69
	c_t5_t50_mem0 += MAS_MEM[0]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 69
	c_t5_t50_mem1 += MAS_MEM[1]

	d_t0_t51 = S.Task('d_t0_t51', length=1, delay_cost=1)
	S += d_t0_t51 >= 69
	d_t0_t51 += MAS[1]

	c_t000 = S.Task('c_t000', length=1, delay_cost=1)
	S += c_t000 >= 70
	c_t000 += MAS[3]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 70
	c_t201_mem0 += MAS_MEM[0]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 70
	c_t201_mem1 += MAS_MEM[7]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 70
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 70
	c_t3_t4_t1_mem0 += MAS_MEM[2]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 70
	c_t3_t4_t1_mem1 += MAS_MEM[5]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=6, delay_cost=1)
	S += c_t4_t0_t4 >= 70
	c_t4_t0_t4 += MM[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 70
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 70
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=1, delay_cost=1)
	S += c_t5_t1_t5 >= 70
	c_t5_t1_t5 += MAS[0]

	c_t5_t50 = S.Task('c_t5_t50', length=1, delay_cost=1)
	S += c_t5_t50 >= 70
	c_t5_t50 += MAS[1]

	d210_mem0 = S.Task('d210_mem0', length=1, delay_cost=1)
	S += d210_mem0 >= 70
	d210_mem0 += MAS_MEM[4]

	d210_mem1 = S.Task('d210_mem1', length=1, delay_cost=1)
	S += d210_mem1 >= 70
	d210_mem1 += MAS_MEM[1]

	d_t2_t20_mem0 = S.Task('d_t2_t20_mem0', length=1, delay_cost=1)
	S += d_t2_t20_mem0 >= 70
	d_t2_t20_mem0 += MM_MEM[0]

	d_t2_t20_mem1 = S.Task('d_t2_t20_mem1', length=1, delay_cost=1)
	S += d_t2_t20_mem1 >= 70
	d_t2_t20_mem1 += MM_MEM[1]

	c_t201 = S.Task('c_t201', length=1, delay_cost=1)
	S += c_t201 >= 71
	c_t201 += MAS[3]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 71
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 71
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 71
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 71
	c_t3_t4_t0_mem0 += MAS_MEM[4]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 71
	c_t3_t4_t0_mem1 += MAS_MEM[5]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=6, delay_cost=1)
	S += c_t3_t4_t1 >= 71
	c_t3_t4_t1 += MM[0]

	d210 = S.Task('d210', length=1, delay_cost=1)
	S += d210 >= 71
	d210 += MAS[0]

	d_t2_t20 = S.Task('d_t2_t20', length=1, delay_cost=1)
	S += d_t2_t20 >= 71
	d_t2_t20 += MAS[1]

	d_t5_t31_mem0 = S.Task('d_t5_t31_mem0', length=1, delay_cost=1)
	S += d_t5_t31_mem0 >= 71
	d_t5_t31_mem0 += MM_MEM[0]

	d_t5_t31_mem1 = S.Task('d_t5_t31_mem1', length=1, delay_cost=1)
	S += d_t5_t31_mem1 >= 71
	d_t5_t31_mem1 += MAS_MEM[7]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 72
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 72
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 72
	c_t3_t1_t4_mem0 += MAS_MEM[2]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 72
	c_t3_t1_t4_mem1 += MAS_MEM[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=6, delay_cost=1)
	S += c_t3_t4_t0 >= 72
	c_t3_t4_t0 += MM[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 72
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t8001_mem0 = S.Task('c_t8001_mem0', length=1, delay_cost=1)
	S += c_t8001_mem0 >= 72
	c_t8001_mem0 += MAS_MEM[6]

	c_t8001_mem1 = S.Task('c_t8001_mem1', length=1, delay_cost=1)
	S += c_t8001_mem1 >= 72
	c_t8001_mem1 += MAS_MEM[5]

	d210_w = S.Task('d210_w', length=1, delay_cost=1)
	S += d210_w >= 72
	d210_w += MAIN_MEM_w

	d_t1_t50_mem0 = S.Task('d_t1_t50_mem0', length=1, delay_cost=1)
	S += d_t1_t50_mem0 >= 72
	d_t1_t50_mem0 += MAS_MEM[4]

	d_t1_t50_mem1 = S.Task('d_t1_t50_mem1', length=1, delay_cost=1)
	S += d_t1_t50_mem1 >= 72
	d_t1_t50_mem1 += MAS_MEM[7]

	d_t4_t31_mem0 = S.Task('d_t4_t31_mem0', length=1, delay_cost=1)
	S += d_t4_t31_mem0 >= 72
	d_t4_t31_mem0 += MM_MEM[0]

	d_t4_t31_mem1 = S.Task('d_t4_t31_mem1', length=1, delay_cost=1)
	S += d_t4_t31_mem1 >= 72
	d_t4_t31_mem1 += MAS_MEM[3]

	d_t511_mem0 = S.Task('d_t511_mem0', length=1, delay_cost=1)
	S += d_t511_mem0 >= 72
	d_t511_mem0 += MAS_MEM[0]

	d_t5_t31 = S.Task('d_t5_t31', length=1, delay_cost=1)
	S += d_t5_t31 >= 72
	d_t5_t31 += MAS[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 73
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 73
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 73
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 73
	c_t3_t0_t4_mem0 += MAS_MEM[0]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 73
	c_t3_t0_t4_mem1 += MAS_MEM[3]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=6, delay_cost=1)
	S += c_t3_t1_t4 >= 73
	c_t3_t1_t4 += MM[0]

	c_t8001 = S.Task('c_t8001', length=1, delay_cost=1)
	S += c_t8001 >= 73
	c_t8001 += MAS[1]

	d_t0_t20_mem0 = S.Task('d_t0_t20_mem0', length=1, delay_cost=1)
	S += d_t0_t20_mem0 >= 73
	d_t0_t20_mem0 += MM_MEM[0]

	d_t0_t20_mem1 = S.Task('d_t0_t20_mem1', length=1, delay_cost=1)
	S += d_t0_t20_mem1 >= 73
	d_t0_t20_mem1 += MM_MEM[1]

	d_t1_t50 = S.Task('d_t1_t50', length=1, delay_cost=1)
	S += d_t1_t50 >= 73
	d_t1_t50 += MAS[2]

	d_t4_t31 = S.Task('d_t4_t31', length=1, delay_cost=1)
	S += d_t4_t31 >= 73
	d_t4_t31 += MAS[3]

	d_t4_t40_mem0 = S.Task('d_t4_t40_mem0', length=1, delay_cost=1)
	S += d_t4_t40_mem0 >= 73
	d_t4_t40_mem0 += MAS_MEM[4]

	d_t4_t40_mem1 = S.Task('d_t4_t40_mem1', length=1, delay_cost=1)
	S += d_t4_t40_mem1 >= 73
	d_t4_t40_mem1 += MAS_MEM[7]

	d_t4_t41_mem0 = S.Task('d_t4_t41_mem0', length=1, delay_cost=1)
	S += d_t4_t41_mem0 >= 73
	d_t4_t41_mem0 += MAS_MEM[6]

	d_t4_t41_mem1 = S.Task('d_t4_t41_mem1', length=1, delay_cost=1)
	S += d_t4_t41_mem1 >= 73
	d_t4_t41_mem1 += MAS_MEM[5]

	d_t511 = S.Task('d_t511', length=1, delay_cost=1)
	S += d_t511 >= 73
	d_t511 += MAS[0]

	d_t5_t40_mem0 = S.Task('d_t5_t40_mem0', length=1, delay_cost=1)
	S += d_t5_t40_mem0 >= 73
	d_t5_t40_mem0 += MAS_MEM[2]

	d_t5_t40_mem1 = S.Task('d_t5_t40_mem1', length=1, delay_cost=1)
	S += d_t5_t40_mem1 >= 73
	d_t5_t40_mem1 += MAS_MEM[1]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 74
	c_t0_t41_mem0 += MM_MEM[0]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 74
	c_t0_t41_mem1 += MAS_MEM[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 74
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 74
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=6, delay_cost=1)
	S += c_t3_t0_t4 >= 74
	c_t3_t0_t4 += MM[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 74
	c_t5_t4_t1_in += MM_in[0]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 74
	c_t5_t4_t1_mem0 += MAS_MEM[6]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 74
	c_t5_t4_t1_mem1 += MAS_MEM[3]

	c_t6010_mem0 = S.Task('c_t6010_mem0', length=1, delay_cost=1)
	S += c_t6010_mem0 >= 74
	c_t6010_mem0 += MAS_MEM[4]

	c_t6010_mem1 = S.Task('c_t6010_mem1', length=1, delay_cost=1)
	S += c_t6010_mem1 >= 74
	c_t6010_mem1 += MAS_MEM[7]

	d_t0_t20 = S.Task('d_t0_t20', length=1, delay_cost=1)
	S += d_t0_t20 >= 74
	d_t0_t20 += MAS[2]

	d_t200_mem0 = S.Task('d_t200_mem0', length=1, delay_cost=1)
	S += d_t200_mem0 >= 74
	d_t200_mem0 += MAS_MEM[2]

	d_t200_mem1 = S.Task('d_t200_mem1', length=1, delay_cost=1)
	S += d_t200_mem1 >= 74
	d_t200_mem1 += MAS_MEM[5]

	d_t4_t40 = S.Task('d_t4_t40', length=1, delay_cost=1)
	S += d_t4_t40 >= 74
	d_t4_t40 += MAS[1]

	d_t4_t41 = S.Task('d_t4_t41', length=1, delay_cost=1)
	S += d_t4_t41 >= 74
	d_t4_t41 += MAS[0]

	d_t5_t40 = S.Task('d_t5_t40', length=1, delay_cost=1)
	S += d_t5_t40 >= 74
	d_t5_t40 += MAS[3]

	c_t0_t41 = S.Task('c_t0_t41', length=1, delay_cost=1)
	S += c_t0_t41 >= 75
	c_t0_t41 += MAS[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 75
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 75
	c_t2_t41_mem0 += MM_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 75
	c_t2_t41_mem1 += MAS_MEM[5]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 75
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=6, delay_cost=1)
	S += c_t5_t4_t1 >= 75
	c_t5_t4_t1 += MM[0]

	c_t6010 = S.Task('c_t6010', length=1, delay_cost=1)
	S += c_t6010 >= 75
	c_t6010 += MAS[1]

	d_t200 = S.Task('d_t200', length=1, delay_cost=1)
	S += d_t200 >= 75
	d_t200 += MAS[2]

	d_t411_mem0 = S.Task('d_t411_mem0', length=1, delay_cost=1)
	S += d_t411_mem0 >= 75
	d_t411_mem0 += MAS_MEM[6]

	d_t4_t2_t0_in = S.Task('d_t4_t2_t0_in', length=1, delay_cost=1)
	S += d_t4_t2_t0_in >= 75
	d_t4_t2_t0_in += MM_in[0]

	d_t4_t2_t0_mem0 = S.Task('d_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem0 >= 75
	d_t4_t2_t0_mem0 += MAS_MEM[0]

	d_t4_t2_t0_mem1 = S.Task('d_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem1 >= 75
	d_t4_t2_t0_mem1 += MAS_MEM[7]

	d_t4_t50_mem0 = S.Task('d_t4_t50_mem0', length=1, delay_cost=1)
	S += d_t4_t50_mem0 >= 75
	d_t4_t50_mem0 += MAS_MEM[4]

	d_t4_t50_mem1 = S.Task('d_t4_t50_mem1', length=1, delay_cost=1)
	S += d_t4_t50_mem1 >= 75
	d_t4_t50_mem1 += MAS_MEM[3]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 76
	c_t011_mem0 += MAS_MEM[0]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 76
	c_t011_mem1 += MAS_MEM[3]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 76
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 76
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t41 = S.Task('c_t2_t41', length=1, delay_cost=1)
	S += c_t2_t41 >= 76
	c_t2_t41 += MAS[1]

	d_t3_t31_mem0 = S.Task('d_t3_t31_mem0', length=1, delay_cost=1)
	S += d_t3_t31_mem0 >= 76
	d_t3_t31_mem0 += MM_MEM[0]

	d_t3_t31_mem1 = S.Task('d_t3_t31_mem1', length=1, delay_cost=1)
	S += d_t3_t31_mem1 >= 76
	d_t3_t31_mem1 += MAS_MEM[7]

	d_t411 = S.Task('d_t411', length=1, delay_cost=1)
	S += d_t411 >= 76
	d_t411 += MAS[2]

	d_t4_t2_t0 = S.Task('d_t4_t2_t0', length=6, delay_cost=1)
	S += d_t4_t2_t0 >= 76
	d_t4_t2_t0 += MM[0]

	d_t4_t2_t1_in = S.Task('d_t4_t2_t1_in', length=1, delay_cost=1)
	S += d_t4_t2_t1_in >= 76
	d_t4_t2_t1_in += MM_in[0]

	d_t4_t2_t1_mem0 = S.Task('d_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem0 >= 76
	d_t4_t2_t1_mem0 += MAS_MEM[4]

	d_t4_t2_t1_mem1 = S.Task('d_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem1 >= 76
	d_t4_t2_t1_mem1 += MAS_MEM[5]

	d_t4_t50 = S.Task('d_t4_t50', length=1, delay_cost=1)
	S += d_t4_t50 >= 76
	d_t4_t50 += MAS[0]

	d_t4_t51_mem0 = S.Task('d_t4_t51_mem0', length=1, delay_cost=1)
	S += d_t4_t51_mem0 >= 76
	d_t4_t51_mem0 += MAS_MEM[6]

	d_t4_t51_mem1 = S.Task('d_t4_t51_mem1', length=1, delay_cost=1)
	S += d_t4_t51_mem1 >= 76
	d_t4_t51_mem1 += MAS_MEM[1]

	c_t011 = S.Task('c_t011', length=1, delay_cost=1)
	S += c_t011 >= 77
	c_t011 += MAS[3]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 77
	c_t211_mem0 += MAS_MEM[2]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 77
	c_t211_mem1 += MAS_MEM[3]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 77
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 77
	c_t5000_mem0 += MAIN_MEM_r[0]

	d_t1_t20_mem0 = S.Task('d_t1_t20_mem0', length=1, delay_cost=1)
	S += d_t1_t20_mem0 >= 77
	d_t1_t20_mem0 += MM_MEM[0]

	d_t1_t20_mem1 = S.Task('d_t1_t20_mem1', length=1, delay_cost=1)
	S += d_t1_t20_mem1 >= 77
	d_t1_t20_mem1 += MM_MEM[1]

	d_t3_t31 = S.Task('d_t3_t31', length=1, delay_cost=1)
	S += d_t3_t31 >= 77
	d_t3_t31 += MAS[0]

	d_t3_t40_mem0 = S.Task('d_t3_t40_mem0', length=1, delay_cost=1)
	S += d_t3_t40_mem0 >= 77
	d_t3_t40_mem0 += MAS_MEM[6]

	d_t3_t40_mem1 = S.Task('d_t3_t40_mem1', length=1, delay_cost=1)
	S += d_t3_t40_mem1 >= 77
	d_t3_t40_mem1 += MAS_MEM[1]

	d_t4_t2_t1 = S.Task('d_t4_t2_t1', length=6, delay_cost=1)
	S += d_t4_t2_t1 >= 77
	d_t4_t2_t1 += MM[0]

	d_t4_t51 = S.Task('d_t4_t51', length=1, delay_cost=1)
	S += d_t4_t51 >= 77
	d_t4_t51 += MAS[1]

	d_t5_t2_t1_in = S.Task('d_t5_t2_t1_in', length=1, delay_cost=1)
	S += d_t5_t2_t1_in >= 77
	d_t5_t2_t1_in += MM_in[0]

	d_t5_t2_t1_mem0 = S.Task('d_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem0 >= 77
	d_t5_t2_t1_mem0 += MAS_MEM[0]

	d_t5_t2_t1_mem1 = S.Task('d_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem1 >= 77
	d_t5_t2_t1_mem1 += MAS_MEM[7]

	c_t211 = S.Task('c_t211', length=1, delay_cost=1)
	S += c_t211 >= 78
	c_t211 += MAS[1]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 78
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 78
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t9_y1_0_mem0 = S.Task('c_t9_y1_0_mem0', length=1, delay_cost=1)
	S += c_t9_y1_0_mem0 >= 78
	c_t9_y1_0_mem0 += MAS_MEM[2]

	c_t9_y1_0_mem1 = S.Task('c_t9_y1_0_mem1', length=1, delay_cost=1)
	S += c_t9_y1_0_mem1 >= 78
	c_t9_y1_0_mem1 += MAS_MEM[3]

	d_t1_t20 = S.Task('d_t1_t20', length=1, delay_cost=1)
	S += d_t1_t20 >= 78
	d_t1_t20 += MAS[3]

	d_t1_t2_t4_in = S.Task('d_t1_t2_t4_in', length=1, delay_cost=1)
	S += d_t1_t2_t4_in >= 78
	d_t1_t2_t4_in += MM_in[0]

	d_t1_t2_t4_mem0 = S.Task('d_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem0 >= 78
	d_t1_t2_t4_mem0 += MAS_MEM[6]

	d_t1_t2_t4_mem1 = S.Task('d_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem1 >= 78
	d_t1_t2_t4_mem1 += MAS_MEM[1]

	d_t2_t2_t5_mem0 = S.Task('d_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem0 >= 78
	d_t2_t2_t5_mem0 += MM_MEM[0]

	d_t2_t2_t5_mem1 = S.Task('d_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem1 >= 78
	d_t2_t2_t5_mem1 += MM_MEM[1]

	d_t3_t40 = S.Task('d_t3_t40', length=1, delay_cost=1)
	S += d_t3_t40 >= 78
	d_t3_t40 += MAS[0]

	d_t3_t41_mem0 = S.Task('d_t3_t41_mem0', length=1, delay_cost=1)
	S += d_t3_t41_mem0 >= 78
	d_t3_t41_mem0 += MAS_MEM[0]

	d_t3_t41_mem1 = S.Task('d_t3_t41_mem1', length=1, delay_cost=1)
	S += d_t3_t41_mem1 >= 78
	d_t3_t41_mem1 += MAS_MEM[7]

	d_t5_t2_t1 = S.Task('d_t5_t2_t1', length=6, delay_cost=1)
	S += d_t5_t2_t1 >= 78
	d_t5_t2_t1 += MM[0]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 79
	c_t1_t41_mem0 += MM_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 79
	c_t1_t41_mem1 += MAS_MEM[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 79
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 79
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t8000_mem0 = S.Task('c_t8000_mem0', length=1, delay_cost=1)
	S += c_t8000_mem0 >= 79
	c_t8000_mem0 += MAS_MEM[6]

	c_t8000_mem1 = S.Task('c_t8000_mem1', length=1, delay_cost=1)
	S += c_t8000_mem1 >= 79
	c_t8000_mem1 += MAS_MEM[7]

	c_t9_y1_0 = S.Task('c_t9_y1_0', length=1, delay_cost=1)
	S += c_t9_y1_0 >= 79
	c_t9_y1_0 += MAS[0]

	c_t9_y1_1_mem0 = S.Task('c_t9_y1_1_mem0', length=1, delay_cost=1)
	S += c_t9_y1_1_mem0 >= 79
	c_t9_y1_1_mem0 += MAS_MEM[2]

	c_t9_y1_1_mem1 = S.Task('c_t9_y1_1_mem1', length=1, delay_cost=1)
	S += c_t9_y1_1_mem1 >= 79
	c_t9_y1_1_mem1 += MAS_MEM[3]

	d_t1_t2_t4 = S.Task('d_t1_t2_t4', length=6, delay_cost=1)
	S += d_t1_t2_t4 >= 79
	d_t1_t2_t4 += MM[0]

	d_t2_t2_t5 = S.Task('d_t2_t2_t5', length=1, delay_cost=1)
	S += d_t2_t2_t5 >= 79
	d_t2_t2_t5 += MAS[3]

	d_t3_t2_t1_in = S.Task('d_t3_t2_t1_in', length=1, delay_cost=1)
	S += d_t3_t2_t1_in >= 79
	d_t3_t2_t1_in += MM_in[0]

	d_t3_t2_t1_mem0 = S.Task('d_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem0 >= 79
	d_t3_t2_t1_mem0 += MAS_MEM[0]

	d_t3_t2_t1_mem1 = S.Task('d_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem1 >= 79
	d_t3_t2_t1_mem1 += MAS_MEM[5]

	d_t3_t41 = S.Task('d_t3_t41', length=1, delay_cost=1)
	S += d_t3_t41 >= 79
	d_t3_t41 += MAS[1]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 80
	c_t111_mem0 += MAS_MEM[0]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 80
	c_t111_mem1 += MAS_MEM[3]

	c_t1_t41 = S.Task('c_t1_t41', length=1, delay_cost=1)
	S += c_t1_t41 >= 80
	c_t1_t41 += MAS[0]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 80
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 80
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t8000 = S.Task('c_t8000', length=1, delay_cost=1)
	S += c_t8000 >= 80
	c_t8000 += MAS[2]

	c_t9_y1_1 = S.Task('c_t9_y1_1', length=1, delay_cost=1)
	S += c_t9_y1_1 >= 80
	c_t9_y1_1 += MAS[3]

	d_t0_t2_t5_mem0 = S.Task('d_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem0 >= 80
	d_t0_t2_t5_mem0 += MM_MEM[0]

	d_t0_t2_t5_mem1 = S.Task('d_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem1 >= 80
	d_t0_t2_t5_mem1 += MM_MEM[1]

	d_t100_mem0 = S.Task('d_t100_mem0', length=1, delay_cost=1)
	S += d_t100_mem0 >= 80
	d_t100_mem0 += MAS_MEM[6]

	d_t100_mem1 = S.Task('d_t100_mem1', length=1, delay_cost=1)
	S += d_t100_mem1 >= 80
	d_t100_mem1 += MAS_MEM[5]

	d_t3_t2_t1 = S.Task('d_t3_t2_t1', length=6, delay_cost=1)
	S += d_t3_t2_t1 >= 80
	d_t3_t2_t1 += MM[0]

	d_t5_t2_t0_in = S.Task('d_t5_t2_t0_in', length=1, delay_cost=1)
	S += d_t5_t2_t0_in >= 80
	d_t5_t2_t0_in += MM_in[0]

	d_t5_t2_t0_mem0 = S.Task('d_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem0 >= 80
	d_t5_t2_t0_mem0 += MAS_MEM[2]

	d_t5_t2_t0_mem1 = S.Task('d_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem1 >= 80
	d_t5_t2_t0_mem1 += MAS_MEM[7]

	c_t111 = S.Task('c_t111', length=1, delay_cost=1)
	S += c_t111 >= 81
	c_t111 += MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 81
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 81
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t8011_mem0 = S.Task('c_t8011_mem0', length=1, delay_cost=1)
	S += c_t8011_mem0 >= 81
	c_t8011_mem0 += MAS_MEM[2]

	c_t8011_mem1 = S.Task('c_t8011_mem1', length=1, delay_cost=1)
	S += c_t8011_mem1 >= 81
	c_t8011_mem1 += MAS_MEM[7]

	d_t0_t2_t5 = S.Task('d_t0_t2_t5', length=1, delay_cost=1)
	S += d_t0_t2_t5 >= 81
	d_t0_t2_t5 += MAS[2]

	d_t100 = S.Task('d_t100', length=1, delay_cost=1)
	S += d_t100 >= 81
	d_t100 += MAS[0]

	d_t1_t2_t5_mem0 = S.Task('d_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem0 >= 81
	d_t1_t2_t5_mem0 += MM_MEM[0]

	d_t1_t2_t5_mem1 = S.Task('d_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem1 >= 81
	d_t1_t2_t5_mem1 += MM_MEM[1]

	d_t2_t2_t4_in = S.Task('d_t2_t2_t4_in', length=1, delay_cost=1)
	S += d_t2_t2_t4_in >= 81
	d_t2_t2_t4_in += MM_in[0]

	d_t2_t2_t4_mem0 = S.Task('d_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem0 >= 81
	d_t2_t2_t4_mem0 += MAS_MEM[4]

	d_t2_t2_t4_mem1 = S.Task('d_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem1 >= 81
	d_t2_t2_t4_mem1 += MAS_MEM[5]

	d_t3_t50_mem0 = S.Task('d_t3_t50_mem0', length=1, delay_cost=1)
	S += d_t3_t50_mem0 >= 81
	d_t3_t50_mem0 += MAS_MEM[6]

	d_t3_t50_mem1 = S.Task('d_t3_t50_mem1', length=1, delay_cost=1)
	S += d_t3_t50_mem1 >= 81
	d_t3_t50_mem1 += MAS_MEM[1]

	d_t5_t2_t0 = S.Task('d_t5_t2_t0', length=6, delay_cost=1)
	S += d_t5_t2_t0 >= 81
	d_t5_t2_t0 += MM[0]

	d_t5_t41_mem0 = S.Task('d_t5_t41_mem0', length=1, delay_cost=1)
	S += d_t5_t41_mem0 >= 81
	d_t5_t41_mem0 += MAS_MEM[0]

	d_t5_t41_mem1 = S.Task('d_t5_t41_mem1', length=1, delay_cost=1)
	S += d_t5_t41_mem1 >= 81
	d_t5_t41_mem1 += MAS_MEM[3]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 82
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 82
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 82
	c_t5_t11_mem0 += MM_MEM[0]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 82
	c_t5_t11_mem1 += MAS_MEM[1]

	c_t7011_mem0 = S.Task('c_t7011_mem0', length=1, delay_cost=1)
	S += c_t7011_mem0 >= 82
	c_t7011_mem0 += MAS_MEM[6]

	c_t7011_mem1 = S.Task('c_t7011_mem1', length=1, delay_cost=1)
	S += c_t7011_mem1 >= 82
	c_t7011_mem1 += MAS_MEM[3]

	c_t8011 = S.Task('c_t8011', length=1, delay_cost=1)
	S += c_t8011 >= 82
	c_t8011 += MAS[2]

	d_t0_t2_t4_in = S.Task('d_t0_t2_t4_in', length=1, delay_cost=1)
	S += d_t0_t2_t4_in >= 82
	d_t0_t2_t4_in += MM_in[0]

	d_t0_t2_t4_mem0 = S.Task('d_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem0 >= 82
	d_t0_t2_t4_mem0 += MAS_MEM[4]

	d_t0_t2_t4_mem1 = S.Task('d_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem1 >= 82
	d_t0_t2_t4_mem1 += MAS_MEM[5]

	d_t1_t2_t5 = S.Task('d_t1_t2_t5', length=1, delay_cost=1)
	S += d_t1_t2_t5 >= 82
	d_t1_t2_t5 += MAS[0]

	d_t2_t2_t4 = S.Task('d_t2_t2_t4', length=6, delay_cost=1)
	S += d_t2_t2_t4 >= 82
	d_t2_t2_t4 += MM[0]

	d_t311_mem0 = S.Task('d_t311_mem0', length=1, delay_cost=1)
	S += d_t311_mem0 >= 82
	d_t311_mem0 += MAS_MEM[0]

	d_t3_t50 = S.Task('d_t3_t50', length=1, delay_cost=1)
	S += d_t3_t50 >= 82
	d_t3_t50 += MAS[1]

	d_t5_t41 = S.Task('d_t5_t41', length=1, delay_cost=1)
	S += d_t5_t41 >= 82
	d_t5_t41 += MAS[3]

	d_t5_t50_mem0 = S.Task('d_t5_t50_mem0', length=1, delay_cost=1)
	S += d_t5_t50_mem0 >= 82
	d_t5_t50_mem0 += MAS_MEM[2]

	d_t5_t50_mem1 = S.Task('d_t5_t50_mem1', length=1, delay_cost=1)
	S += d_t5_t50_mem1 >= 82
	d_t5_t50_mem1 += MAS_MEM[7]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 83
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 83
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 83
	c_t4_t01_mem0 += MM_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 83
	c_t4_t01_mem1 += MAS_MEM[1]

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	S += c_t5_t11 >= 83
	c_t5_t11 += MAS[0]

	c_t7011 = S.Task('c_t7011', length=1, delay_cost=1)
	S += c_t7011 >= 83
	c_t7011 += MAS[3]

	d_s011_mem0 = S.Task('d_s011_mem0', length=1, delay_cost=1)
	S += d_s011_mem0 >= 83
	d_s011_mem0 += MAS_MEM[2]

	d_s011_mem1 = S.Task('d_s011_mem1', length=1, delay_cost=1)
	S += d_s011_mem1 >= 83
	d_s011_mem1 += MAS_MEM[3]

	d_t0_t2_t4 = S.Task('d_t0_t2_t4', length=6, delay_cost=1)
	S += d_t0_t2_t4 >= 83
	d_t0_t2_t4 += MM[0]

	d_t311 = S.Task('d_t311', length=1, delay_cost=1)
	S += d_t311 >= 83
	d_t311 += MAS[1]

	d_t3_t2_t0_in = S.Task('d_t3_t2_t0_in', length=1, delay_cost=1)
	S += d_t3_t2_t0_in >= 83
	d_t3_t2_t0_in += MM_in[0]

	d_t3_t2_t0_mem0 = S.Task('d_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem0 >= 83
	d_t3_t2_t0_mem0 += MAS_MEM[0]

	d_t3_t2_t0_mem1 = S.Task('d_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem1 >= 83
	d_t3_t2_t0_mem1 += MAS_MEM[7]

	d_t5_t50 = S.Task('d_t5_t50', length=1, delay_cost=1)
	S += d_t5_t50 >= 83
	d_t5_t50 += MAS[2]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 84
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 84
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	S += c_t3_t4_t4_in >= 84
	c_t3_t4_t4_in += MM_in[0]

	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem0 >= 84
	c_t3_t4_t4_mem0 += MAS_MEM[0]

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem1 >= 84
	c_t3_t4_t4_mem1 += MAS_MEM[1]

	c_t4_t01 = S.Task('c_t4_t01', length=1, delay_cost=1)
	S += c_t4_t01 >= 84
	c_t4_t01 += MAS[1]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem0 >= 84
	c_t5_t4_t5_mem0 += MM_MEM[0]

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem1 >= 84
	c_t5_t4_t5_mem1 += MM_MEM[1]

	c_t6011_mem0 = S.Task('c_t6011_mem0', length=1, delay_cost=1)
	S += c_t6011_mem0 >= 84
	c_t6011_mem0 += MAS_MEM[6]

	c_t6011_mem1 = S.Task('c_t6011_mem1', length=1, delay_cost=1)
	S += c_t6011_mem1 >= 84
	c_t6011_mem1 += MAS_MEM[7]

	d110_mem0 = S.Task('d110_mem0', length=1, delay_cost=1)
	S += d110_mem0 >= 84
	d110_mem0 += MAS_MEM[2]

	d110_mem1 = S.Task('d110_mem1', length=1, delay_cost=1)
	S += d110_mem1 >= 84
	d110_mem1 += MAS_MEM[5]

	d_s011 = S.Task('d_s011', length=1, delay_cost=1)
	S += d_s011 >= 84
	d_s011 += MAS[3]

	d_t3_t2_t0 = S.Task('d_t3_t2_t0', length=6, delay_cost=1)
	S += d_t3_t2_t0 >= 84
	d_t3_t2_t0 += MM[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 85
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 85
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 85
	c_t3_t11_mem0 += MM_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 85
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=6, delay_cost=1)
	S += c_t3_t4_t4 >= 85
	c_t3_t4_t4 += MM[0]

	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	S += c_t5_t4_t4_in >= 85
	c_t5_t4_t4_in += MM_in[0]

	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem0 >= 85
	c_t5_t4_t4_mem0 += MAS_MEM[6]

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem1 >= 85
	c_t5_t4_t4_mem1 += MAS_MEM[5]

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=1, delay_cost=1)
	S += c_t5_t4_t5 >= 85
	c_t5_t4_t5 += MAS[2]

	c_t6011 = S.Task('c_t6011', length=1, delay_cost=1)
	S += c_t6011 >= 85
	c_t6011 += MAS[3]

	d110 = S.Task('d110', length=1, delay_cost=1)
	S += d110 >= 85
	d110 += MAS[0]

	d_s211_mem0 = S.Task('d_s211_mem0', length=1, delay_cost=1)
	S += d_s211_mem0 >= 85
	d_s211_mem0 += MAS_MEM[0]

	d_s211_mem1 = S.Task('d_s211_mem1', length=1, delay_cost=1)
	S += d_s211_mem1 >= 85
	d_s211_mem1 += MAS_MEM[7]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 86
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 86
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	S += c_t3_t11 >= 86
	c_t3_t11 += MAS[0]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 86
	c_t4_t11_mem0 += MM_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 86
	c_t4_t11_mem1 += MAS_MEM[1]

	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	S += c_t4_t4_t4_in >= 86
	c_t4_t4_t4_in += MM_in[0]

	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem0 >= 86
	c_t4_t4_t4_mem0 += MAS_MEM[2]

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem1 >= 86
	c_t4_t4_t4_mem1 += MAS_MEM[7]

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=6, delay_cost=1)
	S += c_t5_t4_t4 >= 86
	c_t5_t4_t4 += MM[0]

	d110_w = S.Task('d110_w', length=1, delay_cost=1)
	S += d110_w >= 86
	d110_w += MAIN_MEM_w

	d_s211 = S.Task('d_s211', length=1, delay_cost=1)
	S += d_s211 >= 86
	d_s211 += MAS[3]

	d_t3_t51_mem0 = S.Task('d_t3_t51_mem0', length=1, delay_cost=1)
	S += d_t3_t51_mem0 >= 86
	d_t3_t51_mem0 += MAS_MEM[0]

	d_t3_t51_mem1 = S.Task('d_t3_t51_mem1', length=1, delay_cost=1)
	S += d_t3_t51_mem1 >= 86
	d_t3_t51_mem1 += MAS_MEM[3]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 87
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 87
	c_t3_t01_mem0 += MM_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 87
	c_t3_t01_mem1 += MAS_MEM[1]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 87
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	S += c_t4_t11 >= 87
	c_t4_t11 += MAS[2]

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=6, delay_cost=1)
	S += c_t4_t4_t4 >= 87
	c_t4_t4_t4 += MM[0]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 87
	c_t4_t51_mem0 += MAS_MEM[2]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 87
	c_t4_t51_mem1 += MAS_MEM[5]

	d_t3_t51 = S.Task('d_t3_t51', length=1, delay_cost=1)
	S += d_t3_t51 >= 87
	d_t3_t51 += MAS[1]

	d_t4_t2_t4_in = S.Task('d_t4_t2_t4_in', length=1, delay_cost=1)
	S += d_t4_t2_t4_in >= 87
	d_t4_t2_t4_in += MM_in[0]

	d_t4_t2_t4_mem0 = S.Task('d_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem0 >= 87
	d_t4_t2_t4_mem0 += MAS_MEM[4]

	d_t4_t2_t4_mem1 = S.Task('d_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem1 >= 87
	d_t4_t2_t4_mem1 += MAS_MEM[3]

	d_t5_t51_mem0 = S.Task('d_t5_t51_mem0', length=1, delay_cost=1)
	S += d_t5_t51_mem0 >= 87
	d_t5_t51_mem0 += MAS_MEM[0]

	d_t5_t51_mem1 = S.Task('d_t5_t51_mem1', length=1, delay_cost=1)
	S += d_t5_t51_mem1 >= 87
	d_t5_t51_mem1 += MAS_MEM[7]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 88
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t3_s00_mem0 = S.Task('c_t3_s00_mem0', length=1, delay_cost=1)
	S += c_t3_s00_mem0 >= 88
	c_t3_s00_mem0 += MAS_MEM[0]

	c_t3_s00_mem1 = S.Task('c_t3_s00_mem1', length=1, delay_cost=1)
	S += c_t3_s00_mem1 >= 88
	c_t3_s00_mem1 += MAS_MEM[1]

	c_t3_t01 = S.Task('c_t3_t01', length=1, delay_cost=1)
	S += c_t3_t01 >= 88
	c_t3_t01 += MAS[0]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem0 >= 88
	c_t3_t4_t5_mem0 += MM_MEM[0]

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem1 >= 88
	c_t3_t4_t5_mem1 += MM_MEM[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 88
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4_t51 = S.Task('c_t4_t51', length=1, delay_cost=1)
	S += c_t4_t51 >= 88
	c_t4_t51 += MAS[2]

	c_t7000_mem0 = S.Task('c_t7000_mem0', length=1, delay_cost=1)
	S += c_t7000_mem0 >= 88
	c_t7000_mem0 += MAS_MEM[6]

	c_t7000_mem1 = S.Task('c_t7000_mem1', length=1, delay_cost=1)
	S += c_t7000_mem1 >= 88
	c_t7000_mem1 += MAS_MEM[7]

	d_t3_t2_t4_in = S.Task('d_t3_t2_t4_in', length=1, delay_cost=1)
	S += d_t3_t2_t4_in >= 88
	d_t3_t2_t4_in += MM_in[0]

	d_t3_t2_t4_mem0 = S.Task('d_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem0 >= 88
	d_t3_t2_t4_mem0 += MAS_MEM[4]

	d_t3_t2_t4_mem1 = S.Task('d_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem1 >= 88
	d_t3_t2_t4_mem1 += MAS_MEM[5]

	d_t4_t2_t4 = S.Task('d_t4_t2_t4', length=6, delay_cost=1)
	S += d_t4_t2_t4 >= 88
	d_t4_t2_t4 += MM[0]

	d_t5_t51 = S.Task('d_t5_t51', length=1, delay_cost=1)
	S += d_t5_t51 >= 88
	d_t5_t51 += MAS[1]

	c_t3_s00 = S.Task('c_t3_s00', length=1, delay_cost=1)
	S += c_t3_s00 >= 89
	c_t3_s00 += MAS[3]

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=1, delay_cost=1)
	S += c_t3_t4_t5 >= 89
	c_t3_t4_t5 += MAS[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 89
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 89
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_s00_mem0 = S.Task('c_t4_s00_mem0', length=1, delay_cost=1)
	S += c_t4_s00_mem0 >= 89
	c_t4_s00_mem0 += MAS_MEM[0]

	c_t4_s00_mem1 = S.Task('c_t4_s00_mem1', length=1, delay_cost=1)
	S += c_t4_s00_mem1 >= 89
	c_t4_s00_mem1 += MAS_MEM[5]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 89
	c_t5_t01_mem0 += MM_MEM[0]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 89
	c_t5_t01_mem1 += MAS_MEM[1]

	c_t6000_mem0 = S.Task('c_t6000_mem0', length=1, delay_cost=1)
	S += c_t6000_mem0 >= 89
	c_t6000_mem0 += MAS_MEM[6]

	c_t6000_mem1 = S.Task('c_t6000_mem1', length=1, delay_cost=1)
	S += c_t6000_mem1 >= 89
	c_t6000_mem1 += MAS_MEM[7]

	c_t7000 = S.Task('c_t7000', length=1, delay_cost=1)
	S += c_t7000 >= 89
	c_t7000 += MAS[1]

	d_t3_t2_t4 = S.Task('d_t3_t2_t4', length=6, delay_cost=1)
	S += d_t3_t2_t4 >= 89
	d_t3_t2_t4 += MM[0]

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	S += c_t400_mem0 >= 90
	c_t400_mem0 += MAS_MEM[0]

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	S += c_t400_mem1 >= 90
	c_t400_mem1 += MAS_MEM[3]

	c_t4_s00 = S.Task('c_t4_s00', length=1, delay_cost=1)
	S += c_t4_s00 >= 90
	c_t4_s00 += MAS[1]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 90
	c_t4_t40_mem0 += MM_MEM[0]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 90
	c_t4_t40_mem1 += MM_MEM[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 90
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 90
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5_t01 = S.Task('c_t5_t01', length=1, delay_cost=1)
	S += c_t5_t01 >= 90
	c_t5_t01 += MAS[0]

	c_t6000 = S.Task('c_t6000', length=1, delay_cost=1)
	S += c_t6000 >= 90
	c_t6000 += MAS[3]

	d_t000_mem0 = S.Task('d_t000_mem0', length=1, delay_cost=1)
	S += d_t000_mem0 >= 90
	d_t000_mem0 += MAS_MEM[4]

	d_t000_mem1 = S.Task('d_t000_mem1', length=1, delay_cost=1)
	S += d_t000_mem1 >= 90
	d_t000_mem1 += MAS_MEM[7]

	d_t5_t2_t4_in = S.Task('d_t5_t2_t4_in', length=1, delay_cost=1)
	S += d_t5_t2_t4_in >= 90
	d_t5_t2_t4_in += MM_in[0]

	d_t5_t2_t4_mem0 = S.Task('d_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem0 >= 90
	d_t5_t2_t4_mem0 += MAS_MEM[6]

	d_t5_t2_t4_mem1 = S.Task('d_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem1 >= 90
	d_t5_t2_t4_mem1 += MAS_MEM[1]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 91
	c_t3_t51_mem0 += MAS_MEM[0]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 91
	c_t3_t51_mem1 += MAS_MEM[1]

	c_t400 = S.Task('c_t400', length=1, delay_cost=1)
	S += c_t400 >= 91
	c_t400 += MAS[0]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 91
	c_t410_mem0 += MAS_MEM[2]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 91
	c_t410_mem1 += MAS_MEM[3]

	c_t4_t40 = S.Task('c_t4_t40', length=1, delay_cost=1)
	S += c_t4_t40 >= 91
	c_t4_t40 += MAS[1]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 91
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 91
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 91
	c_t5_t40_mem0 += MM_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 91
	c_t5_t40_mem1 += MM_MEM[1]

	d_s1111_mem0 = S.Task('d_s1111_mem0', length=1, delay_cost=1)
	S += d_s1111_mem0 >= 91
	d_s1111_mem0 += MAS_MEM[4]

	d_s1111_mem1 = S.Task('d_s1111_mem1', length=1, delay_cost=1)
	S += d_s1111_mem1 >= 91
	d_s1111_mem1 += MAS_MEM[7]

	d_t000 = S.Task('d_t000', length=1, delay_cost=1)
	S += d_t000 >= 91
	d_t000 += MAS[3]

	d_t5_t2_t4 = S.Task('d_t5_t2_t4', length=6, delay_cost=1)
	S += d_t5_t2_t4 >= 91
	d_t5_t2_t4 += MM[0]

	c_t3_s01_mem0 = S.Task('c_t3_s01_mem0', length=1, delay_cost=1)
	S += c_t3_s01_mem0 >= 92
	c_t3_s01_mem0 += MAS_MEM[0]

	c_t3_s01_mem1 = S.Task('c_t3_s01_mem1', length=1, delay_cost=1)
	S += c_t3_s01_mem1 >= 92
	c_t3_s01_mem1 += MAS_MEM[1]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 92
	c_t3_t40_mem0 += MM_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 92
	c_t3_t40_mem1 += MM_MEM[1]

	c_t3_t51 = S.Task('c_t3_t51', length=1, delay_cost=1)
	S += c_t3_t51 >= 92
	c_t3_t51 += MAS[3]

	c_t410 = S.Task('c_t410', length=1, delay_cost=1)
	S += c_t410 >= 92
	c_t410 += MAS[1]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 92
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 92
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5_t40 = S.Task('c_t5_t40', length=1, delay_cost=1)
	S += c_t5_t40 >= 92
	c_t5_t40 += MAS[0]

	c_t7001_mem0 = S.Task('c_t7001_mem0', length=1, delay_cost=1)
	S += c_t7001_mem0 >= 92
	c_t7001_mem0 += MAS_MEM[4]

	c_t7001_mem1 = S.Task('c_t7001_mem1', length=1, delay_cost=1)
	S += c_t7001_mem1 >= 92
	c_t7001_mem1 += MAS_MEM[7]

	c_t7110_mem0 = S.Task('c_t7110_mem0', length=1, delay_cost=1)
	S += c_t7110_mem0 >= 92
	c_t7110_mem0 += MAS_MEM[2]

	c_t7110_mem1 = S.Task('c_t7110_mem1', length=1, delay_cost=1)
	S += c_t7110_mem1 >= 92
	c_t7110_mem1 += MAS_MEM[3]

	d_s1111 = S.Task('d_s1111', length=1, delay_cost=1)
	S += d_s1111 >= 92
	d_s1111 += MAS[2]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 93
	c_t310_mem0 += MAS_MEM[6]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 93
	c_t310_mem1 += MAS_MEM[3]

	c_t3_s01 = S.Task('c_t3_s01', length=1, delay_cost=1)
	S += c_t3_s01 >= 93
	c_t3_s01 += MAS[0]

	c_t3_t40 = S.Task('c_t3_t40', length=1, delay_cost=1)
	S += c_t3_t40 >= 93
	c_t3_t40 += MAS[3]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem0 >= 93
	c_t4_t4_t5_mem0 += MM_MEM[0]

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem1 >= 93
	c_t4_t4_t5_mem1 += MM_MEM[1]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 93
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 93
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 93
	c_t5_t51_mem0 += MAS_MEM[0]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 93
	c_t5_t51_mem1 += MAS_MEM[1]

	c_t7001 = S.Task('c_t7001', length=1, delay_cost=1)
	S += c_t7001 >= 93
	c_t7001 += MAS[1]

	c_t7110 = S.Task('c_t7110', length=1, delay_cost=1)
	S += c_t7110 >= 93
	c_t7110 += MAS[2]

	d_s1_y1_0_mem0 = S.Task('d_s1_y1_0_mem0', length=1, delay_cost=1)
	S += d_s1_y1_0_mem0 >= 93
	d_s1_y1_0_mem0 += MAS_MEM[4]

	d_s1_y1_0_mem1 = S.Task('d_s1_y1_0_mem1', length=1, delay_cost=1)
	S += d_s1_y1_0_mem1 >= 93
	d_s1_y1_0_mem1 += MAS_MEM[5]

	c_t310 = S.Task('c_t310', length=1, delay_cost=1)
	S += c_t310 >= 94
	c_t310 += MAS[0]

	c_t4_s01_mem0 = S.Task('c_t4_s01_mem0', length=1, delay_cost=1)
	S += c_t4_s01_mem0 >= 94
	c_t4_s01_mem0 += MAS_MEM[4]

	c_t4_s01_mem1 = S.Task('c_t4_s01_mem1', length=1, delay_cost=1)
	S += c_t4_s01_mem1 >= 94
	c_t4_s01_mem1 += MAS_MEM[1]

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=1, delay_cost=1)
	S += c_t4_t4_t5 >= 94
	c_t4_t4_t5 += MAS[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 94
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 94
	c_t510_mem0 += MAS_MEM[0]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 94
	c_t510_mem1 += MAS_MEM[3]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 94
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t51 = S.Task('c_t5_t51', length=1, delay_cost=1)
	S += c_t5_t51 >= 94
	c_t5_t51 += MAS[3]

	d000_mem0 = S.Task('d000_mem0', length=1, delay_cost=1)
	S += d000_mem0 >= 94
	d000_mem0 += MAS_MEM[6]

	d000_mem1 = S.Task('d000_mem1', length=1, delay_cost=1)
	S += d000_mem1 >= 94
	d000_mem1 += MAS_MEM[5]

	d_s1_y1_0 = S.Task('d_s1_y1_0', length=1, delay_cost=1)
	S += d_s1_y1_0 >= 94
	d_s1_y1_0 += MAS[2]

	d_t4_t2_t5_mem0 = S.Task('d_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem0 >= 94
	d_t4_t2_t5_mem0 += MM_MEM[0]

	d_t4_t2_t5_mem1 = S.Task('d_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem1 >= 94
	d_t4_t2_t5_mem1 += MM_MEM[1]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	S += c_t401_mem0 >= 95
	c_t401_mem0 += MAS_MEM[2]

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	S += c_t401_mem1 >= 95
	c_t401_mem1 += MAS_MEM[7]

	c_t4_s01 = S.Task('c_t4_s01', length=1, delay_cost=1)
	S += c_t4_s01 >= 95
	c_t4_s01 += MAS[3]

	c_t510 = S.Task('c_t510', length=1, delay_cost=1)
	S += c_t510 >= 95
	c_t510 += MAS[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 95
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 95
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5_s01_mem0 = S.Task('c_t5_s01_mem0', length=1, delay_cost=1)
	S += c_t5_s01_mem0 >= 95
	c_t5_s01_mem0 += MAS_MEM[0]

	c_t5_s01_mem1 = S.Task('c_t5_s01_mem1', length=1, delay_cost=1)
	S += c_t5_s01_mem1 >= 95
	c_t5_s01_mem1 += MAS_MEM[1]

	d000 = S.Task('d000', length=1, delay_cost=1)
	S += d000 >= 95
	d000 += MAS[0]

	d_t0_t21_mem0 = S.Task('d_t0_t21_mem0', length=1, delay_cost=1)
	S += d_t0_t21_mem0 >= 95
	d_t0_t21_mem0 += MM_MEM[0]

	d_t0_t21_mem1 = S.Task('d_t0_t21_mem1', length=1, delay_cost=1)
	S += d_t0_t21_mem1 >= 95
	d_t0_t21_mem1 += MAS_MEM[5]

	d_t4_t2_t5 = S.Task('d_t4_t2_t5', length=1, delay_cost=1)
	S += d_t4_t2_t5 >= 95
	d_t4_t2_t5 += MAS[2]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 96
	c_t3_t41_mem0 += MM_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 96
	c_t3_t41_mem1 += MAS_MEM[1]

	c_t401 = S.Task('c_t401', length=1, delay_cost=1)
	S += c_t401 >= 96
	c_t401 += MAS[1]

	c_t5_s01 = S.Task('c_t5_s01', length=1, delay_cost=1)
	S += c_t5_s01 >= 96
	c_t5_s01 += MAS[0]

	c_t610_mem0 = S.Task('c_t610_mem0', length=1, delay_cost=1)
	S += c_t610_mem0 >= 96
	c_t610_mem0 += MAS_MEM[0]

	c_t610_mem1 = S.Task('c_t610_mem1', length=1, delay_cost=1)
	S += c_t610_mem1 >= 96
	c_t610_mem1 += MAS_MEM[3]

	c_t810_mem0 = S.Task('c_t810_mem0', length=1, delay_cost=1)
	S += c_t810_mem0 >= 96
	c_t810_mem0 += MAS_MEM[2]

	c_t810_mem1 = S.Task('c_t810_mem1', length=1, delay_cost=1)
	S += c_t810_mem1 >= 96
	c_t810_mem1 += MAS_MEM[7]

	d000_w = S.Task('d000_w', length=1, delay_cost=1)
	S += d000_w >= 96
	d000_w += MAIN_MEM_w

	d_s1_y1_1_mem0 = S.Task('d_s1_y1_1_mem0', length=1, delay_cost=1)
	S += d_s1_y1_1_mem0 >= 96
	d_s1_y1_1_mem0 += MAS_MEM[4]

	d_s1_y1_1_mem1 = S.Task('d_s1_y1_1_mem1', length=1, delay_cost=1)
	S += d_s1_y1_1_mem1 >= 96
	d_s1_y1_1_mem1 += MAS_MEM[5]

	d_t0_t21 = S.Task('d_t0_t21', length=1, delay_cost=1)
	S += d_t0_t21 >= 96
	d_t0_t21 += MAS[3]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 96
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t3_t41 = S.Task('c_t3_t41', length=1, delay_cost=1)
	S += c_t3_t41 >= 97
	c_t3_t41 += MAS[3]

	c_t5_s00_mem0 = S.Task('c_t5_s00_mem0', length=1, delay_cost=1)
	S += c_t5_s00_mem0 >= 97
	c_t5_s00_mem0 += MAS_MEM[0]

	c_t5_s00_mem1 = S.Task('c_t5_s00_mem1', length=1, delay_cost=1)
	S += c_t5_s00_mem1 >= 97
	c_t5_s00_mem1 += MAS_MEM[1]

	c_t610 = S.Task('c_t610', length=1, delay_cost=1)
	S += c_t610 >= 97
	c_t610 += MAS[0]

	c_t810 = S.Task('c_t810', length=1, delay_cost=1)
	S += c_t810 >= 97
	c_t810 += MAS[1]

	d_s1_y1_1 = S.Task('d_s1_y1_1', length=1, delay_cost=1)
	S += d_s1_y1_1 >= 97
	d_s1_y1_1 += MAS[2]

	d_t001_mem0 = S.Task('d_t001_mem0', length=1, delay_cost=1)
	S += d_t001_mem0 >= 97
	d_t001_mem0 += MAS_MEM[6]

	d_t001_mem1 = S.Task('d_t001_mem1', length=1, delay_cost=1)
	S += d_t001_mem1 >= 97
	d_t001_mem1 += MAS_MEM[3]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 97
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t21_mem0 = S.Task('d_t2_t21_mem0', length=1, delay_cost=1)
	S += d_t2_t21_mem0 >= 97
	d_t2_t21_mem0 += MM_MEM[0]

	d_t2_t21_mem1 = S.Task('d_t2_t21_mem1', length=1, delay_cost=1)
	S += d_t2_t21_mem1 >= 97
	d_t2_t21_mem1 += MAS_MEM[7]

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	S += c_t301_mem0 >= 98
	c_t301_mem0 += MAS_MEM[0]

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	S += c_t301_mem1 >= 98
	c_t301_mem1 += MAS_MEM[1]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 98
	c_t311_mem0 += MAS_MEM[6]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 98
	c_t311_mem1 += MAS_MEM[7]

	c_t5_s00 = S.Task('c_t5_s00', length=1, delay_cost=1)
	S += c_t5_s00 >= 98
	c_t5_s00 += MAS[1]

	c_t7101_mem0 = S.Task('c_t7101_mem0', length=1, delay_cost=1)
	S += c_t7101_mem0 >= 98
	c_t7101_mem0 += MAS_MEM[2]

	c_t7101_mem1 = S.Task('c_t7101_mem1', length=1, delay_cost=1)
	S += c_t7101_mem1 >= 98
	c_t7101_mem1 += MAS_MEM[3]

	d_t001 = S.Task('d_t001', length=1, delay_cost=1)
	S += d_t001 >= 98
	d_t001 += MAS[3]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 98
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t21 = S.Task('d_t2_t21', length=1, delay_cost=1)
	S += d_t2_t21 >= 98
	d_t2_t21 += MAS[0]

	d_t4_t20_mem0 = S.Task('d_t4_t20_mem0', length=1, delay_cost=1)
	S += d_t4_t20_mem0 >= 98
	d_t4_t20_mem0 += MM_MEM[0]

	d_t4_t20_mem1 = S.Task('d_t4_t20_mem1', length=1, delay_cost=1)
	S += d_t4_t20_mem1 >= 98
	d_t4_t20_mem1 += MM_MEM[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 99
	c011_mem0 += MAS_MEM[6]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 99
	c011_mem1 += MAS_MEM[3]

	c_t301 = S.Task('c_t301', length=1, delay_cost=1)
	S += c_t301 >= 99
	c_t301 += MAS[0]

	c_t311 = S.Task('c_t311', length=1, delay_cost=1)
	S += c_t311 >= 99
	c_t311 += MAS[2]

	c_t7101 = S.Task('c_t7101', length=1, delay_cost=1)
	S += c_t7101 >= 99
	c_t7101 += MAS[1]

	d_s2000_mem0 = S.Task('d_s2000_mem0', length=1, delay_cost=1)
	S += d_s2000_mem0 >= 99
	d_s2000_mem0 += MAS_MEM[4]

	d_s2000_mem1 = S.Task('d_s2000_mem1', length=1, delay_cost=1)
	S += d_s2000_mem1 >= 99
	d_s2000_mem1 += MAS_MEM[7]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 99
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t201_mem0 = S.Task('d_t201_mem0', length=1, delay_cost=1)
	S += d_t201_mem0 >= 99
	d_t201_mem0 += MAS_MEM[0]

	d_t201_mem1 = S.Task('d_t201_mem1', length=1, delay_cost=1)
	S += d_t201_mem1 >= 99
	d_t201_mem1 += MAS_MEM[5]

	d_t4_t20 = S.Task('d_t4_t20', length=1, delay_cost=1)
	S += d_t4_t20 >= 99
	d_t4_t20 += MAS[3]

	d_t5_t2_t5_mem0 = S.Task('d_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem0 >= 99
	d_t5_t2_t5_mem0 += MM_MEM[0]

	d_t5_t2_t5_mem1 = S.Task('d_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem1 >= 99
	d_t5_t2_t5_mem1 += MM_MEM[1]

	c011 = S.Task('c011', length=1, delay_cost=1)
	S += c011 >= 100
	c011 += MAS[1]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 100
	c_t4_t41_mem0 += MM_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 100
	c_t4_t41_mem1 += MAS_MEM[3]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	S += c_t501_mem0 >= 100
	c_t501_mem0 += MAS_MEM[0]

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	S += c_t501_mem1 >= 100
	c_t501_mem1 += MAS_MEM[1]

	c_t611_mem0 = S.Task('c_t611_mem0', length=1, delay_cost=1)
	S += c_t611_mem0 >= 100
	c_t611_mem0 += MAS_MEM[4]

	c_t611_mem1 = S.Task('c_t611_mem1', length=1, delay_cost=1)
	S += c_t611_mem1 >= 100
	c_t611_mem1 += MAS_MEM[7]

	d001_mem0 = S.Task('d001_mem0', length=1, delay_cost=1)
	S += d001_mem0 >= 100
	d001_mem0 += MAS_MEM[6]

	d001_mem1 = S.Task('d001_mem1', length=1, delay_cost=1)
	S += d001_mem1 >= 100
	d001_mem1 += MAS_MEM[5]

	d_s2000 = S.Task('d_s2000', length=1, delay_cost=1)
	S += d_s2000 >= 100
	d_s2000 += MAS[0]

	d_t201 = S.Task('d_t201', length=1, delay_cost=1)
	S += d_t201 >= 100
	d_t201 += MAS[3]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 100
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t5_t2_t5 = S.Task('d_t5_t2_t5', length=1, delay_cost=1)
	S += d_t5_t2_t5 >= 100
	d_t5_t2_t5 += MAS[2]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 101
	c011_w += MAIN_MEM_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 101
	c111_mem0 += MAS_MEM[2]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 101
	c111_mem1 += MAS_MEM[7]

	c_t4_t41 = S.Task('c_t4_t41', length=1, delay_cost=1)
	S += c_t4_t41 >= 101
	c_t4_t41 += MAS[0]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	S += c_t500_mem0 >= 101
	c_t500_mem0 += MAS_MEM[0]

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	S += c_t500_mem1 >= 101
	c_t500_mem1 += MAS_MEM[3]

	c_t501 = S.Task('c_t501', length=1, delay_cost=1)
	S += c_t501 >= 101
	c_t501 += MAS[3]

	c_t611 = S.Task('c_t611', length=1, delay_cost=1)
	S += c_t611 >= 101
	c_t611 += MAS[1]

	d001 = S.Task('d001', length=1, delay_cost=1)
	S += d001 >= 101
	d001 += MAS[2]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 101
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t3_t2_t5_mem0 = S.Task('d_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem0 >= 101
	d_t3_t2_t5_mem0 += MM_MEM[0]

	d_t3_t2_t5_mem1 = S.Task('d_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem1 >= 101
	d_t3_t2_t5_mem1 += MM_MEM[1]

	d_t400_mem0 = S.Task('d_t400_mem0', length=1, delay_cost=1)
	S += d_t400_mem0 >= 101
	d_t400_mem0 += MAS_MEM[6]

	d_t400_mem1 = S.Task('d_t400_mem1', length=1, delay_cost=1)
	S += d_t400_mem1 >= 101
	d_t400_mem1 += MAS_MEM[1]

	c111 = S.Task('c111', length=1, delay_cost=1)
	S += c111 >= 102
	c111 += MAS[2]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 102
	c210_mem0 += MAS_MEM[2]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 102
	c210_mem1 += MAS_MEM[7]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 102
	c_t411_mem0 += MAS_MEM[0]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 102
	c_t411_mem1 += MAS_MEM[5]

	c_t500 = S.Task('c_t500', length=1, delay_cost=1)
	S += c_t500 >= 102
	c_t500 += MAS[3]

	d001_w = S.Task('d001_w', length=1, delay_cost=1)
	S += d001_w >= 102
	d001_w += MAIN_MEM_w

	d_s0000_mem0 = S.Task('d_s0000_mem0', length=1, delay_cost=1)
	S += d_s0000_mem0 >= 102
	d_s0000_mem0 += MAS_MEM[6]

	d_s0000_mem1 = S.Task('d_s0000_mem1', length=1, delay_cost=1)
	S += d_s0000_mem1 >= 102
	d_s0000_mem1 += MAS_MEM[1]

	d_t3_t2_t5 = S.Task('d_t3_t2_t5', length=1, delay_cost=1)
	S += d_t3_t2_t5 >= 102
	d_t3_t2_t5 += MAS[0]

	d_t400 = S.Task('d_t400', length=1, delay_cost=1)
	S += d_t400 >= 102
	d_t400 += MAS[1]

	d_t5_t20_mem0 = S.Task('d_t5_t20_mem0', length=1, delay_cost=1)
	S += d_t5_t20_mem0 >= 102
	d_t5_t20_mem0 += MM_MEM[0]

	d_t5_t20_mem1 = S.Task('d_t5_t20_mem1', length=1, delay_cost=1)
	S += d_t5_t20_mem1 >= 102
	d_t5_t20_mem1 += MM_MEM[1]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 103
	c111_w += MAIN_MEM_w

	c210 = S.Task('c210', length=1, delay_cost=1)
	S += c210 >= 103
	c210 += MAS[2]

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	S += c_t300_mem0 >= 103
	c_t300_mem0 += MAS_MEM[0]

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	S += c_t300_mem1 >= 103
	c_t300_mem1 += MAS_MEM[7]

	c_t411 = S.Task('c_t411', length=1, delay_cost=1)
	S += c_t411 >= 103
	c_t411 += MAS[3]

	c_t801_mem0 = S.Task('c_t801_mem0', length=1, delay_cost=1)
	S += c_t801_mem0 >= 103
	c_t801_mem0 += MAS_MEM[6]

	c_t801_mem1 = S.Task('c_t801_mem1', length=1, delay_cost=1)
	S += c_t801_mem1 >= 103
	c_t801_mem1 += MAS_MEM[3]

	d_s0000 = S.Task('d_s0000', length=1, delay_cost=1)
	S += d_s0000 >= 103
	d_s0000 += MAS[0]

	d_t1_t21_mem0 = S.Task('d_t1_t21_mem0', length=1, delay_cost=1)
	S += d_t1_t21_mem0 >= 103
	d_t1_t21_mem0 += MM_MEM[0]

	d_t1_t21_mem1 = S.Task('d_t1_t21_mem1', length=1, delay_cost=1)
	S += d_t1_t21_mem1 >= 103
	d_t1_t21_mem1 += MAS_MEM[1]

	d_t500_mem0 = S.Task('d_t500_mem0', length=1, delay_cost=1)
	S += d_t500_mem0 >= 103
	d_t500_mem0 += MAS_MEM[2]

	d_t500_mem1 = S.Task('d_t500_mem1', length=1, delay_cost=1)
	S += d_t500_mem1 >= 103
	d_t500_mem1 += MAS_MEM[5]

	d_t5_t20 = S.Task('d_t5_t20', length=1, delay_cost=1)
	S += d_t5_t20 >= 103
	d_t5_t20 += MAS[1]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 104
	c201_mem0 += MAS_MEM[4]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 104
	c201_mem1 += MAS_MEM[5]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 104
	c210_w += MAIN_MEM_w

	c_t300 = S.Task('c_t300', length=1, delay_cost=1)
	S += c_t300 >= 104
	c_t300 += MAS[3]

	c_t600_mem0 = S.Task('c_t600_mem0', length=1, delay_cost=1)
	S += c_t600_mem0 >= 104
	c_t600_mem0 += MAS_MEM[6]

	c_t600_mem1 = S.Task('c_t600_mem1', length=1, delay_cost=1)
	S += c_t600_mem1 >= 104
	c_t600_mem1 += MAS_MEM[7]

	c_t801 = S.Task('c_t801', length=1, delay_cost=1)
	S += c_t801 >= 104
	c_t801 += MAS[2]

	d_t101_mem0 = S.Task('d_t101_mem0', length=1, delay_cost=1)
	S += d_t101_mem0 >= 104
	d_t101_mem0 += MAS_MEM[0]

	d_t101_mem1 = S.Task('d_t101_mem1', length=1, delay_cost=1)
	S += d_t101_mem1 >= 104
	d_t101_mem1 += MAS_MEM[3]

	d_t1_t21 = S.Task('d_t1_t21', length=1, delay_cost=1)
	S += d_t1_t21 >= 104
	d_t1_t21 += MAS[0]

	d_t3_t20_mem0 = S.Task('d_t3_t20_mem0', length=1, delay_cost=1)
	S += d_t3_t20_mem0 >= 104
	d_t3_t20_mem0 += MM_MEM[0]

	d_t3_t20_mem1 = S.Task('d_t3_t20_mem1', length=1, delay_cost=1)
	S += d_t3_t20_mem1 >= 104
	d_t3_t20_mem1 += MM_MEM[1]

	d_t500 = S.Task('d_t500', length=1, delay_cost=1)
	S += d_t500 >= 104
	d_t500 += MAS[1]

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	S += c100_mem0 >= 105
	c100_mem0 += MAS_MEM[2]

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	S += c100_mem1 >= 105
	c100_mem1 += MAS_MEM[1]

	c201 = S.Task('c201', length=1, delay_cost=1)
	S += c201 >= 105
	c201 += MAS[2]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 105
	c_t5_t41_mem0 += MM_MEM[0]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 105
	c_t5_t41_mem1 += MAS_MEM[5]

	c_t600 = S.Task('c_t600', length=1, delay_cost=1)
	S += c_t600 >= 105
	c_t600 += MAS[1]

	c_t7111_mem0 = S.Task('c_t7111_mem0', length=1, delay_cost=1)
	S += c_t7111_mem0 >= 105
	c_t7111_mem0 += MAS_MEM[6]

	c_t7111_mem1 = S.Task('c_t7111_mem1', length=1, delay_cost=1)
	S += c_t7111_mem1 >= 105
	c_t7111_mem1 += MAS_MEM[7]

	d_t101 = S.Task('d_t101', length=1, delay_cost=1)
	S += d_t101 >= 105
	d_t101 += MAS[3]

	d_t300_mem0 = S.Task('d_t300_mem0', length=1, delay_cost=1)
	S += d_t300_mem0 >= 105
	d_t300_mem0 += MAS_MEM[0]

	d_t300_mem1 = S.Task('d_t300_mem1', length=1, delay_cost=1)
	S += d_t300_mem1 >= 105
	d_t300_mem1 += MAS_MEM[3]

	d_t3_t20 = S.Task('d_t3_t20', length=1, delay_cost=1)
	S += d_t3_t20 >= 105
	d_t3_t20 += MAS[0]

	c100 = S.Task('c100', length=1, delay_cost=1)
	S += c100 >= 106
	c100 += MAS[2]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 106
	c201_w += MAIN_MEM_w

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 106
	c_t511_mem0 += MAS_MEM[0]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 106
	c_t511_mem1 += MAS_MEM[7]

	c_t5_t41 = S.Task('c_t5_t41', length=1, delay_cost=1)
	S += c_t5_t41 >= 106
	c_t5_t41 += MAS[0]

	c_t7111 = S.Task('c_t7111', length=1, delay_cost=1)
	S += c_t7111 >= 106
	c_t7111 += MAS[1]

	c_t7_y1_0_mem0 = S.Task('c_t7_y1_0_mem0', length=1, delay_cost=1)
	S += c_t7_y1_0_mem0 >= 106
	c_t7_y1_0_mem0 += MAS_MEM[4]

	c_t7_y1_0_mem1 = S.Task('c_t7_y1_0_mem1', length=1, delay_cost=1)
	S += c_t7_y1_0_mem1 >= 106
	c_t7_y1_0_mem1 += MAS_MEM[3]

	d_s000_mem0 = S.Task('d_s000_mem0', length=1, delay_cost=1)
	S += d_s000_mem0 >= 106
	d_s000_mem0 += MAS_MEM[6]

	d_s000_mem1 = S.Task('d_s000_mem1', length=1, delay_cost=1)
	S += d_s000_mem1 >= 106
	d_s000_mem1 += MAS_MEM[1]

	d_t300 = S.Task('d_t300', length=1, delay_cost=1)
	S += d_t300 >= 106
	d_t300 += MAS[3]

	d_t5_t21_mem0 = S.Task('d_t5_t21_mem0', length=1, delay_cost=1)
	S += d_t5_t21_mem0 >= 106
	d_t5_t21_mem0 += MM_MEM[0]

	d_t5_t21_mem1 = S.Task('d_t5_t21_mem1', length=1, delay_cost=1)
	S += d_t5_t21_mem1 >= 106
	d_t5_t21_mem1 += MAS_MEM[5]

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	S += c100_w >= 107
	c100_w += MAIN_MEM_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 107
	c110_mem0 += MAS_MEM[0]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 107
	c110_mem1 += MAS_MEM[7]

	c_t511 = S.Task('c_t511', length=1, delay_cost=1)
	S += c_t511 >= 107
	c_t511 += MAS[2]

	c_t7_y1_0 = S.Task('c_t7_y1_0', length=1, delay_cost=1)
	S += c_t7_y1_0 >= 107
	c_t7_y1_0 += MAS[0]

	d_s000 = S.Task('d_s000', length=1, delay_cost=1)
	S += d_s000 >= 107
	d_s000 += MAS[1]

	d_s200_mem0 = S.Task('d_s200_mem0', length=1, delay_cost=1)
	S += d_s200_mem0 >= 107
	d_s200_mem0 += MAS_MEM[2]

	d_s200_mem1 = S.Task('d_s200_mem1', length=1, delay_cost=1)
	S += d_s200_mem1 >= 107
	d_s200_mem1 += MAS_MEM[1]

	d_t4_t21_mem0 = S.Task('d_t4_t21_mem0', length=1, delay_cost=1)
	S += d_t4_t21_mem0 >= 107
	d_t4_t21_mem0 += MM_MEM[0]

	d_t4_t21_mem1 = S.Task('d_t4_t21_mem1', length=1, delay_cost=1)
	S += d_t4_t21_mem1 >= 107
	d_t4_t21_mem1 += MAS_MEM[5]

	d_t501_mem0 = S.Task('d_t501_mem0', length=1, delay_cost=1)
	S += d_t501_mem0 >= 107
	d_t501_mem0 += MAS_MEM[6]

	d_t501_mem1 = S.Task('d_t501_mem1', length=1, delay_cost=1)
	S += d_t501_mem1 >= 107
	d_t501_mem1 += MAS_MEM[3]

	d_t5_t21 = S.Task('d_t5_t21', length=1, delay_cost=1)
	S += d_t5_t21 >= 107
	d_t5_t21 += MAS[3]

	c110 = S.Task('c110', length=1, delay_cost=1)
	S += c110 >= 108
	c110 += MAS[2]

	c_t7100_mem0 = S.Task('c_t7100_mem0', length=1, delay_cost=1)
	S += c_t7100_mem0 >= 108
	c_t7100_mem0 += MAS_MEM[0]

	c_t7100_mem1 = S.Task('c_t7100_mem1', length=1, delay_cost=1)
	S += c_t7100_mem1 >= 108
	c_t7100_mem1 += MAS_MEM[3]

	c_t811_mem0 = S.Task('c_t811_mem0', length=1, delay_cost=1)
	S += c_t811_mem0 >= 108
	c_t811_mem0 += MAS_MEM[4]

	c_t811_mem1 = S.Task('c_t811_mem1', length=1, delay_cost=1)
	S += c_t811_mem1 >= 108
	c_t811_mem1 += MAS_MEM[5]

	d_s200 = S.Task('d_s200', length=1, delay_cost=1)
	S += d_s200 >= 108
	d_s200 += MAS[0]

	d_s2001_mem0 = S.Task('d_s2001_mem0', length=1, delay_cost=1)
	S += d_s2001_mem0 >= 108
	d_s2001_mem0 += MAS_MEM[6]

	d_s2001_mem1 = S.Task('d_s2001_mem1', length=1, delay_cost=1)
	S += d_s2001_mem1 >= 108
	d_s2001_mem1 += MAS_MEM[7]

	d_t3_t21_mem0 = S.Task('d_t3_t21_mem0', length=1, delay_cost=1)
	S += d_t3_t21_mem0 >= 108
	d_t3_t21_mem0 += MM_MEM[0]

	d_t3_t21_mem1 = S.Task('d_t3_t21_mem1', length=1, delay_cost=1)
	S += d_t3_t21_mem1 >= 108
	d_t3_t21_mem1 += MAS_MEM[1]

	d_t4_t21 = S.Task('d_t4_t21', length=1, delay_cost=1)
	S += d_t4_t21 >= 108
	d_t4_t21 += MAS[3]

	d_t501 = S.Task('d_t501', length=1, delay_cost=1)
	S += d_t501 >= 108
	d_t501 += MAS[1]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 109
	c110_w += MAIN_MEM_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	S += c211_mem0 >= 109
	c211_mem0 += MAS_MEM[4]

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	S += c211_mem1 >= 109
	c211_mem1 += MAS_MEM[7]

	c_t7100 = S.Task('c_t7100', length=1, delay_cost=1)
	S += c_t7100 >= 109
	c_t7100 += MAS[1]

	c_t811 = S.Task('c_t811', length=1, delay_cost=1)
	S += c_t811 >= 109
	c_t811 += MAS[2]

	d_s1000_mem0 = S.Task('d_s1000_mem0', length=1, delay_cost=1)
	S += d_s1000_mem0 >= 109
	d_s1000_mem0 += MAS_MEM[0]

	d_s1000_mem1 = S.Task('d_s1000_mem1', length=1, delay_cost=1)
	S += d_s1000_mem1 >= 109
	d_s1000_mem1 += MAS_MEM[5]

	d_s2001 = S.Task('d_s2001', length=1, delay_cost=1)
	S += d_s2001 >= 109
	d_s2001 += MAS[0]

	d_s201_mem0 = S.Task('d_s201_mem0', length=1, delay_cost=1)
	S += d_s201_mem0 >= 109
	d_s201_mem0 += MAS_MEM[2]

	d_s201_mem1 = S.Task('d_s201_mem1', length=1, delay_cost=1)
	S += d_s201_mem1 >= 109
	d_s201_mem1 += MAS_MEM[1]

	d_t301_mem0 = S.Task('d_t301_mem0', length=1, delay_cost=1)
	S += d_t301_mem0 >= 109
	d_t301_mem0 += MAS_MEM[6]

	d_t301_mem1 = S.Task('d_t301_mem1', length=1, delay_cost=1)
	S += d_t301_mem1 >= 109
	d_t301_mem1 += MAS_MEM[3]

	d_t3_t21 = S.Task('d_t3_t21', length=1, delay_cost=1)
	S += d_t3_t21 >= 109
	d_t3_t21 += MAS[3]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 110
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 110
	c010_mem1 += MAS_MEM[3]

	c211 = S.Task('c211', length=1, delay_cost=1)
	S += c211 >= 110
	c211 += MAS[3]

	c_t601_mem0 = S.Task('c_t601_mem0', length=1, delay_cost=1)
	S += c_t601_mem0 >= 110
	c_t601_mem0 += MAS_MEM[0]

	c_t601_mem1 = S.Task('c_t601_mem1', length=1, delay_cost=1)
	S += c_t601_mem1 >= 110
	c_t601_mem1 += MAS_MEM[5]

	d_s0001_mem0 = S.Task('d_s0001_mem0', length=1, delay_cost=1)
	S += d_s0001_mem0 >= 110
	d_s0001_mem0 += MAS_MEM[6]

	d_s0001_mem1 = S.Task('d_s0001_mem1', length=1, delay_cost=1)
	S += d_s0001_mem1 >= 110
	d_s0001_mem1 += MAS_MEM[7]

	d_s1000 = S.Task('d_s1000', length=1, delay_cost=1)
	S += d_s1000 >= 110
	d_s1000 += MAS[0]

	d_s1100_mem0 = S.Task('d_s1100_mem0', length=1, delay_cost=1)
	S += d_s1100_mem0 >= 110
	d_s1100_mem0 += MAS_MEM[2]

	d_s1100_mem1 = S.Task('d_s1100_mem1', length=1, delay_cost=1)
	S += d_s1100_mem1 >= 110
	d_s1100_mem1 += MAS_MEM[1]

	d_s201 = S.Task('d_s201', length=1, delay_cost=1)
	S += d_s201 >= 110
	d_s201 += MAS[1]

	d_t301 = S.Task('d_t301', length=1, delay_cost=1)
	S += d_t301 >= 110
	d_t301 += MAS[2]

	c010 = S.Task('c010', length=1, delay_cost=1)
	S += c010 >= 111
	c010 += MAS[3]

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	S += c211_w >= 111
	c211_w += MAIN_MEM_w

	c_t601 = S.Task('c_t601', length=1, delay_cost=1)
	S += c_t601 >= 111
	c_t601 += MAS[1]

	c_t7_y1_1_mem0 = S.Task('c_t7_y1_1_mem0', length=1, delay_cost=1)
	S += c_t7_y1_1_mem0 >= 111
	c_t7_y1_1_mem0 += MAS_MEM[2]

	c_t7_y1_1_mem1 = S.Task('c_t7_y1_1_mem1', length=1, delay_cost=1)
	S += c_t7_y1_1_mem1 >= 111
	c_t7_y1_1_mem1 += MAS_MEM[5]

	d211_mem0 = S.Task('d211_mem0', length=1, delay_cost=1)
	S += d211_mem0 >= 111
	d211_mem0 += MAS_MEM[0]

	d211_mem1 = S.Task('d211_mem1', length=1, delay_cost=1)
	S += d211_mem1 >= 111
	d211_mem1 += MAS_MEM[7]

	d_s0001 = S.Task('d_s0001', length=1, delay_cost=1)
	S += d_s0001 >= 111
	d_s0001 += MAS[0]

	d_s001_mem0 = S.Task('d_s001_mem0', length=1, delay_cost=1)
	S += d_s001_mem0 >= 111
	d_s001_mem0 += MAS_MEM[4]

	d_s001_mem1 = S.Task('d_s001_mem1', length=1, delay_cost=1)
	S += d_s001_mem1 >= 111
	d_s001_mem1 += MAS_MEM[1]

	d_s1100 = S.Task('d_s1100', length=1, delay_cost=1)
	S += d_s1100 >= 111
	d_s1100 += MAS[2]

	d_t401_mem0 = S.Task('d_t401_mem0', length=1, delay_cost=1)
	S += d_t401_mem0 >= 111
	d_t401_mem0 += MAS_MEM[6]

	d_t401_mem1 = S.Task('d_t401_mem1', length=1, delay_cost=1)
	S += d_t401_mem1 >= 111
	d_t401_mem1 += MAS_MEM[3]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 112
	c010_w += MAIN_MEM_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	S += c101_mem0 >= 112
	c101_mem0 += MAS_MEM[2]

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	S += c101_mem1 >= 112
	c101_mem1 += MAS_MEM[7]

	c_t7_y1_1 = S.Task('c_t7_y1_1', length=1, delay_cost=1)
	S += c_t7_y1_1 >= 112
	c_t7_y1_1 += MAS[0]

	c_t800_mem0 = S.Task('c_t800_mem0', length=1, delay_cost=1)
	S += c_t800_mem0 >= 112
	c_t800_mem0 += MAS_MEM[6]

	c_t800_mem1 = S.Task('c_t800_mem1', length=1, delay_cost=1)
	S += c_t800_mem1 >= 112
	c_t800_mem1 += MAS_MEM[5]

	d211 = S.Task('d211', length=1, delay_cost=1)
	S += d211 >= 112
	d211 += MAS[3]

	d_s001 = S.Task('d_s001', length=1, delay_cost=1)
	S += d_s001 >= 112
	d_s001 += MAS[2]

	d_t401 = S.Task('d_t401', length=1, delay_cost=1)
	S += d_t401 >= 112
	d_t401 += MAS[1]

	c101 = S.Task('c101', length=1, delay_cost=1)
	S += c101 >= 113
	c101 += MAS[2]

	c_t800 = S.Task('c_t800', length=1, delay_cost=1)
	S += c_t800 >= 113
	c_t800 += MAS[3]

	d211_w = S.Task('d211_w', length=1, delay_cost=1)
	S += d211_w >= 113
	d211_w += MAIN_MEM_w

	d_s1001_mem0 = S.Task('d_s1001_mem0', length=1, delay_cost=1)
	S += d_s1001_mem0 >= 113
	d_s1001_mem0 += MAS_MEM[6]

	d_s1001_mem1 = S.Task('d_s1001_mem1', length=1, delay_cost=1)
	S += d_s1001_mem1 >= 113
	d_s1001_mem1 += MAS_MEM[7]

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	S += c101_w >= 114
	c101_w += MAIN_MEM_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 114
	c200_mem0 += MAS_MEM[6]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 114
	c200_mem1 += MAS_MEM[7]

	d_s1001 = S.Task('d_s1001', length=1, delay_cost=1)
	S += d_s1001 >= 114
	d_s1001 += MAS[0]

	d_s1101_mem0 = S.Task('d_s1101_mem0', length=1, delay_cost=1)
	S += d_s1101_mem0 >= 114
	d_s1101_mem0 += MAS_MEM[2]

	d_s1101_mem1 = S.Task('d_s1101_mem1', length=1, delay_cost=1)
	S += d_s1101_mem1 >= 114
	d_s1101_mem1 += MAS_MEM[1]

	c200 = S.Task('c200', length=1, delay_cost=1)
	S += c200 >= 115
	c200 += MAS[2]

	d111_mem0 = S.Task('d111_mem0', length=1, delay_cost=1)
	S += d111_mem0 >= 115
	d111_mem0 += MAS_MEM[6]

	d111_mem1 = S.Task('d111_mem1', length=1, delay_cost=1)
	S += d111_mem1 >= 115
	d111_mem1 += MAS_MEM[7]

	d_s1101 = S.Task('d_s1101', length=1, delay_cost=1)
	S += d_s1101 >= 115
	d_s1101 += MAS[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 116
	c200_w += MAIN_MEM_w

	d111 = S.Task('d111', length=1, delay_cost=1)
	S += d111 >= 116
	d111 += MAS[0]

	d111_w = S.Task('d111_w', length=1, delay_cost=1)
	S += d111_w >= 117
	d111_w += MAIN_MEM_w


	# new tasks
	d010 = S.Task('d010', length=1, delay_cost=1)
	d010 += alt(MAS)

	S += 20<d010

	d010_w = S.Task('d010_w', length=1, delay_cost=1)
	d010_w += alt(MAIN_MEM_w)
	S += d010 <= d010_w

	d010_mem0 = S.Task('d010_mem0', length=1, delay_cost=1)
	d010_mem0 += MAS_MEM[0]
	S += 30 < d010_mem0
	S += d010_mem0 <= d010

	d010_mem1 = S.Task('d010_mem1', length=1, delay_cost=1)
	d010_mem1 += MAS_MEM[5]
	S += 111 < d010_mem1
	S += d010_mem1 <= d010

	d011 = S.Task('d011', length=1, delay_cost=1)
	d011 += alt(MAS)

	S += 20<d011

	d011_w = S.Task('d011_w', length=1, delay_cost=1)
	d011_w += alt(MAIN_MEM_w)
	S += d011 <= d011_w

	d011_mem0 = S.Task('d011_mem0', length=1, delay_cost=1)
	d011_mem0 += MAS_MEM[4]
	S += 59 < d011_mem0
	S += d011_mem0 <= d011

	d011_mem1 = S.Task('d011_mem1', length=1, delay_cost=1)
	d011_mem1 += MAS_MEM[3]
	S += 115 < d011_mem1
	S += d011_mem1 <= d011

	d100 = S.Task('d100', length=1, delay_cost=1)
	d100 += alt(MAS)

	S += 32<d100

	d100_w = S.Task('d100_w', length=1, delay_cost=1)
	d100_w += alt(MAIN_MEM_w)
	S += d100 <= d100_w

	d100_mem0 = S.Task('d100_mem0', length=1, delay_cost=1)
	d100_mem0 += MAS_MEM[2]
	S += 107 < d100_mem0
	S += d100_mem0 <= d100

	d100_mem1 = S.Task('d100_mem1', length=1, delay_cost=1)
	d100_mem1 += MAS_MEM[7]
	S += 68 < d100_mem1
	S += d100_mem1 <= d100

	d101 = S.Task('d101', length=1, delay_cost=1)
	d101 += alt(MAS)

	S += 28<d101

	d101_w = S.Task('d101_w', length=1, delay_cost=1)
	d101_w += alt(MAIN_MEM_w)
	S += d101 <= d101_w

	d101_mem0 = S.Task('d101_mem0', length=1, delay_cost=1)
	d101_mem0 += MAS_MEM[4]
	S += 112 < d101_mem0
	S += d101_mem0 <= d101

	d101_mem1 = S.Task('d101_mem1', length=1, delay_cost=1)
	d101_mem1 += MAS_MEM[7]
	S += 60 < d101_mem1
	S += d101_mem1 <= d101

	d200 = S.Task('d200', length=1, delay_cost=1)
	d200 += alt(MAS)

	S += 29<d200

	d200_w = S.Task('d200_w', length=1, delay_cost=1)
	d200_w += alt(MAIN_MEM_w)
	S += d200 <= d200_w

	d200_mem0 = S.Task('d200_mem0', length=1, delay_cost=1)
	d200_mem0 += MAS_MEM[0]
	S += 81 < d200_mem0
	S += d200_mem0 <= d200

	d200_mem1 = S.Task('d200_mem1', length=1, delay_cost=1)
	d200_mem1 += MAS_MEM[1]
	S += 108 < d200_mem1
	S += d200_mem1 <= d200

	d201 = S.Task('d201', length=1, delay_cost=1)
	d201 += alt(MAS)

	S += 32<d201

	d201_w = S.Task('d201_w', length=1, delay_cost=1)
	d201_w += alt(MAIN_MEM_w)
	S += d201 <= d201_w

	d201_mem0 = S.Task('d201_mem0', length=1, delay_cost=1)
	d201_mem0 += MAS_MEM[6]
	S += 105 < d201_mem0
	S += d201_mem0 <= d201

	d201_mem1 = S.Task('d201_mem1', length=1, delay_cost=1)
	d201_mem1 += MAS_MEM[3]
	S += 110 < d201_mem1
	S += d201_mem1 <= d201

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 24<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[6]
	S += 70 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += MAS_MEM[1]
	S += 107 < c000_mem1
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 27<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[4]
	S += 65 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += MAS_MEM[1]
	S += 112 < c001_mem1
	S += c001_mem1 <= c001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/MUL_n_SQR/schedule15.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

