from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 132
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 0
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 0
	k0_10_Z1_mem0 += MAIN_MEM_r

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 0
	k0_10_Z1_mem1 += MAIN_MEM_r

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 1
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 1
	NX0_mem0 += MAIN_MEM_r

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 1
	NX0_mem1 += MAIN_MEM_r

	k0_10_Z1 = S.Task('k0_10_Z1', length=5, delay_cost=1)
	S += k0_10_Z1 >= 1
	k0_10_Z1 += MM[0]

	NX0 = S.Task('NX0', length=5, delay_cost=1)
	S += NX0 >= 2
	NX0 += MM[0]

	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 2
	Z_exp2_in += MM_in[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 2
	Z_exp2_mem0 += MAIN_MEM_r

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 2
	Z_exp2_mem1 += MAIN_MEM_r

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 3
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 3
	DY0_mem0 += MAIN_MEM_r

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 3
	DY0_mem1 += MAIN_MEM_r

	Z_exp2 = S.Task('Z_exp2', length=5, delay_cost=1)
	S += Z_exp2 >= 3
	Z_exp2 += MM[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 4
	DX0_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 4
	DX0_mem0 += MAIN_MEM_r

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 4
	DX0_mem1 += MAIN_MEM_r

	DY0 = S.Task('DY0', length=5, delay_cost=1)
	S += DY0 >= 4
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=5, delay_cost=1)
	S += DX0 >= 5
	DX0 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 5
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 5
	k2_14_Z1_mem0 += MAIN_MEM_r

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 5
	k2_14_Z1_mem1 += MAIN_MEM_r

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 6
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 6
	NX1__mem1 += MM_MEM[0]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 6
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 6
	NY0_mem0 += MAIN_MEM_r

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 6
	NY0_mem1 += MAIN_MEM_r

	k2_14_Z1 = S.Task('k2_14_Z1', length=5, delay_cost=1)
	S += k2_14_Z1 >= 6
	k2_14_Z1 += MM[0]

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 7
	NX1_ += MAS[0]

	NY0 = S.Task('NY0', length=5, delay_cost=1)
	S += NY0 >= 7
	NY0 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 7
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 7
	k3_14_Z2_mem0 += MAIN_MEM_r

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 7
	k3_14_Z2_mem1 += MM_MEM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 8
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 8
	k1_9_Z2_mem0 += MAIN_MEM_r

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 8
	k1_9_Z2_mem1 += MM_MEM[0]

	k3_14_Z2 = S.Task('k3_14_Z2', length=5, delay_cost=1)
	S += k3_14_Z2 >= 8
	k3_14_Z2 += MM[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 9
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 9
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 9
	Z_exp3_mem1 += MAIN_MEM_r

	k1_9_Z2 = S.Task('k1_9_Z2', length=5, delay_cost=1)
	S += k1_9_Z2 >= 9
	k1_9_Z2 += MM[0]

	Z_exp3 = S.Task('Z_exp3', length=5, delay_cost=1)
	S += Z_exp3 >= 10
	Z_exp3 += MM[0]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 10
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 10
	k0_9_Z2_mem0 += MAIN_MEM_r

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 10
	k0_9_Z2_mem1 += MM_MEM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 11
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 11
	NX1_mem0 += MAS_MEM[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 11
	NX1_mem1 += MAIN_MEM_r

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 11
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 11
	NY1__mem1 += MM_MEM[0]

	k0_9_Z2 = S.Task('k0_9_Z2', length=5, delay_cost=1)
	S += k0_9_Z2 >= 11
	k0_9_Z2 += MM[0]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 12
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 12
	DY1__mem1 += MM_MEM[0]

	NX1 = S.Task('NX1', length=5, delay_cost=1)
	S += NX1 >= 12
	NX1 += MM[0]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 12
	NY1_ += MAS[0]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 12
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 12
	NY1_mem0 += MAS_MEM[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 12
	NY1_mem1 += MAIN_MEM_r

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 13
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 13
	DX1__mem1 += MM_MEM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 13
	DY1_ += MAS[3]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 13
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 13
	DY1_mem0 += MAS_MEM[3]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 13
	DY1_mem1 += MAIN_MEM_r

	NY1 = S.Task('NY1', length=5, delay_cost=1)
	S += NY1 >= 13
	NY1 += MM[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 14
	DX1_ += MAS[0]

	DY1 = S.Task('DY1', length=5, delay_cost=1)
	S += DY1 >= 14
	DY1 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 14
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 14
	k3_13_Z3_mem0 += MAIN_MEM_r

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 14
	k3_13_Z3_mem1 += MM_MEM[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 15
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 15
	k2_13_Z2_mem0 += MAIN_MEM_r

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 15
	k2_13_Z2_mem1 += MM_MEM[0]

	k3_13_Z3 = S.Task('k3_13_Z3', length=5, delay_cost=1)
	S += k3_13_Z3 >= 15
	k3_13_Z3 += MM[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 16
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 16
	DX1_mem0 += MAS_MEM[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 16
	DX1_mem1 += MAIN_MEM_r

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 16
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 16
	NX2__mem1 += MM_MEM[0]

	k2_13_Z2 = S.Task('k2_13_Z2', length=5, delay_cost=1)
	S += k2_13_Z2 >= 16
	k2_13_Z2 += MM[0]

	DX1 = S.Task('DX1', length=5, delay_cost=1)
	S += DX1 >= 17
	DX1 += MM[0]

	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	S += NX2_ >= 17
	NX2_ += MAS[2]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 17
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 17
	k1_8_Z3_mem0 += MAIN_MEM_r

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 17
	k1_8_Z3_mem1 += MM_MEM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 18
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 18
	k0_8_Z3_mem0 += MAIN_MEM_r

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 18
	k0_8_Z3_mem1 += MM_MEM[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=5, delay_cost=1)
	S += k1_8_Z3 >= 18
	k1_8_Z3 += MM[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 19
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 19
	DY2__mem1 += MM_MEM[0]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 19
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 19
	NX2_mem0 += MAS_MEM[2]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 19
	NX2_mem1 += MAIN_MEM_r

	k0_8_Z3 = S.Task('k0_8_Z3', length=5, delay_cost=1)
	S += k0_8_Z3 >= 19
	k0_8_Z3 += MM[0]

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	S += DY2_ >= 20
	DY2_ += MAS[3]

	NX2 = S.Task('NX2', length=5, delay_cost=1)
	S += NX2 >= 20
	NX2 += MM[0]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 20
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 20
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 20
	Z_exp4_mem1 += MAIN_MEM_r

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 21
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 21
	DY2_mem0 += MAS_MEM[3]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 21
	DY2_mem1 += MAIN_MEM_r

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 21
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 21
	NY2__mem1 += MM_MEM[0]

	Z_exp4 = S.Task('Z_exp4', length=5, delay_cost=1)
	S += Z_exp4 >= 21
	Z_exp4 += MM[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 22
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 22
	DX2__mem1 += MM_MEM[0]

	DY2 = S.Task('DY2', length=5, delay_cost=1)
	S += DY2 >= 22
	DY2 += MM[0]

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	S += NY2_ >= 22
	NY2_ += MAS[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 22
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 22
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 22
	NY2_mem1 += MAIN_MEM_r

	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	S += DX2_ >= 23
	DX2_ += MAS[0]

	NY2 = S.Task('NY2', length=5, delay_cost=1)
	S += NY2 >= 23
	NY2 += MM[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 23
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 23
	k2_12_Z3_mem0 += MAIN_MEM_r

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 23
	k2_12_Z3_mem1 += MM_MEM[0]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 24
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 24
	DX2_mem0 += MAS_MEM[0]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 24
	DX2_mem1 += MAIN_MEM_r

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 24
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 24
	NX3__mem1 += MM_MEM[0]

	k2_12_Z3 = S.Task('k2_12_Z3', length=5, delay_cost=1)
	S += k2_12_Z3 >= 24
	k2_12_Z3 += MM[0]

	DX2 = S.Task('DX2', length=5, delay_cost=1)
	S += DX2 >= 25
	DX2 += MM[0]

	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	S += NX3_ >= 25
	NX3_ += MAS[3]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 25
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 25
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 25
	Z_exp5_mem1 += MAIN_MEM_r

	Z_exp5 = S.Task('Z_exp5', length=5, delay_cost=1)
	S += Z_exp5 >= 26
	Z_exp5 += MM[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 26
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 26
	k2_11_Z4_mem0 += MAIN_MEM_r

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 26
	k2_11_Z4_mem1 += MM_MEM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 27
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 27
	k0_7_Z4_mem0 += MAIN_MEM_r

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 27
	k0_7_Z4_mem1 += MM_MEM[0]

	k2_11_Z4 = S.Task('k2_11_Z4', length=5, delay_cost=1)
	S += k2_11_Z4 >= 27
	k2_11_Z4 += MM[0]

	k0_7_Z4 = S.Task('k0_7_Z4', length=5, delay_cost=1)
	S += k0_7_Z4 >= 28
	k0_7_Z4 += MM[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 28
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 28
	k3_12_Z4_mem0 += MAIN_MEM_r

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 28
	k3_12_Z4_mem1 += MM_MEM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 29
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 29
	k1_7_Z4_mem0 += MAIN_MEM_r

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 29
	k1_7_Z4_mem1 += MM_MEM[0]

	k3_12_Z4 = S.Task('k3_12_Z4', length=5, delay_cost=1)
	S += k3_12_Z4 >= 29
	k3_12_Z4 += MM[0]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 30
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 30
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 30
	Z_exp6_mem1 += MAIN_MEM_r

	k1_7_Z4 = S.Task('k1_7_Z4', length=5, delay_cost=1)
	S += k1_7_Z4 >= 30
	k1_7_Z4 += MM[0]

	Z_exp6 = S.Task('Z_exp6', length=5, delay_cost=1)
	S += Z_exp6 >= 31
	Z_exp6 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 31
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 31
	k3_11_Z5_mem0 += MAIN_MEM_r

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 31
	k3_11_Z5_mem1 += MM_MEM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 32
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 32
	k0_6_Z5_mem0 += MAIN_MEM_r

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 32
	k0_6_Z5_mem1 += MM_MEM[0]

	k3_11_Z5 = S.Task('k3_11_Z5', length=5, delay_cost=1)
	S += k3_11_Z5 >= 32
	k3_11_Z5 += MM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=5, delay_cost=1)
	S += k0_6_Z5 >= 33
	k0_6_Z5 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 33
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 33
	k2_10_Z5_mem0 += MAIN_MEM_r

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 33
	k2_10_Z5_mem1 += MM_MEM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 34
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 34
	k1_6_Z5_mem0 += MAIN_MEM_r

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 34
	k1_6_Z5_mem1 += MM_MEM[0]

	k2_10_Z5 = S.Task('k2_10_Z5', length=5, delay_cost=1)
	S += k2_10_Z5 >= 34
	k2_10_Z5 += MM[0]

	k1_6_Z5 = S.Task('k1_6_Z5', length=5, delay_cost=1)
	S += k1_6_Z5 >= 35
	k1_6_Z5 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 35
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 35
	k3_10_Z6_mem0 += MAIN_MEM_r

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 35
	k3_10_Z6_mem1 += MM_MEM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 36
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 36
	k2_9_Z6_mem0 += MAIN_MEM_r

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 36
	k2_9_Z6_mem1 += MM_MEM[0]

	k3_10_Z6 = S.Task('k3_10_Z6', length=5, delay_cost=1)
	S += k3_10_Z6 >= 36
	k3_10_Z6 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 37
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 37
	k0_5_Z6_mem0 += MAIN_MEM_r

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 37
	k0_5_Z6_mem1 += MM_MEM[0]

	k2_9_Z6 = S.Task('k2_9_Z6', length=5, delay_cost=1)
	S += k2_9_Z6 >= 37
	k2_9_Z6 += MM[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 38
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 38
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 38
	Z_exp7_mem1 += MAIN_MEM_r

	k0_5_Z6 = S.Task('k0_5_Z6', length=5, delay_cost=1)
	S += k0_5_Z6 >= 38
	k0_5_Z6 += MM[0]

	Z_exp7 = S.Task('Z_exp7', length=5, delay_cost=1)
	S += Z_exp7 >= 39
	Z_exp7 += MM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 39
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 39
	k1_5_Z6_mem0 += MAIN_MEM_r

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 39
	k1_5_Z6_mem1 += MM_MEM[0]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 40
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 40
	NY3__mem1 += MM_MEM[0]

	k1_5_Z6 = S.Task('k1_5_Z6', length=5, delay_cost=1)
	S += k1_5_Z6 >= 40
	k1_5_Z6 += MM[0]

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
	S += NY3_ >= 41
	NY3_ += MAS[0]


	# new tasks
	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	Z_exp8_in += alt(MM_in)
	Z_exp8 = S.Task('Z_exp8', length=5, delay_cost=1)
	Z_exp8 += alt(MM)
	S += Z_exp8>=Z_exp8_in

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	Z_exp8_mem0 += MM_MEM[0]
	S += 43 < Z_exp8_mem0
	S += Z_exp8_mem0 <= Z_exp8

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	Z_exp8_mem1 += MAIN_MEM_r
	S += Z_exp8_mem1 <= Z_exp8

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	NX3_in += alt(MM_in)
	NX3 = S.Task('NX3', length=5, delay_cost=1)
	NX3 += alt(MM)
	S += NX3>=NX3_in

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	NX3_mem0 += MAS_MEM[3]
	S += 25 < NX3_mem0
	S += NX3_mem0 <= NX3

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	NX3_mem1 += MAIN_MEM_r
	S += NX3_mem1 <= NX3

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	k0_4_Z7_in += alt(MM_in)
	k0_4_Z7 = S.Task('k0_4_Z7', length=5, delay_cost=1)
	k0_4_Z7 += alt(MM)
	S += k0_4_Z7>=k0_4_Z7_in

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	k0_4_Z7_mem0 += MAIN_MEM_r
	S += k0_4_Z7_mem0 <= k0_4_Z7

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	k0_4_Z7_mem1 += MM_MEM[0]
	S += 43 < k0_4_Z7_mem1
	S += k0_4_Z7_mem1 <= k0_4_Z7

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	DX3_ += alt(MAS)

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	DX3__mem0 += MM_MEM[0]
	S += 29 < DX3__mem0
	S += DX3__mem0 <= DX3_

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	DX3__mem1 += MM_MEM[0]
	S += 34 < DX3__mem1
	S += DX3__mem1 <= DX3_

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	k1_4_Z7_in += alt(MM_in)
	k1_4_Z7 = S.Task('k1_4_Z7', length=5, delay_cost=1)
	k1_4_Z7 += alt(MM)
	S += k1_4_Z7>=k1_4_Z7_in

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	k1_4_Z7_mem0 += MAIN_MEM_r
	S += k1_4_Z7_mem0 <= k1_4_Z7

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	k1_4_Z7_mem1 += MM_MEM[0]
	S += 43 < k1_4_Z7_mem1
	S += k1_4_Z7_mem1 <= k1_4_Z7

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	NY3_in += alt(MM_in)
	NY3 = S.Task('NY3', length=5, delay_cost=1)
	NY3 += alt(MM)
	S += NY3>=NY3_in

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	NY3_mem0 += MAS_MEM[0]
	S += 41 < NY3_mem0
	S += NY3_mem0 <= NY3

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	NY3_mem1 += MAIN_MEM_r
	S += NY3_mem1 <= NY3

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	k2_8_Z7_in += alt(MM_in)
	k2_8_Z7 = S.Task('k2_8_Z7', length=5, delay_cost=1)
	k2_8_Z7 += alt(MM)
	S += k2_8_Z7>=k2_8_Z7_in

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	k2_8_Z7_mem0 += MAIN_MEM_r
	S += k2_8_Z7_mem0 <= k2_8_Z7

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	k2_8_Z7_mem1 += MM_MEM[0]
	S += 43 < k2_8_Z7_mem1
	S += k2_8_Z7_mem1 <= k2_8_Z7

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	DY3_ += alt(MAS)

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	DY3__mem0 += MM_MEM[0]
	S += 26 < DY3__mem0
	S += DY3__mem0 <= DY3_

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	DY3__mem1 += MM_MEM[0]
	S += 33 < DY3__mem1
	S += DY3__mem1 <= DY3_

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	k3_9_Z7_in += alt(MM_in)
	k3_9_Z7 = S.Task('k3_9_Z7', length=5, delay_cost=1)
	k3_9_Z7 += alt(MM)
	S += k3_9_Z7>=k3_9_Z7_in

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	k3_9_Z7_mem0 += MAIN_MEM_r
	S += k3_9_Z7_mem0 <= k3_9_Z7

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	k3_9_Z7_mem1 += MM_MEM[0]
	S += 43 < k3_9_Z7_mem1
	S += k3_9_Z7_mem1 <= k3_9_Z7

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	Z_exp9_in += alt(MM_in)
	Z_exp9 = S.Task('Z_exp9', length=5, delay_cost=1)
	Z_exp9 += alt(MM)
	S += Z_exp9>=Z_exp9_in

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	Z_exp9_mem0 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < Z_exp9_mem0*MM_MEM[0]
	S += Z_exp9_mem0 <= Z_exp9

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	Z_exp9_mem1 += MAIN_MEM_r
	S += Z_exp9_mem1 <= Z_exp9

	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	NX4_ += alt(MAS)

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	NX4__mem0 += alt(MM_MEM)
	S += (NX3*MM[0])-1 < NX4__mem0*MM_MEM[0]
	S += NX4__mem0 <= NX4_

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	NX4__mem1 += MM_MEM[0]
	S += 32 < NX4__mem1
	S += NX4__mem1 <= NX4_

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	k0_3_Z8_in += alt(MM_in)
	k0_3_Z8 = S.Task('k0_3_Z8', length=5, delay_cost=1)
	k0_3_Z8 += alt(MM)
	S += k0_3_Z8>=k0_3_Z8_in

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	k0_3_Z8_mem0 += MAIN_MEM_r
	S += k0_3_Z8_mem0 <= k0_3_Z8

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	k0_3_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k0_3_Z8_mem1*MM_MEM[0]
	S += k0_3_Z8_mem1 <= k0_3_Z8

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	DX3_in += alt(MM_in)
	DX3 = S.Task('DX3', length=5, delay_cost=1)
	DX3 += alt(MM)
	S += DX3>=DX3_in

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	DX3_mem0 += alt(MAS_MEM)
	S += (DX3_*MAS[0])-1 < DX3_mem0*MAS_MEM[0]
	S += (DX3_*MAS[1])-1 < DX3_mem0*MAS_MEM[1]
	S += (DX3_*MAS[2])-1 < DX3_mem0*MAS_MEM[2]
	S += (DX3_*MAS[3])-1 < DX3_mem0*MAS_MEM[3]
	S += DX3_mem0 <= DX3

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	DX3_mem1 += MAIN_MEM_r
	S += DX3_mem1 <= DX3

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	k1_3_Z8_in += alt(MM_in)
	k1_3_Z8 = S.Task('k1_3_Z8', length=5, delay_cost=1)
	k1_3_Z8 += alt(MM)
	S += k1_3_Z8>=k1_3_Z8_in

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	k1_3_Z8_mem0 += MAIN_MEM_r
	S += k1_3_Z8_mem0 <= k1_3_Z8

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	k1_3_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k1_3_Z8_mem1*MM_MEM[0]
	S += k1_3_Z8_mem1 <= k1_3_Z8

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	NY4_ += alt(MAS)

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	NY4__mem0 += alt(MM_MEM)
	S += (NY3*MM[0])-1 < NY4__mem0*MM_MEM[0]
	S += NY4__mem0 <= NY4_

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	NY4__mem1 += MM_MEM[0]
	S += 31 < NY4__mem1
	S += NY4__mem1 <= NY4_

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	k2_7_Z8_in += alt(MM_in)
	k2_7_Z8 = S.Task('k2_7_Z8', length=5, delay_cost=1)
	k2_7_Z8 += alt(MM)
	S += k2_7_Z8>=k2_7_Z8_in

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	k2_7_Z8_mem0 += MAIN_MEM_r
	S += k2_7_Z8_mem0 <= k2_7_Z8

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	k2_7_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k2_7_Z8_mem1*MM_MEM[0]
	S += k2_7_Z8_mem1 <= k2_7_Z8

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	DY3_in += alt(MM_in)
	DY3 = S.Task('DY3', length=5, delay_cost=1)
	DY3 += alt(MM)
	S += DY3>=DY3_in

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	DY3_mem0 += alt(MAS_MEM)
	S += (DY3_*MAS[0])-1 < DY3_mem0*MAS_MEM[0]
	S += (DY3_*MAS[1])-1 < DY3_mem0*MAS_MEM[1]
	S += (DY3_*MAS[2])-1 < DY3_mem0*MAS_MEM[2]
	S += (DY3_*MAS[3])-1 < DY3_mem0*MAS_MEM[3]
	S += DY3_mem0 <= DY3

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	DY3_mem1 += MAIN_MEM_r
	S += DY3_mem1 <= DY3

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	k3_8_Z8_in += alt(MM_in)
	k3_8_Z8 = S.Task('k3_8_Z8', length=5, delay_cost=1)
	k3_8_Z8 += alt(MM)
	S += k3_8_Z8>=k3_8_Z8_in

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	k3_8_Z8_mem0 += MAIN_MEM_r
	S += k3_8_Z8_mem0 <= k3_8_Z8

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	k3_8_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k3_8_Z8_mem1*MM_MEM[0]
	S += k3_8_Z8_mem1 <= k3_8_Z8

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	Z_exp10_in += alt(MM_in)
	Z_exp10 = S.Task('Z_exp10', length=5, delay_cost=1)
	Z_exp10 += alt(MM)
	S += Z_exp10>=Z_exp10_in

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	Z_exp10_mem0 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < Z_exp10_mem0*MM_MEM[0]
	S += Z_exp10_mem0 <= Z_exp10

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	Z_exp10_mem1 += MAIN_MEM_r
	S += Z_exp10_mem1 <= Z_exp10

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	NX4_in += alt(MM_in)
	NX4 = S.Task('NX4', length=5, delay_cost=1)
	NX4 += alt(MM)
	S += NX4>=NX4_in

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	NX4_mem0 += alt(MAS_MEM)
	S += (NX4_*MAS[0])-1 < NX4_mem0*MAS_MEM[0]
	S += (NX4_*MAS[1])-1 < NX4_mem0*MAS_MEM[1]
	S += (NX4_*MAS[2])-1 < NX4_mem0*MAS_MEM[2]
	S += (NX4_*MAS[3])-1 < NX4_mem0*MAS_MEM[3]
	S += NX4_mem0 <= NX4

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	NX4_mem1 += MAIN_MEM_r
	S += NX4_mem1 <= NX4

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	k0_2_Z9_in += alt(MM_in)
	k0_2_Z9 = S.Task('k0_2_Z9', length=5, delay_cost=1)
	k0_2_Z9 += alt(MM)
	S += k0_2_Z9>=k0_2_Z9_in

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	k0_2_Z9_mem0 += MAIN_MEM_r
	S += k0_2_Z9_mem0 <= k0_2_Z9

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	k0_2_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k0_2_Z9_mem1*MM_MEM[0]
	S += k0_2_Z9_mem1 <= k0_2_Z9

	DX4_ = S.Task('DX4_', length=1, delay_cost=1)
	DX4_ += alt(MAS)

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	DX4__mem0 += alt(MM_MEM)
	S += (DX3*MM[0])-1 < DX4__mem0*MM_MEM[0]
	S += DX4__mem0 <= DX4_

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	DX4__mem1 += MM_MEM[0]
	S += 39 < DX4__mem1
	S += DX4__mem1 <= DX4_

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	k1_2_Z9_in += alt(MM_in)
	k1_2_Z9 = S.Task('k1_2_Z9', length=5, delay_cost=1)
	k1_2_Z9 += alt(MM)
	S += k1_2_Z9>=k1_2_Z9_in

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	k1_2_Z9_mem0 += MAIN_MEM_r
	S += k1_2_Z9_mem0 <= k1_2_Z9

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	k1_2_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k1_2_Z9_mem1*MM_MEM[0]
	S += k1_2_Z9_mem1 <= k1_2_Z9

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	NY4_in += alt(MM_in)
	NY4 = S.Task('NY4', length=5, delay_cost=1)
	NY4 += alt(MM)
	S += NY4>=NY4_in

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	NY4_mem0 += alt(MAS_MEM)
	S += (NY4_*MAS[0])-1 < NY4_mem0*MAS_MEM[0]
	S += (NY4_*MAS[1])-1 < NY4_mem0*MAS_MEM[1]
	S += (NY4_*MAS[2])-1 < NY4_mem0*MAS_MEM[2]
	S += (NY4_*MAS[3])-1 < NY4_mem0*MAS_MEM[3]
	S += NY4_mem0 <= NY4

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	NY4_mem1 += MAIN_MEM_r
	S += NY4_mem1 <= NY4

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	k2_6_Z9_in += alt(MM_in)
	k2_6_Z9 = S.Task('k2_6_Z9', length=5, delay_cost=1)
	k2_6_Z9 += alt(MM)
	S += k2_6_Z9>=k2_6_Z9_in

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	k2_6_Z9_mem0 += MAIN_MEM_r
	S += k2_6_Z9_mem0 <= k2_6_Z9

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	k2_6_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k2_6_Z9_mem1*MM_MEM[0]
	S += k2_6_Z9_mem1 <= k2_6_Z9

	DY4_ = S.Task('DY4_', length=1, delay_cost=1)
	DY4_ += alt(MAS)

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	DY4__mem0 += alt(MM_MEM)
	S += (DY3*MM[0])-1 < DY4__mem0*MM_MEM[0]
	S += DY4__mem0 <= DY4_

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	DY4__mem1 += MM_MEM[0]
	S += 36 < DY4__mem1
	S += DY4__mem1 <= DY4_

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	k3_7_Z9_in += alt(MM_in)
	k3_7_Z9 = S.Task('k3_7_Z9', length=5, delay_cost=1)
	k3_7_Z9 += alt(MM)
	S += k3_7_Z9>=k3_7_Z9_in

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	k3_7_Z9_mem0 += MAIN_MEM_r
	S += k3_7_Z9_mem0 <= k3_7_Z9

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	k3_7_Z9_mem1 += alt(MM_MEM)
	S += (Z_exp9*MM[0])-1 < k3_7_Z9_mem1*MM_MEM[0]
	S += k3_7_Z9_mem1 <= k3_7_Z9

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	Z_exp11_in += alt(MM_in)
	Z_exp11 = S.Task('Z_exp11', length=5, delay_cost=1)
	Z_exp11 += alt(MM)
	S += Z_exp11>=Z_exp11_in

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	Z_exp11_mem0 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < Z_exp11_mem0*MM_MEM[0]
	S += Z_exp11_mem0 <= Z_exp11

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	Z_exp11_mem1 += MAIN_MEM_r
	S += Z_exp11_mem1 <= Z_exp11

	NX5_ = S.Task('NX5_', length=1, delay_cost=1)
	NX5_ += alt(MAS)

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	NX5__mem0 += alt(MM_MEM)
	S += (NX4*MM[0])-1 < NX5__mem0*MM_MEM[0]
	S += NX5__mem0 <= NX5_

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	NX5__mem1 += MM_MEM[0]
	S += 37 < NX5__mem1
	S += NX5__mem1 <= NX5_

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	k0_1_Z10_in += alt(MM_in)
	k0_1_Z10 = S.Task('k0_1_Z10', length=5, delay_cost=1)
	k0_1_Z10 += alt(MM)
	S += k0_1_Z10>=k0_1_Z10_in

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	k0_1_Z10_mem0 += MAIN_MEM_r
	S += k0_1_Z10_mem0 <= k0_1_Z10

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	k0_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k0_1_Z10_mem1*MM_MEM[0]
	S += k0_1_Z10_mem1 <= k0_1_Z10

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	DX4_in += alt(MM_in)
	DX4 = S.Task('DX4', length=5, delay_cost=1)
	DX4 += alt(MM)
	S += DX4>=DX4_in

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	DX4_mem0 += alt(MAS_MEM)
	S += (DX4_*MAS[0])-1 < DX4_mem0*MAS_MEM[0]
	S += (DX4_*MAS[1])-1 < DX4_mem0*MAS_MEM[1]
	S += (DX4_*MAS[2])-1 < DX4_mem0*MAS_MEM[2]
	S += (DX4_*MAS[3])-1 < DX4_mem0*MAS_MEM[3]
	S += DX4_mem0 <= DX4

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	DX4_mem1 += MAIN_MEM_r
	S += DX4_mem1 <= DX4

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	k1_1_Z10_in += alt(MM_in)
	k1_1_Z10 = S.Task('k1_1_Z10', length=5, delay_cost=1)
	k1_1_Z10 += alt(MM)
	S += k1_1_Z10>=k1_1_Z10_in

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	k1_1_Z10_mem0 += MAIN_MEM_r
	S += k1_1_Z10_mem0 <= k1_1_Z10

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	k1_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k1_1_Z10_mem1*MM_MEM[0]
	S += k1_1_Z10_mem1 <= k1_1_Z10

	NY5_ = S.Task('NY5_', length=1, delay_cost=1)
	NY5_ += alt(MAS)

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	NY5__mem0 += alt(MM_MEM)
	S += (NY4*MM[0])-1 < NY5__mem0*MM_MEM[0]
	S += NY5__mem0 <= NY5_

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	NY5__mem1 += MM_MEM[0]
	S += 38 < NY5__mem1
	S += NY5__mem1 <= NY5_

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	k2_5_Z10_in += alt(MM_in)
	k2_5_Z10 = S.Task('k2_5_Z10', length=5, delay_cost=1)
	k2_5_Z10 += alt(MM)
	S += k2_5_Z10>=k2_5_Z10_in

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	k2_5_Z10_mem0 += MAIN_MEM_r
	S += k2_5_Z10_mem0 <= k2_5_Z10

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	k2_5_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k2_5_Z10_mem1*MM_MEM[0]
	S += k2_5_Z10_mem1 <= k2_5_Z10

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	DY4_in += alt(MM_in)
	DY4 = S.Task('DY4', length=5, delay_cost=1)
	DY4 += alt(MM)
	S += DY4>=DY4_in

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	DY4_mem0 += alt(MAS_MEM)
	S += (DY4_*MAS[0])-1 < DY4_mem0*MAS_MEM[0]
	S += (DY4_*MAS[1])-1 < DY4_mem0*MAS_MEM[1]
	S += (DY4_*MAS[2])-1 < DY4_mem0*MAS_MEM[2]
	S += (DY4_*MAS[3])-1 < DY4_mem0*MAS_MEM[3]
	S += DY4_mem0 <= DY4

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	DY4_mem1 += MAIN_MEM_r
	S += DY4_mem1 <= DY4

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	k3_6_Z10_in += alt(MM_in)
	k3_6_Z10 = S.Task('k3_6_Z10', length=5, delay_cost=1)
	k3_6_Z10 += alt(MM)
	S += k3_6_Z10>=k3_6_Z10_in

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	k3_6_Z10_mem0 += MAIN_MEM_r
	S += k3_6_Z10_mem0 <= k3_6_Z10

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	k3_6_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k3_6_Z10_mem1*MM_MEM[0]
	S += k3_6_Z10_mem1 <= k3_6_Z10

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	Z_exp12_in += alt(MM_in)
	Z_exp12 = S.Task('Z_exp12', length=5, delay_cost=1)
	Z_exp12 += alt(MM)
	S += Z_exp12>=Z_exp12_in

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	Z_exp12_mem0 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < Z_exp12_mem0*MM_MEM[0]
	S += Z_exp12_mem0 <= Z_exp12

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	Z_exp12_mem1 += MAIN_MEM_r
	S += Z_exp12_mem1 <= Z_exp12

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	NX5_in += alt(MM_in)
	NX5 = S.Task('NX5', length=5, delay_cost=1)
	NX5 += alt(MM)
	S += NX5>=NX5_in

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	NX5_mem0 += alt(MAS_MEM)
	S += (NX5_*MAS[0])-1 < NX5_mem0*MAS_MEM[0]
	S += (NX5_*MAS[1])-1 < NX5_mem0*MAS_MEM[1]
	S += (NX5_*MAS[2])-1 < NX5_mem0*MAS_MEM[2]
	S += (NX5_*MAS[3])-1 < NX5_mem0*MAS_MEM[3]
	S += NX5_mem0 <= NX5

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	NX5_mem1 += MAIN_MEM_r
	S += NX5_mem1 <= NX5

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	k0_0_Z11_in += alt(MM_in)
	k0_0_Z11 = S.Task('k0_0_Z11', length=5, delay_cost=1)
	k0_0_Z11 += alt(MM)
	S += k0_0_Z11>=k0_0_Z11_in

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	k0_0_Z11_mem0 += MAIN_MEM_r
	S += k0_0_Z11_mem0 <= k0_0_Z11

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	k0_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k0_0_Z11_mem1*MM_MEM[0]
	S += k0_0_Z11_mem1 <= k0_0_Z11

	DX5_ = S.Task('DX5_', length=1, delay_cost=1)
	DX5_ += alt(MAS)

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	DX5__mem0 += alt(MM_MEM)
	S += (DX4*MM[0])-1 < DX5__mem0*MM_MEM[0]
	S += DX5__mem0 <= DX5_

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	DX5__mem1 += MM_MEM[0]
	S += 44 < DX5__mem1
	S += DX5__mem1 <= DX5_

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	k1_0_Z11_in += alt(MM_in)
	k1_0_Z11 = S.Task('k1_0_Z11', length=5, delay_cost=1)
	k1_0_Z11 += alt(MM)
	S += k1_0_Z11>=k1_0_Z11_in

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	k1_0_Z11_mem0 += MAIN_MEM_r
	S += k1_0_Z11_mem0 <= k1_0_Z11

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	k1_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k1_0_Z11_mem1*MM_MEM[0]
	S += k1_0_Z11_mem1 <= k1_0_Z11

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	NY5_in += alt(MM_in)
	NY5 = S.Task('NY5', length=5, delay_cost=1)
	NY5 += alt(MM)
	S += NY5>=NY5_in

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	NY5_mem0 += alt(MAS_MEM)
	S += (NY5_*MAS[0])-1 < NY5_mem0*MAS_MEM[0]
	S += (NY5_*MAS[1])-1 < NY5_mem0*MAS_MEM[1]
	S += (NY5_*MAS[2])-1 < NY5_mem0*MAS_MEM[2]
	S += (NY5_*MAS[3])-1 < NY5_mem0*MAS_MEM[3]
	S += NY5_mem0 <= NY5

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	NY5_mem1 += MAIN_MEM_r
	S += NY5_mem1 <= NY5

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	k2_4_Z11_in += alt(MM_in)
	k2_4_Z11 = S.Task('k2_4_Z11', length=5, delay_cost=1)
	k2_4_Z11 += alt(MM)
	S += k2_4_Z11>=k2_4_Z11_in

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	k2_4_Z11_mem0 += MAIN_MEM_r
	S += k2_4_Z11_mem0 <= k2_4_Z11

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	k2_4_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k2_4_Z11_mem1*MM_MEM[0]
	S += k2_4_Z11_mem1 <= k2_4_Z11

	DY5_ = S.Task('DY5_', length=1, delay_cost=1)
	DY5_ += alt(MAS)

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	DY5__mem0 += alt(MM_MEM)
	S += (DY4*MM[0])-1 < DY5__mem0*MM_MEM[0]
	S += DY5__mem0 <= DY5_

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	DY5__mem1 += MM_MEM[0]
	S += 40 < DY5__mem1
	S += DY5__mem1 <= DY5_

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	k3_5_Z11_in += alt(MM_in)
	k3_5_Z11 = S.Task('k3_5_Z11', length=5, delay_cost=1)
	k3_5_Z11 += alt(MM)
	S += k3_5_Z11>=k3_5_Z11_in

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	k3_5_Z11_mem0 += MAIN_MEM_r
	S += k3_5_Z11_mem0 <= k3_5_Z11

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	k3_5_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k3_5_Z11_mem1*MM_MEM[0]
	S += k3_5_Z11_mem1 <= k3_5_Z11

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/ISOGENY/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

