from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 199
	S = Scenario("schedule13", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 0
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 0
	d_t0_t3_t0_in += MM_in[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 0
	d_t2_t11_in += MAS_in[2]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 0
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 0
	d_t3010_in += MAS_in[1]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 0
	d_t3011_in += MAS_in[0]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 0
	d_t4001_in += MAS_in[3]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 1
	d_t0_a1_1_in += MAS_in[3]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=4, delay_cost=1)
	S += d_t0_t3_t0 >= 1
	d_t0_t3_t0 += MM[0]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 1
	d_t0_t3_t2_in += MAS_in[2]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 1
	d_t0_t3_t3_in += MAS_in[1]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 1
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 1
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 1
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t11 = S.Task('d_t2_t11', length=3, delay_cost=1)
	S += d_t2_t11 >= 1
	d_t2_t11 += MAS[2]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 1
	d_t3000_in += MAS_in[0]

	d_t3010 = S.Task('d_t3010', length=3, delay_cost=1)
	S += d_t3010 >= 1
	d_t3010 += MAS[1]

	d_t3011 = S.Task('d_t3011', length=3, delay_cost=1)
	S += d_t3011 >= 1
	d_t3011 += MAS[0]

	d_t4001 = S.Task('d_t4001', length=3, delay_cost=1)
	S += d_t4001 >= 1
	d_t4001 += MAS[3]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 2
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=3, delay_cost=1)
	S += d_t0_a1_1 >= 2
	d_t0_a1_1 += MAS[3]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 2
	d_t0_t10_in += MAS_in[1]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 2
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=3, delay_cost=1)
	S += d_t0_t3_t2 >= 2
	d_t0_t3_t2 += MAS[2]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=3, delay_cost=1)
	S += d_t0_t3_t3 >= 2
	d_t0_t3_t3 += MAS[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=4, delay_cost=1)
	S += d_t1_t3_t1 >= 2
	d_t1_t3_t1 += MM[0]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 2
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 2
	d_t2_a1_1_in += MAS_in[3]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 2
	d_t2_t3_t3_in += MAS_in[2]

	d_t3000 = S.Task('d_t3000', length=3, delay_cost=1)
	S += d_t3000 >= 2
	d_t3000 += MAS[0]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 2
	d_t4000_in += MAS_in[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 3
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_t10 = S.Task('d_t0_t10', length=3, delay_cost=1)
	S += d_t0_t10 >= 3
	d_t0_t10 += MAS[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=4, delay_cost=1)
	S += d_t0_t3_t1 >= 3
	d_t0_t3_t1 += MM[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 3
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 3
	d_t1_t10_in += MAS_in[2]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 3
	d_t1_t3_t2_in += MAS_in[3]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 3
	d_t2_a1_0_in += MAS_in[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=3, delay_cost=1)
	S += d_t2_a1_1 >= 3
	d_t2_a1_1 += MAS[3]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 3
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=3, delay_cost=1)
	S += d_t2_t3_t3 >= 3
	d_t2_t3_t3 += MAS[2]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 3
	d_t3001_in += MAS_in[0]

	d_t4000 = S.Task('d_t4000', length=3, delay_cost=1)
	S += d_t4000 >= 3
	d_t4000 += MAS[0]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 4
	d_t1_a1_1_in += MAS_in[1]

	d_t1_t10 = S.Task('d_t1_t10', length=3, delay_cost=1)
	S += d_t1_t10 >= 4
	d_t1_t10 += MAS[2]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 4
	d_t1_t11_in += MAS_in[2]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 4
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=3, delay_cost=1)
	S += d_t1_t3_t2 >= 4
	d_t1_t3_t2 += MAS[3]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=3, delay_cost=1)
	S += d_t2_a1_0 >= 4
	d_t2_a1_0 += MAS[1]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 4
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 4
	d_t2_t10_in += MAS_in[3]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 4
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=4, delay_cost=1)
	S += d_t2_t3_t1 >= 4
	d_t2_t3_t1 += MM[0]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 4
	d_t2_t3_t2_in += MAS_in[0]

	d_t3001 = S.Task('d_t3001', length=3, delay_cost=1)
	S += d_t3001 >= 4
	d_t3001 += MAS[0]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 5
	d_t0_a1_0_in += MAS_in[3]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 5
	d_t0_t11_in += MAS_in[1]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 5
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 5
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 5
	d_t1_a1_0_in += MAS_in[2]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=3, delay_cost=1)
	S += d_t1_a1_1 >= 5
	d_t1_a1_1 += MAS[1]

	d_t1_t11 = S.Task('d_t1_t11', length=3, delay_cost=1)
	S += d_t1_t11 >= 5
	d_t1_t11 += MAS[2]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=4, delay_cost=1)
	S += d_t1_t3_t0 >= 5
	d_t1_t3_t0 += MM[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 5
	d_t1_t3_t3_in += MAS_in[0]

	d_t2_t10 = S.Task('d_t2_t10', length=3, delay_cost=1)
	S += d_t2_t10 >= 5
	d_t2_t10 += MAS[3]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 5
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=3, delay_cost=1)
	S += d_t2_t3_t2 >= 5
	d_t2_t3_t2 += MAS[0]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 6
	c_t0_t0_t3_in += MAS_in[2]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 6
	c_t0_t1_t3_in += MAS_in[3]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 6
	c_t1_t0_t1_in += MM_in[0]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=3, delay_cost=1)
	S += d_t0_a1_0 >= 6
	d_t0_a1_0 += MAS[3]

	d_t0_t11 = S.Task('d_t0_t11', length=3, delay_cost=1)
	S += d_t0_t11 >= 6
	d_t0_t11 += MAS[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=3, delay_cost=1)
	S += d_t1_a1_0 >= 6
	d_t1_a1_0 += MAS[2]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=3, delay_cost=1)
	S += d_t1_t3_t3 >= 6
	d_t1_t3_t3 += MAS[0]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=4, delay_cost=1)
	S += d_t2_t3_t0 >= 6
	d_t2_t3_t0 += MM[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 6
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 6
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 6
	d_t4010_in += MAS_in[0]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 6
	d_t5011_in += MAS_in[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	S += c_t0_t0_t3 >= 7
	c_t0_t0_t3 += MAS[2]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 7
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	S += c_t0_t1_t3 >= 7
	c_t0_t1_t3 += MAS[3]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 7
	c_t0_t30_in += MAS_in[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=4, delay_cost=1)
	S += c_t1_t0_t1 >= 7
	c_t1_t0_t1 += MM[0]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 7
	c_t1_t0_t3_in += MAS_in[2]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 7
	c_t1_t31_in += MAS_in[3]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 7
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 7
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t4010 = S.Task('d_t4010', length=3, delay_cost=1)
	S += d_t4010 >= 7
	d_t4010 += MAS[0]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 7
	d_t5010_in += MAS_in[0]

	d_t5011 = S.Task('d_t5011', length=3, delay_cost=1)
	S += d_t5011 >= 7
	d_t5011 += MAS[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 8
	c_t0_t0_t2_in += MAS_in[2]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=4, delay_cost=1)
	S += c_t0_t1_t0 >= 8
	c_t0_t1_t0 += MM[0]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 8
	c_t0_t20_in += MAS_in[3]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 8
	c_t0_t30 += MAS[1]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 8
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	S += c_t1_t0_t3 >= 8
	c_t1_t0_t3 += MAS[2]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 8
	c_t1_t21_in += MAS_in[1]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 8
	c_t1_t30_in += MAS_in[0]

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	S += c_t1_t31 >= 8
	c_t1_t31 += MAS[3]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 8
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 8
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=3, delay_cost=1)
	S += d_t5010 >= 8
	d_t5010 += MAS[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 9
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	S += c_t0_t0_t2 >= 9
	c_t0_t0_t2 += MAS[2]

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	S += c_t0_t20 >= 9
	c_t0_t20 += MAS[3]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 9
	c_t0_t21_in += MAS_in[3]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 9
	c_t0_t31_in += MAS_in[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=4, delay_cost=1)
	S += c_t1_t0_t0 >= 9
	c_t1_t0_t0 += MM[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 9
	c_t1_t20_in += MAS_in[1]

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	S += c_t1_t21 >= 9
	c_t1_t21 += MAS[1]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 9
	c_t1_t30 += MAS[0]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 9
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 9
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 9
	d_t5001_in += MAS_in[2]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 10
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=4, delay_cost=1)
	S += c_t0_t0_t1 >= 10
	c_t0_t0_t1 += MM[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 10
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	S += c_t0_t21 >= 10
	c_t0_t21 += MAS[3]

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	S += c_t0_t31 >= 10
	c_t0_t31 += MAS[0]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 10
	c_t1_t1_t2_in += MAS_in[1]

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	S += c_t1_t20 >= 10
	c_t1_t20 += MAS[1]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 10
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 10
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 10
	d_t4011_in += MAS_in[3]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 10
	d_t5000_in += MAS_in[2]

	d_t5001 = S.Task('d_t5001', length=3, delay_cost=1)
	S += d_t5001 >= 10
	d_t5001 += MAS[2]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=4, delay_cost=1)
	S += c_t0_t0_t0 >= 11
	c_t0_t0_t0 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 11
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	S += c_t0_t1_t2 >= 11
	c_t0_t1_t2 += MAS[0]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 11
	c_t1_t0_t2_in += MAS_in[3]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	S += c_t1_t1_t2 >= 11
	c_t1_t1_t2 += MAS[1]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 11
	c_t1_t1_t3_in += MAS_in[0]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 11
	c_t4100_in += MAS_in[2]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 11
	c_t5001_in += MAS_in[1]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 11
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 11
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4011 = S.Task('d_t4011', length=3, delay_cost=1)
	S += d_t4011 >= 11
	d_t4011 += MAS[3]

	d_t5000 = S.Task('d_t5000', length=3, delay_cost=1)
	S += d_t5000 >= 11
	d_t5000 += MAS[2]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=4, delay_cost=1)
	S += c_t0_t1_t1 >= 12
	c_t0_t1_t1 += MM[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	S += c_t1_t0_t2 >= 12
	c_t1_t0_t2 += MAS[3]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 12
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	S += c_t1_t1_t3 >= 12
	c_t1_t1_t3 += MAS[0]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 12
	c_t2_t30_in += MAS_in[3]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 12
	c_t2_t31_in += MAS_in[2]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 12
	c_t3001_in += MAS_in[1]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 12
	c_t4000_in += MAS_in[0]

	c_t4100 = S.Task('c_t4100', length=3, delay_cost=1)
	S += c_t4100 >= 12
	c_t4100 += MAS[2]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 12
	c_t5001 += MAS[1]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 12
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 13
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=4, delay_cost=1)
	S += c_t1_t1_t1 >= 13
	c_t1_t1_t1 += MM[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 13
	c_t2_t0_t2_in += MAS_in[1]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 13
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 13
	c_t2_t1_t3_in += MAS_in[2]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 13
	c_t2_t30 += MAS[3]

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	S += c_t2_t31 >= 13
	c_t2_t31 += MAS[2]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 13
	c_t3001 += MAS[1]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 13
	c_t3111_in += MAS_in[3]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 13
	c_t4000 += MAS[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 13
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 13
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=4, delay_cost=1)
	S += c_t1_t1_t0 >= 14
	c_t1_t1_t0 += MM[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=3, delay_cost=1)
	S += c_t2_t0_t2 >= 14
	c_t2_t0_t2 += MAS[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 14
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=3, delay_cost=1)
	S += c_t2_t1_t2 >= 14
	c_t2_t1_t2 += MAS[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=3, delay_cost=1)
	S += c_t2_t1_t3 >= 14
	c_t2_t1_t3 += MAS[2]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 14
	c_t2_t20_in += MAS_in[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 14
	c_t2_t21_in += MAS_in[2]

	c_t3111 = S.Task('c_t3111', length=3, delay_cost=1)
	S += c_t3111 >= 14
	c_t3111 += MAS[3]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 14
	c_t4101_in += MAS_in[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 14
	c_t4111_in += MAS_in[3]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 14
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 14
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=4, delay_cost=1)
	S += c_t2_t1_t0 >= 15
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 15
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t20 = S.Task('c_t2_t20', length=3, delay_cost=1)
	S += c_t2_t20 >= 15
	c_t2_t20 += MAS[1]

	c_t2_t21 = S.Task('c_t2_t21', length=3, delay_cost=1)
	S += c_t2_t21 >= 15
	c_t2_t21 += MAS[2]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 15
	c_t3101_in += MAS_in[2]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 15
	c_t4001_in += MAS_in[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 15
	c_t4010_in += MAS_in[0]

	c_t4101 = S.Task('c_t4101', length=3, delay_cost=1)
	S += c_t4101 >= 15
	c_t4101 += MAS[0]

	c_t4111 = S.Task('c_t4111', length=3, delay_cost=1)
	S += c_t4111 >= 15
	c_t4111 += MAS[3]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 15
	c_t5000_in += MAS_in[3]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 15
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 15
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 16
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 16
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=4, delay_cost=1)
	S += c_t2_t1_t1 >= 16
	c_t2_t1_t1 += MM[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 16
	c_t3010_in += MAS_in[2]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 16
	c_t3011_in += MAS_in[1]

	c_t3101 = S.Task('c_t3101', length=3, delay_cost=1)
	S += c_t3101 >= 16
	c_t3101 += MAS[2]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 16
	c_t4001 += MAS[1]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 16
	c_t4010 += MAS[0]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 16
	c_t4011_in += MAS_in[3]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 16
	c_t5000 += MAS[3]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 16
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 16
	d_t4001_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 17
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=4, delay_cost=1)
	S += c_t2_t0_t1 >= 17
	c_t2_t0_t1 += MM[0]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=3, delay_cost=1)
	S += c_t2_t0_t3 >= 17
	c_t2_t0_t3 += MAS[0]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 17
	c_t3000_in += MAS_in[1]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 17
	c_t3010 += MAS[2]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 17
	c_t3011 += MAS[1]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 17
	c_t3100_in += MAS_in[3]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 17
	c_t3110_in += MAS_in[2]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 17
	c_t4011 += MAS[3]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 17
	c_t4110_in += MAS_in[0]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 17
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 17
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=4, delay_cost=1)
	S += c_t2_t0_t0 >= 18
	c_t2_t0_t0 += MM[0]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 18
	c_t3000 += MAS[1]

	c_t3100 = S.Task('c_t3100', length=3, delay_cost=1)
	S += c_t3100 >= 18
	c_t3100 += MAS[3]

	c_t3110 = S.Task('c_t3110', length=3, delay_cost=1)
	S += c_t3110 >= 18
	c_t3110 += MAS[2]

	c_t4110 = S.Task('c_t4110', length=3, delay_cost=1)
	S += c_t4110 >= 18
	c_t4110 += MAS[0]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 18
	c_t5011_in += MAS_in[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 18
	c_t5100_in += MAS_in[3]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 18
	c_t5110_in += MAS_in[2]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 18
	c_t5111_in += MAS_in[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 18
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 18
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 18
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 18
	d_t3_t3_t1_mem0 += MAS_MEM[0]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 18
	d_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 19
	c_t0_t00_in += MAS_in[1]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 19
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 19
	c_t0_t00_mem1 += MM_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 19
	c_t5010_in += MAS_in[2]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 19
	c_t5011 += MAS[1]

	c_t5100 = S.Task('c_t5100', length=3, delay_cost=1)
	S += c_t5100 >= 19
	c_t5100 += MAS[3]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 19
	c_t5101_in += MAS_in[0]

	c_t5110 = S.Task('c_t5110', length=3, delay_cost=1)
	S += c_t5110 >= 19
	c_t5110 += MAS[2]

	c_t5111 = S.Task('c_t5111', length=3, delay_cost=1)
	S += c_t5111 >= 19
	c_t5111 += MAS[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 19
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 19
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=4, delay_cost=1)
	S += d_t3_t3_t1 >= 19
	d_t3_t3_t1 += MM[0]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 19
	d_t3_t3_t2_in += MAS_in[3]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 19
	d_t3_t3_t2_mem0 += MAS_MEM[0]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 19
	d_t3_t3_t2_mem1 += MAS_MEM[1]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 19
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 19
	d_t5_t3_t1_mem0 += MAS_MEM[4]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 19
	d_t5_t3_t1_mem1 += MAS_MEM[3]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 20
	c_t0_t00 += MAS[1]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 20
	c_t5010 += MAS[2]

	c_t5101 = S.Task('c_t5101', length=3, delay_cost=1)
	S += c_t5101 >= 20
	c_t5101 += MAS[0]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 20
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 20
	d_t1_t2_t3_in += MAS_in[0]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 20
	d_t1_t2_t3_mem0 += MAS_MEM[4]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 20
	d_t1_t2_t3_mem1 += MAS_MEM[5]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 20
	d_t1_t30_in += MAS_in[1]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 20
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 20
	d_t1_t30_mem1 += MM_MEM[1]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 20
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 20
	d_t3_a1_1_in += MAS_in[2]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 20
	d_t3_a1_1_mem0 += MAS_MEM[0]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 20
	d_t3_a1_1_mem1 += MAS_MEM[3]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=3, delay_cost=1)
	S += d_t3_t3_t2 >= 20
	d_t3_t3_t2 += MAS[3]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 20
	d_t3_t3_t3_in += MAS_in[3]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 20
	d_t3_t3_t3_mem0 += MAS_MEM[2]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 20
	d_t3_t3_t3_mem1 += MAS_MEM[1]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 20
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 20
	d_t4_t3_t1_mem0 += MAS_MEM[6]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 20
	d_t4_t3_t1_mem1 += MAS_MEM[7]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=4, delay_cost=1)
	S += d_t5_t3_t1 >= 20
	d_t5_t3_t1 += MM[0]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 21
	c_t0_t0_t5_in += MAS_in[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 21
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 21
	c_t0_t0_t5_mem1 += MM_MEM[1]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 21
	d_t0_t3_t4_in += MM_in[0]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 21
	d_t0_t3_t4_mem0 += MAS_MEM[4]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 21
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 21
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=3, delay_cost=1)
	S += d_t1_t2_t3 >= 21
	d_t1_t2_t3 += MAS[0]

	d_t1_t30 = S.Task('d_t1_t30', length=3, delay_cost=1)
	S += d_t1_t30 >= 21
	d_t1_t30 += MAS[1]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 21
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 21
	d_t2_t2_t3_in += MAS_in[0]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 21
	d_t2_t2_t3_mem0 += MAS_MEM[6]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 21
	d_t2_t2_t3_mem1 += MAS_MEM[5]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=3, delay_cost=1)
	S += d_t3_a1_1 >= 21
	d_t3_a1_1 += MAS[2]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=3, delay_cost=1)
	S += d_t3_t3_t3 >= 21
	d_t3_t3_t3 += MAS[3]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=4, delay_cost=1)
	S += d_t4_t3_t1 >= 21
	d_t4_t3_t1 += MM[0]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 21
	d_t4_t3_t3_in += MAS_in[1]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 21
	d_t4_t3_t3_mem0 += MAS_MEM[0]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 21
	d_t4_t3_t3_mem1 += MAS_MEM[7]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 21
	d_t5_a1_1_in += MAS_in[3]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 21
	d_t5_a1_1_mem0 += MAS_MEM[2]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 21
	d_t5_a1_1_mem1 += MAS_MEM[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=3, delay_cost=1)
	S += c_t0_t0_t5 >= 22
	c_t0_t0_t5 += MAS[2]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 22
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=4, delay_cost=1)
	S += d_t0_t3_t4 >= 22
	d_t0_t3_t4 += MM[0]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=3, delay_cost=1)
	S += d_t2_t2_t3 >= 22
	d_t2_t2_t3 += MAS[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 22
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 22
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 22
	d_t2_t3_t4_mem0 += MAS_MEM[0]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 22
	d_t2_t3_t4_mem1 += MAS_MEM[5]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 22
	d_t2_t3_t5_in += MAS_in[0]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 22
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 22
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 22
	d_t3_a1_0_in += MAS_in[3]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 22
	d_t3_a1_0_mem0 += MAS_MEM[2]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 22
	d_t3_a1_0_mem1 += MAS_MEM[1]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 22
	d_t4_t11_in += MAS_in[2]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 22
	d_t4_t11_mem0 += MAS_MEM[6]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 22
	d_t4_t11_mem1 += MAS_MEM[7]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=3, delay_cost=1)
	S += d_t4_t3_t3 >= 22
	d_t4_t3_t3 += MAS[1]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=3, delay_cost=1)
	S += d_t5_a1_1 >= 22
	d_t5_a1_1 += MAS[3]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 22
	d_t5_t11_in += MAS_in[1]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 22
	d_t5_t11_mem0 += MAS_MEM[4]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 22
	d_t5_t11_mem1 += MAS_MEM[3]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 23
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 23
	c_t0_t0_t4_mem0 += MAS_MEM[4]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 23
	c_t0_t0_t4_mem1 += MAS_MEM[5]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 23
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 23
	d_t0_t2_t3_in += MAS_in[3]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 23
	d_t0_t2_t3_mem0 += MAS_MEM[2]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 23
	d_t0_t2_t3_mem1 += MAS_MEM[3]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 23
	d_t0_t30_in += MAS_in[0]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 23
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 23
	d_t0_t30_mem1 += MM_MEM[1]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=4, delay_cost=1)
	S += d_t2_t3_t4 >= 23
	d_t2_t3_t4 += MM[0]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=3, delay_cost=1)
	S += d_t2_t3_t5 >= 23
	d_t2_t3_t5 += MAS[0]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 23
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=3, delay_cost=1)
	S += d_t3_a1_0 >= 23
	d_t3_a1_0 += MAS[3]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 23
	d_t4_a1_0_in += MAS_in[2]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 23
	d_t4_a1_0_mem0 += MAS_MEM[0]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 23
	d_t4_a1_0_mem1 += MAS_MEM[7]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 23
	d_t4_a1_1_in += MAS_in[1]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 23
	d_t4_a1_1_mem0 += MAS_MEM[6]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 23
	d_t4_a1_1_mem1 += MAS_MEM[1]

	d_t4_t11 = S.Task('d_t4_t11', length=3, delay_cost=1)
	S += d_t4_t11 >= 23
	d_t4_t11 += MAS[2]

	d_t5_t11 = S.Task('d_t5_t11', length=3, delay_cost=1)
	S += d_t5_t11 >= 23
	d_t5_t11 += MAS[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=4, delay_cost=1)
	S += c_t0_t0_t4 >= 24
	c_t0_t0_t4 += MM[0]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 24
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 24
	c_t0_t4_t0_mem0 += MAS_MEM[6]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 24
	c_t0_t4_t0_mem1 += MAS_MEM[3]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 24
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 24
	d_t0_t00_in += MAS_in[3]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 24
	d_t0_t00_mem1 += MAS_MEM[7]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=3, delay_cost=1)
	S += d_t0_t2_t3 >= 24
	d_t0_t2_t3 += MAS[3]

	d_t0_t30 = S.Task('d_t0_t30', length=3, delay_cost=1)
	S += d_t0_t30 >= 24
	d_t0_t30 += MAS[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 24
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 24
	d_t1_t3_t5_in += MAS_in[0]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 24
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 24
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=3, delay_cost=1)
	S += d_t4_a1_0 >= 24
	d_t4_a1_0 += MAS[2]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=3, delay_cost=1)
	S += d_t4_a1_1 >= 24
	d_t4_a1_1 += MAS[1]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 24
	d_t4_t10_in += MAS_in[2]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 24
	d_t4_t10_mem0 += MAS_MEM[0]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 24
	d_t4_t10_mem1 += MAS_MEM[1]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 24
	d_t5_t3_t2_in += MAS_in[1]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 24
	d_t5_t3_t2_mem0 += MAS_MEM[4]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 24
	d_t5_t3_t2_mem1 += MAS_MEM[5]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 25
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 25
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 25
	c_t0_t1_t4_mem1 += MAS_MEM[7]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 25
	c_t0_t1_t5_in += MAS_in[1]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 25
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 25
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=4, delay_cost=1)
	S += c_t0_t4_t0 >= 25
	c_t0_t4_t0 += MM[0]

	d_t0_t00 = S.Task('d_t0_t00', length=3, delay_cost=1)
	S += d_t0_t00 >= 25
	d_t0_t00 += MAS[3]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 25
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 25
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 25
	d_t1_t00_in += MAS_in[2]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 25
	d_t1_t00_mem1 += MAS_MEM[5]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 25
	d_t1_t01_in += MAS_in[0]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 25
	d_t1_t01_mem1 += MAS_MEM[3]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=3, delay_cost=1)
	S += d_t1_t3_t5 >= 25
	d_t1_t3_t5 += MAS[0]

	d_t4_t10 = S.Task('d_t4_t10', length=3, delay_cost=1)
	S += d_t4_t10 >= 25
	d_t4_t10 += MAS[2]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 25
	d_t5_t10_in += MAS_in[3]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 25
	d_t5_t10_mem0 += MAS_MEM[4]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 25
	d_t5_t10_mem1 += MAS_MEM[1]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=3, delay_cost=1)
	S += d_t5_t3_t2 >= 25
	d_t5_t3_t2 += MAS[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=4, delay_cost=1)
	S += c_t0_t1_t4 >= 26
	c_t0_t1_t4 += MM[0]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=3, delay_cost=1)
	S += c_t0_t1_t5 >= 26
	c_t0_t1_t5 += MAS[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 26
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 26
	c_t0_t4_t1_mem0 += MAS_MEM[6]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 26
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 26
	c_t3_t20_in += MAS_in[1]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 26
	c_t3_t20_mem0 += MAS_MEM[2]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 26
	c_t3_t20_mem1 += MAS_MEM[5]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 26
	d_t0_t01_in += MAS_in[2]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 26
	d_t0_t01_mem1 += MAS_MEM[7]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 26
	d_t0_t3_t5_in += MAS_in[3]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 26
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 26
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 26
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_t00 = S.Task('d_t1_t00', length=3, delay_cost=1)
	S += d_t1_t00 >= 26
	d_t1_t00 += MAS[2]

	d_t1_t01 = S.Task('d_t1_t01', length=3, delay_cost=1)
	S += d_t1_t01 >= 26
	d_t1_t01 += MAS[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 26
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 26
	d_t5_a1_0_in += MAS_in[0]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 26
	d_t5_a1_0_mem0 += MAS_MEM[0]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 26
	d_t5_a1_0_mem1 += MAS_MEM[3]

	d_t5_t10 = S.Task('d_t5_t10', length=3, delay_cost=1)
	S += d_t5_t10 >= 26
	d_t5_t10 += MAS[3]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=4, delay_cost=1)
	S += c_t0_t4_t1 >= 27
	c_t0_t4_t1 += MM[0]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 27
	c_t2_t4_t3_in += MAS_in[3]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 27
	c_t2_t4_t3_mem0 += MAS_MEM[6]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 27
	c_t2_t4_t3_mem1 += MAS_MEM[5]

	c_t3_t20 = S.Task('c_t3_t20', length=3, delay_cost=1)
	S += c_t3_t20 >= 27
	c_t3_t20 += MAS[1]

	d_t0_t01 = S.Task('d_t0_t01', length=3, delay_cost=1)
	S += d_t0_t01 >= 27
	d_t0_t01 += MAS[2]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=3, delay_cost=1)
	S += d_t0_t3_t5 >= 27
	d_t0_t3_t5 += MAS[3]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 27
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 27
	d_t2_t01_in += MAS_in[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 27
	d_t2_t01_mem1 += MAS_MEM[7]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 27
	d_t2_t30_in += MAS_in[1]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 27
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 27
	d_t2_t30_mem1 += MM_MEM[1]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 27
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=3, delay_cost=1)
	S += d_t5_a1_0 >= 27
	d_t5_a1_0 += MAS[0]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 27
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 27
	d_t5_t3_t0_mem0 += MAS_MEM[4]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 27
	d_t5_t3_t0_mem1 += MAS_MEM[1]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 27
	d_t5_t3_t3_in += MAS_in[2]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 27
	d_t5_t3_t3_mem0 += MAS_MEM[0]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 27
	d_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 28
	c_t0_t10_in += MAS_in[0]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 28
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 28
	c_t0_t10_mem1 += MM_MEM[1]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 28
	c_t2_t4_t2_in += MAS_in[2]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 28
	c_t2_t4_t2_mem0 += MAS_MEM[2]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 28
	c_t2_t4_t2_mem1 += MAS_MEM[5]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=3, delay_cost=1)
	S += c_t2_t4_t3 >= 28
	c_t2_t4_t3 += MAS[3]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 28
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 28
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 28
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 28
	d_t1_t3_t4_mem0 += MAS_MEM[6]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 28
	d_t1_t3_t4_mem1 += MAS_MEM[1]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 28
	d_t2_t00_in += MAS_in[3]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 28
	d_t2_t00_mem1 += MAS_MEM[3]

	d_t2_t01 = S.Task('d_t2_t01', length=3, delay_cost=1)
	S += d_t2_t01 >= 28
	d_t2_t01 += MAS[0]

	d_t2_t30 = S.Task('d_t2_t30', length=3, delay_cost=1)
	S += d_t2_t30 >= 28
	d_t2_t30 += MAS[1]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 28
	d_t4_t3_t2_in += MAS_in[1]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 28
	d_t4_t3_t2_mem0 += MAS_MEM[0]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 28
	d_t4_t3_t2_mem1 += MAS_MEM[7]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=4, delay_cost=1)
	S += d_t5_t3_t0 >= 28
	d_t5_t3_t0 += MM[0]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=3, delay_cost=1)
	S += d_t5_t3_t3 >= 28
	d_t5_t3_t3 += MAS[2]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 29
	c_t0_t10 += MAS[0]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 29
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 29
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 29
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=3, delay_cost=1)
	S += c_t2_t4_t2 >= 29
	c_t2_t4_t2 += MAS[2]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 29
	c_t3_t0_t3_in += MAS_in[2]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 29
	c_t3_t0_t3_mem0 += MAS_MEM[6]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 29
	c_t3_t0_t3_mem1 += MAS_MEM[5]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 29
	c_t4_t21_in += MAS_in[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 29
	c_t4_t21_mem0 += MAS_MEM[2]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 29
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 29
	c_t4_t30_in += MAS_in[3]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 29
	c_t4_t30_mem0 += MAS_MEM[4]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 29
	c_t4_t30_mem1 += MAS_MEM[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 29
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=4, delay_cost=1)
	S += d_t1_t3_t4 >= 29
	d_t1_t3_t4 += MM[0]

	d_t2_t00 = S.Task('d_t2_t00', length=3, delay_cost=1)
	S += d_t2_t00 >= 29
	d_t2_t00 += MAS[3]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 29
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 29
	d_t3_t3_t0_mem0 += MAS_MEM[0]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 29
	d_t3_t3_t0_mem1 += MAS_MEM[3]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 29
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=3, delay_cost=1)
	S += d_t4_t3_t2 >= 29
	d_t4_t3_t2 += MAS[1]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 30
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 30
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 30
	c_t1_t0_t4_mem0 += MAS_MEM[6]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 30
	c_t1_t0_t4_mem1 += MAS_MEM[5]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 30
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 30
	c_t2_t00 += MAS[1]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 30
	c_t2_t10_in += MAS_in[0]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 30
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 30
	c_t2_t10_mem1 += MM_MEM[1]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=3, delay_cost=1)
	S += c_t3_t0_t3 >= 30
	c_t3_t0_t3 += MAS[2]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 30
	c_t3_t1_t3_in += MAS_in[2]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 30
	c_t3_t1_t3_mem0 += MAS_MEM[4]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 30
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 30
	c_t3_t21_in += MAS_in[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 30
	c_t3_t21_mem0 += MAS_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 30
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t4_t21 = S.Task('c_t4_t21', length=3, delay_cost=1)
	S += c_t4_t21 >= 30
	c_t4_t21 += MAS[0]

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	S += c_t4_t30 >= 30
	c_t4_t30 += MAS[3]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 30
	d_t3_t11_in += MAS_in[3]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 30
	d_t3_t11_mem0 += MAS_MEM[0]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 30
	d_t3_t11_mem1 += MAS_MEM[1]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=4, delay_cost=1)
	S += d_t3_t3_t0 >= 30
	d_t3_t3_t0 += MM[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 31
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 31
	c_t0_t4_t2_in += MAS_in[0]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 31
	c_t0_t4_t2_mem0 += MAS_MEM[6]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 31
	c_t0_t4_t2_mem1 += MAS_MEM[7]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=4, delay_cost=1)
	S += c_t1_t0_t4 >= 31
	c_t1_t0_t4 += MM[0]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 31
	c_t2_t0_t5_in += MAS_in[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 31
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 31
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 31
	c_t2_t10 += MAS[0]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 31
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 31
	c_t3_t0_t1_mem0 += MAS_MEM[2]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 31
	c_t3_t0_t1_mem1 += MAS_MEM[5]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=3, delay_cost=1)
	S += c_t3_t1_t3 >= 31
	c_t3_t1_t3 += MAS[2]

	c_t3_t21 = S.Task('c_t3_t21', length=3, delay_cost=1)
	S += c_t3_t21 >= 31
	c_t3_t21 += MAS[1]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 31
	c_t4_t0_t3_in += MAS_in[3]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 31
	c_t4_t0_t3_mem0 += MAS_MEM[4]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 31
	c_t4_t0_t3_mem1 += MAS_MEM[1]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 31
	d_t3_t10_in += MAS_in[2]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 31
	d_t3_t10_mem0 += MAS_MEM[0]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 31
	d_t3_t10_mem1 += MAS_MEM[3]

	d_t3_t11 = S.Task('d_t3_t11', length=3, delay_cost=1)
	S += d_t3_t11 >= 31
	d_t3_t11 += MAS[3]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 31
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 32
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=3, delay_cost=1)
	S += c_t0_t4_t2 >= 32
	c_t0_t4_t2 += MAS[0]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 32
	c_t1_t00_in += MAS_in[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 32
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 32
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 32
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=3, delay_cost=1)
	S += c_t2_t0_t5 >= 32
	c_t2_t0_t5 += MAS[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=4, delay_cost=1)
	S += c_t3_t0_t1 >= 32
	c_t3_t0_t1 += MM[0]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 32
	c_t3_t0_t2_in += MAS_in[3]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 32
	c_t3_t0_t2_mem0 += MAS_MEM[2]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 32
	c_t3_t0_t2_mem1 += MAS_MEM[3]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 32
	c_t3_t30_in += MAS_in[2]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 32
	c_t3_t30_mem0 += MAS_MEM[6]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 32
	c_t3_t30_mem1 += MAS_MEM[5]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 32
	c_t3_t31_in += MAS_in[1]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 32
	c_t3_t31_mem0 += MAS_MEM[4]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 32
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=3, delay_cost=1)
	S += c_t4_t0_t3 >= 32
	c_t4_t0_t3 += MAS[3]

	d_t3_t10 = S.Task('d_t3_t10', length=3, delay_cost=1)
	S += d_t3_t10 >= 32
	d_t3_t10 += MAS[2]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 32
	d_t4_t3_t0_in += MM_in[0]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 32
	d_t4_t3_t0_mem0 += MAS_MEM[0]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 32
	d_t4_t3_t0_mem1 += MAS_MEM[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 33
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 33
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 33
	c_t1_t00 += MAS[0]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 33
	c_t1_t10_in += MAS_in[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 33
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 33
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 33
	c_t1_t4_t2_in += MAS_in[0]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 33
	c_t1_t4_t2_mem0 += MAS_MEM[2]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 33
	c_t1_t4_t2_mem1 += MAS_MEM[3]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 33
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 33
	c_t2_t4_t1_mem0 += MAS_MEM[4]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 33
	c_t2_t4_t1_mem1 += MAS_MEM[5]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=3, delay_cost=1)
	S += c_t3_t0_t2 >= 33
	c_t3_t0_t2 += MAS[3]

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	S += c_t3_t30 >= 33
	c_t3_t30 += MAS[2]

	c_t3_t31 = S.Task('c_t3_t31', length=3, delay_cost=1)
	S += c_t3_t31 >= 33
	c_t3_t31 += MAS[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 33
	c_t4_t1_t2_in += MAS_in[2]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 33
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 33
	c_t4_t1_t2_mem1 += MAS_MEM[7]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 33
	c_t5_t0_t3_in += MAS_in[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 33
	c_t5_t0_t3_mem0 += MAS_MEM[6]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 33
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=4, delay_cost=1)
	S += d_t4_t3_t0 >= 33
	d_t4_t3_t0 += MM[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 34
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 34
	c_t0_t4_t3_in += MAS_in[3]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 34
	c_t0_t4_t3_mem0 += MAS_MEM[2]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 34
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 34
	c_t1_t0_t5_in += MAS_in[1]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 34
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 34
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 34
	c_t1_t10 += MAS[3]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=3, delay_cost=1)
	S += c_t1_t4_t2 >= 34
	c_t1_t4_t2 += MAS[0]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 34
	c_t1_t4_t3_in += MAS_in[2]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 34
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 34
	c_t1_t4_t3_mem1 += MAS_MEM[7]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=4, delay_cost=1)
	S += c_t2_t4_t1 >= 34
	c_t2_t4_t1 += MM[0]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 34
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 34
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 34
	c_t3_t1_t0_mem1 += MAS_MEM[5]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=3, delay_cost=1)
	S += c_t4_t1_t2 >= 34
	c_t4_t1_t2 += MAS[2]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 34
	c_t5_t0_t2_in += MAS_in[0]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 34
	c_t5_t0_t2_mem0 += MAS_MEM[6]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 34
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=3, delay_cost=1)
	S += c_t5_t0_t3 >= 34
	c_t5_t0_t3 += MAS[1]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 34
	d_t5010_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=3, delay_cost=1)
	S += c_t0_t4_t3 >= 35
	c_t0_t4_t3 += MAS[3]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=3, delay_cost=1)
	S += c_t1_t0_t5 >= 35
	c_t1_t0_t5 += MAS[1]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 35
	c_t1_t1_t5_in += MAS_in[2]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 35
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 35
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 35
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 35
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 35
	c_t1_t4_t0_mem0 += MAS_MEM[2]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 35
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=3, delay_cost=1)
	S += c_t1_t4_t3 >= 35
	c_t1_t4_t3 += MAS[2]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=4, delay_cost=1)
	S += c_t3_t1_t0 >= 35
	c_t3_t1_t0 += MM[0]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 35
	c_t3_t1_t2_in += MAS_in[1]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 35
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 35
	c_t3_t1_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 35
	c_t4_t1_t3_in += MAS_in[3]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 35
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 35
	c_t4_t1_t3_mem1 += MAS_MEM[7]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=3, delay_cost=1)
	S += c_t5_t0_t2 >= 35
	c_t5_t0_t2 += MAS[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 35
	c_t5_t30_in += MAS_in[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 35
	c_t5_t30_mem0 += MAS_MEM[6]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 35
	c_t5_t30_mem1 += MAS_MEM[5]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 35
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 36
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=3, delay_cost=1)
	S += c_t1_t1_t5 >= 36
	c_t1_t1_t5 += MAS[2]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=4, delay_cost=1)
	S += c_t1_t4_t0 >= 36
	c_t1_t4_t0 += MM[0]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 36
	c_t2_t1_t5_in += MAS_in[2]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 36
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 36
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 36
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 36
	c_t3_t0_t0_mem0 += MAS_MEM[2]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 36
	c_t3_t0_t0_mem1 += MAS_MEM[7]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=3, delay_cost=1)
	S += c_t3_t1_t2 >= 36
	c_t3_t1_t2 += MAS[1]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=3, delay_cost=1)
	S += c_t4_t1_t3 >= 36
	c_t4_t1_t3 += MAS[3]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 36
	c_t4_t20_in += MAS_in[3]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 36
	c_t4_t20_mem0 += MAS_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 36
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 36
	c_t5_t1_t2_in += MAS_in[1]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 36
	c_t5_t1_t2_mem0 += MAS_MEM[4]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 36
	c_t5_t1_t2_mem1 += MAS_MEM[3]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 36
	c_t5_t20_in += MAS_in[0]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 36
	c_t5_t20_mem0 += MAS_MEM[6]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 36
	c_t5_t20_mem1 += MAS_MEM[5]

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	S += c_t5_t30 >= 36
	c_t5_t30 += MAS[0]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 36
	d_t5011_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 37
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 37
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=3, delay_cost=1)
	S += c_t2_t1_t5 >= 37
	c_t2_t1_t5 += MAS[2]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=4, delay_cost=1)
	S += c_t3_t0_t0 >= 37
	c_t3_t0_t0 += MM[0]

	c_t4_t20 = S.Task('c_t4_t20', length=3, delay_cost=1)
	S += c_t4_t20 >= 37
	c_t4_t20 += MAS[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 37
	c_t4_t31_in += MAS_in[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 37
	c_t4_t31_mem0 += MAS_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 37
	c_t4_t31_mem1 += MAS_MEM[7]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 37
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 37
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 37
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=3, delay_cost=1)
	S += c_t5_t1_t2 >= 37
	c_t5_t1_t2 += MAS[1]

	c_t5_t20 = S.Task('c_t5_t20', length=3, delay_cost=1)
	S += c_t5_t20 >= 37
	c_t5_t20 += MAS[0]

	d_t4_t01_in = S.Task('d_t4_t01_in', length=1, delay_cost=1)
	S += d_t4_t01_in >= 37
	d_t4_t01_in += MAS_in[1]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	S += d_t4_t01_mem0 >= 37
	d_t4_t01_mem0 += MAS_MEM[6]

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	S += d_t4_t01_mem1 >= 37
	d_t4_t01_mem1 += MAS_MEM[3]

	d_t4_t2_t3_in = S.Task('d_t4_t2_t3_in', length=1, delay_cost=1)
	S += d_t4_t2_t3_in >= 37
	d_t4_t2_t3_in += MAS_in[3]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem0 >= 37
	d_t4_t2_t3_mem0 += MAS_MEM[4]

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem1 >= 37
	d_t4_t2_t3_mem1 += MAS_MEM[5]

	d_t4_t30_in = S.Task('d_t4_t30_in', length=1, delay_cost=1)
	S += d_t4_t30_in >= 37
	d_t4_t30_in += MAS_in[2]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	S += d_t4_t30_mem0 >= 37
	d_t4_t30_mem0 += MM_MEM[0]

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	S += d_t4_t30_mem1 >= 37
	d_t4_t30_mem1 += MM_MEM[1]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 38
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 38
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 38
	c_t4_t0_t2_in += MAS_in[3]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 38
	c_t4_t0_t2_mem0 += MAS_MEM[0]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 38
	c_t4_t0_t2_mem1 += MAS_MEM[3]

	c_t4_t31 = S.Task('c_t4_t31', length=3, delay_cost=1)
	S += c_t4_t31 >= 38
	c_t4_t31 += MAS[0]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 38
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 38
	c_t5_t0_t0_mem0 += MAS_MEM[6]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 38
	c_t5_t0_t0_mem1 += MAS_MEM[7]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=4, delay_cost=1)
	S += c_t5_t0_t1 >= 38
	c_t5_t0_t1 += MM[0]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 38
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 38
	c_t5_t1_t3_mem0 += MAS_MEM[4]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 38
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	d_t110_in = S.Task('d_t110_in', length=1, delay_cost=1)
	S += d_t110_in >= 38
	d_t110_in += MAS_in[1]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	S += d_t110_mem0 >= 38
	d_t110_mem0 += MAS_MEM[2]

	d_t3_t3_t5_in = S.Task('d_t3_t3_t5_in', length=1, delay_cost=1)
	S += d_t3_t3_t5_in >= 38
	d_t3_t3_t5_in += MAS_in[0]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem0 >= 38
	d_t3_t3_t5_mem0 += MM_MEM[0]

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem1 >= 38
	d_t3_t3_t5_mem1 += MM_MEM[1]

	d_t4_t01 = S.Task('d_t4_t01', length=3, delay_cost=1)
	S += d_t4_t01 >= 38
	d_t4_t01 += MAS[1]

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=3, delay_cost=1)
	S += d_t4_t2_t3 >= 38
	d_t4_t2_t3 += MAS[3]

	d_t4_t30 = S.Task('d_t4_t30', length=3, delay_cost=1)
	S += d_t4_t30 >= 38
	d_t4_t30 += MAS[2]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 39
	c_t0_t40_in += MAS_in[2]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 39
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 39
	c_t0_t40_mem1 += MM_MEM[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 39
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 39
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 39
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 39
	c_t4_t0_t1_mem0 += MAS_MEM[2]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 39
	c_t4_t0_t1_mem1 += MAS_MEM[1]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=3, delay_cost=1)
	S += c_t4_t0_t2 >= 39
	c_t4_t0_t2 += MAS[3]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=4, delay_cost=1)
	S += c_t5_t0_t0 >= 39
	c_t5_t0_t0 += MM[0]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=3, delay_cost=1)
	S += c_t5_t1_t3 >= 39
	c_t5_t1_t3 += MAS[2]

	d_t110 = S.Task('d_t110', length=3, delay_cost=1)
	S += d_t110 >= 39
	d_t110 += MAS[1]

	d_t3_t01_in = S.Task('d_t3_t01_in', length=1, delay_cost=1)
	S += d_t3_t01_in >= 39
	d_t3_t01_in += MAS_in[1]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	S += d_t3_t01_mem0 >= 39
	d_t3_t01_mem0 += MAS_MEM[0]

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	S += d_t3_t01_mem1 >= 39
	d_t3_t01_mem1 += MAS_MEM[5]

	d_t3_t2_t3_in = S.Task('d_t3_t2_t3_in', length=1, delay_cost=1)
	S += d_t3_t2_t3_in >= 39
	d_t3_t2_t3_in += MAS_in[3]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem0 >= 39
	d_t3_t2_t3_mem0 += MAS_MEM[4]

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem1 >= 39
	d_t3_t2_t3_mem1 += MAS_MEM[7]

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=3, delay_cost=1)
	S += d_t3_t3_t5 >= 39
	d_t3_t3_t5 += MAS[0]

	d_t5_t2_t3_in = S.Task('d_t5_t2_t3_in', length=1, delay_cost=1)
	S += d_t5_t2_t3_in >= 39
	d_t5_t2_t3_in += MAS_in[0]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem0 >= 39
	d_t5_t2_t3_mem0 += MAS_MEM[6]

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem1 >= 39
	d_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t0_t40 = S.Task('c_t0_t40', length=3, delay_cost=1)
	S += c_t0_t40 >= 40
	c_t0_t40 += MAS[2]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 40
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 40
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 40
	c_t1_t50_in += MAS_in[0]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 40
	c_t1_t50_mem0 += MAS_MEM[0]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 40
	c_t1_t50_mem1 += MAS_MEM[7]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 40
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 40
	c_t2_t0_t4_mem0 += MAS_MEM[2]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 40
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 40
	c_t3_t4_t3_in += MAS_in[2]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 40
	c_t3_t4_t3_mem0 += MAS_MEM[4]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 40
	c_t3_t4_t3_mem1 += MAS_MEM[3]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=4, delay_cost=1)
	S += c_t4_t0_t1 >= 40
	c_t4_t0_t1 += MM[0]

	d_t0_t2_t2_in = S.Task('d_t0_t2_t2_in', length=1, delay_cost=1)
	S += d_t0_t2_t2_in >= 40
	d_t0_t2_t2_in += MAS_in[3]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem0 >= 40
	d_t0_t2_t2_mem0 += MAS_MEM[6]

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem1 >= 40
	d_t0_t2_t2_mem1 += MAS_MEM[5]

	d_t3_t01 = S.Task('d_t3_t01', length=3, delay_cost=1)
	S += d_t3_t01 >= 40
	d_t3_t01 += MAS[1]

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=3, delay_cost=1)
	S += d_t3_t2_t3 >= 40
	d_t3_t2_t3 += MAS[3]

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=3, delay_cost=1)
	S += d_t5_t2_t3 >= 40
	d_t5_t2_t3 += MAS[0]

	d_t5_t30_in = S.Task('d_t5_t30_in', length=1, delay_cost=1)
	S += d_t5_t30_in >= 40
	d_t5_t30_in += MAS_in[1]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	S += d_t5_t30_mem0 >= 40
	d_t5_t30_mem0 += MM_MEM[0]

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	S += d_t5_t30_mem1 >= 40
	d_t5_t30_mem1 += MM_MEM[1]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 41
	c_t0_t4_t5_in += MAS_in[1]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 41
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 41
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 41
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 41
	c_t1_t1_t4_mem0 += MAS_MEM[2]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 41
	c_t1_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t50 = S.Task('c_t1_t50', length=3, delay_cost=1)
	S += c_t1_t50 >= 41
	c_t1_t50 += MAS[0]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=4, delay_cost=1)
	S += c_t2_t0_t4 >= 41
	c_t2_t0_t4 += MM[0]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=3, delay_cost=1)
	S += c_t3_t4_t3 >= 41
	c_t3_t4_t3 += MAS[2]

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=3, delay_cost=1)
	S += d_t0_t2_t2 >= 41
	d_t0_t2_t2 += MAS[3]

	d_t3_t00_in = S.Task('d_t3_t00_in', length=1, delay_cost=1)
	S += d_t3_t00_in >= 41
	d_t3_t00_in += MAS_in[0]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	S += d_t3_t00_mem0 >= 41
	d_t3_t00_mem0 += MAS_MEM[0]

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	S += d_t3_t00_mem1 >= 41
	d_t3_t00_mem1 += MAS_MEM[7]

	d_t410_in = S.Task('d_t410_in', length=1, delay_cost=1)
	S += d_t410_in >= 41
	d_t410_in += MAS_in[2]

	d_t410_mem0 = S.Task('d_t410_mem0', length=1, delay_cost=1)
	S += d_t410_mem0 >= 41
	d_t410_mem0 += MAS_MEM[4]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 41
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 41
	d_t5001_mem1 += MAIN_MEM_r[1]

	d_t5_t30 = S.Task('d_t5_t30', length=3, delay_cost=1)
	S += d_t5_t30 >= 41
	d_t5_t30 += MAS[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 42
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=3, delay_cost=1)
	S += c_t0_t4_t5 >= 42
	c_t0_t4_t5 += MAS[1]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 42
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=4, delay_cost=1)
	S += c_t1_t1_t4 >= 42
	c_t1_t1_t4 += MM[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 42
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 42
	c_t1_t4_t1_mem0 += MAS_MEM[2]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 42
	c_t1_t4_t1_mem1 += MAS_MEM[7]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 42
	c_t5_t31_in += MAS_in[1]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 42
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 42
	c_t5_t31_mem1 += MAS_MEM[1]

	d_t3_t00 = S.Task('d_t3_t00', length=3, delay_cost=1)
	S += d_t3_t00 >= 42
	d_t3_t00 += MAS[0]

	d_t3_t30_in = S.Task('d_t3_t30_in', length=1, delay_cost=1)
	S += d_t3_t30_in >= 42
	d_t3_t30_in += MAS_in[3]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	S += d_t3_t30_mem0 >= 42
	d_t3_t30_mem0 += MM_MEM[0]

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	S += d_t3_t30_mem1 >= 42
	d_t3_t30_mem1 += MM_MEM[1]

	d_t410 = S.Task('d_t410', length=3, delay_cost=1)
	S += d_t410 >= 42
	d_t410 += MAS[2]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 43
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=4, delay_cost=1)
	S += c_t1_t4_t1 >= 43
	c_t1_t4_t1 += MM[0]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 43
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 43
	c_t4_t0_t0_mem0 += MAS_MEM[0]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 43
	c_t4_t0_t0_mem1 += MAS_MEM[5]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 43
	c_t5_t21_in += MAS_in[0]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 43
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 43
	c_t5_t21_mem1 += MAS_MEM[3]

	c_t5_t31 = S.Task('c_t5_t31', length=3, delay_cost=1)
	S += c_t5_t31 >= 43
	c_t5_t31 += MAS[1]

	d_t2_t2_t2_in = S.Task('d_t2_t2_t2_in', length=1, delay_cost=1)
	S += d_t2_t2_t2_in >= 43
	d_t2_t2_t2_in += MAS_in[3]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem0 >= 43
	d_t2_t2_t2_mem0 += MAS_MEM[6]

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem1 >= 43
	d_t2_t2_t2_mem1 += MAS_MEM[1]

	d_t3_t30 = S.Task('d_t3_t30', length=3, delay_cost=1)
	S += d_t3_t30 >= 43
	d_t3_t30 += MAS[3]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 43
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t5_t01_in = S.Task('d_t5_t01_in', length=1, delay_cost=1)
	S += d_t5_t01_in >= 43
	d_t5_t01_in += MAS_in[1]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	S += d_t5_t01_mem0 >= 43
	d_t5_t01_mem0 += MAS_MEM[4]

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	S += d_t5_t01_mem1 >= 43
	d_t5_t01_mem1 += MAS_MEM[7]

	d_t5_t3_t5_in = S.Task('d_t5_t3_t5_in', length=1, delay_cost=1)
	S += d_t5_t3_t5_in >= 43
	d_t5_t3_t5_in += MAS_in[2]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem0 >= 43
	d_t5_t3_t5_mem0 += MM_MEM[0]

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem1 >= 43
	d_t5_t3_t5_mem1 += MM_MEM[1]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 44
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 44
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 44
	c_t2_t01_in += MAS_in[1]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 44
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 44
	c_t2_t01_mem1 += MAS_MEM[3]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 44
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 44
	c_t3_t1_t1_mem0 += MAS_MEM[2]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 44
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=4, delay_cost=1)
	S += c_t4_t0_t0 >= 44
	c_t4_t0_t0 += MM[0]

	c_t5_t21 = S.Task('c_t5_t21', length=3, delay_cost=1)
	S += c_t5_t21 >= 44
	c_t5_t21 += MAS[0]

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=3, delay_cost=1)
	S += d_t2_t2_t2 >= 44
	d_t2_t2_t2 += MAS[3]

	d_t4_t00_in = S.Task('d_t4_t00_in', length=1, delay_cost=1)
	S += d_t4_t00_in >= 44
	d_t4_t00_in += MAS_in[2]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	S += d_t4_t00_mem0 >= 44
	d_t4_t00_mem0 += MAS_MEM[0]

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	S += d_t4_t00_mem1 >= 44
	d_t4_t00_mem1 += MAS_MEM[5]

	d_t5_t00_in = S.Task('d_t5_t00_in', length=1, delay_cost=1)
	S += d_t5_t00_in >= 44
	d_t5_t00_in += MAS_in[0]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	S += d_t5_t00_mem0 >= 44
	d_t5_t00_mem0 += MAS_MEM[4]

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	S += d_t5_t00_mem1 >= 44
	d_t5_t00_mem1 += MAS_MEM[1]

	d_t5_t01 = S.Task('d_t5_t01', length=3, delay_cost=1)
	S += d_t5_t01 >= 44
	d_t5_t01 += MAS[1]

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=3, delay_cost=1)
	S += d_t5_t3_t5 >= 44
	d_t5_t3_t5 += MAS[2]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 45
	c_t0_t11_in += MAS_in[2]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 45
	c_t0_t11_mem0 += MM_MEM[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 45
	c_t0_t11_mem1 += MAS_MEM[3]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 45
	c_t0_t50_in += MAS_in[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 45
	c_t0_t50_mem0 += MAS_MEM[2]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 45
	c_t0_t50_mem1 += MAS_MEM[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 45
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 45
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t01 = S.Task('c_t2_t01', length=3, delay_cost=1)
	S += c_t2_t01 >= 45
	c_t2_t01 += MAS[1]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 45
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 45
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 45
	c_t2_t1_t4_mem1 += MAS_MEM[5]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=4, delay_cost=1)
	S += c_t3_t1_t1 >= 45
	c_t3_t1_t1 += MM[0]

	d_t310_in = S.Task('d_t310_in', length=1, delay_cost=1)
	S += d_t310_in >= 45
	d_t310_in += MAS_in[0]

	d_t310_mem0 = S.Task('d_t310_mem0', length=1, delay_cost=1)
	S += d_t310_mem0 >= 45
	d_t310_mem0 += MAS_MEM[6]

	d_t4_t00 = S.Task('d_t4_t00', length=3, delay_cost=1)
	S += d_t4_t00 >= 45
	d_t4_t00 += MAS[2]

	d_t5_t00 = S.Task('d_t5_t00', length=3, delay_cost=1)
	S += d_t5_t00 >= 45
	d_t5_t00 += MAS[0]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 46
	c_t0_t01_in += MAS_in[3]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 46
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 46
	c_t0_t01_mem1 += MAS_MEM[5]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 46
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t11 = S.Task('c_t0_t11', length=3, delay_cost=1)
	S += c_t0_t11 >= 46
	c_t0_t11 += MAS[2]

	c_t0_t50 = S.Task('c_t0_t50', length=3, delay_cost=1)
	S += c_t0_t50 >= 46
	c_t0_t50 += MAS[3]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=4, delay_cost=1)
	S += c_t2_t1_t4 >= 46
	c_t2_t1_t4 += MM[0]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 46
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 46
	c_t2_t4_t0_mem0 += MAS_MEM[2]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 46
	c_t2_t4_t0_mem1 += MAS_MEM[7]

	d_t010_in = S.Task('d_t010_in', length=1, delay_cost=1)
	S += d_t010_in >= 46
	d_t010_in += MAS_in[2]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	S += d_t010_mem0 >= 46
	d_t010_mem0 += MAS_MEM[0]

	d_t1_t2_t2_in = S.Task('d_t1_t2_t2_in', length=1, delay_cost=1)
	S += d_t1_t2_t2_in >= 46
	d_t1_t2_t2_in += MAS_in[1]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem0 >= 46
	d_t1_t2_t2_mem0 += MAS_MEM[4]

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem1 >= 46
	d_t1_t2_t2_mem1 += MAS_MEM[1]

	d_t310 = S.Task('d_t310', length=3, delay_cost=1)
	S += d_t310 >= 46
	d_t310 += MAS[0]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 46
	d_t5001_mem0 += MAIN_MEM_r[0]

	c_t0_t01 = S.Task('c_t0_t01', length=3, delay_cost=1)
	S += c_t0_t01 >= 47
	c_t0_t01 += MAS[3]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 47
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 47
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 47
	c_t1_t4_t5_in += MAS_in[1]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 47
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 47
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=4, delay_cost=1)
	S += c_t2_t4_t0 >= 47
	c_t2_t4_t0 += MM[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 47
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 47
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 47
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	d_t010 = S.Task('d_t010', length=3, delay_cost=1)
	S += d_t010 >= 47
	d_t010 += MAS[2]

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=3, delay_cost=1)
	S += d_t1_t2_t2 >= 47
	d_t1_t2_t2 += MAS[1]

	d_t210_in = S.Task('d_t210_in', length=1, delay_cost=1)
	S += d_t210_in >= 47
	d_t210_in += MAS_in[0]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	S += d_t210_mem0 >= 47
	d_t210_mem0 += MAS_MEM[2]

	d_t4_t2_t2_in = S.Task('d_t4_t2_t2_in', length=1, delay_cost=1)
	S += d_t4_t2_t2_in >= 47
	d_t4_t2_t2_in += MAS_in[2]

	d_t4_t2_t2_mem0 = S.Task('d_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem0 >= 47
	d_t4_t2_t2_mem0 += MAS_MEM[4]

	d_t4_t2_t2_mem1 = S.Task('d_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem1 >= 47
	d_t4_t2_t2_mem1 += MAS_MEM[3]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 48
	c_t1_t11_in += MAS_in[2]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 48
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 48
	c_t1_t11_mem1 += MAS_MEM[5]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 48
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 48
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=3, delay_cost=1)
	S += c_t1_t4_t5 >= 48
	c_t1_t4_t5 += MAS[1]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 48
	c_t3_t4_t2_in += MAS_in[3]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 48
	c_t3_t4_t2_mem0 += MAS_MEM[2]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 48
	c_t3_t4_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=4, delay_cost=1)
	S += c_t4_t1_t0 >= 48
	c_t4_t1_t0 += MM[0]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 48
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 48
	c_t4_t1_t1_mem0 += MAS_MEM[6]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 48
	c_t4_t1_t1_mem1 += MAS_MEM[7]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 48
	c_t5_t4_t2_in += MAS_in[1]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 48
	c_t5_t4_t2_mem0 += MAS_MEM[0]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 48
	c_t5_t4_t2_mem1 += MAS_MEM[1]

	d_t210 = S.Task('d_t210', length=3, delay_cost=1)
	S += d_t210 >= 48
	d_t210 += MAS[0]

	d_t4_t2_t2 = S.Task('d_t4_t2_t2', length=3, delay_cost=1)
	S += d_t4_t2_t2 >= 48
	d_t4_t2_t2 += MAS[2]

	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	S += c_t0_t51_in >= 49
	c_t0_t51_in += MAS_in[3]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 49
	c_t0_t51_mem0 += MAS_MEM[6]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 49
	c_t0_t51_mem1 += MAS_MEM[5]

	c_t1_t11 = S.Task('c_t1_t11', length=3, delay_cost=1)
	S += c_t1_t11 >= 49
	c_t1_t11 += MAS[2]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 49
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 49
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=3, delay_cost=1)
	S += c_t3_t4_t2 >= 49
	c_t3_t4_t2 += MAS[3]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=4, delay_cost=1)
	S += c_t4_t1_t1 >= 49
	c_t4_t1_t1 += MM[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 49
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 49
	c_t5_t1_t1_mem0 += MAS_MEM[2]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 49
	c_t5_t1_t1_mem1 += MAS_MEM[1]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=3, delay_cost=1)
	S += c_t5_t4_t2 >= 49
	c_t5_t4_t2 += MAS[1]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 49
	c_t5_t4_t3_in += MAS_in[1]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 49
	c_t5_t4_t3_mem0 += MAS_MEM[0]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 49
	c_t5_t4_t3_mem1 += MAS_MEM[3]

	d_t0_t31_in = S.Task('d_t0_t31_in', length=1, delay_cost=1)
	S += d_t0_t31_in >= 49
	d_t0_t31_in += MAS_in[2]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	S += d_t0_t31_mem0 >= 49
	d_t0_t31_mem0 += MM_MEM[0]

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	S += d_t0_t31_mem1 >= 49
	d_t0_t31_mem1 += MAS_MEM[7]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 50
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t51 = S.Task('c_t0_t51', length=3, delay_cost=1)
	S += c_t0_t51 >= 50
	c_t0_t51 += MAS[3]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 50
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 50
	c_t1_t40_in += MAS_in[3]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 50
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 50
	c_t1_t40_mem1 += MM_MEM[1]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 50
	c_t4_t4_t2_in += MAS_in[0]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 50
	c_t4_t4_t2_mem0 += MAS_MEM[6]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 50
	c_t4_t4_t2_mem1 += MAS_MEM[1]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 50
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 50
	c_t5_t1_t0_mem0 += MAS_MEM[4]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 50
	c_t5_t1_t0_mem1 += MAS_MEM[5]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=4, delay_cost=1)
	S += c_t5_t1_t1 >= 50
	c_t5_t1_t1 += MM[0]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=3, delay_cost=1)
	S += c_t5_t4_t3 >= 50
	c_t5_t4_t3 += MAS[1]

	d_t0_t31 = S.Task('d_t0_t31', length=3, delay_cost=1)
	S += d_t0_t31 >= 50
	d_t0_t31 += MAS[2]

	d_t510_in = S.Task('d_t510_in', length=1, delay_cost=1)
	S += d_t510_in >= 50
	d_t510_in += MAS_in[2]

	d_t510_mem0 = S.Task('d_t510_mem0', length=1, delay_cost=1)
	S += d_t510_mem0 >= 50
	d_t510_mem0 += MAS_MEM[2]

	d_t5_t2_t2_in = S.Task('d_t5_t2_t2_in', length=1, delay_cost=1)
	S += d_t5_t2_t2_in >= 50
	d_t5_t2_t2_in += MAS_in[1]

	d_t5_t2_t2_mem0 = S.Task('d_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem0 >= 50
	d_t5_t2_t2_mem0 += MAS_MEM[0]

	d_t5_t2_t2_mem1 = S.Task('d_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem1 >= 50
	d_t5_t2_t2_mem1 += MAS_MEM[3]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 51
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 51
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t40 = S.Task('c_t1_t40', length=3, delay_cost=1)
	S += c_t1_t40 >= 51
	c_t1_t40 += MAS[3]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 51
	c_t2_t40_in += MAS_in[1]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 51
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 51
	c_t2_t40_mem1 += MM_MEM[1]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 51
	c_t2_t50_in += MAS_in[2]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 51
	c_t2_t50_mem0 += MAS_MEM[2]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 51
	c_t2_t50_mem1 += MAS_MEM[1]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=3, delay_cost=1)
	S += c_t4_t4_t2 >= 51
	c_t4_t4_t2 += MAS[0]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=4, delay_cost=1)
	S += c_t5_t1_t0 >= 51
	c_t5_t1_t0 += MM[0]

	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	S += d_t1_t2_t0_in >= 51
	d_t1_t2_t0_in += MM_in[0]

	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem0 >= 51
	d_t1_t2_t0_mem0 += MAS_MEM[4]

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem1 >= 51
	d_t1_t2_t0_mem1 += MAS_MEM[5]

	d_t3_t2_t2_in = S.Task('d_t3_t2_t2_in', length=1, delay_cost=1)
	S += d_t3_t2_t2_in >= 51
	d_t3_t2_t2_in += MAS_in[3]

	d_t3_t2_t2_mem0 = S.Task('d_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem0 >= 51
	d_t3_t2_t2_mem0 += MAS_MEM[0]

	d_t3_t2_t2_mem1 = S.Task('d_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem1 >= 51
	d_t3_t2_t2_mem1 += MAS_MEM[3]

	d_t510 = S.Task('d_t510', length=3, delay_cost=1)
	S += d_t510 >= 51
	d_t510 += MAS[2]

	d_t5_t2_t2 = S.Task('d_t5_t2_t2', length=3, delay_cost=1)
	S += d_t5_t2_t2 >= 51
	d_t5_t2_t2 += MAS[1]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 52
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 52
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t40 = S.Task('c_t2_t40', length=3, delay_cost=1)
	S += c_t2_t40 >= 52
	c_t2_t40 += MAS[1]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 52
	c_t2_t4_t5_in += MAS_in[1]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 52
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 52
	c_t2_t4_t5_mem1 += MM_MEM[1]

	c_t2_t50 = S.Task('c_t2_t50', length=3, delay_cost=1)
	S += c_t2_t50 >= 52
	c_t2_t50 += MAS[2]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 52
	c_t4_t4_t3_in += MAS_in[2]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 52
	c_t4_t4_t3_mem0 += MAS_MEM[6]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 52
	c_t4_t4_t3_mem1 += MAS_MEM[1]

	d_s2010_in = S.Task('d_s2010_in', length=1, delay_cost=1)
	S += d_s2010_in >= 52
	d_s2010_in += MAS_in[0]

	d_s2010_mem0 = S.Task('d_s2010_mem0', length=1, delay_cost=1)
	S += d_s2010_mem0 >= 52
	d_s2010_mem0 += MAS_MEM[0]

	d_s2010_mem1 = S.Task('d_s2010_mem1', length=1, delay_cost=1)
	S += d_s2010_mem1 >= 52
	d_s2010_mem1 += MAS_MEM[5]

	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	S += d_t0_t2_t1_in >= 52
	d_t0_t2_t1_in += MM_in[0]

	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem0 >= 52
	d_t0_t2_t1_mem0 += MAS_MEM[4]

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem1 >= 52
	d_t0_t2_t1_mem1 += MAS_MEM[3]

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=4, delay_cost=1)
	S += d_t1_t2_t0 >= 52
	d_t1_t2_t0 += MM[0]

	d_t3_t2_t2 = S.Task('d_t3_t2_t2', length=3, delay_cost=1)
	S += d_t3_t2_t2 >= 52
	d_t3_t2_t2 += MAS[3]

	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	S += c_t010_in >= 53
	c_t010_in += MAS_in[0]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 53
	c_t010_mem0 += MAS_MEM[4]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 53
	c_t010_mem1 += MAS_MEM[7]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 53
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	S += c_t110_in >= 53
	c_t110_in += MAS_in[2]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 53
	c_t110_mem0 += MAS_MEM[6]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 53
	c_t110_mem1 += MAS_MEM[1]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 53
	c_t2_t11_in += MAS_in[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 53
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 53
	c_t2_t11_mem1 += MAS_MEM[5]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=3, delay_cost=1)
	S += c_t2_t4_t5 >= 53
	c_t2_t4_t5 += MAS[1]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=3, delay_cost=1)
	S += c_t4_t4_t3 >= 53
	c_t4_t4_t3 += MAS[2]

	d_s2010 = S.Task('d_s2010', length=3, delay_cost=1)
	S += d_s2010 >= 53
	d_s2010 += MAS[0]

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=4, delay_cost=1)
	S += d_t0_t2_t1 >= 53
	d_t0_t2_t1 += MM[0]

	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	S += d_t4_t3_t4_in >= 53
	d_t4_t3_t4_in += MM_in[0]

	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem0 >= 53
	d_t4_t3_t4_mem0 += MAS_MEM[2]

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem1 >= 53
	d_t4_t3_t4_mem1 += MAS_MEM[3]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 53
	d_t5000_mem1 += MAIN_MEM_r[1]

	c_t010 = S.Task('c_t010', length=3, delay_cost=1)
	S += c_t010 >= 54
	c_t010 += MAS[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 54
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t110 = S.Task('c_t110', length=3, delay_cost=1)
	S += c_t110 >= 54
	c_t110 += MAS[2]

	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	S += c_t1_s01_in >= 54
	c_t1_s01_in += MAS_in[0]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	S += c_t1_s01_mem0 >= 54
	c_t1_s01_mem0 += MAS_MEM[4]

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	S += c_t1_s01_mem1 >= 54
	c_t1_s01_mem1 += MAS_MEM[7]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 54
	c_t1_t01_in += MAS_in[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 54
	c_t1_t01_mem0 += MM_MEM[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 54
	c_t1_t01_mem1 += MAS_MEM[3]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 54
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=3, delay_cost=1)
	S += c_t2_t11 >= 54
	c_t2_t11 += MAS[3]

	d_s1010_in = S.Task('d_s1010_in', length=1, delay_cost=1)
	S += d_s1010_in >= 54
	d_s1010_in += MAS_in[1]

	d_s1010_mem0 = S.Task('d_s1010_mem0', length=1, delay_cost=1)
	S += d_s1010_mem0 >= 54
	d_s1010_mem0 += MAS_MEM[2]

	d_s1010_mem1 = S.Task('d_s1010_mem1', length=1, delay_cost=1)
	S += d_s1010_mem1 >= 54
	d_s1010_mem1 += MAS_MEM[1]

	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	S += d_t2_t2_t1_in >= 54
	d_t2_t2_t1_in += MM_in[0]

	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem0 >= 54
	d_t2_t2_t1_mem0 += MAS_MEM[0]

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem1 >= 54
	d_t2_t2_t1_mem1 += MAS_MEM[5]

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=4, delay_cost=1)
	S += d_t4_t3_t4 >= 54
	d_t4_t3_t4 += MM[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 55
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_s01 = S.Task('c_t1_s01', length=3, delay_cost=1)
	S += c_t1_s01 >= 55
	c_t1_s01 += MAS[0]

	c_t1_t01 = S.Task('c_t1_t01', length=3, delay_cost=1)
	S += c_t1_t01 >= 55
	c_t1_t01 += MAS[3]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 55
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	d_s0010_in = S.Task('d_s0010_in', length=1, delay_cost=1)
	S += d_s0010_in >= 55
	d_s0010_in += MAS_in[1]

	d_s0010_mem0 = S.Task('d_s0010_mem0', length=1, delay_cost=1)
	S += d_s0010_mem0 >= 55
	d_s0010_mem0 += MAS_MEM[4]

	d_s0010_mem1 = S.Task('d_s0010_mem1', length=1, delay_cost=1)
	S += d_s0010_mem1 >= 55
	d_s0010_mem1 += MAS_MEM[3]

	d_s1010 = S.Task('d_s1010', length=3, delay_cost=1)
	S += d_s1010 >= 55
	d_s1010 += MAS[1]

	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	S += d_t1_t2_t1_in >= 55
	d_t1_t2_t1_in += MM_in[0]

	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem0 >= 55
	d_t1_t2_t1_mem0 += MAS_MEM[0]

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem1 >= 55
	d_t1_t2_t1_mem1 += MAS_MEM[5]

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=4, delay_cost=1)
	S += d_t2_t2_t1 >= 55
	d_t2_t2_t1 += MM[0]

	d_t2_t31_in = S.Task('d_t2_t31_in', length=1, delay_cost=1)
	S += d_t2_t31_in >= 55
	d_t2_t31_in += MAS_in[3]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	S += d_t2_t31_mem0 >= 55
	d_t2_t31_mem0 += MM_MEM[0]

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	S += d_t2_t31_mem1 >= 55
	d_t2_t31_mem1 += MAS_MEM[1]

	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	S += c_t0_s01_in >= 56
	c_t0_s01_in += MAS_in[0]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	S += c_t0_s01_mem0 >= 56
	c_t0_s01_mem0 += MAS_MEM[4]

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	S += c_t0_s01_mem1 >= 56
	c_t0_s01_mem1 += MAS_MEM[1]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 56
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 56
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 56
	c_t0_t4_t4_mem0 += MAS_MEM[0]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 56
	c_t0_t4_t4_mem1 += MAS_MEM[7]

	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	S += c_t1_s00_in >= 56
	c_t1_s00_in += MAS_in[3]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	S += c_t1_s00_mem0 >= 56
	c_t1_s00_mem0 += MAS_MEM[6]

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	S += c_t1_s00_mem1 >= 56
	c_t1_s00_mem1 += MAS_MEM[5]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 56
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	d_s0010 = S.Task('d_s0010', length=3, delay_cost=1)
	S += d_s0010 >= 56
	d_s0010 += MAS[1]

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=4, delay_cost=1)
	S += d_t1_t2_t1 >= 56
	d_t1_t2_t1 += MM[0]

	d_t2_t31 = S.Task('d_t2_t31', length=3, delay_cost=1)
	S += d_t2_t31 >= 56
	d_t2_t31 += MAS[3]

	d_t4_t3_t5_in = S.Task('d_t4_t3_t5_in', length=1, delay_cost=1)
	S += d_t4_t3_t5_in >= 56
	d_t4_t3_t5_in += MAS_in[1]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem0 >= 56
	d_t4_t3_t5_mem0 += MM_MEM[0]

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem1 >= 56
	d_t4_t3_t5_mem1 += MM_MEM[1]

	c_t0_s01 = S.Task('c_t0_s01', length=3, delay_cost=1)
	S += c_t0_s01 >= 57
	c_t0_s01 += MAS[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 57
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=4, delay_cost=1)
	S += c_t0_t4_t4 >= 57
	c_t0_t4_t4 += MM[0]

	c_t1_s00 = S.Task('c_t1_s00', length=3, delay_cost=1)
	S += c_t1_s00 >= 57
	c_t1_s00 += MAS[3]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 57
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	S += c_t1_t51_in >= 57
	c_t1_t51_in += MAS_in[2]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 57
	c_t1_t51_mem0 += MAS_MEM[6]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 57
	c_t1_t51_mem1 += MAS_MEM[5]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 57
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 57
	c_t2_t4_t4_mem0 += MAS_MEM[4]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 57
	c_t2_t4_t4_mem1 += MAS_MEM[7]

	d_t1_t31_in = S.Task('d_t1_t31_in', length=1, delay_cost=1)
	S += d_t1_t31_in >= 57
	d_t1_t31_in += MAS_in[1]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	S += d_t1_t31_mem0 >= 57
	d_t1_t31_mem0 += MM_MEM[0]

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	S += d_t1_t31_mem1 >= 57
	d_t1_t31_mem1 += MAS_MEM[1]

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=3, delay_cost=1)
	S += d_t4_t3_t5 >= 57
	d_t4_t3_t5 += MAS[1]

	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	S += c_t0_s00_in >= 58
	c_t0_s00_in += MAS_in[2]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	S += c_t0_s00_mem0 >= 58
	c_t0_s00_mem0 += MAS_MEM[0]

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	S += c_t0_s00_mem1 >= 58
	c_t0_s00_mem1 += MAS_MEM[5]

	c_t1_t51 = S.Task('c_t1_t51', length=3, delay_cost=1)
	S += c_t1_t51 >= 58
	c_t1_t51 += MAS[2]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=4, delay_cost=1)
	S += c_t2_t4_t4 >= 58
	c_t2_t4_t4 += MM[0]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 58
	c_t4_t00_in += MAS_in[3]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 58
	c_t4_t00_mem0 += MM_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 58
	c_t4_t00_mem1 += MM_MEM[1]

	d_t0_t41_in = S.Task('d_t0_t41_in', length=1, delay_cost=1)
	S += d_t0_t41_in >= 58
	d_t0_t41_in += MAS_in[1]

	d_t0_t41_mem0 = S.Task('d_t0_t41_mem0', length=1, delay_cost=1)
	S += d_t0_t41_mem0 >= 58
	d_t0_t41_mem0 += MAS_MEM[4]

	d_t0_t41_mem1 = S.Task('d_t0_t41_mem1', length=1, delay_cost=1)
	S += d_t0_t41_mem1 >= 58
	d_t0_t41_mem1 += MAS_MEM[1]

	d_t1_t31 = S.Task('d_t1_t31', length=3, delay_cost=1)
	S += d_t1_t31 >= 58
	d_t1_t31 += MAS[1]

	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	S += d_t2_t2_t0_in >= 58
	d_t2_t2_t0_in += MM_in[0]

	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem0 >= 58
	d_t2_t2_t0_mem0 += MAS_MEM[6]

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem1 >= 58
	d_t2_t2_t0_mem1 += MAS_MEM[7]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 58
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 58
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t0_s00 = S.Task('c_t0_s00', length=3, delay_cost=1)
	S += c_t0_s00 >= 59
	c_t0_s00 += MAS[2]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 59
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	S += c_t2_s00_in >= 59
	c_t2_s00_in += MAS_in[3]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	S += c_t2_s00_mem0 >= 59
	c_t2_s00_mem0 += MAS_MEM[0]

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	S += c_t2_s00_mem1 >= 59
	c_t2_s00_mem1 += MAS_MEM[7]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 59
	c_t3_t1_t5_in += MAS_in[2]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 59
	c_t3_t1_t5_mem0 += MM_MEM[0]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 59
	c_t3_t1_t5_mem1 += MM_MEM[1]

	c_t4_t00 = S.Task('c_t4_t00', length=3, delay_cost=1)
	S += c_t4_t00 >= 59
	c_t4_t00 += MAS[3]

	d_t011_in = S.Task('d_t011_in', length=1, delay_cost=1)
	S += d_t011_in >= 59
	d_t011_in += MAS_in[0]

	d_t011_mem0 = S.Task('d_t011_mem0', length=1, delay_cost=1)
	S += d_t011_mem0 >= 59
	d_t011_mem0 += MAS_MEM[4]

	d_t0_t41 = S.Task('d_t0_t41', length=3, delay_cost=1)
	S += d_t0_t41 >= 59
	d_t0_t41 += MAS[1]

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=4, delay_cost=1)
	S += d_t2_t2_t0 >= 59
	d_t2_t2_t0 += MM[0]

	d_t2_t41_in = S.Task('d_t2_t41_in', length=1, delay_cost=1)
	S += d_t2_t41_in >= 59
	d_t2_t41_in += MAS_in[1]

	d_t2_t41_mem0 = S.Task('d_t2_t41_mem0', length=1, delay_cost=1)
	S += d_t2_t41_mem0 >= 59
	d_t2_t41_mem0 += MAS_MEM[6]

	d_t2_t41_mem1 = S.Task('d_t2_t41_mem1', length=1, delay_cost=1)
	S += d_t2_t41_mem1 >= 59
	d_t2_t41_mem1 += MAS_MEM[3]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 59
	d_t4010_mem1 += MAIN_MEM_r[1]

	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	S += d_t5_t3_t4_in >= 59
	d_t5_t3_t4_in += MM_in[0]

	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem0 >= 59
	d_t5_t3_t4_mem0 += MAS_MEM[2]

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem1 >= 59
	d_t5_t3_t4_mem1 += MAS_MEM[5]

	c_t2_s00 = S.Task('c_t2_s00', length=3, delay_cost=1)
	S += c_t2_s00 >= 60
	c_t2_s00 += MAS[3]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 60
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 60
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 60
	c_t3_t00_in += MAS_in[2]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 60
	c_t3_t00_mem0 += MM_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 60
	c_t3_t00_mem1 += MM_MEM[1]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=3, delay_cost=1)
	S += c_t3_t1_t5 >= 60
	c_t3_t1_t5 += MAS[2]

	d_s210_in = S.Task('d_s210_in', length=1, delay_cost=1)
	S += d_s210_in >= 60
	d_s210_in += MAS_in[3]

	d_s210_mem0 = S.Task('d_s210_mem0', length=1, delay_cost=1)
	S += d_s210_mem0 >= 60
	d_s210_mem0 += MAS_MEM[4]

	d_s210_mem1 = S.Task('d_s210_mem1', length=1, delay_cost=1)
	S += d_s210_mem1 >= 60
	d_s210_mem1 += MAS_MEM[1]

	d_t011 = S.Task('d_t011', length=3, delay_cost=1)
	S += d_t011 >= 60
	d_t011 += MAS[0]

	d_t0_t40_in = S.Task('d_t0_t40_in', length=1, delay_cost=1)
	S += d_t0_t40_in >= 60
	d_t0_t40_in += MAS_in[1]

	d_t0_t40_mem0 = S.Task('d_t0_t40_mem0', length=1, delay_cost=1)
	S += d_t0_t40_mem0 >= 60
	d_t0_t40_mem0 += MAS_MEM[0]

	d_t0_t40_mem1 = S.Task('d_t0_t40_mem1', length=1, delay_cost=1)
	S += d_t0_t40_mem1 >= 60
	d_t0_t40_mem1 += MAS_MEM[5]

	d_t1_t41_in = S.Task('d_t1_t41_in', length=1, delay_cost=1)
	S += d_t1_t41_in >= 60
	d_t1_t41_in += MAS_in[0]

	d_t1_t41_mem0 = S.Task('d_t1_t41_mem0', length=1, delay_cost=1)
	S += d_t1_t41_mem0 >= 60
	d_t1_t41_mem0 += MAS_MEM[2]

	d_t1_t41_mem1 = S.Task('d_t1_t41_mem1', length=1, delay_cost=1)
	S += d_t1_t41_mem1 >= 60
	d_t1_t41_mem1 += MAS_MEM[3]

	d_t2_t41 = S.Task('d_t2_t41', length=3, delay_cost=1)
	S += d_t2_t41 >= 60
	d_t2_t41 += MAS[1]

	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	S += d_t3_t3_t4_in >= 60
	d_t3_t3_t4_in += MM_in[0]

	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem0 >= 60
	d_t3_t3_t4_mem0 += MAS_MEM[6]

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem1 >= 60
	d_t3_t3_t4_mem1 += MAS_MEM[7]

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=4, delay_cost=1)
	S += d_t5_t3_t4 >= 60
	d_t5_t3_t4 += MM[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 61
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 61
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3_t00 = S.Task('c_t3_t00', length=3, delay_cost=1)
	S += c_t3_t00 >= 61
	c_t3_t00 += MAS[2]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 61
	c_t5_t0_t5_in += MAS_in[2]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 61
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 61
	c_t5_t0_t5_mem1 += MM_MEM[1]

	c_t6010_in = S.Task('c_t6010_in', length=1, delay_cost=1)
	S += c_t6010_in >= 61
	c_t6010_in += MAS_in[3]

	c_t6010_mem0 = S.Task('c_t6010_mem0', length=1, delay_cost=1)
	S += c_t6010_mem0 >= 61
	c_t6010_mem0 += MAS_MEM[0]

	c_t6010_mem1 = S.Task('c_t6010_mem1', length=1, delay_cost=1)
	S += c_t6010_mem1 >= 61
	c_t6010_mem1 += MAS_MEM[5]

	d_s210 = S.Task('d_s210', length=3, delay_cost=1)
	S += d_s210 >= 61
	d_s210 += MAS[3]

	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	S += d_t0_t2_t0_in >= 61
	d_t0_t2_t0_in += MM_in[0]

	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem0 >= 61
	d_t0_t2_t0_mem0 += MAS_MEM[6]

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem1 >= 61
	d_t0_t2_t0_mem1 += MAS_MEM[3]

	d_t0_t40 = S.Task('d_t0_t40', length=3, delay_cost=1)
	S += d_t0_t40 >= 61
	d_t0_t40 += MAS[1]

	d_t1_t41 = S.Task('d_t1_t41', length=3, delay_cost=1)
	S += d_t1_t41 >= 61
	d_t1_t41 += MAS[0]

	d_t2_t40_in = S.Task('d_t2_t40_in', length=1, delay_cost=1)
	S += d_t2_t40_in >= 61
	d_t2_t40_in += MAS_in[0]

	d_t2_t40_mem0 = S.Task('d_t2_t40_mem0', length=1, delay_cost=1)
	S += d_t2_t40_mem0 >= 61
	d_t2_t40_mem0 += MAS_MEM[2]

	d_t2_t40_mem1 = S.Task('d_t2_t40_mem1', length=1, delay_cost=1)
	S += d_t2_t40_mem1 >= 61
	d_t2_t40_mem1 += MAS_MEM[7]

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=4, delay_cost=1)
	S += d_t3_t3_t4 >= 61
	d_t3_t3_t4 += MM[0]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 62
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 62
	c_t1_t4_t4_mem0 += MAS_MEM[0]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 62
	c_t1_t4_t4_mem1 += MAS_MEM[5]

	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	S += c_t2_s01_in >= 62
	c_t2_s01_in += MAS_in[2]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	S += c_t2_s01_mem0 >= 62
	c_t2_s01_mem0 += MAS_MEM[6]

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	S += c_t2_s01_mem1 >= 62
	c_t2_s01_mem1 += MAS_MEM[1]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 62
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 62
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	S += c_t2_t51_in >= 62
	c_t2_t51_in += MAS_in[0]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 62
	c_t2_t51_mem0 += MAS_MEM[2]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 62
	c_t2_t51_mem1 += MAS_MEM[7]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 62
	c_t5_t00_in += MAS_in[3]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 62
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 62
	c_t5_t00_mem1 += MM_MEM[1]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=3, delay_cost=1)
	S += c_t5_t0_t5 >= 62
	c_t5_t0_t5 += MAS[2]

	c_t6010 = S.Task('c_t6010', length=3, delay_cost=1)
	S += c_t6010 >= 62
	c_t6010 += MAS[3]

	d_s1110_in = S.Task('d_s1110_in', length=1, delay_cost=1)
	S += d_s1110_in >= 62
	d_s1110_in += MAS_in[1]

	d_s1110_mem0 = S.Task('d_s1110_mem0', length=1, delay_cost=1)
	S += d_s1110_mem0 >= 62
	d_s1110_mem0 += MAS_MEM[4]

	d_s1110_mem1 = S.Task('d_s1110_mem1', length=1, delay_cost=1)
	S += d_s1110_mem1 >= 62
	d_s1110_mem1 += MAS_MEM[3]

	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=4, delay_cost=1)
	S += d_t0_t2_t0 >= 62
	d_t0_t2_t0 += MM[0]

	d_t2_t40 = S.Task('d_t2_t40', length=3, delay_cost=1)
	S += d_t2_t40 >= 62
	d_t2_t40 += MAS[0]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=4, delay_cost=1)
	S += c_t1_t4_t4 >= 63
	c_t1_t4_t4 += MM[0]

	c_t2_s01 = S.Task('c_t2_s01', length=3, delay_cost=1)
	S += c_t2_s01 >= 63
	c_t2_s01 += MAS[2]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 63
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t51 = S.Task('c_t2_t51', length=3, delay_cost=1)
	S += c_t2_t51 >= 63
	c_t2_t51 += MAS[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 63
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 63
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 63
	c_t4_t0_t4_mem0 += MAS_MEM[6]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 63
	c_t4_t0_t4_mem1 += MAS_MEM[7]

	c_t5_t00 = S.Task('c_t5_t00', length=3, delay_cost=1)
	S += c_t5_t00 >= 63
	c_t5_t00 += MAS[3]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 63
	c_t5_t1_t5_in += MAS_in[1]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 63
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 63
	c_t5_t1_t5_mem1 += MM_MEM[1]

	d_s1110 = S.Task('d_s1110', length=3, delay_cost=1)
	S += d_s1110 >= 63
	d_s1110 += MAS[1]

	d_t1_t40_in = S.Task('d_t1_t40_in', length=1, delay_cost=1)
	S += d_t1_t40_in >= 63
	d_t1_t40_in += MAS_in[2]

	d_t1_t40_mem0 = S.Task('d_t1_t40_mem0', length=1, delay_cost=1)
	S += d_t1_t40_mem0 >= 63
	d_t1_t40_mem0 += MAS_MEM[2]

	d_t1_t40_mem1 = S.Task('d_t1_t40_mem1', length=1, delay_cost=1)
	S += d_t1_t40_mem1 >= 63
	d_t1_t40_mem1 += MAS_MEM[3]

	c_t100_in = S.Task('c_t100_in', length=1, delay_cost=1)
	S += c_t100_in >= 64
	c_t100_in += MAS_in[3]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 64
	c_t100_mem0 += MAS_MEM[0]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 64
	c_t100_mem1 += MAS_MEM[7]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 64
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 64
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 64
	c_t3_t0_t5_in += MAS_in[2]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 64
	c_t3_t0_t5_mem0 += MM_MEM[0]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 64
	c_t3_t0_t5_mem1 += MM_MEM[1]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 64
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 64
	c_t3_t1_t4_mem0 += MAS_MEM[2]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 64
	c_t3_t1_t4_mem1 += MAS_MEM[5]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=4, delay_cost=1)
	S += c_t4_t0_t4 >= 64
	c_t4_t0_t4 += MM[0]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=3, delay_cost=1)
	S += c_t5_t1_t5 >= 64
	c_t5_t1_t5 += MAS[1]

	d_t0_t51_in = S.Task('d_t0_t51_in', length=1, delay_cost=1)
	S += d_t0_t51_in >= 64
	d_t0_t51_in += MAS_in[0]

	d_t0_t51_mem0 = S.Task('d_t0_t51_mem0', length=1, delay_cost=1)
	S += d_t0_t51_mem0 >= 64
	d_t0_t51_mem0 += MAS_MEM[4]

	d_t0_t51_mem1 = S.Task('d_t0_t51_mem1', length=1, delay_cost=1)
	S += d_t0_t51_mem1 >= 64
	d_t0_t51_mem1 += MAS_MEM[3]

	d_t1_t40 = S.Task('d_t1_t40', length=3, delay_cost=1)
	S += d_t1_t40 >= 64
	d_t1_t40 += MAS[2]

	d_t211_in = S.Task('d_t211_in', length=1, delay_cost=1)
	S += d_t211_in >= 64
	d_t211_in += MAS_in[1]

	d_t211_mem0 = S.Task('d_t211_mem0', length=1, delay_cost=1)
	S += d_t211_mem0 >= 64
	d_t211_mem0 += MAS_MEM[6]

	c_t100 = S.Task('c_t100', length=3, delay_cost=1)
	S += c_t100 >= 65
	c_t100 += MAS[3]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 65
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 65
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=3, delay_cost=1)
	S += c_t3_t0_t5 >= 65
	c_t3_t0_t5 += MAS[2]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 65
	c_t3_t10_in += MAS_in[2]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 65
	c_t3_t10_mem0 += MM_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 65
	c_t3_t10_mem1 += MM_MEM[1]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=4, delay_cost=1)
	S += c_t3_t1_t4 >= 65
	c_t3_t1_t4 += MM[0]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 65
	c_t4_t4_t0_in += MM_in[0]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 65
	c_t4_t4_t0_mem0 += MAS_MEM[6]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 65
	c_t4_t4_t0_mem1 += MAS_MEM[7]

	d_t0_t50_in = S.Task('d_t0_t50_in', length=1, delay_cost=1)
	S += d_t0_t50_in >= 65
	d_t0_t50_in += MAS_in[0]

	d_t0_t50_mem0 = S.Task('d_t0_t50_mem0', length=1, delay_cost=1)
	S += d_t0_t50_mem0 >= 65
	d_t0_t50_mem0 += MAS_MEM[0]

	d_t0_t50_mem1 = S.Task('d_t0_t50_mem1', length=1, delay_cost=1)
	S += d_t0_t50_mem1 >= 65
	d_t0_t50_mem1 += MAS_MEM[3]

	d_t0_t51 = S.Task('d_t0_t51', length=3, delay_cost=1)
	S += d_t0_t51 >= 65
	d_t0_t51 += MAS[0]

	d_t111_in = S.Task('d_t111_in', length=1, delay_cost=1)
	S += d_t111_in >= 65
	d_t111_in += MAS_in[3]

	d_t111_mem0 = S.Task('d_t111_mem0', length=1, delay_cost=1)
	S += d_t111_mem0 >= 65
	d_t111_mem0 += MAS_MEM[2]

	d_t211 = S.Task('d_t211', length=3, delay_cost=1)
	S += d_t211 >= 65
	d_t211 += MAS[1]

	c_t101_in = S.Task('c_t101_in', length=1, delay_cost=1)
	S += c_t101_in >= 66
	c_t101_in += MAS_in[1]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 66
	c_t101_mem0 += MAS_MEM[6]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 66
	c_t101_mem1 += MAS_MEM[1]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 66
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t10 = S.Task('c_t3_t10', length=3, delay_cost=1)
	S += c_t3_t10 >= 66
	c_t3_t10 += MAS[2]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 66
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 66
	c_t4_t0_t5_in += MAS_in[2]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 66
	c_t4_t0_t5_mem0 += MM_MEM[0]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 66
	c_t4_t0_t5_mem1 += MM_MEM[1]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=4, delay_cost=1)
	S += c_t4_t4_t0 >= 66
	c_t4_t4_t0 += MM[0]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 66
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 66
	c_t5_t1_t4_mem0 += MAS_MEM[2]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 66
	c_t5_t1_t4_mem1 += MAS_MEM[5]

	d_s010_in = S.Task('d_s010_in', length=1, delay_cost=1)
	S += d_s010_in >= 66
	d_s010_in += MAS_in[3]

	d_s010_mem0 = S.Task('d_s010_mem0', length=1, delay_cost=1)
	S += d_s010_mem0 >= 66
	d_s010_mem0 += MAS_MEM[0]

	d_s010_mem1 = S.Task('d_s010_mem1', length=1, delay_cost=1)
	S += d_s010_mem1 >= 66
	d_s010_mem1 += MAS_MEM[3]

	d_t0_t50 = S.Task('d_t0_t50', length=3, delay_cost=1)
	S += d_t0_t50 >= 66
	d_t0_t50 += MAS[0]

	d_t111 = S.Task('d_t111', length=3, delay_cost=1)
	S += d_t111 >= 66
	d_t111 += MAS[3]

	c_t101 = S.Task('c_t101', length=3, delay_cost=1)
	S += c_t101 >= 67
	c_t101 += MAS[1]

	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	S += c_t210_in >= 67
	c_t210_in += MAS_in[0]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 67
	c_t210_mem0 += MAS_MEM[2]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 67
	c_t210_mem1 += MAS_MEM[5]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 67
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 67
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=3, delay_cost=1)
	S += c_t4_t0_t5 >= 67
	c_t4_t0_t5 += MAS[2]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 67
	c_t4_t10_in += MAS_in[2]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 67
	c_t4_t10_mem0 += MM_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 67
	c_t4_t10_mem1 += MM_MEM[1]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 67
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 67
	c_t4_t4_t1_mem0 += MAS_MEM[0]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 67
	c_t4_t4_t1_mem1 += MAS_MEM[1]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=4, delay_cost=1)
	S += c_t5_t1_t4 >= 67
	c_t5_t1_t4 += MM[0]

	d_s010 = S.Task('d_s010', length=3, delay_cost=1)
	S += d_s010 >= 67
	d_s010 += MAS[3]

	d_t2_t51_in = S.Task('d_t2_t51_in', length=1, delay_cost=1)
	S += d_t2_t51_in >= 67
	d_t2_t51_in += MAS_in[1]

	d_t2_t51_mem0 = S.Task('d_t2_t51_mem0', length=1, delay_cost=1)
	S += d_t2_t51_mem0 >= 67
	d_t2_t51_mem0 += MAS_MEM[6]

	d_t2_t51_mem1 = S.Task('d_t2_t51_mem1', length=1, delay_cost=1)
	S += d_t2_t51_mem1 >= 67
	d_t2_t51_mem1 += MAS_MEM[3]

	c_t210 = S.Task('c_t210', length=3, delay_cost=1)
	S += c_t210 >= 68
	c_t210 += MAS[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 68
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	S += c_t3_t50_in >= 68
	c_t3_t50_in += MAS_in[2]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 68
	c_t3_t50_mem0 += MAS_MEM[4]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 68
	c_t3_t50_mem1 += MAS_MEM[5]

	c_t4_t10 = S.Task('c_t4_t10', length=3, delay_cost=1)
	S += c_t4_t10 >= 68
	c_t4_t10 += MAS[2]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 68
	c_t4_t1_t5_in += MAS_in[0]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 68
	c_t4_t1_t5_mem0 += MM_MEM[0]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 68
	c_t4_t1_t5_mem1 += MM_MEM[1]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=4, delay_cost=1)
	S += c_t4_t4_t1 >= 68
	c_t4_t4_t1 += MM[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 68
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 68
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 68
	c_t5_t0_t4_mem0 += MAS_MEM[0]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 68
	c_t5_t0_t4_mem1 += MAS_MEM[3]

	d_t2_t50_in = S.Task('d_t2_t50_in', length=1, delay_cost=1)
	S += d_t2_t50_in >= 68
	d_t2_t50_in += MAS_in[3]

	d_t2_t50_mem0 = S.Task('d_t2_t50_mem0', length=1, delay_cost=1)
	S += d_t2_t50_mem0 >= 68
	d_t2_t50_mem0 += MAS_MEM[2]

	d_t2_t50_mem1 = S.Task('d_t2_t50_mem1', length=1, delay_cost=1)
	S += d_t2_t50_mem1 >= 68
	d_t2_t50_mem1 += MAS_MEM[1]

	d_t2_t51 = S.Task('d_t2_t51', length=3, delay_cost=1)
	S += d_t2_t51 >= 68
	d_t2_t51 += MAS[1]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 69
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 69
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 69
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 69
	c_t3_t0_t4_mem0 += MAS_MEM[6]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 69
	c_t3_t0_t4_mem1 += MAS_MEM[5]

	c_t3_t50 = S.Task('c_t3_t50', length=3, delay_cost=1)
	S += c_t3_t50 >= 69
	c_t3_t50 += MAS[2]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=3, delay_cost=1)
	S += c_t4_t1_t5 >= 69
	c_t4_t1_t5 += MAS[0]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=4, delay_cost=1)
	S += c_t5_t0_t4 >= 69
	c_t5_t0_t4 += MM[0]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 69
	c_t5_t10_in += MAS_in[3]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 69
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 69
	c_t5_t10_mem1 += MM_MEM[1]

	d_t2_t50 = S.Task('d_t2_t50', length=3, delay_cost=1)
	S += d_t2_t50 >= 69
	d_t2_t50 += MAS[3]

	d_t6_y1_0_in = S.Task('d_t6_y1_0_in', length=1, delay_cost=1)
	S += d_t6_y1_0_in >= 69
	d_t6_y1_0_in += MAS_in[1]

	d_t6_y1_0_mem0 = S.Task('d_t6_y1_0_mem0', length=1, delay_cost=1)
	S += d_t6_y1_0_mem0 >= 69
	d_t6_y1_0_mem0 += MAS_MEM[0]

	d_t6_y1_0_mem1 = S.Task('d_t6_y1_0_mem1', length=1, delay_cost=1)
	S += d_t6_y1_0_mem1 >= 69
	d_t6_y1_0_mem1 += MAS_MEM[3]

	d_t6_y1_1_in = S.Task('d_t6_y1_1_in', length=1, delay_cost=1)
	S += d_t6_y1_1_in >= 69
	d_t6_y1_1_in += MAS_in[0]

	d_t6_y1_1_mem0 = S.Task('d_t6_y1_1_mem0', length=1, delay_cost=1)
	S += d_t6_y1_1_mem0 >= 69
	d_t6_y1_1_mem0 += MAS_MEM[2]

	d_t6_y1_1_mem1 = S.Task('d_t6_y1_1_mem1', length=1, delay_cost=1)
	S += d_t6_y1_1_mem1 >= 69
	d_t6_y1_1_mem1 += MAS_MEM[1]

	c_t001_in = S.Task('c_t001_in', length=1, delay_cost=1)
	S += c_t001_in >= 70
	c_t001_in += MAS_in[0]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 70
	c_t001_mem0 += MAS_MEM[6]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 70
	c_t001_mem1 += MAS_MEM[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 70
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=4, delay_cost=1)
	S += c_t3_t0_t4 >= 70
	c_t3_t0_t4 += MM[0]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 70
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 70
	c_t3_t4_t1_mem0 += MAS_MEM[2]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 70
	c_t3_t4_t1_mem1 += MAS_MEM[3]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 70
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t5_t10 = S.Task('c_t5_t10', length=3, delay_cost=1)
	S += c_t5_t10 >= 70
	c_t5_t10 += MAS[3]

	d_s0011_in = S.Task('d_s0011_in', length=1, delay_cost=1)
	S += d_s0011_in >= 70
	d_s0011_in += MAS_in[2]

	d_s0011_mem0 = S.Task('d_s0011_mem0', length=1, delay_cost=1)
	S += d_s0011_mem0 >= 70
	d_s0011_mem0 += MAS_MEM[0]

	d_s0011_mem1 = S.Task('d_s0011_mem1', length=1, delay_cost=1)
	S += d_s0011_mem1 >= 70
	d_s0011_mem1 += MAS_MEM[7]

	d_t5_t31_in = S.Task('d_t5_t31_in', length=1, delay_cost=1)
	S += d_t5_t31_in >= 70
	d_t5_t31_in += MAS_in[3]

	d_t5_t31_mem0 = S.Task('d_t5_t31_mem0', length=1, delay_cost=1)
	S += d_t5_t31_mem0 >= 70
	d_t5_t31_mem0 += MM_MEM[0]

	d_t5_t31_mem1 = S.Task('d_t5_t31_mem1', length=1, delay_cost=1)
	S += d_t5_t31_mem1 >= 70
	d_t5_t31_mem1 += MAS_MEM[5]

	d_t6_y1_0 = S.Task('d_t6_y1_0', length=3, delay_cost=1)
	S += d_t6_y1_0 >= 70
	d_t6_y1_0 += MAS[1]

	d_t6_y1_1 = S.Task('d_t6_y1_1', length=3, delay_cost=1)
	S += d_t6_y1_1 >= 70
	d_t6_y1_1 += MAS[0]

	c_t001 = S.Task('c_t001', length=3, delay_cost=1)
	S += c_t001 >= 71
	c_t001 += MAS[0]

	c_t200_in = S.Task('c_t200_in', length=1, delay_cost=1)
	S += c_t200_in >= 71
	c_t200_in += MAS_in[2]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 71
	c_t200_mem0 += MAS_MEM[2]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 71
	c_t200_mem1 += MAS_MEM[7]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 71
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 71
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=4, delay_cost=1)
	S += c_t3_t4_t1 >= 71
	c_t3_t4_t1 += MM[0]

	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	S += c_t4_t50_in >= 71
	c_t4_t50_in += MAS_in[3]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 71
	c_t4_t50_mem0 += MAS_MEM[6]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 71
	c_t4_t50_mem1 += MAS_MEM[5]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 71
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 71
	c_t5_t4_t0_mem0 += MAS_MEM[0]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 71
	c_t5_t4_t0_mem1 += MAS_MEM[1]

	d_s0011 = S.Task('d_s0011', length=3, delay_cost=1)
	S += d_s0011 >= 71
	d_s0011 += MAS[2]

	d_t2_t20_in = S.Task('d_t2_t20_in', length=1, delay_cost=1)
	S += d_t2_t20_in >= 71
	d_t2_t20_in += MAS_in[1]

	d_t2_t20_mem0 = S.Task('d_t2_t20_mem0', length=1, delay_cost=1)
	S += d_t2_t20_mem0 >= 71
	d_t2_t20_mem0 += MM_MEM[0]

	d_t2_t20_mem1 = S.Task('d_t2_t20_mem1', length=1, delay_cost=1)
	S += d_t2_t20_mem1 >= 71
	d_t2_t20_mem1 += MM_MEM[1]

	d_t5_t31 = S.Task('d_t5_t31', length=3, delay_cost=1)
	S += d_t5_t31 >= 71
	d_t5_t31 += MAS[3]

	c_t200 = S.Task('c_t200', length=3, delay_cost=1)
	S += c_t200 >= 72
	c_t200 += MAS[2]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 72
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 72
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4_t50 = S.Task('c_t4_t50', length=3, delay_cost=1)
	S += c_t4_t50 >= 72
	c_t4_t50 += MAS[3]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=4, delay_cost=1)
	S += c_t5_t4_t0 >= 72
	c_t5_t4_t0 += MM[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 72
	c_t5_t4_t1_in += MM_in[0]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 72
	c_t5_t4_t1_mem0 += MAS_MEM[0]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 72
	c_t5_t4_t1_mem1 += MAS_MEM[3]

	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	S += c_t5_t50_in >= 72
	c_t5_t50_in += MAS_in[1]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 72
	c_t5_t50_mem0 += MAS_MEM[6]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 72
	c_t5_t50_mem1 += MAS_MEM[7]

	c_t7010_in = S.Task('c_t7010_in', length=1, delay_cost=1)
	S += c_t7010_in >= 72
	c_t7010_in += MAS_in[2]

	c_t7010_mem0 = S.Task('c_t7010_mem0', length=1, delay_cost=1)
	S += c_t7010_mem0 >= 72
	c_t7010_mem0 += MAS_MEM[4]

	c_t7010_mem1 = S.Task('c_t7010_mem1', length=1, delay_cost=1)
	S += c_t7010_mem1 >= 72
	c_t7010_mem1 += MAS_MEM[1]

	d_t0_t20_in = S.Task('d_t0_t20_in', length=1, delay_cost=1)
	S += d_t0_t20_in >= 72
	d_t0_t20_in += MAS_in[0]

	d_t0_t20_mem0 = S.Task('d_t0_t20_mem0', length=1, delay_cost=1)
	S += d_t0_t20_mem0 >= 72
	d_t0_t20_mem0 += MM_MEM[0]

	d_t0_t20_mem1 = S.Task('d_t0_t20_mem1', length=1, delay_cost=1)
	S += d_t0_t20_mem1 >= 72
	d_t0_t20_mem1 += MM_MEM[1]

	d_t1_t50_in = S.Task('d_t1_t50_in', length=1, delay_cost=1)
	S += d_t1_t50_in >= 72
	d_t1_t50_in += MAS_in[3]

	d_t1_t50_mem0 = S.Task('d_t1_t50_mem0', length=1, delay_cost=1)
	S += d_t1_t50_mem0 >= 72
	d_t1_t50_mem0 += MAS_MEM[2]

	d_t1_t50_mem1 = S.Task('d_t1_t50_mem1', length=1, delay_cost=1)
	S += d_t1_t50_mem1 >= 72
	d_t1_t50_mem1 += MAS_MEM[5]

	d_t2_t20 = S.Task('d_t2_t20', length=3, delay_cost=1)
	S += d_t2_t20 >= 72
	d_t2_t20 += MAS[1]

	c_t000_in = S.Task('c_t000_in', length=1, delay_cost=1)
	S += c_t000_in >= 73
	c_t000_in += MAS_in[0]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 73
	c_t000_mem0 += MAS_MEM[2]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 73
	c_t000_mem1 += MAS_MEM[5]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 73
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 73
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 73
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 73
	c_t4_t1_t4_mem0 += MAS_MEM[4]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 73
	c_t4_t1_t4_mem1 += MAS_MEM[7]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=4, delay_cost=1)
	S += c_t5_t4_t1 >= 73
	c_t5_t4_t1 += MM[0]

	c_t5_t50 = S.Task('c_t5_t50', length=3, delay_cost=1)
	S += c_t5_t50 >= 73
	c_t5_t50 += MAS[1]

	c_t7010 = S.Task('c_t7010', length=3, delay_cost=1)
	S += c_t7010 >= 73
	c_t7010 += MAS[2]

	c_t8010_in = S.Task('c_t8010_in', length=1, delay_cost=1)
	S += c_t8010_in >= 73
	c_t8010_in += MAS_in[3]

	c_t8010_mem0 = S.Task('c_t8010_mem0', length=1, delay_cost=1)
	S += c_t8010_mem0 >= 73
	c_t8010_mem0 += MAS_MEM[0]

	c_t8010_mem1 = S.Task('c_t8010_mem1', length=1, delay_cost=1)
	S += c_t8010_mem1 >= 73
	c_t8010_mem1 += MAS_MEM[1]

	d_s1011_in = S.Task('d_s1011_in', length=1, delay_cost=1)
	S += d_s1011_in >= 73
	d_s1011_in += MAS_in[1]

	d_s1011_mem0 = S.Task('d_s1011_mem0', length=1, delay_cost=1)
	S += d_s1011_mem0 >= 73
	d_s1011_mem0 += MAS_MEM[6]

	d_s1011_mem1 = S.Task('d_s1011_mem1', length=1, delay_cost=1)
	S += d_s1011_mem1 >= 73
	d_s1011_mem1 += MAS_MEM[3]

	d_t0_t20 = S.Task('d_t0_t20', length=3, delay_cost=1)
	S += d_t0_t20 >= 73
	d_t0_t20 += MAS[0]

	d_t0_t2_t5_in = S.Task('d_t0_t2_t5_in', length=1, delay_cost=1)
	S += d_t0_t2_t5_in >= 73
	d_t0_t2_t5_in += MAS_in[2]

	d_t0_t2_t5_mem0 = S.Task('d_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem0 >= 73
	d_t0_t2_t5_mem0 += MM_MEM[0]

	d_t0_t2_t5_mem1 = S.Task('d_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem1 >= 73
	d_t0_t2_t5_mem1 += MM_MEM[1]

	d_t1_t50 = S.Task('d_t1_t50', length=3, delay_cost=1)
	S += d_t1_t50 >= 73
	d_t1_t50 += MAS[3]

	c_t000 = S.Task('c_t000', length=3, delay_cost=1)
	S += c_t000 >= 74
	c_t000 += MAS[0]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 74
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 74
	c_t3_t4_t0_mem0 += MAS_MEM[2]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 74
	c_t3_t4_t0_mem1 += MAS_MEM[5]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 74
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=4, delay_cost=1)
	S += c_t4_t1_t4 >= 74
	c_t4_t1_t4 += MM[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 74
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t8010 = S.Task('c_t8010', length=3, delay_cost=1)
	S += c_t8010 >= 74
	c_t8010 += MAS[3]

	d_s1011 = S.Task('d_s1011', length=3, delay_cost=1)
	S += d_s1011 >= 74
	d_s1011 += MAS[1]

	d_t0_t2_t5 = S.Task('d_t0_t2_t5', length=3, delay_cost=1)
	S += d_t0_t2_t5 >= 74
	d_t0_t2_t5 += MAS[2]

	d_t1_t20_in = S.Task('d_t1_t20_in', length=1, delay_cost=1)
	S += d_t1_t20_in >= 74
	d_t1_t20_in += MAS_in[1]

	d_t1_t20_mem0 = S.Task('d_t1_t20_mem0', length=1, delay_cost=1)
	S += d_t1_t20_mem0 >= 74
	d_t1_t20_mem0 += MM_MEM[0]

	d_t1_t20_mem1 = S.Task('d_t1_t20_mem1', length=1, delay_cost=1)
	S += d_t1_t20_mem1 >= 74
	d_t1_t20_mem1 += MM_MEM[1]

	d_t5_t41_in = S.Task('d_t5_t41_in', length=1, delay_cost=1)
	S += d_t5_t41_in >= 74
	d_t5_t41_in += MAS_in[0]

	d_t5_t41_mem0 = S.Task('d_t5_t41_mem0', length=1, delay_cost=1)
	S += d_t5_t41_mem0 >= 74
	d_t5_t41_mem0 += MAS_MEM[6]

	d_t5_t41_mem1 = S.Task('d_t5_t41_mem1', length=1, delay_cost=1)
	S += d_t5_t41_mem1 >= 74
	d_t5_t41_mem1 += MAS_MEM[3]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 75
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 75
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=4, delay_cost=1)
	S += c_t3_t4_t0 >= 75
	c_t3_t4_t0 += MM[0]

	d_t1_t20 = S.Task('d_t1_t20', length=3, delay_cost=1)
	S += d_t1_t20 >= 75
	d_t1_t20 += MAS[1]

	d_t3_t2_t1_in = S.Task('d_t3_t2_t1_in', length=1, delay_cost=1)
	S += d_t3_t2_t1_in >= 75
	d_t3_t2_t1_in += MM_in[0]

	d_t3_t2_t1_mem0 = S.Task('d_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem0 >= 75
	d_t3_t2_t1_mem0 += MAS_MEM[2]

	d_t3_t2_t1_mem1 = S.Task('d_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem1 >= 75
	d_t3_t2_t1_mem1 += MAS_MEM[7]

	d_t4_t31_in = S.Task('d_t4_t31_in', length=1, delay_cost=1)
	S += d_t4_t31_in >= 75
	d_t4_t31_in += MAS_in[1]

	d_t4_t31_mem0 = S.Task('d_t4_t31_mem0', length=1, delay_cost=1)
	S += d_t4_t31_mem0 >= 75
	d_t4_t31_mem0 += MM_MEM[0]

	d_t4_t31_mem1 = S.Task('d_t4_t31_mem1', length=1, delay_cost=1)
	S += d_t4_t31_mem1 >= 75
	d_t4_t31_mem1 += MAS_MEM[3]

	d_t511_in = S.Task('d_t511_in', length=1, delay_cost=1)
	S += d_t511_in >= 75
	d_t511_in += MAS_in[0]

	d_t511_mem0 = S.Task('d_t511_mem0', length=1, delay_cost=1)
	S += d_t511_mem0 >= 75
	d_t511_mem0 += MAS_MEM[6]

	d_t5_t41 = S.Task('d_t5_t41', length=3, delay_cost=1)
	S += d_t5_t41 >= 75
	d_t5_t41 += MAS[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 76
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 76
	c_t3111_mem0 += MAIN_MEM_r[0]

	d_t1_t2_t4_in = S.Task('d_t1_t2_t4_in', length=1, delay_cost=1)
	S += d_t1_t2_t4_in >= 76
	d_t1_t2_t4_in += MM_in[0]

	d_t1_t2_t4_mem0 = S.Task('d_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem0 >= 76
	d_t1_t2_t4_mem0 += MAS_MEM[2]

	d_t1_t2_t4_mem1 = S.Task('d_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem1 >= 76
	d_t1_t2_t4_mem1 += MAS_MEM[1]

	d_t1_t2_t5_in = S.Task('d_t1_t2_t5_in', length=1, delay_cost=1)
	S += d_t1_t2_t5_in >= 76
	d_t1_t2_t5_in += MAS_in[0]

	d_t1_t2_t5_mem0 = S.Task('d_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem0 >= 76
	d_t1_t2_t5_mem0 += MM_MEM[0]

	d_t1_t2_t5_mem1 = S.Task('d_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem1 >= 76
	d_t1_t2_t5_mem1 += MM_MEM[1]

	d_t3_t2_t1 = S.Task('d_t3_t2_t1', length=4, delay_cost=1)
	S += d_t3_t2_t1 >= 76
	d_t3_t2_t1 += MM[0]

	d_t4_t31 = S.Task('d_t4_t31', length=3, delay_cost=1)
	S += d_t4_t31 >= 76
	d_t4_t31 += MAS[1]

	d_t511 = S.Task('d_t511', length=3, delay_cost=1)
	S += d_t511 >= 76
	d_t511 += MAS[0]

	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	S += c_t2_t41_in >= 77
	c_t2_t41_in += MAS_in[0]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 77
	c_t2_t41_mem0 += MM_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 77
	c_t2_t41_mem1 += MAS_MEM[3]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 77
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 77
	c_t5001_mem1 += MAIN_MEM_r[1]

	d_t1_t2_t4 = S.Task('d_t1_t2_t4', length=4, delay_cost=1)
	S += d_t1_t2_t4 >= 77
	d_t1_t2_t4 += MM[0]

	d_t1_t2_t5 = S.Task('d_t1_t2_t5', length=3, delay_cost=1)
	S += d_t1_t2_t5 >= 77
	d_t1_t2_t5 += MAS[0]

	d_t4_t2_t0_in = S.Task('d_t4_t2_t0_in', length=1, delay_cost=1)
	S += d_t4_t2_t0_in >= 77
	d_t4_t2_t0_in += MM_in[0]

	d_t4_t2_t0_mem0 = S.Task('d_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem0 >= 77
	d_t4_t2_t0_mem0 += MAS_MEM[4]

	d_t4_t2_t0_mem1 = S.Task('d_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem1 >= 77
	d_t4_t2_t0_mem1 += MAS_MEM[5]

	d_t5_t40_in = S.Task('d_t5_t40_in', length=1, delay_cost=1)
	S += d_t5_t40_in >= 77
	d_t5_t40_in += MAS_in[3]

	d_t5_t40_mem0 = S.Task('d_t5_t40_mem0', length=1, delay_cost=1)
	S += d_t5_t40_mem0 >= 77
	d_t5_t40_mem0 += MAS_MEM[2]

	d_t5_t40_mem1 = S.Task('d_t5_t40_mem1', length=1, delay_cost=1)
	S += d_t5_t40_mem1 >= 77
	d_t5_t40_mem1 += MAS_MEM[7]

	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	S += c_t0_t41_in >= 78
	c_t0_t41_in += MAS_in[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 78
	c_t0_t41_mem0 += MM_MEM[0]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 78
	c_t0_t41_mem1 += MAS_MEM[3]

	c_t2_t41 = S.Task('c_t2_t41', length=3, delay_cost=1)
	S += c_t2_t41 >= 78
	c_t2_t41 += MAS[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 78
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 78
	c_t5000_mem0 += MAIN_MEM_r[0]

	d_t4_t2_t0 = S.Task('d_t4_t2_t0', length=4, delay_cost=1)
	S += d_t4_t2_t0 >= 78
	d_t4_t2_t0 += MM[0]

	d_t4_t2_t1_in = S.Task('d_t4_t2_t1_in', length=1, delay_cost=1)
	S += d_t4_t2_t1_in >= 78
	d_t4_t2_t1_in += MM_in[0]

	d_t4_t2_t1_mem0 = S.Task('d_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem0 >= 78
	d_t4_t2_t1_mem0 += MAS_MEM[2]

	d_t4_t2_t1_mem1 = S.Task('d_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem1 >= 78
	d_t4_t2_t1_mem1 += MAS_MEM[5]

	d_t5_t40 = S.Task('d_t5_t40', length=3, delay_cost=1)
	S += d_t5_t40 >= 78
	d_t5_t40 += MAS[3]

	c_t0_t41 = S.Task('c_t0_t41', length=3, delay_cost=1)
	S += c_t0_t41 >= 79
	c_t0_t41 += MAS[3]

	c_t201_in = S.Task('c_t201_in', length=1, delay_cost=1)
	S += c_t201_in >= 79
	c_t201_in += MAS_in[0]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 79
	c_t201_mem0 += MAS_MEM[2]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 79
	c_t201_mem1 += MAS_MEM[5]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 79
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 79
	c_t4000_mem0 += MAIN_MEM_r[0]

	d_t3_t31_in = S.Task('d_t3_t31_in', length=1, delay_cost=1)
	S += d_t3_t31_in >= 79
	d_t3_t31_in += MAS_in[3]

	d_t3_t31_mem0 = S.Task('d_t3_t31_mem0', length=1, delay_cost=1)
	S += d_t3_t31_mem0 >= 79
	d_t3_t31_mem0 += MM_MEM[0]

	d_t3_t31_mem1 = S.Task('d_t3_t31_mem1', length=1, delay_cost=1)
	S += d_t3_t31_mem1 >= 79
	d_t3_t31_mem1 += MAS_MEM[1]

	d_t4_t2_t1 = S.Task('d_t4_t2_t1', length=4, delay_cost=1)
	S += d_t4_t2_t1 >= 79
	d_t4_t2_t1 += MM[0]

	d_t4_t40_in = S.Task('d_t4_t40_in', length=1, delay_cost=1)
	S += d_t4_t40_in >= 79
	d_t4_t40_in += MAS_in[1]

	d_t4_t40_mem0 = S.Task('d_t4_t40_mem0', length=1, delay_cost=1)
	S += d_t4_t40_mem0 >= 79
	d_t4_t40_mem0 += MAS_MEM[4]

	d_t4_t40_mem1 = S.Task('d_t4_t40_mem1', length=1, delay_cost=1)
	S += d_t4_t40_mem1 >= 79
	d_t4_t40_mem1 += MAS_MEM[3]

	d_t5_t2_t0_in = S.Task('d_t5_t2_t0_in', length=1, delay_cost=1)
	S += d_t5_t2_t0_in >= 79
	d_t5_t2_t0_in += MM_in[0]

	d_t5_t2_t0_mem0 = S.Task('d_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem0 >= 79
	d_t5_t2_t0_mem0 += MAS_MEM[0]

	d_t5_t2_t0_mem1 = S.Task('d_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem1 >= 79
	d_t5_t2_t0_mem1 += MAS_MEM[7]

	c_t201 = S.Task('c_t201', length=3, delay_cost=1)
	S += c_t201 >= 80
	c_t201 += MAS[0]

	c_t211_in = S.Task('c_t211_in', length=1, delay_cost=1)
	S += c_t211_in >= 80
	c_t211_in += MAS_in[2]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 80
	c_t211_mem0 += MAS_MEM[0]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 80
	c_t211_mem1 += MAS_MEM[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 80
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 80
	c_t4111_mem1 += MAIN_MEM_r[1]

	d_t2_t2_t5_in = S.Task('d_t2_t2_t5_in', length=1, delay_cost=1)
	S += d_t2_t2_t5_in >= 80
	d_t2_t2_t5_in += MAS_in[1]

	d_t2_t2_t5_mem0 = S.Task('d_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem0 >= 80
	d_t2_t2_t5_mem0 += MM_MEM[0]

	d_t2_t2_t5_mem1 = S.Task('d_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem1 >= 80
	d_t2_t2_t5_mem1 += MM_MEM[1]

	d_t3_t31 = S.Task('d_t3_t31', length=3, delay_cost=1)
	S += d_t3_t31 >= 80
	d_t3_t31 += MAS[3]

	d_t4_t40 = S.Task('d_t4_t40', length=3, delay_cost=1)
	S += d_t4_t40 >= 80
	d_t4_t40 += MAS[1]

	d_t5_t2_t0 = S.Task('d_t5_t2_t0', length=4, delay_cost=1)
	S += d_t5_t2_t0 >= 80
	d_t5_t2_t0 += MM[0]

	d_t5_t2_t1_in = S.Task('d_t5_t2_t1_in', length=1, delay_cost=1)
	S += d_t5_t2_t1_in >= 80
	d_t5_t2_t1_in += MM_in[0]

	d_t5_t2_t1_mem0 = S.Task('d_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem0 >= 80
	d_t5_t2_t1_mem0 += MAS_MEM[2]

	d_t5_t2_t1_mem1 = S.Task('d_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem1 >= 80
	d_t5_t2_t1_mem1 += MAS_MEM[3]

	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	S += c_t1_t41_in >= 81
	c_t1_t41_in += MAS_in[2]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 81
	c_t1_t41_mem0 += MM_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 81
	c_t1_t41_mem1 += MAS_MEM[3]

	c_t211 = S.Task('c_t211', length=3, delay_cost=1)
	S += c_t211 >= 81
	c_t211 += MAS[2]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 81
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 81
	c_t4110_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t4_in = S.Task('d_t0_t2_t4_in', length=1, delay_cost=1)
	S += d_t0_t2_t4_in >= 81
	d_t0_t2_t4_in += MM_in[0]

	d_t0_t2_t4_mem0 = S.Task('d_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem0 >= 81
	d_t0_t2_t4_mem0 += MAS_MEM[6]

	d_t0_t2_t4_mem1 = S.Task('d_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem1 >= 81
	d_t0_t2_t4_mem1 += MAS_MEM[7]

	d_t1_t51_in = S.Task('d_t1_t51_in', length=1, delay_cost=1)
	S += d_t1_t51_in >= 81
	d_t1_t51_in += MAS_in[0]

	d_t1_t51_mem0 = S.Task('d_t1_t51_mem0', length=1, delay_cost=1)
	S += d_t1_t51_mem0 >= 81
	d_t1_t51_mem0 += MAS_MEM[2]

	d_t1_t51_mem1 = S.Task('d_t1_t51_mem1', length=1, delay_cost=1)
	S += d_t1_t51_mem1 >= 81
	d_t1_t51_mem1 += MAS_MEM[1]

	d_t2_t2_t5 = S.Task('d_t2_t2_t5', length=3, delay_cost=1)
	S += d_t2_t2_t5 >= 81
	d_t2_t2_t5 += MAS[1]

	d_t5_t2_t1 = S.Task('d_t5_t2_t1', length=4, delay_cost=1)
	S += d_t5_t2_t1 >= 81
	d_t5_t2_t1 += MM[0]

	c_t1_t41 = S.Task('c_t1_t41', length=3, delay_cost=1)
	S += c_t1_t41 >= 82
	c_t1_t41 += MAS[2]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 82
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 82
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 82
	c_t5_t11_in += MAS_in[2]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 82
	c_t5_t11_mem0 += MM_MEM[0]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 82
	c_t5_t11_mem1 += MAS_MEM[3]

	d_t0_t2_t4 = S.Task('d_t0_t2_t4', length=4, delay_cost=1)
	S += d_t0_t2_t4 >= 82
	d_t0_t2_t4 += MM[0]

	d_t1_t51 = S.Task('d_t1_t51', length=3, delay_cost=1)
	S += d_t1_t51 >= 82
	d_t1_t51 += MAS[0]

	d_t2_t2_t4_in = S.Task('d_t2_t2_t4_in', length=1, delay_cost=1)
	S += d_t2_t2_t4_in >= 82
	d_t2_t2_t4_in += MM_in[0]

	d_t2_t2_t4_mem0 = S.Task('d_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem0 >= 82
	d_t2_t2_t4_mem0 += MAS_MEM[6]

	d_t2_t2_t4_mem1 = S.Task('d_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem1 >= 82
	d_t2_t2_t4_mem1 += MAS_MEM[1]

	d_t4_t41_in = S.Task('d_t4_t41_in', length=1, delay_cost=1)
	S += d_t4_t41_in >= 82
	d_t4_t41_in += MAS_in[1]

	d_t4_t41_mem0 = S.Task('d_t4_t41_mem0', length=1, delay_cost=1)
	S += d_t4_t41_mem0 >= 82
	d_t4_t41_mem0 += MAS_MEM[2]

	d_t4_t41_mem1 = S.Task('d_t4_t41_mem1', length=1, delay_cost=1)
	S += d_t4_t41_mem1 >= 82
	d_t4_t41_mem1 += MAS_MEM[5]

	c_t011_in = S.Task('c_t011_in', length=1, delay_cost=1)
	S += c_t011_in >= 83
	c_t011_in += MAS_in[2]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 83
	c_t011_mem0 += MAS_MEM[6]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 83
	c_t011_mem1 += MAS_MEM[7]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 83
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 83
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t5_t11 = S.Task('c_t5_t11', length=3, delay_cost=1)
	S += c_t5_t11 >= 83
	c_t5_t11 += MAS[2]

	c_t5_t4_t5_in = S.Task('c_t5_t4_t5_in', length=1, delay_cost=1)
	S += c_t5_t4_t5_in >= 83
	c_t5_t4_t5_in += MAS_in[1]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem0 >= 83
	c_t5_t4_t5_mem0 += MM_MEM[0]

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem1 >= 83
	c_t5_t4_t5_mem1 += MM_MEM[1]

	d_s2011_in = S.Task('d_s2011_in', length=1, delay_cost=1)
	S += d_s2011_in >= 83
	d_s2011_in += MAS_in[3]

	d_s2011_mem0 = S.Task('d_s2011_mem0', length=1, delay_cost=1)
	S += d_s2011_mem0 >= 83
	d_s2011_mem0 += MAS_MEM[2]

	d_s2011_mem1 = S.Task('d_s2011_mem1', length=1, delay_cost=1)
	S += d_s2011_mem1 >= 83
	d_s2011_mem1 += MAS_MEM[1]

	d_t2_t2_t4 = S.Task('d_t2_t2_t4', length=4, delay_cost=1)
	S += d_t2_t2_t4 >= 83
	d_t2_t2_t4 += MM[0]

	d_t3_t2_t0_in = S.Task('d_t3_t2_t0_in', length=1, delay_cost=1)
	S += d_t3_t2_t0_in >= 83
	d_t3_t2_t0_in += MM_in[0]

	d_t3_t2_t0_mem0 = S.Task('d_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem0 >= 83
	d_t3_t2_t0_mem0 += MAS_MEM[0]

	d_t3_t2_t0_mem1 = S.Task('d_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem1 >= 83
	d_t3_t2_t0_mem1 += MAS_MEM[5]

	d_t4_t41 = S.Task('d_t4_t41', length=3, delay_cost=1)
	S += d_t4_t41 >= 83
	d_t4_t41 += MAS[1]

	c_t011 = S.Task('c_t011', length=3, delay_cost=1)
	S += c_t011 >= 84
	c_t011 += MAS[2]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 84
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 84
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	S += c_t4_t01_in >= 84
	c_t4_t01_in += MAS_in[2]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 84
	c_t4_t01_mem0 += MM_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 84
	c_t4_t01_mem1 += MAS_MEM[5]

	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	S += c_t5_t4_t4_in >= 84
	c_t5_t4_t4_in += MM_in[0]

	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem0 >= 84
	c_t5_t4_t4_mem0 += MAS_MEM[2]

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem1 >= 84
	c_t5_t4_t4_mem1 += MAS_MEM[3]

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=3, delay_cost=1)
	S += c_t5_t4_t5 >= 84
	c_t5_t4_t5 += MAS[1]

	d_s2011 = S.Task('d_s2011', length=3, delay_cost=1)
	S += d_s2011 >= 84
	d_s2011 += MAS[3]

	d_t3_t2_t0 = S.Task('d_t3_t2_t0', length=4, delay_cost=1)
	S += d_t3_t2_t0 >= 84
	d_t3_t2_t0 += MM[0]

	d_t3_t41_in = S.Task('d_t3_t41_in', length=1, delay_cost=1)
	S += d_t3_t41_in >= 84
	d_t3_t41_in += MAS_in[1]

	d_t3_t41_mem0 = S.Task('d_t3_t41_mem0', length=1, delay_cost=1)
	S += d_t3_t41_mem0 >= 84
	d_t3_t41_mem0 += MAS_MEM[6]

	d_t3_t41_mem1 = S.Task('d_t3_t41_mem1', length=1, delay_cost=1)
	S += d_t3_t41_mem1 >= 84
	d_t3_t41_mem1 += MAS_MEM[7]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 85
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 85
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	S += c_t3_t4_t4_in >= 85
	c_t3_t4_t4_in += MM_in[0]

	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem0 >= 85
	c_t3_t4_t4_mem0 += MAS_MEM[6]

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem1 >= 85
	c_t3_t4_t4_mem1 += MAS_MEM[5]

	c_t4_t01 = S.Task('c_t4_t01', length=3, delay_cost=1)
	S += c_t4_t01 >= 85
	c_t4_t01 += MAS[2]

	c_t4_t4_t5_in = S.Task('c_t4_t4_t5_in', length=1, delay_cost=1)
	S += c_t4_t4_t5_in >= 85
	c_t4_t4_t5_in += MAS_in[0]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem0 >= 85
	c_t4_t4_t5_mem0 += MM_MEM[0]

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem1 >= 85
	c_t4_t4_t5_mem1 += MM_MEM[1]

	c_t5_s01_in = S.Task('c_t5_s01_in', length=1, delay_cost=1)
	S += c_t5_s01_in >= 85
	c_t5_s01_in += MAS_in[1]

	c_t5_s01_mem0 = S.Task('c_t5_s01_mem0', length=1, delay_cost=1)
	S += c_t5_s01_mem0 >= 85
	c_t5_s01_mem0 += MAS_MEM[4]

	c_t5_s01_mem1 = S.Task('c_t5_s01_mem1', length=1, delay_cost=1)
	S += c_t5_s01_mem1 >= 85
	c_t5_s01_mem1 += MAS_MEM[7]

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=4, delay_cost=1)
	S += c_t5_t4_t4 >= 85
	c_t5_t4_t4 += MM[0]

	d_t3_t41 = S.Task('d_t3_t41', length=3, delay_cost=1)
	S += d_t3_t41 >= 85
	d_t3_t41 += MAS[1]

	d_t411_in = S.Task('d_t411_in', length=1, delay_cost=1)
	S += d_t411_in >= 85
	d_t411_in += MAS_in[2]

	d_t411_mem0 = S.Task('d_t411_mem0', length=1, delay_cost=1)
	S += d_t411_mem0 >= 85
	d_t411_mem0 += MAS_MEM[2]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 86
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=4, delay_cost=1)
	S += c_t3_t4_t4 >= 86
	c_t3_t4_t4 += MM[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 86
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	S += c_t4_t40_in >= 86
	c_t4_t40_in += MAS_in[0]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 86
	c_t4_t40_mem0 += MM_MEM[0]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 86
	c_t4_t40_mem1 += MM_MEM[1]

	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	S += c_t4_t4_t4_in >= 86
	c_t4_t4_t4_in += MM_in[0]

	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem0 >= 86
	c_t4_t4_t4_mem0 += MAS_MEM[0]

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem1 >= 86
	c_t4_t4_t4_mem1 += MAS_MEM[5]

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=3, delay_cost=1)
	S += c_t4_t4_t5 >= 86
	c_t4_t4_t5 += MAS[0]

	c_t5_s01 = S.Task('c_t5_s01', length=3, delay_cost=1)
	S += c_t5_s01 >= 86
	c_t5_s01 += MAS[1]

	d_t3_t40_in = S.Task('d_t3_t40_in', length=1, delay_cost=1)
	S += d_t3_t40_in >= 86
	d_t3_t40_in += MAS_in[1]

	d_t3_t40_mem0 = S.Task('d_t3_t40_mem0', length=1, delay_cost=1)
	S += d_t3_t40_mem0 >= 86
	d_t3_t40_mem0 += MAS_MEM[6]

	d_t3_t40_mem1 = S.Task('d_t3_t40_mem1', length=1, delay_cost=1)
	S += d_t3_t40_mem1 >= 86
	d_t3_t40_mem1 += MAS_MEM[7]

	d_t411 = S.Task('d_t411', length=3, delay_cost=1)
	S += d_t411 >= 86
	d_t411 += MAS[2]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 87
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 87
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4_t40 = S.Task('c_t4_t40', length=3, delay_cost=1)
	S += c_t4_t40 >= 87
	c_t4_t40 += MAS[0]

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=4, delay_cost=1)
	S += c_t4_t4_t4 >= 87
	c_t4_t4_t4 += MM[0]

	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	S += c_t5_t01_in >= 87
	c_t5_t01_in += MAS_in[2]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 87
	c_t5_t01_mem0 += MM_MEM[0]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 87
	c_t5_t01_mem1 += MAS_MEM[5]

	d_t311_in = S.Task('d_t311_in', length=1, delay_cost=1)
	S += d_t311_in >= 87
	d_t311_in += MAS_in[0]

	d_t311_mem0 = S.Task('d_t311_mem0', length=1, delay_cost=1)
	S += d_t311_mem0 >= 87
	d_t311_mem0 += MAS_MEM[6]

	d_t3_t40 = S.Task('d_t3_t40', length=3, delay_cost=1)
	S += d_t3_t40 >= 87
	d_t3_t40 += MAS[1]

	d_t4_t2_t4_in = S.Task('d_t4_t2_t4_in', length=1, delay_cost=1)
	S += d_t4_t2_t4_in >= 87
	d_t4_t2_t4_in += MM_in[0]

	d_t4_t2_t4_mem0 = S.Task('d_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem0 >= 87
	d_t4_t2_t4_mem0 += MAS_MEM[4]

	d_t4_t2_t4_mem1 = S.Task('d_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem1 >= 87
	d_t4_t2_t4_mem1 += MAS_MEM[7]

	c_t111_in = S.Task('c_t111_in', length=1, delay_cost=1)
	S += c_t111_in >= 88
	c_t111_in += MAS_in[2]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 88
	c_t111_mem0 += MAS_MEM[4]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 88
	c_t111_mem1 += MAS_MEM[5]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 88
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 88
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t5_in = S.Task('c_t3_t4_t5_in', length=1, delay_cost=1)
	S += c_t3_t4_t5_in >= 88
	c_t3_t4_t5_in += MAS_in[0]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem0 >= 88
	c_t3_t4_t5_mem0 += MM_MEM[0]

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem1 >= 88
	c_t3_t4_t5_mem1 += MM_MEM[1]

	c_t5_t01 = S.Task('c_t5_t01', length=3, delay_cost=1)
	S += c_t5_t01 >= 88
	c_t5_t01 += MAS[2]

	d_t311 = S.Task('d_t311', length=3, delay_cost=1)
	S += d_t311 >= 88
	d_t311 += MAS[0]

	d_t3_t2_t4_in = S.Task('d_t3_t2_t4_in', length=1, delay_cost=1)
	S += d_t3_t2_t4_in >= 88
	d_t3_t2_t4_in += MM_in[0]

	d_t3_t2_t4_mem0 = S.Task('d_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem0 >= 88
	d_t3_t2_t4_mem0 += MAS_MEM[6]

	d_t3_t2_t4_mem1 = S.Task('d_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem1 >= 88
	d_t3_t2_t4_mem1 += MAS_MEM[7]

	d_t4_t2_t4 = S.Task('d_t4_t2_t4', length=4, delay_cost=1)
	S += d_t4_t2_t4 >= 88
	d_t4_t2_t4 += MM[0]

	c_t111 = S.Task('c_t111', length=3, delay_cost=1)
	S += c_t111 >= 89
	c_t111 += MAS[2]

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=3, delay_cost=1)
	S += c_t3_t4_t5 >= 89
	c_t3_t4_t5 += MAS[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 89
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 89
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t410_in = S.Task('c_t410_in', length=1, delay_cost=1)
	S += c_t410_in >= 89
	c_t410_in += MAS_in[0]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 89
	c_t410_mem0 += MAS_MEM[0]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 89
	c_t410_mem1 += MAS_MEM[7]

	c_t5_s00_in = S.Task('c_t5_s00_in', length=1, delay_cost=1)
	S += c_t5_s00_in >= 89
	c_t5_s00_in += MAS_in[2]

	c_t5_s00_mem0 = S.Task('c_t5_s00_mem0', length=1, delay_cost=1)
	S += c_t5_s00_mem0 >= 89
	c_t5_s00_mem0 += MAS_MEM[6]

	c_t5_s00_mem1 = S.Task('c_t5_s00_mem1', length=1, delay_cost=1)
	S += c_t5_s00_mem1 >= 89
	c_t5_s00_mem1 += MAS_MEM[5]

	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	S += c_t5_t40_in >= 89
	c_t5_t40_in += MAS_in[1]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 89
	c_t5_t40_mem0 += MM_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 89
	c_t5_t40_mem1 += MM_MEM[1]

	d_t3_t2_t4 = S.Task('d_t3_t2_t4', length=4, delay_cost=1)
	S += d_t3_t2_t4 >= 89
	d_t3_t2_t4 += MM[0]

	d_t5_t2_t4_in = S.Task('d_t5_t2_t4_in', length=1, delay_cost=1)
	S += d_t5_t2_t4_in >= 89
	d_t5_t2_t4_in += MM_in[0]

	d_t5_t2_t4_mem0 = S.Task('d_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem0 >= 89
	d_t5_t2_t4_mem0 += MAS_MEM[2]

	d_t5_t2_t4_mem1 = S.Task('d_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem1 >= 89
	d_t5_t2_t4_mem1 += MAS_MEM[1]

	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	S += c_t3_t40_in >= 90
	c_t3_t40_in += MAS_in[2]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 90
	c_t3_t40_mem0 += MM_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 90
	c_t3_t40_mem1 += MM_MEM[1]

	c_t410 = S.Task('c_t410', length=3, delay_cost=1)
	S += c_t410 >= 90
	c_t410 += MAS[0]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 90
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 90
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5_s00 = S.Task('c_t5_s00', length=3, delay_cost=1)
	S += c_t5_s00 >= 90
	c_t5_s00 += MAS[2]

	c_t5_t40 = S.Task('c_t5_t40', length=3, delay_cost=1)
	S += c_t5_t40 >= 90
	c_t5_t40 += MAS[1]

	c_t5_t51_in = S.Task('c_t5_t51_in', length=1, delay_cost=1)
	S += c_t5_t51_in >= 90
	c_t5_t51_in += MAS_in[1]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 90
	c_t5_t51_mem0 += MAS_MEM[4]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 90
	c_t5_t51_mem1 += MAS_MEM[5]

	d_t5_t2_t4 = S.Task('d_t5_t2_t4', length=4, delay_cost=1)
	S += d_t5_t2_t4 >= 90
	d_t5_t2_t4 += MM[0]

	c_t3_t40 = S.Task('c_t3_t40', length=3, delay_cost=1)
	S += c_t3_t40 >= 91
	c_t3_t40 += MAS[2]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 91
	c_t4_t11_in += MAS_in[2]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 91
	c_t4_t11_mem0 += MM_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 91
	c_t4_t11_mem1 += MAS_MEM[1]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 91
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 91
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t51 = S.Task('c_t5_t51', length=3, delay_cost=1)
	S += c_t5_t51 >= 91
	c_t5_t51 += MAS[1]

	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	S += c_t3_t01_in >= 92
	c_t3_t01_in += MAS_in[2]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 92
	c_t3_t01_mem0 += MM_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 92
	c_t3_t01_mem1 += MAS_MEM[5]

	c_t4_t11 = S.Task('c_t4_t11', length=3, delay_cost=1)
	S += c_t4_t11 >= 92
	c_t4_t11 += MAS[2]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 92
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 92
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t510_in = S.Task('c_t510_in', length=1, delay_cost=1)
	S += c_t510_in >= 92
	c_t510_in += MAS_in[0]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 92
	c_t510_mem0 += MAS_MEM[2]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 92
	c_t510_mem1 += MAS_MEM[3]

	c_t3_t01 = S.Task('c_t3_t01', length=3, delay_cost=1)
	S += c_t3_t01 >= 93
	c_t3_t01 += MAS[2]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 93
	c_t3_t11_in += MAS_in[2]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 93
	c_t3_t11_mem0 += MM_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 93
	c_t3_t11_mem1 += MAS_MEM[5]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 93
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 93
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t510 = S.Task('c_t510', length=3, delay_cost=1)
	S += c_t510 >= 93
	c_t510 += MAS[0]

	c_t310_in = S.Task('c_t310_in', length=1, delay_cost=1)
	S += c_t310_in >= 94
	c_t310_in += MAS_in[2]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 94
	c_t310_mem0 += MAS_MEM[4]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 94
	c_t310_mem1 += MAS_MEM[5]

	c_t3_t11 = S.Task('c_t3_t11', length=3, delay_cost=1)
	S += c_t3_t11 >= 94
	c_t3_t11 += MAS[2]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 94
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 94
	c_t5110_mem1 += MAIN_MEM_r[1]

	d_t3_t20_in = S.Task('d_t3_t20_in', length=1, delay_cost=1)
	S += d_t3_t20_in >= 94
	d_t3_t20_in += MAS_in[0]

	d_t3_t20_mem0 = S.Task('d_t3_t20_mem0', length=1, delay_cost=1)
	S += d_t3_t20_mem0 >= 94
	d_t3_t20_mem0 += MM_MEM[0]

	d_t3_t20_mem1 = S.Task('d_t3_t20_mem1', length=1, delay_cost=1)
	S += d_t3_t20_mem1 >= 94
	d_t3_t20_mem1 += MM_MEM[1]

	c_t310 = S.Task('c_t310', length=3, delay_cost=1)
	S += c_t310 >= 95
	c_t310 += MAS[2]

	c_t4_t51_in = S.Task('c_t4_t51_in', length=1, delay_cost=1)
	S += c_t4_t51_in >= 95
	c_t4_t51_in += MAS_in[1]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 95
	c_t4_t51_mem0 += MAS_MEM[4]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 95
	c_t4_t51_mem1 += MAS_MEM[5]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 95
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 95
	c_t5010_mem1 += MAIN_MEM_r[1]

	d_t3_t20 = S.Task('d_t3_t20', length=3, delay_cost=1)
	S += d_t3_t20 >= 95
	d_t3_t20 += MAS[0]

	d_t5_t20_in = S.Task('d_t5_t20_in', length=1, delay_cost=1)
	S += d_t5_t20_in >= 95
	d_t5_t20_in += MAS_in[2]

	d_t5_t20_mem0 = S.Task('d_t5_t20_mem0', length=1, delay_cost=1)
	S += d_t5_t20_mem0 >= 95
	d_t5_t20_mem0 += MM_MEM[0]

	d_t5_t20_mem1 = S.Task('d_t5_t20_mem1', length=1, delay_cost=1)
	S += d_t5_t20_mem1 >= 95
	d_t5_t20_mem1 += MM_MEM[1]

	c_t3_s01_in = S.Task('c_t3_s01_in', length=1, delay_cost=1)
	S += c_t3_s01_in >= 96
	c_t3_s01_in += MAS_in[1]

	c_t3_s01_mem0 = S.Task('c_t3_s01_mem0', length=1, delay_cost=1)
	S += c_t3_s01_mem0 >= 96
	c_t3_s01_mem0 += MAS_MEM[4]

	c_t3_s01_mem1 = S.Task('c_t3_s01_mem1', length=1, delay_cost=1)
	S += c_t3_s01_mem1 >= 96
	c_t3_s01_mem1 += MAS_MEM[5]

	c_t4_t51 = S.Task('c_t4_t51', length=3, delay_cost=1)
	S += c_t4_t51 >= 96
	c_t4_t51 += MAS[1]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 96
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t4_t2_t5_in = S.Task('d_t4_t2_t5_in', length=1, delay_cost=1)
	S += d_t4_t2_t5_in >= 96
	d_t4_t2_t5_in += MAS_in[0]

	d_t4_t2_t5_mem0 = S.Task('d_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem0 >= 96
	d_t4_t2_t5_mem0 += MM_MEM[0]

	d_t4_t2_t5_mem1 = S.Task('d_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem1 >= 96
	d_t4_t2_t5_mem1 += MM_MEM[1]

	d_t5_t20 = S.Task('d_t5_t20', length=3, delay_cost=1)
	S += d_t5_t20 >= 96
	d_t5_t20 += MAS[2]

	c_t3_s01 = S.Task('c_t3_s01', length=3, delay_cost=1)
	S += c_t3_s01 >= 97
	c_t3_s01 += MAS[1]

	c_t3_t51_in = S.Task('c_t3_t51_in', length=1, delay_cost=1)
	S += c_t3_t51_in >= 97
	c_t3_t51_in += MAS_in[2]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 97
	c_t3_t51_mem0 += MAS_MEM[4]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 97
	c_t3_t51_mem1 += MAS_MEM[5]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 97
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t3_t2_t5_in = S.Task('d_t3_t2_t5_in', length=1, delay_cost=1)
	S += d_t3_t2_t5_in >= 97
	d_t3_t2_t5_in += MAS_in[1]

	d_t3_t2_t5_mem0 = S.Task('d_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem0 >= 97
	d_t3_t2_t5_mem0 += MM_MEM[0]

	d_t3_t2_t5_mem1 = S.Task('d_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem1 >= 97
	d_t3_t2_t5_mem1 += MM_MEM[1]

	d_t4_t2_t5 = S.Task('d_t4_t2_t5', length=3, delay_cost=1)
	S += d_t4_t2_t5 >= 97
	d_t4_t2_t5 += MAS[0]

	c_t3_s00_in = S.Task('c_t3_s00_in', length=1, delay_cost=1)
	S += c_t3_s00_in >= 98
	c_t3_s00_in += MAS_in[2]

	c_t3_s00_mem0 = S.Task('c_t3_s00_mem0', length=1, delay_cost=1)
	S += c_t3_s00_mem0 >= 98
	c_t3_s00_mem0 += MAS_MEM[4]

	c_t3_s00_mem1 = S.Task('c_t3_s00_mem1', length=1, delay_cost=1)
	S += c_t3_s00_mem1 >= 98
	c_t3_s00_mem1 += MAS_MEM[5]

	c_t3_t41_in = S.Task('c_t3_t41_in', length=1, delay_cost=1)
	S += c_t3_t41_in >= 98
	c_t3_t41_in += MAS_in[3]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 98
	c_t3_t41_mem0 += MM_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 98
	c_t3_t41_mem1 += MAS_MEM[1]

	c_t3_t51 = S.Task('c_t3_t51', length=3, delay_cost=1)
	S += c_t3_t51 >= 98
	c_t3_t51 += MAS[2]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 98
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t3_t2_t5 = S.Task('d_t3_t2_t5', length=3, delay_cost=1)
	S += d_t3_t2_t5 >= 98
	d_t3_t2_t5 += MAS[1]

	c_t3_s00 = S.Task('c_t3_s00', length=3, delay_cost=1)
	S += c_t3_s00 >= 99
	c_t3_s00 += MAS[2]

	c_t3_t41 = S.Task('c_t3_t41', length=3, delay_cost=1)
	S += c_t3_t41 >= 99
	c_t3_t41 += MAS[3]

	c_t4_s00_in = S.Task('c_t4_s00_in', length=1, delay_cost=1)
	S += c_t4_s00_in >= 99
	c_t4_s00_in += MAS_in[3]

	c_t4_s00_mem0 = S.Task('c_t4_s00_mem0', length=1, delay_cost=1)
	S += c_t4_s00_mem0 >= 99
	c_t4_s00_mem0 += MAS_MEM[4]

	c_t4_s00_mem1 = S.Task('c_t4_s00_mem1', length=1, delay_cost=1)
	S += c_t4_s00_mem1 >= 99
	c_t4_s00_mem1 += MAS_MEM[5]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 99
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t4_t20_in = S.Task('d_t4_t20_in', length=1, delay_cost=1)
	S += d_t4_t20_in >= 99
	d_t4_t20_in += MAS_in[0]

	d_t4_t20_mem0 = S.Task('d_t4_t20_mem0', length=1, delay_cost=1)
	S += d_t4_t20_mem0 >= 99
	d_t4_t20_mem0 += MM_MEM[0]

	d_t4_t20_mem1 = S.Task('d_t4_t20_mem1', length=1, delay_cost=1)
	S += d_t4_t20_mem1 >= 99
	d_t4_t20_mem1 += MM_MEM[1]

	c_t4_s00 = S.Task('c_t4_s00', length=3, delay_cost=1)
	S += c_t4_s00 >= 100
	c_t4_s00 += MAS[3]

	c_t4_s01_in = S.Task('c_t4_s01_in', length=1, delay_cost=1)
	S += c_t4_s01_in >= 100
	c_t4_s01_in += MAS_in[1]

	c_t4_s01_mem0 = S.Task('c_t4_s01_mem0', length=1, delay_cost=1)
	S += c_t4_s01_mem0 >= 100
	c_t4_s01_mem0 += MAS_MEM[4]

	c_t4_s01_mem1 = S.Task('c_t4_s01_mem1', length=1, delay_cost=1)
	S += c_t4_s01_mem1 >= 100
	c_t4_s01_mem1 += MAS_MEM[5]

	d_t1_t21_in = S.Task('d_t1_t21_in', length=1, delay_cost=1)
	S += d_t1_t21_in >= 100
	d_t1_t21_in += MAS_in[3]

	d_t1_t21_mem0 = S.Task('d_t1_t21_mem0', length=1, delay_cost=1)
	S += d_t1_t21_mem0 >= 100
	d_t1_t21_mem0 += MM_MEM[0]

	d_t1_t21_mem1 = S.Task('d_t1_t21_mem1', length=1, delay_cost=1)
	S += d_t1_t21_mem1 >= 100
	d_t1_t21_mem1 += MAS_MEM[1]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 100
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t4_t20 = S.Task('d_t4_t20', length=3, delay_cost=1)
	S += d_t4_t20 >= 100
	d_t4_t20 += MAS[0]

	c_t4_s01 = S.Task('c_t4_s01', length=3, delay_cost=1)
	S += c_t4_s01 >= 101
	c_t4_s01 += MAS[1]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 101
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t0_t21_in = S.Task('d_t0_t21_in', length=1, delay_cost=1)
	S += d_t0_t21_in >= 101
	d_t0_t21_in += MAS_in[3]

	d_t0_t21_mem0 = S.Task('d_t0_t21_mem0', length=1, delay_cost=1)
	S += d_t0_t21_mem0 >= 101
	d_t0_t21_mem0 += MM_MEM[0]

	d_t0_t21_mem1 = S.Task('d_t0_t21_mem1', length=1, delay_cost=1)
	S += d_t0_t21_mem1 >= 101
	d_t0_t21_mem1 += MAS_MEM[5]

	d_t1_t21 = S.Task('d_t1_t21', length=3, delay_cost=1)
	S += d_t1_t21 >= 101
	d_t1_t21 += MAS[3]

	d_t0_t21 = S.Task('d_t0_t21', length=3, delay_cost=1)
	S += d_t0_t21 >= 102
	d_t0_t21 += MAS[3]

	d_t5_t2_t5_in = S.Task('d_t5_t2_t5_in', length=1, delay_cost=1)
	S += d_t5_t2_t5_in >= 102
	d_t5_t2_t5_in += MAS_in[0]

	d_t5_t2_t5_mem0 = S.Task('d_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem0 >= 102
	d_t5_t2_t5_mem0 += MM_MEM[0]

	d_t5_t2_t5_mem1 = S.Task('d_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem1 >= 102
	d_t5_t2_t5_mem1 += MM_MEM[1]

	d_t2_t21_in = S.Task('d_t2_t21_in', length=1, delay_cost=1)
	S += d_t2_t21_in >= 103
	d_t2_t21_in += MAS_in[1]

	d_t2_t21_mem0 = S.Task('d_t2_t21_mem0', length=1, delay_cost=1)
	S += d_t2_t21_mem0 >= 103
	d_t2_t21_mem0 += MM_MEM[0]

	d_t2_t21_mem1 = S.Task('d_t2_t21_mem1', length=1, delay_cost=1)
	S += d_t2_t21_mem1 >= 103
	d_t2_t21_mem1 += MAS_MEM[3]

	d_t5_t2_t5 = S.Task('d_t5_t2_t5', length=3, delay_cost=1)
	S += d_t5_t2_t5 >= 103
	d_t5_t2_t5 += MAS[0]

	c_t4_t41_in = S.Task('c_t4_t41_in', length=1, delay_cost=1)
	S += c_t4_t41_in >= 104
	c_t4_t41_in += MAS_in[1]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 104
	c_t4_t41_mem0 += MM_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 104
	c_t4_t41_mem1 += MAS_MEM[1]

	d_t2_t21 = S.Task('d_t2_t21', length=3, delay_cost=1)
	S += d_t2_t21 >= 104
	d_t2_t21 += MAS[1]

	c_t4_t41 = S.Task('c_t4_t41', length=3, delay_cost=1)
	S += c_t4_t41 >= 105
	c_t4_t41 += MAS[1]

	c_t5_t41_in = S.Task('c_t5_t41_in', length=1, delay_cost=1)
	S += c_t5_t41_in >= 105
	c_t5_t41_in += MAS_in[3]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 105
	c_t5_t41_mem0 += MM_MEM[0]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 105
	c_t5_t41_mem1 += MAS_MEM[3]

	c_t5_t41 = S.Task('c_t5_t41', length=3, delay_cost=1)
	S += c_t5_t41 >= 106
	c_t5_t41 += MAS[3]


	# new tasks
	d_t000 = S.Task('d_t000', length=3, delay_cost=1)
	d_t000 += alt(MAS)
	d_t000_in = S.Task('d_t000_in', length=1, delay_cost=1)
	d_t000_in += alt(MAS_in)
	S += d_t000_in*MAS_in[0]<=d_t000*MAS[0]

	S += d_t000_in*MAS_in[1]<=d_t000*MAS[1]

	S += d_t000_in*MAS_in[2]<=d_t000*MAS[2]

	S += d_t000_in*MAS_in[3]<=d_t000*MAS[3]

	d_t000_mem0 = S.Task('d_t000_mem0', length=1, delay_cost=1)
	d_t000_mem0 += MAS_MEM[0]
	S += 75 < d_t000_mem0
	S += d_t000_mem0 <= d_t000

	d_t000_mem1 = S.Task('d_t000_mem1', length=1, delay_cost=1)
	d_t000_mem1 += MAS_MEM[1]
	S += 68 < d_t000_mem1
	S += d_t000_mem1 <= d_t000

	d_t001 = S.Task('d_t001', length=3, delay_cost=1)
	d_t001 += alt(MAS)
	d_t001_in = S.Task('d_t001_in', length=1, delay_cost=1)
	d_t001_in += alt(MAS_in)
	S += d_t001_in*MAS_in[0]<=d_t001*MAS[0]

	S += d_t001_in*MAS_in[1]<=d_t001*MAS[1]

	S += d_t001_in*MAS_in[2]<=d_t001*MAS[2]

	S += d_t001_in*MAS_in[3]<=d_t001*MAS[3]

	d_t001_mem0 = S.Task('d_t001_mem0', length=1, delay_cost=1)
	d_t001_mem0 += MAS_MEM[6]
	S += 104 < d_t001_mem0
	S += d_t001_mem0 <= d_t001

	d_t001_mem1 = S.Task('d_t001_mem1', length=1, delay_cost=1)
	d_t001_mem1 += MAS_MEM[1]
	S += 67 < d_t001_mem1
	S += d_t001_mem1 <= d_t001

	d_t100 = S.Task('d_t100', length=3, delay_cost=1)
	d_t100 += alt(MAS)
	d_t100_in = S.Task('d_t100_in', length=1, delay_cost=1)
	d_t100_in += alt(MAS_in)
	S += d_t100_in*MAS_in[0]<=d_t100*MAS[0]

	S += d_t100_in*MAS_in[1]<=d_t100*MAS[1]

	S += d_t100_in*MAS_in[2]<=d_t100*MAS[2]

	S += d_t100_in*MAS_in[3]<=d_t100*MAS[3]

	d_t100_mem0 = S.Task('d_t100_mem0', length=1, delay_cost=1)
	d_t100_mem0 += MAS_MEM[2]
	S += 77 < d_t100_mem0
	S += d_t100_mem0 <= d_t100

	d_t100_mem1 = S.Task('d_t100_mem1', length=1, delay_cost=1)
	d_t100_mem1 += MAS_MEM[7]
	S += 75 < d_t100_mem1
	S += d_t100_mem1 <= d_t100

	d_t101 = S.Task('d_t101', length=3, delay_cost=1)
	d_t101 += alt(MAS)
	d_t101_in = S.Task('d_t101_in', length=1, delay_cost=1)
	d_t101_in += alt(MAS_in)
	S += d_t101_in*MAS_in[0]<=d_t101*MAS[0]

	S += d_t101_in*MAS_in[1]<=d_t101*MAS[1]

	S += d_t101_in*MAS_in[2]<=d_t101*MAS[2]

	S += d_t101_in*MAS_in[3]<=d_t101*MAS[3]

	d_t101_mem0 = S.Task('d_t101_mem0', length=1, delay_cost=1)
	d_t101_mem0 += MAS_MEM[6]
	S += 103 < d_t101_mem0
	S += d_t101_mem0 <= d_t101

	d_t101_mem1 = S.Task('d_t101_mem1', length=1, delay_cost=1)
	d_t101_mem1 += MAS_MEM[1]
	S += 84 < d_t101_mem1
	S += d_t101_mem1 <= d_t101

	d_t200 = S.Task('d_t200', length=3, delay_cost=1)
	d_t200 += alt(MAS)
	d_t200_in = S.Task('d_t200_in', length=1, delay_cost=1)
	d_t200_in += alt(MAS_in)
	S += d_t200_in*MAS_in[0]<=d_t200*MAS[0]

	S += d_t200_in*MAS_in[1]<=d_t200*MAS[1]

	S += d_t200_in*MAS_in[2]<=d_t200*MAS[2]

	S += d_t200_in*MAS_in[3]<=d_t200*MAS[3]

	d_t200_mem0 = S.Task('d_t200_mem0', length=1, delay_cost=1)
	d_t200_mem0 += MAS_MEM[2]
	S += 74 < d_t200_mem0
	S += d_t200_mem0 <= d_t200

	d_t200_mem1 = S.Task('d_t200_mem1', length=1, delay_cost=1)
	d_t200_mem1 += MAS_MEM[7]
	S += 71 < d_t200_mem1
	S += d_t200_mem1 <= d_t200

	d_t201 = S.Task('d_t201', length=3, delay_cost=1)
	d_t201 += alt(MAS)
	d_t201_in = S.Task('d_t201_in', length=1, delay_cost=1)
	d_t201_in += alt(MAS_in)
	S += d_t201_in*MAS_in[0]<=d_t201*MAS[0]

	S += d_t201_in*MAS_in[1]<=d_t201*MAS[1]

	S += d_t201_in*MAS_in[2]<=d_t201*MAS[2]

	S += d_t201_in*MAS_in[3]<=d_t201*MAS[3]

	d_t201_mem0 = S.Task('d_t201_mem0', length=1, delay_cost=1)
	d_t201_mem0 += MAS_MEM[2]
	S += 106 < d_t201_mem0
	S += d_t201_mem0 <= d_t201

	d_t201_mem1 = S.Task('d_t201_mem1', length=1, delay_cost=1)
	d_t201_mem1 += MAS_MEM[3]
	S += 70 < d_t201_mem1
	S += d_t201_mem1 <= d_t201

	d_t3_t21 = S.Task('d_t3_t21', length=3, delay_cost=1)
	d_t3_t21 += alt(MAS)
	d_t3_t21_in = S.Task('d_t3_t21_in', length=1, delay_cost=1)
	d_t3_t21_in += alt(MAS_in)
	S += d_t3_t21_in*MAS_in[0]<=d_t3_t21*MAS[0]

	S += d_t3_t21_in*MAS_in[1]<=d_t3_t21*MAS[1]

	S += d_t3_t21_in*MAS_in[2]<=d_t3_t21*MAS[2]

	S += d_t3_t21_in*MAS_in[3]<=d_t3_t21*MAS[3]

	d_t3_t21_mem0 = S.Task('d_t3_t21_mem0', length=1, delay_cost=1)
	d_t3_t21_mem0 += MM_MEM[0]
	S += 92 < d_t3_t21_mem0
	S += d_t3_t21_mem0 <= d_t3_t21

	d_t3_t21_mem1 = S.Task('d_t3_t21_mem1', length=1, delay_cost=1)
	d_t3_t21_mem1 += MAS_MEM[3]
	S += 100 < d_t3_t21_mem1
	S += d_t3_t21_mem1 <= d_t3_t21

	d_t3_t50 = S.Task('d_t3_t50', length=3, delay_cost=1)
	d_t3_t50 += alt(MAS)
	d_t3_t50_in = S.Task('d_t3_t50_in', length=1, delay_cost=1)
	d_t3_t50_in += alt(MAS_in)
	S += d_t3_t50_in*MAS_in[0]<=d_t3_t50*MAS[0]

	S += d_t3_t50_in*MAS_in[1]<=d_t3_t50*MAS[1]

	S += d_t3_t50_in*MAS_in[2]<=d_t3_t50*MAS[2]

	S += d_t3_t50_in*MAS_in[3]<=d_t3_t50*MAS[3]

	d_t3_t50_mem0 = S.Task('d_t3_t50_mem0', length=1, delay_cost=1)
	d_t3_t50_mem0 += MAS_MEM[6]
	S += 45 < d_t3_t50_mem0
	S += d_t3_t50_mem0 <= d_t3_t50

	d_t3_t50_mem1 = S.Task('d_t3_t50_mem1', length=1, delay_cost=1)
	d_t3_t50_mem1 += MAS_MEM[3]
	S += 89 < d_t3_t50_mem1
	S += d_t3_t50_mem1 <= d_t3_t50

	d_t3_t51 = S.Task('d_t3_t51', length=3, delay_cost=1)
	d_t3_t51 += alt(MAS)
	d_t3_t51_in = S.Task('d_t3_t51_in', length=1, delay_cost=1)
	d_t3_t51_in += alt(MAS_in)
	S += d_t3_t51_in*MAS_in[0]<=d_t3_t51*MAS[0]

	S += d_t3_t51_in*MAS_in[1]<=d_t3_t51*MAS[1]

	S += d_t3_t51_in*MAS_in[2]<=d_t3_t51*MAS[2]

	S += d_t3_t51_in*MAS_in[3]<=d_t3_t51*MAS[3]

	d_t3_t51_mem0 = S.Task('d_t3_t51_mem0', length=1, delay_cost=1)
	d_t3_t51_mem0 += MAS_MEM[6]
	S += 82 < d_t3_t51_mem0
	S += d_t3_t51_mem0 <= d_t3_t51

	d_t3_t51_mem1 = S.Task('d_t3_t51_mem1', length=1, delay_cost=1)
	d_t3_t51_mem1 += MAS_MEM[3]
	S += 87 < d_t3_t51_mem1
	S += d_t3_t51_mem1 <= d_t3_t51

	d_t4_t21 = S.Task('d_t4_t21', length=3, delay_cost=1)
	d_t4_t21 += alt(MAS)
	d_t4_t21_in = S.Task('d_t4_t21_in', length=1, delay_cost=1)
	d_t4_t21_in += alt(MAS_in)
	S += d_t4_t21_in*MAS_in[0]<=d_t4_t21*MAS[0]

	S += d_t4_t21_in*MAS_in[1]<=d_t4_t21*MAS[1]

	S += d_t4_t21_in*MAS_in[2]<=d_t4_t21*MAS[2]

	S += d_t4_t21_in*MAS_in[3]<=d_t4_t21*MAS[3]

	d_t4_t21_mem0 = S.Task('d_t4_t21_mem0', length=1, delay_cost=1)
	d_t4_t21_mem0 += MM_MEM[0]
	S += 91 < d_t4_t21_mem0
	S += d_t4_t21_mem0 <= d_t4_t21

	d_t4_t21_mem1 = S.Task('d_t4_t21_mem1', length=1, delay_cost=1)
	d_t4_t21_mem1 += MAS_MEM[1]
	S += 99 < d_t4_t21_mem1
	S += d_t4_t21_mem1 <= d_t4_t21

	d_t4_t50 = S.Task('d_t4_t50', length=3, delay_cost=1)
	d_t4_t50 += alt(MAS)
	d_t4_t50_in = S.Task('d_t4_t50_in', length=1, delay_cost=1)
	d_t4_t50_in += alt(MAS_in)
	S += d_t4_t50_in*MAS_in[0]<=d_t4_t50*MAS[0]

	S += d_t4_t50_in*MAS_in[1]<=d_t4_t50*MAS[1]

	S += d_t4_t50_in*MAS_in[2]<=d_t4_t50*MAS[2]

	S += d_t4_t50_in*MAS_in[3]<=d_t4_t50*MAS[3]

	d_t4_t50_mem0 = S.Task('d_t4_t50_mem0', length=1, delay_cost=1)
	d_t4_t50_mem0 += MAS_MEM[4]
	S += 40 < d_t4_t50_mem0
	S += d_t4_t50_mem0 <= d_t4_t50

	d_t4_t50_mem1 = S.Task('d_t4_t50_mem1', length=1, delay_cost=1)
	d_t4_t50_mem1 += MAS_MEM[3]
	S += 82 < d_t4_t50_mem1
	S += d_t4_t50_mem1 <= d_t4_t50

	d_t4_t51 = S.Task('d_t4_t51', length=3, delay_cost=1)
	d_t4_t51 += alt(MAS)
	d_t4_t51_in = S.Task('d_t4_t51_in', length=1, delay_cost=1)
	d_t4_t51_in += alt(MAS_in)
	S += d_t4_t51_in*MAS_in[0]<=d_t4_t51*MAS[0]

	S += d_t4_t51_in*MAS_in[1]<=d_t4_t51*MAS[1]

	S += d_t4_t51_in*MAS_in[2]<=d_t4_t51*MAS[2]

	S += d_t4_t51_in*MAS_in[3]<=d_t4_t51*MAS[3]

	d_t4_t51_mem0 = S.Task('d_t4_t51_mem0', length=1, delay_cost=1)
	d_t4_t51_mem0 += MAS_MEM[2]
	S += 78 < d_t4_t51_mem0
	S += d_t4_t51_mem0 <= d_t4_t51

	d_t4_t51_mem1 = S.Task('d_t4_t51_mem1', length=1, delay_cost=1)
	d_t4_t51_mem1 += MAS_MEM[3]
	S += 85 < d_t4_t51_mem1
	S += d_t4_t51_mem1 <= d_t4_t51

	d_t5_t21 = S.Task('d_t5_t21', length=3, delay_cost=1)
	d_t5_t21 += alt(MAS)
	d_t5_t21_in = S.Task('d_t5_t21_in', length=1, delay_cost=1)
	d_t5_t21_in += alt(MAS_in)
	S += d_t5_t21_in*MAS_in[0]<=d_t5_t21*MAS[0]

	S += d_t5_t21_in*MAS_in[1]<=d_t5_t21*MAS[1]

	S += d_t5_t21_in*MAS_in[2]<=d_t5_t21*MAS[2]

	S += d_t5_t21_in*MAS_in[3]<=d_t5_t21*MAS[3]

	d_t5_t21_mem0 = S.Task('d_t5_t21_mem0', length=1, delay_cost=1)
	d_t5_t21_mem0 += MM_MEM[0]
	S += 93 < d_t5_t21_mem0
	S += d_t5_t21_mem0 <= d_t5_t21

	d_t5_t21_mem1 = S.Task('d_t5_t21_mem1', length=1, delay_cost=1)
	d_t5_t21_mem1 += MAS_MEM[1]
	S += 105 < d_t5_t21_mem1
	S += d_t5_t21_mem1 <= d_t5_t21

	d_t5_t50 = S.Task('d_t5_t50', length=3, delay_cost=1)
	d_t5_t50 += alt(MAS)
	d_t5_t50_in = S.Task('d_t5_t50_in', length=1, delay_cost=1)
	d_t5_t50_in += alt(MAS_in)
	S += d_t5_t50_in*MAS_in[0]<=d_t5_t50*MAS[0]

	S += d_t5_t50_in*MAS_in[1]<=d_t5_t50*MAS[1]

	S += d_t5_t50_in*MAS_in[2]<=d_t5_t50*MAS[2]

	S += d_t5_t50_in*MAS_in[3]<=d_t5_t50*MAS[3]

	d_t5_t50_mem0 = S.Task('d_t5_t50_mem0', length=1, delay_cost=1)
	d_t5_t50_mem0 += MAS_MEM[2]
	S += 43 < d_t5_t50_mem0
	S += d_t5_t50_mem0 <= d_t5_t50

	d_t5_t50_mem1 = S.Task('d_t5_t50_mem1', length=1, delay_cost=1)
	d_t5_t50_mem1 += MAS_MEM[7]
	S += 80 < d_t5_t50_mem1
	S += d_t5_t50_mem1 <= d_t5_t50

	d_t5_t51 = S.Task('d_t5_t51', length=3, delay_cost=1)
	d_t5_t51 += alt(MAS)
	d_t5_t51_in = S.Task('d_t5_t51_in', length=1, delay_cost=1)
	d_t5_t51_in += alt(MAS_in)
	S += d_t5_t51_in*MAS_in[0]<=d_t5_t51*MAS[0]

	S += d_t5_t51_in*MAS_in[1]<=d_t5_t51*MAS[1]

	S += d_t5_t51_in*MAS_in[2]<=d_t5_t51*MAS[2]

	S += d_t5_t51_in*MAS_in[3]<=d_t5_t51*MAS[3]

	d_t5_t51_mem0 = S.Task('d_t5_t51_mem0', length=1, delay_cost=1)
	d_t5_t51_mem0 += MAS_MEM[6]
	S += 73 < d_t5_t51_mem0
	S += d_t5_t51_mem0 <= d_t5_t51

	d_t5_t51_mem1 = S.Task('d_t5_t51_mem1', length=1, delay_cost=1)
	d_t5_t51_mem1 += MAS_MEM[1]
	S += 77 < d_t5_t51_mem1
	S += d_t5_t51_mem1 <= d_t5_t51

	d_s011 = S.Task('d_s011', length=3, delay_cost=1)
	d_s011 += alt(MAS)
	d_s011_in = S.Task('d_s011_in', length=1, delay_cost=1)
	d_s011_in += alt(MAS_in)
	S += d_s011_in*MAS_in[0]<=d_s011*MAS[0]

	S += d_s011_in*MAS_in[1]<=d_s011*MAS[1]

	S += d_s011_in*MAS_in[2]<=d_s011*MAS[2]

	S += d_s011_in*MAS_in[3]<=d_s011*MAS[3]

	d_s011_mem0 = S.Task('d_s011_mem0', length=1, delay_cost=1)
	d_s011_mem0 += MAS_MEM[0]
	S += 90 < d_s011_mem0
	S += d_s011_mem0 <= d_s011

	d_s011_mem1 = S.Task('d_s011_mem1', length=1, delay_cost=1)
	d_s011_mem1 += MAS_MEM[5]
	S += 73 < d_s011_mem1
	S += d_s011_mem1 <= d_s011

	d_s1111 = S.Task('d_s1111', length=3, delay_cost=1)
	d_s1111 += alt(MAS)
	d_s1111_in = S.Task('d_s1111_in', length=1, delay_cost=1)
	d_s1111_in += alt(MAS_in)
	S += d_s1111_in*MAS_in[0]<=d_s1111*MAS[0]

	S += d_s1111_in*MAS_in[1]<=d_s1111*MAS[1]

	S += d_s1111_in*MAS_in[2]<=d_s1111*MAS[2]

	S += d_s1111_in*MAS_in[3]<=d_s1111*MAS[3]

	d_s1111_mem0 = S.Task('d_s1111_mem0', length=1, delay_cost=1)
	d_s1111_mem0 += MAS_MEM[4]
	S += 88 < d_s1111_mem0
	S += d_s1111_mem0 <= d_s1111

	d_s1111_mem1 = S.Task('d_s1111_mem1', length=1, delay_cost=1)
	d_s1111_mem1 += MAS_MEM[3]
	S += 76 < d_s1111_mem1
	S += d_s1111_mem1 <= d_s1111

	d_s211 = S.Task('d_s211', length=3, delay_cost=1)
	d_s211 += alt(MAS)
	d_s211_in = S.Task('d_s211_in', length=1, delay_cost=1)
	d_s211_in += alt(MAS_in)
	S += d_s211_in*MAS_in[0]<=d_s211*MAS[0]

	S += d_s211_in*MAS_in[1]<=d_s211*MAS[1]

	S += d_s211_in*MAS_in[2]<=d_s211*MAS[2]

	S += d_s211_in*MAS_in[3]<=d_s211*MAS[3]

	d_s211_mem0 = S.Task('d_s211_mem0', length=1, delay_cost=1)
	d_s211_mem0 += MAS_MEM[0]
	S += 78 < d_s211_mem0
	S += d_s211_mem0 <= d_s211

	d_s211_mem1 = S.Task('d_s211_mem1', length=1, delay_cost=1)
	d_s211_mem1 += MAS_MEM[7]
	S += 86 < d_s211_mem1
	S += d_s211_mem1 <= d_s211

	d210 = S.Task('d210', length=3, delay_cost=1)
	d210 += alt(MAS)
	d210_in = S.Task('d210_in', length=1, delay_cost=1)
	d210_in += alt(MAS_in)
	S += d210_in*MAS_in[0]<=d210*MAS[0]

	S += d210_in*MAS_in[1]<=d210*MAS[1]

	S += d210_in*MAS_in[2]<=d210*MAS[2]

	S += d210_in*MAS_in[3]<=d210*MAS[3]

	S += 20<d210

	d210_w = S.Task('d210_w', length=1, delay_cost=1)
	d210_w += alt(MAIN_MEM_w)
	S += d210 <= d210_w

	d210_mem0 = S.Task('d210_mem0', length=1, delay_cost=1)
	d210_mem0 += MAS_MEM[2]
	S += 41 < d210_mem0
	S += d210_mem0 <= d210

	d210_mem1 = S.Task('d210_mem1', length=1, delay_cost=1)
	d210_mem1 += MAS_MEM[7]
	S += 63 < d210_mem1
	S += d210_mem1 <= d210

	c_t300 = S.Task('c_t300', length=3, delay_cost=1)
	c_t300 += alt(MAS)
	c_t300_in = S.Task('c_t300_in', length=1, delay_cost=1)
	c_t300_in += alt(MAS_in)
	S += c_t300_in*MAS_in[0]<=c_t300*MAS[0]

	S += c_t300_in*MAS_in[1]<=c_t300*MAS[1]

	S += c_t300_in*MAS_in[2]<=c_t300*MAS[2]

	S += c_t300_in*MAS_in[3]<=c_t300*MAS[3]

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	c_t300_mem0 += MAS_MEM[4]
	S += 63 < c_t300_mem0
	S += c_t300_mem0 <= c_t300

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	c_t300_mem1 += MAS_MEM[5]
	S += 101 < c_t300_mem1
	S += c_t300_mem1 <= c_t300

	c_t301 = S.Task('c_t301', length=3, delay_cost=1)
	c_t301 += alt(MAS)
	c_t301_in = S.Task('c_t301_in', length=1, delay_cost=1)
	c_t301_in += alt(MAS_in)
	S += c_t301_in*MAS_in[0]<=c_t301*MAS[0]

	S += c_t301_in*MAS_in[1]<=c_t301*MAS[1]

	S += c_t301_in*MAS_in[2]<=c_t301*MAS[2]

	S += c_t301_in*MAS_in[3]<=c_t301*MAS[3]

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	c_t301_mem0 += MAS_MEM[4]
	S += 95 < c_t301_mem0
	S += c_t301_mem0 <= c_t301

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	c_t301_mem1 += MAS_MEM[3]
	S += 99 < c_t301_mem1
	S += c_t301_mem1 <= c_t301

	c_t311 = S.Task('c_t311', length=3, delay_cost=1)
	c_t311 += alt(MAS)
	c_t311_in = S.Task('c_t311_in', length=1, delay_cost=1)
	c_t311_in += alt(MAS_in)
	S += c_t311_in*MAS_in[0]<=c_t311*MAS[0]

	S += c_t311_in*MAS_in[1]<=c_t311*MAS[1]

	S += c_t311_in*MAS_in[2]<=c_t311*MAS[2]

	S += c_t311_in*MAS_in[3]<=c_t311*MAS[3]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	c_t311_mem0 += MAS_MEM[6]
	S += 101 < c_t311_mem0
	S += c_t311_mem0 <= c_t311

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	c_t311_mem1 += MAS_MEM[5]
	S += 100 < c_t311_mem1
	S += c_t311_mem1 <= c_t311

	c_t400 = S.Task('c_t400', length=3, delay_cost=1)
	c_t400 += alt(MAS)
	c_t400_in = S.Task('c_t400_in', length=1, delay_cost=1)
	c_t400_in += alt(MAS_in)
	S += c_t400_in*MAS_in[0]<=c_t400*MAS[0]

	S += c_t400_in*MAS_in[1]<=c_t400*MAS[1]

	S += c_t400_in*MAS_in[2]<=c_t400*MAS[2]

	S += c_t400_in*MAS_in[3]<=c_t400*MAS[3]

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	c_t400_mem0 += MAS_MEM[6]
	S += 61 < c_t400_mem0
	S += c_t400_mem0 <= c_t400

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	c_t400_mem1 += MAS_MEM[7]
	S += 102 < c_t400_mem1
	S += c_t400_mem1 <= c_t400

	c_t401 = S.Task('c_t401', length=3, delay_cost=1)
	c_t401 += alt(MAS)
	c_t401_in = S.Task('c_t401_in', length=1, delay_cost=1)
	c_t401_in += alt(MAS_in)
	S += c_t401_in*MAS_in[0]<=c_t401*MAS[0]

	S += c_t401_in*MAS_in[1]<=c_t401*MAS[1]

	S += c_t401_in*MAS_in[2]<=c_t401*MAS[2]

	S += c_t401_in*MAS_in[3]<=c_t401*MAS[3]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	c_t401_mem0 += MAS_MEM[4]
	S += 87 < c_t401_mem0
	S += c_t401_mem0 <= c_t401

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	c_t401_mem1 += MAS_MEM[3]
	S += 103 < c_t401_mem1
	S += c_t401_mem1 <= c_t401

	c_t411 = S.Task('c_t411', length=3, delay_cost=1)
	c_t411 += alt(MAS)
	c_t411_in = S.Task('c_t411_in', length=1, delay_cost=1)
	c_t411_in += alt(MAS_in)
	S += c_t411_in*MAS_in[0]<=c_t411*MAS[0]

	S += c_t411_in*MAS_in[1]<=c_t411*MAS[1]

	S += c_t411_in*MAS_in[2]<=c_t411*MAS[2]

	S += c_t411_in*MAS_in[3]<=c_t411*MAS[3]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	c_t411_mem0 += MAS_MEM[2]
	S += 107 < c_t411_mem0
	S += c_t411_mem0 <= c_t411

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	c_t411_mem1 += MAS_MEM[3]
	S += 98 < c_t411_mem1
	S += c_t411_mem1 <= c_t411

	c_t500 = S.Task('c_t500', length=3, delay_cost=1)
	c_t500 += alt(MAS)
	c_t500_in = S.Task('c_t500_in', length=1, delay_cost=1)
	c_t500_in += alt(MAS_in)
	S += c_t500_in*MAS_in[0]<=c_t500*MAS[0]

	S += c_t500_in*MAS_in[1]<=c_t500*MAS[1]

	S += c_t500_in*MAS_in[2]<=c_t500*MAS[2]

	S += c_t500_in*MAS_in[3]<=c_t500*MAS[3]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	c_t500_mem0 += MAS_MEM[6]
	S += 65 < c_t500_mem0
	S += c_t500_mem0 <= c_t500

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	c_t500_mem1 += MAS_MEM[5]
	S += 92 < c_t500_mem1
	S += c_t500_mem1 <= c_t500

	c_t501 = S.Task('c_t501', length=3, delay_cost=1)
	c_t501 += alt(MAS)
	c_t501_in = S.Task('c_t501_in', length=1, delay_cost=1)
	c_t501_in += alt(MAS_in)
	S += c_t501_in*MAS_in[0]<=c_t501*MAS[0]

	S += c_t501_in*MAS_in[1]<=c_t501*MAS[1]

	S += c_t501_in*MAS_in[2]<=c_t501*MAS[2]

	S += c_t501_in*MAS_in[3]<=c_t501*MAS[3]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	c_t501_mem0 += MAS_MEM[4]
	S += 90 < c_t501_mem0
	S += c_t501_mem0 <= c_t501

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	c_t501_mem1 += MAS_MEM[3]
	S += 88 < c_t501_mem1
	S += c_t501_mem1 <= c_t501

	c_t511 = S.Task('c_t511', length=3, delay_cost=1)
	c_t511 += alt(MAS)
	c_t511_in = S.Task('c_t511_in', length=1, delay_cost=1)
	c_t511_in += alt(MAS_in)
	S += c_t511_in*MAS_in[0]<=c_t511*MAS[0]

	S += c_t511_in*MAS_in[1]<=c_t511*MAS[1]

	S += c_t511_in*MAS_in[2]<=c_t511*MAS[2]

	S += c_t511_in*MAS_in[3]<=c_t511*MAS[3]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	c_t511_mem0 += MAS_MEM[6]
	S += 108 < c_t511_mem0
	S += c_t511_mem0 <= c_t511

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	c_t511_mem1 += MAS_MEM[3]
	S += 93 < c_t511_mem1
	S += c_t511_mem1 <= c_t511

	c_t6000 = S.Task('c_t6000', length=3, delay_cost=1)
	c_t6000 += alt(MAS)
	c_t6000_in = S.Task('c_t6000_in', length=1, delay_cost=1)
	c_t6000_in += alt(MAS_in)
	S += c_t6000_in*MAS_in[0]<=c_t6000*MAS[0]

	S += c_t6000_in*MAS_in[1]<=c_t6000*MAS[1]

	S += c_t6000_in*MAS_in[2]<=c_t6000*MAS[2]

	S += c_t6000_in*MAS_in[3]<=c_t6000*MAS[3]

	c_t6000_mem0 = S.Task('c_t6000_mem0', length=1, delay_cost=1)
	c_t6000_mem0 += MAS_MEM[0]
	S += 76 < c_t6000_mem0
	S += c_t6000_mem0 <= c_t6000

	c_t6000_mem1 = S.Task('c_t6000_mem1', length=1, delay_cost=1)
	c_t6000_mem1 += MAS_MEM[7]
	S += 67 < c_t6000_mem1
	S += c_t6000_mem1 <= c_t6000

	c_t6001 = S.Task('c_t6001', length=3, delay_cost=1)
	c_t6001 += alt(MAS)
	c_t6001_in = S.Task('c_t6001_in', length=1, delay_cost=1)
	c_t6001_in += alt(MAS_in)
	S += c_t6001_in*MAS_in[0]<=c_t6001*MAS[0]

	S += c_t6001_in*MAS_in[1]<=c_t6001*MAS[1]

	S += c_t6001_in*MAS_in[2]<=c_t6001*MAS[2]

	S += c_t6001_in*MAS_in[3]<=c_t6001*MAS[3]

	c_t6001_mem0 = S.Task('c_t6001_mem0', length=1, delay_cost=1)
	c_t6001_mem0 += MAS_MEM[0]
	S += 73 < c_t6001_mem0
	S += c_t6001_mem0 <= c_t6001

	c_t6001_mem1 = S.Task('c_t6001_mem1', length=1, delay_cost=1)
	c_t6001_mem1 += MAS_MEM[3]
	S += 69 < c_t6001_mem1
	S += c_t6001_mem1 <= c_t6001

	c_t6011 = S.Task('c_t6011', length=3, delay_cost=1)
	c_t6011 += alt(MAS)
	c_t6011_in = S.Task('c_t6011_in', length=1, delay_cost=1)
	c_t6011_in += alt(MAS_in)
	S += c_t6011_in*MAS_in[0]<=c_t6011*MAS[0]

	S += c_t6011_in*MAS_in[1]<=c_t6011*MAS[1]

	S += c_t6011_in*MAS_in[2]<=c_t6011*MAS[2]

	S += c_t6011_in*MAS_in[3]<=c_t6011*MAS[3]

	c_t6011_mem0 = S.Task('c_t6011_mem0', length=1, delay_cost=1)
	c_t6011_mem0 += MAS_MEM[4]
	S += 86 < c_t6011_mem0
	S += c_t6011_mem0 <= c_t6011

	c_t6011_mem1 = S.Task('c_t6011_mem1', length=1, delay_cost=1)
	c_t6011_mem1 += MAS_MEM[5]
	S += 91 < c_t6011_mem1
	S += c_t6011_mem1 <= c_t6011

	c_t610 = S.Task('c_t610', length=3, delay_cost=1)
	c_t610 += alt(MAS)
	c_t610_in = S.Task('c_t610_in', length=1, delay_cost=1)
	c_t610_in += alt(MAS_in)
	S += c_t610_in*MAS_in[0]<=c_t610*MAS[0]

	S += c_t610_in*MAS_in[1]<=c_t610*MAS[1]

	S += c_t610_in*MAS_in[2]<=c_t610*MAS[2]

	S += c_t610_in*MAS_in[3]<=c_t610*MAS[3]

	c_t610_mem0 = S.Task('c_t610_mem0', length=1, delay_cost=1)
	c_t610_mem0 += MAS_MEM[4]
	S += 97 < c_t610_mem0
	S += c_t610_mem0 <= c_t610

	c_t610_mem1 = S.Task('c_t610_mem1', length=1, delay_cost=1)
	c_t610_mem1 += MAS_MEM[7]
	S += 64 < c_t610_mem1
	S += c_t610_mem1 <= c_t610

	c_t9_y1_0 = S.Task('c_t9_y1_0', length=3, delay_cost=1)
	c_t9_y1_0 += alt(MAS)
	c_t9_y1_0_in = S.Task('c_t9_y1_0_in', length=1, delay_cost=1)
	c_t9_y1_0_in += alt(MAS_in)
	S += c_t9_y1_0_in*MAS_in[0]<=c_t9_y1_0*MAS[0]

	S += c_t9_y1_0_in*MAS_in[1]<=c_t9_y1_0*MAS[1]

	S += c_t9_y1_0_in*MAS_in[2]<=c_t9_y1_0*MAS[2]

	S += c_t9_y1_0_in*MAS_in[3]<=c_t9_y1_0*MAS[3]

	c_t9_y1_0_mem0 = S.Task('c_t9_y1_0_mem0', length=1, delay_cost=1)
	c_t9_y1_0_mem0 += MAS_MEM[0]
	S += 70 < c_t9_y1_0_mem0
	S += c_t9_y1_0_mem0 <= c_t9_y1_0

	c_t9_y1_0_mem1 = S.Task('c_t9_y1_0_mem1', length=1, delay_cost=1)
	c_t9_y1_0_mem1 += MAS_MEM[5]
	S += 83 < c_t9_y1_0_mem1
	S += c_t9_y1_0_mem1 <= c_t9_y1_0

	c_t9_y1_1 = S.Task('c_t9_y1_1', length=3, delay_cost=1)
	c_t9_y1_1 += alt(MAS)
	c_t9_y1_1_in = S.Task('c_t9_y1_1_in', length=1, delay_cost=1)
	c_t9_y1_1_in += alt(MAS_in)
	S += c_t9_y1_1_in*MAS_in[0]<=c_t9_y1_1*MAS[0]

	S += c_t9_y1_1_in*MAS_in[1]<=c_t9_y1_1*MAS[1]

	S += c_t9_y1_1_in*MAS_in[2]<=c_t9_y1_1*MAS[2]

	S += c_t9_y1_1_in*MAS_in[3]<=c_t9_y1_1*MAS[3]

	c_t9_y1_1_mem0 = S.Task('c_t9_y1_1_mem0', length=1, delay_cost=1)
	c_t9_y1_1_mem0 += MAS_MEM[4]
	S += 83 < c_t9_y1_1_mem0
	S += c_t9_y1_1_mem0 <= c_t9_y1_1

	c_t9_y1_1_mem1 = S.Task('c_t9_y1_1_mem1', length=1, delay_cost=1)
	c_t9_y1_1_mem1 += MAS_MEM[1]
	S += 70 < c_t9_y1_1_mem1
	S += c_t9_y1_1_mem1 <= c_t9_y1_1

	c_t7000 = S.Task('c_t7000', length=3, delay_cost=1)
	c_t7000 += alt(MAS)
	c_t7000_in = S.Task('c_t7000_in', length=1, delay_cost=1)
	c_t7000_in += alt(MAS_in)
	S += c_t7000_in*MAS_in[0]<=c_t7000*MAS[0]

	S += c_t7000_in*MAS_in[1]<=c_t7000*MAS[1]

	S += c_t7000_in*MAS_in[2]<=c_t7000*MAS[2]

	S += c_t7000_in*MAS_in[3]<=c_t7000*MAS[3]

	c_t7000_mem0 = S.Task('c_t7000_mem0', length=1, delay_cost=1)
	c_t7000_mem0 += MAS_MEM[6]
	S += 67 < c_t7000_mem0
	S += c_t7000_mem0 <= c_t7000

	c_t7000_mem1 = S.Task('c_t7000_mem1', length=1, delay_cost=1)
	c_t7000_mem1 += MAS_MEM[5]
	S += 74 < c_t7000_mem1
	S += c_t7000_mem1 <= c_t7000

	c_t7001 = S.Task('c_t7001', length=3, delay_cost=1)
	c_t7001 += alt(MAS)
	c_t7001_in = S.Task('c_t7001_in', length=1, delay_cost=1)
	c_t7001_in += alt(MAS_in)
	S += c_t7001_in*MAS_in[0]<=c_t7001*MAS[0]

	S += c_t7001_in*MAS_in[1]<=c_t7001*MAS[1]

	S += c_t7001_in*MAS_in[2]<=c_t7001*MAS[2]

	S += c_t7001_in*MAS_in[3]<=c_t7001*MAS[3]

	c_t7001_mem0 = S.Task('c_t7001_mem0', length=1, delay_cost=1)
	c_t7001_mem0 += MAS_MEM[2]
	S += 69 < c_t7001_mem0
	S += c_t7001_mem0 <= c_t7001

	c_t7001_mem1 = S.Task('c_t7001_mem1', length=1, delay_cost=1)
	c_t7001_mem1 += MAS_MEM[1]
	S += 82 < c_t7001_mem1
	S += c_t7001_mem1 <= c_t7001

	c_t7011 = S.Task('c_t7011', length=3, delay_cost=1)
	c_t7011 += alt(MAS)
	c_t7011_in = S.Task('c_t7011_in', length=1, delay_cost=1)
	c_t7011_in += alt(MAS_in)
	S += c_t7011_in*MAS_in[0]<=c_t7011*MAS[0]

	S += c_t7011_in*MAS_in[1]<=c_t7011*MAS[1]

	S += c_t7011_in*MAS_in[2]<=c_t7011*MAS[2]

	S += c_t7011_in*MAS_in[3]<=c_t7011*MAS[3]

	c_t7011_mem0 = S.Task('c_t7011_mem0', length=1, delay_cost=1)
	c_t7011_mem0 += MAS_MEM[4]
	S += 91 < c_t7011_mem0
	S += c_t7011_mem0 <= c_t7011

	c_t7011_mem1 = S.Task('c_t7011_mem1', length=1, delay_cost=1)
	c_t7011_mem1 += MAS_MEM[5]
	S += 83 < c_t7011_mem1
	S += c_t7011_mem1 <= c_t7011

	c_t7110 = S.Task('c_t7110', length=3, delay_cost=1)
	c_t7110 += alt(MAS)
	c_t7110_in = S.Task('c_t7110_in', length=1, delay_cost=1)
	c_t7110_in += alt(MAS_in)
	S += c_t7110_in*MAS_in[0]<=c_t7110*MAS[0]

	S += c_t7110_in*MAS_in[1]<=c_t7110*MAS[1]

	S += c_t7110_in*MAS_in[2]<=c_t7110*MAS[2]

	S += c_t7110_in*MAS_in[3]<=c_t7110*MAS[3]

	c_t7110_mem0 = S.Task('c_t7110_mem0', length=1, delay_cost=1)
	c_t7110_mem0 += MAS_MEM[0]
	S += 92 < c_t7110_mem0
	S += c_t7110_mem0 <= c_t7110

	c_t7110_mem1 = S.Task('c_t7110_mem1', length=1, delay_cost=1)
	c_t7110_mem1 += MAS_MEM[5]
	S += 75 < c_t7110_mem1
	S += c_t7110_mem1 <= c_t7110

	c_t8000 = S.Task('c_t8000', length=3, delay_cost=1)
	c_t8000 += alt(MAS)
	c_t8000_in = S.Task('c_t8000_in', length=1, delay_cost=1)
	c_t8000_in += alt(MAS_in)
	S += c_t8000_in*MAS_in[0]<=c_t8000*MAS[0]

	S += c_t8000_in*MAS_in[1]<=c_t8000*MAS[1]

	S += c_t8000_in*MAS_in[2]<=c_t8000*MAS[2]

	S += c_t8000_in*MAS_in[3]<=c_t8000*MAS[3]

	c_t8000_mem0 = S.Task('c_t8000_mem0', length=1, delay_cost=1)
	c_t8000_mem0 += MAS_MEM[4]
	S += 74 < c_t8000_mem0
	S += c_t8000_mem0 <= c_t8000

	c_t8000_mem1 = S.Task('c_t8000_mem1', length=1, delay_cost=1)
	c_t8000_mem1 += MAS_MEM[1]
	S += 76 < c_t8000_mem1
	S += c_t8000_mem1 <= c_t8000

	c_t8001 = S.Task('c_t8001', length=3, delay_cost=1)
	c_t8001 += alt(MAS)
	c_t8001_in = S.Task('c_t8001_in', length=1, delay_cost=1)
	c_t8001_in += alt(MAS_in)
	S += c_t8001_in*MAS_in[0]<=c_t8001*MAS[0]

	S += c_t8001_in*MAS_in[1]<=c_t8001*MAS[1]

	S += c_t8001_in*MAS_in[2]<=c_t8001*MAS[2]

	S += c_t8001_in*MAS_in[3]<=c_t8001*MAS[3]

	c_t8001_mem0 = S.Task('c_t8001_mem0', length=1, delay_cost=1)
	c_t8001_mem0 += MAS_MEM[0]
	S += 82 < c_t8001_mem0
	S += c_t8001_mem0 <= c_t8001

	c_t8001_mem1 = S.Task('c_t8001_mem1', length=1, delay_cost=1)
	c_t8001_mem1 += MAS_MEM[1]
	S += 73 < c_t8001_mem1
	S += c_t8001_mem1 <= c_t8001

	c_t8011 = S.Task('c_t8011', length=3, delay_cost=1)
	c_t8011 += alt(MAS)
	c_t8011_in = S.Task('c_t8011_in', length=1, delay_cost=1)
	c_t8011_in += alt(MAS_in)
	S += c_t8011_in*MAS_in[0]<=c_t8011*MAS[0]

	S += c_t8011_in*MAS_in[1]<=c_t8011*MAS[1]

	S += c_t8011_in*MAS_in[2]<=c_t8011*MAS[2]

	S += c_t8011_in*MAS_in[3]<=c_t8011*MAS[3]

	c_t8011_mem0 = S.Task('c_t8011_mem0', length=1, delay_cost=1)
	c_t8011_mem0 += MAS_MEM[4]
	S += 83 < c_t8011_mem0
	S += c_t8011_mem0 <= c_t8011

	c_t8011_mem1 = S.Task('c_t8011_mem1', length=1, delay_cost=1)
	c_t8011_mem1 += MAS_MEM[5]
	S += 86 < c_t8011_mem1
	S += c_t8011_mem1 <= c_t8011

	c_t810 = S.Task('c_t810', length=3, delay_cost=1)
	c_t810 += alt(MAS)
	c_t810_in = S.Task('c_t810_in', length=1, delay_cost=1)
	c_t810_in += alt(MAS_in)
	S += c_t810_in*MAS_in[0]<=c_t810*MAS[0]

	S += c_t810_in*MAS_in[1]<=c_t810*MAS[1]

	S += c_t810_in*MAS_in[2]<=c_t810*MAS[2]

	S += c_t810_in*MAS_in[3]<=c_t810*MAS[3]

	c_t810_mem0 = S.Task('c_t810_mem0', length=1, delay_cost=1)
	c_t810_mem0 += MAS_MEM[0]
	S += 95 < c_t810_mem0
	S += c_t810_mem0 <= c_t810

	c_t810_mem1 = S.Task('c_t810_mem1', length=1, delay_cost=1)
	c_t810_mem1 += MAS_MEM[7]
	S += 76 < c_t810_mem1
	S += c_t810_mem1 <= c_t810

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage3MAS4/FP12_LADDERMUL/schedule13.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

