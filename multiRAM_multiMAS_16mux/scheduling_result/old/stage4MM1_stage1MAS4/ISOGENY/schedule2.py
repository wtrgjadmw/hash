from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 148
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 0
	DY0_mem1 += MAIN_MEM_r[1]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 0
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 0
	k2_14_Z1_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 1
	DX0_mem0 += MAIN_MEM_r[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 1
	NX1_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 1
	NY0_in += MM_in[0]

	k2_14_Z1 = S.Task('k2_14_Z1', length=4, delay_cost=1)
	S += k2_14_Z1 >= 1
	k2_14_Z1 += MM[0]

	NY0 = S.Task('NY0', length=4, delay_cost=1)
	S += NY0 >= 2
	NY0 += MM[0]

	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 2
	Z_exp2_in += MM_in[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 2
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 2
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 3
	NY1_mem1 += MAIN_MEM_r[1]

	Z_exp2 = S.Task('Z_exp2', length=4, delay_cost=1)
	S += Z_exp2 >= 3
	Z_exp2 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 3
	k0_10_Z1_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 3
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 4
	NX0_in += MM_in[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 4
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=4, delay_cost=1)
	S += k0_10_Z1 >= 4
	k0_10_Z1 += MM[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 4
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 5
	DX0_in += MM_in[0]

	NX0 = S.Task('NX0', length=4, delay_cost=1)
	S += NX0 >= 5
	NX0 += MM[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 5
	NX0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 5
	NY0_mem1 += MAIN_MEM_r[1]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 5
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 5
	NY1__mem1 += MM_MEM[1]

	DX0 = S.Task('DX0', length=4, delay_cost=1)
	S += DX0 >= 6
	DX0 += MM[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 6
	DX0_mem1 += MAIN_MEM_r[1]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 6
	NY1_ += MAS[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 6
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 6
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 6
	k1_9_Z2_mem1 += MM_MEM[1]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 7
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k1_9_Z2 = S.Task('k1_9_Z2', length=4, delay_cost=1)
	S += k1_9_Z2 >= 7
	k1_9_Z2 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 7
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 7
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 7
	k3_14_Z2_mem1 += MM_MEM[1]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 8
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 8
	DY0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 8
	NX0_mem1 += MAIN_MEM_r[1]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 8
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 8
	NX1__mem1 += MM_MEM[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=4, delay_cost=1)
	S += k3_14_Z2 >= 8
	k3_14_Z2 += MM[0]

	DY0 = S.Task('DY0', length=4, delay_cost=1)
	S += DY0 >= 9
	DY0 += MM[0]

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 9
	NX1_ += MAS[1]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 9
	NY0_mem0 += MAIN_MEM_r[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 9
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 9
	Z_exp3_mem0 += MM_MEM[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 9
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 10
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 10
	DX1__mem1 += MM_MEM[1]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 10
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 10
	NY1_mem0 += MAS_MEM[0]

	Z_exp3 = S.Task('Z_exp3', length=4, delay_cost=1)
	S += Z_exp3 >= 10
	Z_exp3 += MM[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 10
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 11
	DX1_ += MAS[2]

	NY1 = S.Task('NY1', length=4, delay_cost=1)
	S += NY1 >= 11
	NY1 += MM[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 11
	Z_exp2_mem0 += MAIN_MEM_r[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 11
	Z_exp5_mem1 += MAIN_MEM_r[1]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 11
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 11
	k2_13_Z2_mem1 += MM_MEM[1]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 12
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 12
	DY1__mem1 += MM_MEM[1]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 12
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 12
	NX1_mem0 += MAS_MEM[2]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 12
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2 = S.Task('k2_13_Z2', length=4, delay_cost=1)
	S += k2_13_Z2 >= 12
	k2_13_Z2 += MM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 13
	DY1_ += MAS[1]

	NX1 = S.Task('NX1', length=4, delay_cost=1)
	S += NX1 >= 13
	NX1 += MM[0]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 13
	NX2_mem1 += MAIN_MEM_r[1]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 13
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 13
	k0_9_Z2_mem1 += MM_MEM[1]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 13
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 14
	NX3_mem1 += MAIN_MEM_r[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=4, delay_cost=1)
	S += k0_9_Z2 >= 14
	k0_9_Z2 += MM[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 14
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 14
	k1_8_Z3_mem1 += MM_MEM[1]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 14
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=4, delay_cost=1)
	S += k1_8_Z3 >= 15
	k1_8_Z3 += MM[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 15
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 15
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 15
	k3_13_Z3_mem1 += MM_MEM[1]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 16
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 16
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 16
	k2_12_Z3_mem1 += MM_MEM[1]

	k3_13_Z3 = S.Task('k3_13_Z3', length=4, delay_cost=1)
	S += k3_13_Z3 >= 16
	k3_13_Z3 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 17
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 17
	k0_8_Z3_mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=4, delay_cost=1)
	S += k2_12_Z3 >= 17
	k2_12_Z3 += MM[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 17
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 18
	DX1_mem1 += MAIN_MEM_r[1]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 18
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 18
	Z_exp4_mem0 += MM_MEM[0]

	k0_8_Z3 = S.Task('k0_8_Z3', length=4, delay_cost=1)
	S += k0_8_Z3 >= 18
	k0_8_Z3 += MM[0]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 19
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 19
	DY1_mem0 += MAS_MEM[2]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 19
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 19
	NY2__mem1 += MM_MEM[1]

	Z_exp4 = S.Task('Z_exp4', length=4, delay_cost=1)
	S += Z_exp4 >= 19
	Z_exp4 += MM[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 20
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 20
	DX1_mem0 += MAS_MEM[4]

	DY1 = S.Task('DY1', length=4, delay_cost=1)
	S += DY1 >= 20
	DY1 += MM[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 20
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 20
	NX2__mem1 += MM_MEM[1]

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	S += NY2_ >= 20
	NY2_ += MAS[2]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 20
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	DX1 = S.Task('DX1', length=4, delay_cost=1)
	S += DX1 >= 21
	DX1 += MM[0]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 21
	DY1_mem1 += MAIN_MEM_r[1]

	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	S += NX2_ >= 21
	NX2_ += MAS[0]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 21
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 21
	NX2_mem0 += MAS_MEM[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 21
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	NX2 = S.Task('NX2', length=4, delay_cost=1)
	S += NX2 >= 22
	NX2 += MM[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 22
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 23
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 23
	NY2_mem0 += MAS_MEM[4]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 23
	NY2_mem1 += MAIN_MEM_r[1]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 23
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	S += DY2_ >= 24
	DY2_ += MAS[1]

	NY2 = S.Task('NY2', length=4, delay_cost=1)
	S += NY2 >= 24
	NY2 += MM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 24
	NY3_mem1 += MAIN_MEM_r[1]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 24
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 25
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 25
	NX3__mem1 += MM_MEM[1]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 25
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	S += NX3_ >= 26
	NX3_ += MAS[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 26
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 27
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 27
	NX3_mem0 += MAS_MEM[0]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 27
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 27
	NY3__mem1 += MM_MEM[1]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 27
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	NX3 = S.Task('NX3', length=4, delay_cost=1)
	S += NX3 >= 28
	NX3 += MM[0]

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
	S += NY3_ >= 28
	NY3_ += MAS[1]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 28
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 28
	NY3_mem0 += MAS_MEM[2]

	NY3 = S.Task('NY3', length=4, delay_cost=1)
	S += NY3 >= 29
	NY3 += MM[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 29
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 29
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 29
	k0_7_Z4_mem1 += MM_MEM[1]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 30
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 30
	Z_exp5_mem0 += MM_MEM[0]

	k0_7_Z4 = S.Task('k0_7_Z4', length=4, delay_cost=1)
	S += k0_7_Z4 >= 30
	k0_7_Z4 += MM[0]

	Z_exp5 = S.Task('Z_exp5', length=4, delay_cost=1)
	S += Z_exp5 >= 31
	Z_exp5 += MM[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 31
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 32
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 32
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 32
	k2_11_Z4_mem1 += MM_MEM[1]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 33
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 33
	NX4__mem1 += MM_MEM[1]

	k2_11_Z4 = S.Task('k2_11_Z4', length=4, delay_cost=1)
	S += k2_11_Z4 >= 33
	k2_11_Z4 += MM[0]

	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	S += NX4_ >= 34
	NX4_ += MAS[3]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 34
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 34
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 34
	k3_11_Z5_mem1 += MM_MEM[1]

	k3_11_Z5 = S.Task('k3_11_Z5', length=4, delay_cost=1)
	S += k3_11_Z5 >= 35
	k3_11_Z5 += MM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 36
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 36
	k1_6_Z5_mem1 += MM_MEM[1]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 37
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 37
	k0_6_Z5_mem1 += MM_MEM[1]

	k1_6_Z5 = S.Task('k1_6_Z5', length=4, delay_cost=1)
	S += k1_6_Z5 >= 37
	k1_6_Z5 += MM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=4, delay_cost=1)
	S += k0_6_Z5 >= 38
	k0_6_Z5 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 38
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 38
	k2_10_Z5_mem1 += MM_MEM[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=4, delay_cost=1)
	S += k2_10_Z5 >= 39
	k2_10_Z5 += MM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 40
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 40
	k2_9_Z6_mem1 += MM_MEM[1]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 41
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 41
	NY4__mem1 += MM_MEM[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=4, delay_cost=1)
	S += k2_9_Z6 >= 41
	k2_9_Z6 += MM[0]

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	S += NY4_ >= 42
	NY4_ += MAS[2]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 42
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 42
	k0_5_Z6_mem1 += MM_MEM[1]

	k0_5_Z6 = S.Task('k0_5_Z6', length=4, delay_cost=1)
	S += k0_5_Z6 >= 43
	k0_5_Z6 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 45
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 45
	k3_10_Z6_mem1 += MM_MEM[1]

	k3_10_Z6 = S.Task('k3_10_Z6', length=4, delay_cost=1)
	S += k3_10_Z6 >= 46
	k3_10_Z6 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 46
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 46
	k3_9_Z7_mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 47
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 47
	k0_3_Z8_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=4, delay_cost=1)
	S += k3_9_Z7 >= 47
	k3_9_Z7 += MM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=4, delay_cost=1)
	S += k0_3_Z8 >= 48
	k0_3_Z8 += MM[0]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 50
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 50
	k1_4_Z7_mem1 += MM_MEM[1]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 51
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 51
	k1_3_Z8_mem1 += MM_MEM[1]

	k1_4_Z7 = S.Task('k1_4_Z7', length=4, delay_cost=1)
	S += k1_4_Z7 >= 51
	k1_4_Z7 += MM[0]

	k1_3_Z8 = S.Task('k1_3_Z8', length=4, delay_cost=1)
	S += k1_3_Z8 >= 52
	k1_3_Z8 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 52
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 52
	k2_7_Z8_mem1 += MM_MEM[1]

	k2_7_Z8 = S.Task('k2_7_Z8', length=4, delay_cost=1)
	S += k2_7_Z8 >= 53
	k2_7_Z8 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 53
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 53
	k3_8_Z8_mem1 += MM_MEM[1]

	k3_8_Z8 = S.Task('k3_8_Z8', length=4, delay_cost=1)
	S += k3_8_Z8 >= 54
	k3_8_Z8 += MM[0]


	# new tasks
	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	k1_7_Z4_in += alt(MM_in)
	k1_7_Z4 = S.Task('k1_7_Z4', length=4, delay_cost=1)
	k1_7_Z4 += alt(MM)
	S += k1_7_Z4>=k1_7_Z4_in

	S += k1_7_Z4<1000

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	k1_7_Z4_mem0 += MAIN_MEM_r[0]
	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	k1_7_Z4_mem1 += MM_MEM[1]
	S += 22 < k1_7_Z4_mem1
	S += k1_7_Z4_mem1 <= k1_7_Z4

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	k3_12_Z4_in += alt(MM_in)
	k3_12_Z4 = S.Task('k3_12_Z4', length=4, delay_cost=1)
	k3_12_Z4 += alt(MM)
	S += k3_12_Z4>=k3_12_Z4_in

	S += k3_12_Z4<1000

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	k3_12_Z4_mem0 += MAIN_MEM_r[0]
	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	k3_12_Z4_mem1 += MM_MEM[1]
	S += 22 < k3_12_Z4_mem1
	S += k3_12_Z4_mem1 <= k3_12_Z4

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	Z_exp6_in += alt(MM_in)
	Z_exp6 = S.Task('Z_exp6', length=4, delay_cost=1)
	Z_exp6 += alt(MM)
	S += Z_exp6>=Z_exp6_in

	S += Z_exp6<41

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	Z_exp6_mem0 += MM_MEM[0]
	S += 34 < Z_exp6_mem0
	S += Z_exp6_mem0 <= Z_exp6

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	Z_exp6_mem1 += MAIN_MEM_r[1]
	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	DX2_ += alt(MAS)

	S += DX2_<1000

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	DX2__mem0 += MM_MEM[0]
	S += 24 < DX2__mem0
	S += DX2__mem0 <= DX2_

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	DX2__mem1 += MM_MEM[1]
	S += 18 < DX2__mem1
	S += DX2__mem1 <= DX2_

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	Z_exp7_in += alt(MM_in)
	Z_exp7 = S.Task('Z_exp7', length=4, delay_cost=1)
	Z_exp7 += alt(MM)
	S += Z_exp7>=Z_exp7_in

	S += Z_exp7<47

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	Z_exp7_mem0 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < Z_exp7_mem0*MM_MEM[0]
	S += Z_exp7_mem0 <= Z_exp7

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	Z_exp7_mem1 += MAIN_MEM_r[1]
	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	DX2_in += alt(MM_in)
	DX2 = S.Task('DX2', length=4, delay_cost=1)
	DX2 += alt(MM)
	S += DX2>=DX2_in

	S += DX2<1000

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	DX2_mem0 += alt(MAS_MEM)
	S += (DX2_*MAS[0])-1 < DX2_mem0*MAS_MEM[0]
	S += (DX2_*MAS[1])-1 < DX2_mem0*MAS_MEM[2]
	S += (DX2_*MAS[2])-1 < DX2_mem0*MAS_MEM[4]
	S += (DX2_*MAS[3])-1 < DX2_mem0*MAS_MEM[6]
	S += DX2_mem0 <= DX2

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	DX2_mem1 += MAIN_MEM_r[1]
	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	k1_5_Z6_in += alt(MM_in)
	k1_5_Z6 = S.Task('k1_5_Z6', length=4, delay_cost=1)
	k1_5_Z6 += alt(MM)
	S += k1_5_Z6>=k1_5_Z6_in

	S += k1_5_Z6<1000

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	k1_5_Z6_mem0 += MAIN_MEM_r[0]
	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	k1_5_Z6_mem1 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < k1_5_Z6_mem1*MM_MEM[1]
	S += k1_5_Z6_mem1 <= k1_5_Z6

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	DY2_in += alt(MM_in)
	DY2 = S.Task('DY2', length=4, delay_cost=1)
	DY2 += alt(MM)
	S += DY2>=DY2_in

	S += DY2<1000

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	DY2_mem0 += MAS_MEM[2]
	S += 24 < DY2_mem0
	S += DY2_mem0 <= DY2

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	DY2_mem1 += MAIN_MEM_r[1]
	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	Z_exp8_in += alt(MM_in)
	Z_exp8 = S.Task('Z_exp8', length=4, delay_cost=1)
	Z_exp8 += alt(MM)
	S += Z_exp8>=Z_exp8_in

	S += Z_exp8<48

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	Z_exp8_mem0 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < Z_exp8_mem0*MM_MEM[0]
	S += Z_exp8_mem0 <= Z_exp8

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	Z_exp8_mem1 += MAIN_MEM_r[1]
	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	k0_4_Z7_in += alt(MM_in)
	k0_4_Z7 = S.Task('k0_4_Z7', length=4, delay_cost=1)
	k0_4_Z7 += alt(MM)
	S += k0_4_Z7>=k0_4_Z7_in

	S += k0_4_Z7<1000

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	k0_4_Z7_mem0 += MAIN_MEM_r[0]
	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	k0_4_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k0_4_Z7_mem1*MM_MEM[1]
	S += k0_4_Z7_mem1 <= k0_4_Z7

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	DX3_ += alt(MAS)

	S += DX3_<1000

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	DX3__mem0 += alt(MM_MEM)
	S += (DX2*MM[0])-1 < DX3__mem0*MM_MEM[0]
	S += DX3__mem0 <= DX3_

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	DX3__mem1 += alt(MM_MEM)
	S += (k1_7_Z4*MM[0])-1 < DX3__mem1*MM_MEM[1]
	S += DX3__mem1 <= DX3_

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	k2_8_Z7_in += alt(MM_in)
	k2_8_Z7 = S.Task('k2_8_Z7', length=4, delay_cost=1)
	k2_8_Z7 += alt(MM)
	S += k2_8_Z7>=k2_8_Z7_in

	S += k2_8_Z7<1000

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	k2_8_Z7_mem0 += MAIN_MEM_r[0]
	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	k2_8_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k2_8_Z7_mem1*MM_MEM[1]
	S += k2_8_Z7_mem1 <= k2_8_Z7

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	DY3_ += alt(MAS)

	S += DY3_<1000

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	DY3__mem0 += alt(MM_MEM)
	S += (DY2*MM[0])-1 < DY3__mem0*MM_MEM[0]
	S += DY3__mem0 <= DY3_

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	DY3__mem1 += alt(MM_MEM)
	S += (k3_12_Z4*MM[0])-1 < DY3__mem1*MM_MEM[1]
	S += DY3__mem1 <= DY3_

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	Z_exp9_in += alt(MM_in)
	Z_exp9 = S.Task('Z_exp9', length=4, delay_cost=1)
	Z_exp9 += alt(MM)
	S += Z_exp9>=Z_exp9_in

	S += Z_exp9<1000

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	Z_exp9_mem0 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < Z_exp9_mem0*MM_MEM[0]
	S += Z_exp9_mem0 <= Z_exp9

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	Z_exp9_mem1 += MAIN_MEM_r[1]
	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	DX3_in += alt(MM_in)
	DX3 = S.Task('DX3', length=4, delay_cost=1)
	DX3 += alt(MM)
	S += DX3>=DX3_in

	S += DX3<1000

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	DX3_mem0 += alt(MAS_MEM)
	S += (DX3_*MAS[0])-1 < DX3_mem0*MAS_MEM[0]
	S += (DX3_*MAS[1])-1 < DX3_mem0*MAS_MEM[2]
	S += (DX3_*MAS[2])-1 < DX3_mem0*MAS_MEM[4]
	S += (DX3_*MAS[3])-1 < DX3_mem0*MAS_MEM[6]
	S += DX3_mem0 <= DX3

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	DX3_mem1 += MAIN_MEM_r[1]
	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	DY3_in += alt(MM_in)
	DY3 = S.Task('DY3', length=4, delay_cost=1)
	DY3 += alt(MM)
	S += DY3>=DY3_in

	S += DY3<1000

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	DY3_mem0 += alt(MAS_MEM)
	S += (DY3_*MAS[0])-1 < DY3_mem0*MAS_MEM[0]
	S += (DY3_*MAS[1])-1 < DY3_mem0*MAS_MEM[2]
	S += (DY3_*MAS[2])-1 < DY3_mem0*MAS_MEM[4]
	S += (DY3_*MAS[3])-1 < DY3_mem0*MAS_MEM[6]
	S += DY3_mem0 <= DY3

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	DY3_mem1 += MAIN_MEM_r[1]
	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	Z_exp10_in += alt(MM_in)
	Z_exp10 = S.Task('Z_exp10', length=4, delay_cost=1)
	Z_exp10 += alt(MM)
	S += Z_exp10>=Z_exp10_in

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	Z_exp10_mem0 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < Z_exp10_mem0*MM_MEM[0]
	S += Z_exp10_mem0 <= Z_exp10

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	Z_exp10_mem1 += MAIN_MEM_r[1]
	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	NX4_in += alt(MM_in)
	NX4 = S.Task('NX4', length=4, delay_cost=1)
	NX4 += alt(MM)
	S += NX4>=NX4_in

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	NX4_mem0 += MAS_MEM[6]
	S += 34 < NX4_mem0
	S += NX4_mem0 <= NX4

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	NX4_mem1 += MAIN_MEM_r[1]
	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	k0_2_Z9_in += alt(MM_in)
	k0_2_Z9 = S.Task('k0_2_Z9', length=4, delay_cost=1)
	k0_2_Z9 += alt(MM)
	S += k0_2_Z9>=k0_2_Z9_in

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	k0_2_Z9_mem0 += MAIN_MEM_r[0]
	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	k0_2_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k0_2_Z9_mem1*MM_MEM[1]
	S += k0_2_Z9_mem1 <= k0_2_Z9

	DX4_ = S.Task('DX4_', length=1, delay_cost=1)
	DX4_ += alt(MAS)

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	DX4__mem0 += alt(MM_MEM)
	S += (DX3*MM[0])-1 < DX4__mem0*MM_MEM[0]
	S += DX4__mem0 <= DX4_

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	DX4__mem1 += MM_MEM[1]
	S += 40 < DX4__mem1
	S += DX4__mem1 <= DX4_

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	k1_2_Z9_in += alt(MM_in)
	k1_2_Z9 = S.Task('k1_2_Z9', length=4, delay_cost=1)
	k1_2_Z9 += alt(MM)
	S += k1_2_Z9>=k1_2_Z9_in

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	k1_2_Z9_mem0 += MAIN_MEM_r[0]
	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	k1_2_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k1_2_Z9_mem1*MM_MEM[1]
	S += k1_2_Z9_mem1 <= k1_2_Z9

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	NY4_in += alt(MM_in)
	NY4 = S.Task('NY4', length=4, delay_cost=1)
	NY4 += alt(MM)
	S += NY4>=NY4_in

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	NY4_mem0 += MAS_MEM[4]
	S += 42 < NY4_mem0
	S += NY4_mem0 <= NY4

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	NY4_mem1 += MAIN_MEM_r[1]
	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	k2_6_Z9_in += alt(MM_in)
	k2_6_Z9 = S.Task('k2_6_Z9', length=4, delay_cost=1)
	k2_6_Z9 += alt(MM)
	S += k2_6_Z9>=k2_6_Z9_in

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	k2_6_Z9_mem0 += MAIN_MEM_r[0]
	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	k2_6_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k2_6_Z9_mem1*MM_MEM[1]
	S += k2_6_Z9_mem1 <= k2_6_Z9

	DY4_ = S.Task('DY4_', length=1, delay_cost=1)
	DY4_ += alt(MAS)

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	DY4__mem0 += alt(MM_MEM)
	S += (DY3*MM[0])-1 < DY4__mem0*MM_MEM[0]
	S += DY4__mem0 <= DY4_

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	DY4__mem1 += MM_MEM[1]
	S += 38 < DY4__mem1
	S += DY4__mem1 <= DY4_

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	k3_7_Z9_in += alt(MM_in)
	k3_7_Z9 = S.Task('k3_7_Z9', length=4, delay_cost=1)
	k3_7_Z9 += alt(MM)
	S += k3_7_Z9>=k3_7_Z9_in

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	k3_7_Z9_mem0 += MAIN_MEM_r[0]
	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	k3_7_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k3_7_Z9_mem1*MM_MEM[1]
	S += k3_7_Z9_mem1 <= k3_7_Z9

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	Z_exp11_in += alt(MM_in)
	Z_exp11 = S.Task('Z_exp11', length=4, delay_cost=1)
	Z_exp11 += alt(MM)
	S += Z_exp11>=Z_exp11_in

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	Z_exp11_mem0 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < Z_exp11_mem0*MM_MEM[0]
	S += Z_exp11_mem0 <= Z_exp11

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	Z_exp11_mem1 += MAIN_MEM_r[1]
	NX5_ = S.Task('NX5_', length=1, delay_cost=1)
	NX5_ += alt(MAS)

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	NX5__mem0 += alt(MM_MEM)
	S += (NX4*MM[0])-1 < NX5__mem0*MM_MEM[0]
	S += NX5__mem0 <= NX5_

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	NX5__mem1 += MM_MEM[1]
	S += 41 < NX5__mem1
	S += NX5__mem1 <= NX5_

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	k0_1_Z10_in += alt(MM_in)
	k0_1_Z10 = S.Task('k0_1_Z10', length=4, delay_cost=1)
	k0_1_Z10 += alt(MM)
	S += k0_1_Z10>=k0_1_Z10_in

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	k0_1_Z10_mem0 += MAIN_MEM_r[0]
	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	k0_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k0_1_Z10_mem1*MM_MEM[1]
	S += k0_1_Z10_mem1 <= k0_1_Z10

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	DX4_in += alt(MM_in)
	DX4 = S.Task('DX4', length=4, delay_cost=1)
	DX4 += alt(MM)
	S += DX4>=DX4_in

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	DX4_mem0 += alt(MAS_MEM)
	S += (DX4_*MAS[0])-1 < DX4_mem0*MAS_MEM[0]
	S += (DX4_*MAS[1])-1 < DX4_mem0*MAS_MEM[2]
	S += (DX4_*MAS[2])-1 < DX4_mem0*MAS_MEM[4]
	S += (DX4_*MAS[3])-1 < DX4_mem0*MAS_MEM[6]
	S += DX4_mem0 <= DX4

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	DX4_mem1 += MAIN_MEM_r[1]
	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	k1_1_Z10_in += alt(MM_in)
	k1_1_Z10 = S.Task('k1_1_Z10', length=4, delay_cost=1)
	k1_1_Z10 += alt(MM)
	S += k1_1_Z10>=k1_1_Z10_in

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	k1_1_Z10_mem0 += MAIN_MEM_r[0]
	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	k1_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k1_1_Z10_mem1*MM_MEM[1]
	S += k1_1_Z10_mem1 <= k1_1_Z10

	NY5_ = S.Task('NY5_', length=1, delay_cost=1)
	NY5_ += alt(MAS)

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	NY5__mem0 += alt(MM_MEM)
	S += (NY4*MM[0])-1 < NY5__mem0*MM_MEM[0]
	S += NY5__mem0 <= NY5_

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	NY5__mem1 += MM_MEM[1]
	S += 42 < NY5__mem1
	S += NY5__mem1 <= NY5_

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	k2_5_Z10_in += alt(MM_in)
	k2_5_Z10 = S.Task('k2_5_Z10', length=4, delay_cost=1)
	k2_5_Z10 += alt(MM)
	S += k2_5_Z10>=k2_5_Z10_in

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	k2_5_Z10_mem0 += MAIN_MEM_r[0]
	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	k2_5_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k2_5_Z10_mem1*MM_MEM[1]
	S += k2_5_Z10_mem1 <= k2_5_Z10

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	DY4_in += alt(MM_in)
	DY4 = S.Task('DY4', length=4, delay_cost=1)
	DY4 += alt(MM)
	S += DY4>=DY4_in

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	DY4_mem0 += alt(MAS_MEM)
	S += (DY4_*MAS[0])-1 < DY4_mem0*MAS_MEM[0]
	S += (DY4_*MAS[1])-1 < DY4_mem0*MAS_MEM[2]
	S += (DY4_*MAS[2])-1 < DY4_mem0*MAS_MEM[4]
	S += (DY4_*MAS[3])-1 < DY4_mem0*MAS_MEM[6]
	S += DY4_mem0 <= DY4

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	DY4_mem1 += MAIN_MEM_r[1]
	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	k3_6_Z10_in += alt(MM_in)
	k3_6_Z10 = S.Task('k3_6_Z10', length=4, delay_cost=1)
	k3_6_Z10 += alt(MM)
	S += k3_6_Z10>=k3_6_Z10_in

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	k3_6_Z10_mem0 += MAIN_MEM_r[0]
	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	k3_6_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k3_6_Z10_mem1*MM_MEM[1]
	S += k3_6_Z10_mem1 <= k3_6_Z10

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	Z_exp12_in += alt(MM_in)
	Z_exp12 = S.Task('Z_exp12', length=4, delay_cost=1)
	Z_exp12 += alt(MM)
	S += Z_exp12>=Z_exp12_in

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	Z_exp12_mem0 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < Z_exp12_mem0*MM_MEM[0]
	S += Z_exp12_mem0 <= Z_exp12

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	Z_exp12_mem1 += MAIN_MEM_r[1]
	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	NX5_in += alt(MM_in)
	NX5 = S.Task('NX5', length=4, delay_cost=1)
	NX5 += alt(MM)
	S += NX5>=NX5_in

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	NX5_mem0 += alt(MAS_MEM)
	S += (NX5_*MAS[0])-1 < NX5_mem0*MAS_MEM[0]
	S += (NX5_*MAS[1])-1 < NX5_mem0*MAS_MEM[2]
	S += (NX5_*MAS[2])-1 < NX5_mem0*MAS_MEM[4]
	S += (NX5_*MAS[3])-1 < NX5_mem0*MAS_MEM[6]
	S += NX5_mem0 <= NX5

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	NX5_mem1 += MAIN_MEM_r[1]
	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	k0_0_Z11_in += alt(MM_in)
	k0_0_Z11 = S.Task('k0_0_Z11', length=4, delay_cost=1)
	k0_0_Z11 += alt(MM)
	S += k0_0_Z11>=k0_0_Z11_in

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	k0_0_Z11_mem0 += MAIN_MEM_r[0]
	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	k0_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k0_0_Z11_mem1*MM_MEM[1]
	S += k0_0_Z11_mem1 <= k0_0_Z11

	DX5_ = S.Task('DX5_', length=1, delay_cost=1)
	DX5_ += alt(MAS)

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	DX5__mem0 += alt(MM_MEM)
	S += (DX4*MM[0])-1 < DX5__mem0*MM_MEM[0]
	S += DX5__mem0 <= DX5_

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	DX5__mem1 += alt(MM_MEM)
	S += (k1_5_Z6*MM[0])-1 < DX5__mem1*MM_MEM[1]
	S += DX5__mem1 <= DX5_

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	k1_0_Z11_in += alt(MM_in)
	k1_0_Z11 = S.Task('k1_0_Z11', length=4, delay_cost=1)
	k1_0_Z11 += alt(MM)
	S += k1_0_Z11>=k1_0_Z11_in

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	k1_0_Z11_mem0 += MAIN_MEM_r[0]
	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	k1_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k1_0_Z11_mem1*MM_MEM[1]
	S += k1_0_Z11_mem1 <= k1_0_Z11

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	NY5_in += alt(MM_in)
	NY5 = S.Task('NY5', length=4, delay_cost=1)
	NY5 += alt(MM)
	S += NY5>=NY5_in

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	NY5_mem0 += alt(MAS_MEM)
	S += (NY5_*MAS[0])-1 < NY5_mem0*MAS_MEM[0]
	S += (NY5_*MAS[1])-1 < NY5_mem0*MAS_MEM[2]
	S += (NY5_*MAS[2])-1 < NY5_mem0*MAS_MEM[4]
	S += (NY5_*MAS[3])-1 < NY5_mem0*MAS_MEM[6]
	S += NY5_mem0 <= NY5

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	NY5_mem1 += MAIN_MEM_r[1]
	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	k2_4_Z11_in += alt(MM_in)
	k2_4_Z11 = S.Task('k2_4_Z11', length=4, delay_cost=1)
	k2_4_Z11 += alt(MM)
	S += k2_4_Z11>=k2_4_Z11_in

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	k2_4_Z11_mem0 += MAIN_MEM_r[0]
	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	k2_4_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k2_4_Z11_mem1*MM_MEM[1]
	S += k2_4_Z11_mem1 <= k2_4_Z11

	DY5_ = S.Task('DY5_', length=1, delay_cost=1)
	DY5_ += alt(MAS)

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	DY5__mem0 += alt(MM_MEM)
	S += (DY4*MM[0])-1 < DY5__mem0*MM_MEM[0]
	S += DY5__mem0 <= DY5_

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	DY5__mem1 += MM_MEM[1]
	S += 49 < DY5__mem1
	S += DY5__mem1 <= DY5_

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	k3_5_Z11_in += alt(MM_in)
	k3_5_Z11 = S.Task('k3_5_Z11', length=4, delay_cost=1)
	k3_5_Z11 += alt(MM)
	S += k3_5_Z11>=k3_5_Z11_in

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	k3_5_Z11_mem0 += MAIN_MEM_r[0]
	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	k3_5_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k3_5_Z11_mem1*MM_MEM[1]
	S += k3_5_Z11_mem1 <= k3_5_Z11

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	Z_exp13_in += alt(MM_in)
	Z_exp13 = S.Task('Z_exp13', length=4, delay_cost=1)
	Z_exp13 += alt(MM)
	S += Z_exp13>=Z_exp13_in

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	Z_exp13_mem0 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < Z_exp13_mem0*MM_MEM[0]
	S += Z_exp13_mem0 <= Z_exp13

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	Z_exp13_mem1 += MAIN_MEM_r[1]
	NX6_ = S.Task('NX6_', length=1, delay_cost=1)
	NX6_ += alt(MAS)

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	NX6__mem0 += alt(MM_MEM)
	S += (NX5*MM[0])-1 < NX6__mem0*MM_MEM[0]
	S += NX6__mem0 <= NX6_

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	NX6__mem1 += MM_MEM[1]
	S += 46 < NX6__mem1
	S += NX6__mem1 <= NX6_

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	DX5_in += alt(MM_in)
	DX5 = S.Task('DX5', length=4, delay_cost=1)
	DX5 += alt(MM)
	S += DX5>=DX5_in

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	DX5_mem0 += alt(MAS_MEM)
	S += (DX5_*MAS[0])-1 < DX5_mem0*MAS_MEM[0]
	S += (DX5_*MAS[1])-1 < DX5_mem0*MAS_MEM[2]
	S += (DX5_*MAS[2])-1 < DX5_mem0*MAS_MEM[4]
	S += (DX5_*MAS[3])-1 < DX5_mem0*MAS_MEM[6]
	S += DX5_mem0 <= DX5

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	DX5_mem1 += MAIN_MEM_r[1]
	NY6_ = S.Task('NY6_', length=1, delay_cost=1)
	NY6_ += alt(MAS)

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	NY6__mem0 += alt(MM_MEM)
	S += (NY5*MM[0])-1 < NY6__mem0*MM_MEM[0]
	S += NY6__mem0 <= NY6_

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	NY6__mem1 += MM_MEM[1]
	S += 44 < NY6__mem1
	S += NY6__mem1 <= NY6_

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	k2_3_Z12_in += alt(MM_in)
	k2_3_Z12 = S.Task('k2_3_Z12', length=4, delay_cost=1)
	k2_3_Z12 += alt(MM)
	S += k2_3_Z12>=k2_3_Z12_in

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	k2_3_Z12_mem0 += MAIN_MEM_r[0]
	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	k2_3_Z12_mem1 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < k2_3_Z12_mem1*MM_MEM[1]
	S += k2_3_Z12_mem1 <= k2_3_Z12

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	DY5_in += alt(MM_in)
	DY5 = S.Task('DY5', length=4, delay_cost=1)
	DY5 += alt(MM)
	S += DY5>=DY5_in

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	DY5_mem0 += alt(MAS_MEM)
	S += (DY5_*MAS[0])-1 < DY5_mem0*MAS_MEM[0]
	S += (DY5_*MAS[1])-1 < DY5_mem0*MAS_MEM[2]
	S += (DY5_*MAS[2])-1 < DY5_mem0*MAS_MEM[4]
	S += (DY5_*MAS[3])-1 < DY5_mem0*MAS_MEM[6]
	S += DY5_mem0 <= DY5

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	DY5_mem1 += MAIN_MEM_r[1]
	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	k3_4_Z12_in += alt(MM_in)
	k3_4_Z12 = S.Task('k3_4_Z12', length=4, delay_cost=1)
	k3_4_Z12 += alt(MM)
	S += k3_4_Z12>=k3_4_Z12_in

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	k3_4_Z12_mem0 += MAIN_MEM_r[0]
	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	k3_4_Z12_mem1 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < k3_4_Z12_mem1*MM_MEM[1]
	S += k3_4_Z12_mem1 <= k3_4_Z12

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	Z_exp14_in += alt(MM_in)
	Z_exp14 = S.Task('Z_exp14', length=4, delay_cost=1)
	Z_exp14 += alt(MM)
	S += Z_exp14>=Z_exp14_in

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	Z_exp14_mem0 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < Z_exp14_mem0*MM_MEM[0]
	S += Z_exp14_mem0 <= Z_exp14

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	Z_exp14_mem1 += MAIN_MEM_r[1]
	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	NX6_in += alt(MM_in)
	NX6 = S.Task('NX6', length=4, delay_cost=1)
	NX6 += alt(MM)
	S += NX6>=NX6_in

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	NX6_mem0 += alt(MAS_MEM)
	S += (NX6_*MAS[0])-1 < NX6_mem0*MAS_MEM[0]
	S += (NX6_*MAS[1])-1 < NX6_mem0*MAS_MEM[2]
	S += (NX6_*MAS[2])-1 < NX6_mem0*MAS_MEM[4]
	S += (NX6_*MAS[3])-1 < NX6_mem0*MAS_MEM[6]
	S += NX6_mem0 <= NX6

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	NX6_mem1 += MAIN_MEM_r[1]
	DX6_ = S.Task('DX6_', length=1, delay_cost=1)
	DX6_ += alt(MAS)

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	DX6__mem0 += alt(MM_MEM)
	S += (DX5*MM[0])-1 < DX6__mem0*MM_MEM[0]
	S += DX6__mem0 <= DX6_

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	DX6__mem1 += MM_MEM[1]
	S += 54 < DX6__mem1
	S += DX6__mem1 <= DX6_

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	NY6_in += alt(MM_in)
	NY6 = S.Task('NY6', length=4, delay_cost=1)
	NY6 += alt(MM)
	S += NY6>=NY6_in

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	NY6_mem0 += alt(MAS_MEM)
	S += (NY6_*MAS[0])-1 < NY6_mem0*MAS_MEM[0]
	S += (NY6_*MAS[1])-1 < NY6_mem0*MAS_MEM[2]
	S += (NY6_*MAS[2])-1 < NY6_mem0*MAS_MEM[4]
	S += (NY6_*MAS[3])-1 < NY6_mem0*MAS_MEM[6]
	S += NY6_mem0 <= NY6

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	NY6_mem1 += MAIN_MEM_r[1]
	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	k2_2_Z13_in += alt(MM_in)
	k2_2_Z13 = S.Task('k2_2_Z13', length=4, delay_cost=1)
	k2_2_Z13 += alt(MM)
	S += k2_2_Z13>=k2_2_Z13_in

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	k2_2_Z13_mem0 += MAIN_MEM_r[0]
	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	k2_2_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k2_2_Z13_mem1*MM_MEM[1]
	S += k2_2_Z13_mem1 <= k2_2_Z13

	DY6_ = S.Task('DY6_', length=1, delay_cost=1)
	DY6_ += alt(MAS)

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	DY6__mem0 += alt(MM_MEM)
	S += (DY5*MM[0])-1 < DY6__mem0*MM_MEM[0]
	S += DY6__mem0 <= DY6_

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	DY6__mem1 += MM_MEM[1]
	S += 50 < DY6__mem1
	S += DY6__mem1 <= DY6_

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	k3_3_Z13_in += alt(MM_in)
	k3_3_Z13 = S.Task('k3_3_Z13', length=4, delay_cost=1)
	k3_3_Z13 += alt(MM)
	S += k3_3_Z13>=k3_3_Z13_in

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	k3_3_Z13_mem0 += MAIN_MEM_r[0]
	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	k3_3_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k3_3_Z13_mem1*MM_MEM[1]
	S += k3_3_Z13_mem1 <= k3_3_Z13

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	Z_exp15_in += alt(MM_in)
	Z_exp15 = S.Task('Z_exp15', length=4, delay_cost=1)
	Z_exp15 += alt(MM)
	S += Z_exp15>=Z_exp15_in

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	Z_exp15_mem0 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < Z_exp15_mem0*MM_MEM[0]
	S += Z_exp15_mem0 <= Z_exp15

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	Z_exp15_mem1 += MAIN_MEM_r[1]
	NX7_ = S.Task('NX7_', length=1, delay_cost=1)
	NX7_ += alt(MAS)

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	NX7__mem0 += alt(MM_MEM)
	S += (NX6*MM[0])-1 < NX7__mem0*MM_MEM[0]
	S += NX7__mem0 <= NX7_

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	NX7__mem1 += alt(MM_MEM)
	S += (k0_4_Z7*MM[0])-1 < NX7__mem1*MM_MEM[1]
	S += NX7__mem1 <= NX7_

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	DX6_in += alt(MM_in)
	DX6 = S.Task('DX6', length=4, delay_cost=1)
	DX6 += alt(MM)
	S += DX6>=DX6_in

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	DX6_mem0 += alt(MAS_MEM)
	S += (DX6_*MAS[0])-1 < DX6_mem0*MAS_MEM[0]
	S += (DX6_*MAS[1])-1 < DX6_mem0*MAS_MEM[2]
	S += (DX6_*MAS[2])-1 < DX6_mem0*MAS_MEM[4]
	S += (DX6_*MAS[3])-1 < DX6_mem0*MAS_MEM[6]
	S += DX6_mem0 <= DX6

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	DX6_mem1 += MAIN_MEM_r[1]
	NY7_ = S.Task('NY7_', length=1, delay_cost=1)
	NY7_ += alt(MAS)

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	NY7__mem0 += alt(MM_MEM)
	S += (NY6*MM[0])-1 < NY7__mem0*MM_MEM[0]
	S += NY7__mem0 <= NY7_

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	NY7__mem1 += alt(MM_MEM)
	S += (k2_8_Z7*MM[0])-1 < NY7__mem1*MM_MEM[1]
	S += NY7__mem1 <= NY7_

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	k2_1_Z14_in += alt(MM_in)
	k2_1_Z14 = S.Task('k2_1_Z14', length=4, delay_cost=1)
	k2_1_Z14 += alt(MM)
	S += k2_1_Z14>=k2_1_Z14_in

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	k2_1_Z14_mem0 += MAIN_MEM_r[0]
	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	k2_1_Z14_mem1 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < k2_1_Z14_mem1*MM_MEM[1]
	S += k2_1_Z14_mem1 <= k2_1_Z14

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	DY6_in += alt(MM_in)
	DY6 = S.Task('DY6', length=4, delay_cost=1)
	DY6 += alt(MM)
	S += DY6>=DY6_in

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	DY6_mem0 += alt(MAS_MEM)
	S += (DY6_*MAS[0])-1 < DY6_mem0*MAS_MEM[0]
	S += (DY6_*MAS[1])-1 < DY6_mem0*MAS_MEM[2]
	S += (DY6_*MAS[2])-1 < DY6_mem0*MAS_MEM[4]
	S += (DY6_*MAS[3])-1 < DY6_mem0*MAS_MEM[6]
	S += DY6_mem0 <= DY6

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	DY6_mem1 += MAIN_MEM_r[1]
	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	k3_2_Z14_in += alt(MM_in)
	k3_2_Z14 = S.Task('k3_2_Z14', length=4, delay_cost=1)
	k3_2_Z14 += alt(MM)
	S += k3_2_Z14>=k3_2_Z14_in

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	k3_2_Z14_mem0 += MAIN_MEM_r[0]
	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	k3_2_Z14_mem1 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < k3_2_Z14_mem1*MM_MEM[1]
	S += k3_2_Z14_mem1 <= k3_2_Z14

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage1MAS4/ISOGENY/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

