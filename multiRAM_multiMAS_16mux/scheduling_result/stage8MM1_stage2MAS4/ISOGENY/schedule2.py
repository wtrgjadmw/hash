from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 191
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 0
	Z_exp2_in += MM_in[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 0
	Z_exp2_mem0 += MAIN_MEM_r[0]

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 0
	Z_exp2_mem1 += MAIN_MEM_r[1]

	Z_exp2 = S.Task('Z_exp2', length=8, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 1
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 1
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 1
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 2
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 2
	NY0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 2
	NY0_mem1 += MAIN_MEM_r[1]

	k2_14_Z1 = S.Task('k2_14_Z1', length=8, delay_cost=1)
	S += k2_14_Z1 >= 2
	k2_14_Z1 += MM[0]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 3
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 3
	NX0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 3
	NX0_mem1 += MAIN_MEM_r[1]

	NY0 = S.Task('NY0', length=8, delay_cost=1)
	S += NY0 >= 3
	NY0 += MM[0]

	NX0 = S.Task('NX0', length=8, delay_cost=1)
	S += NX0 >= 4
	NX0 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 4
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 4
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 4
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 5
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 5
	DY0_mem0 += MAIN_MEM_r[0]

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 5
	DY0_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=8, delay_cost=1)
	S += k0_10_Z1 >= 5
	k0_10_Z1 += MM[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 6
	DX0_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 6
	DX0_mem0 += MAIN_MEM_r[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 6
	DX0_mem1 += MAIN_MEM_r[1]

	DY0 = S.Task('DY0', length=8, delay_cost=1)
	S += DY0 >= 6
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=8, delay_cost=1)
	S += DX0 >= 7
	DX0 += MM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 8
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 8
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 8
	k1_9_Z2_mem1 += MM_MEM[1]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 9
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 9
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 9
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k1_9_Z2 = S.Task('k1_9_Z2', length=8, delay_cost=1)
	S += k1_9_Z2 >= 9
	k1_9_Z2 += MM[0]

	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	S += NY1__in >= 10
	NY1__in += MAS_in[0]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 10
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 10
	NY1__mem1 += MM_MEM[1]

	Z_exp3 = S.Task('Z_exp3', length=8, delay_cost=1)
	S += Z_exp3 >= 10
	Z_exp3 += MM[0]

	NY1_ = S.Task('NY1_', length=2, delay_cost=1)
	S += NY1_ >= 11
	NY1_ += MAS[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 11
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 11
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 11
	k2_13_Z2_mem1 += MM_MEM[1]

	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	S += NX1__in >= 12
	NX1__in += MAS_in[0]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 12
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 12
	NX1__mem1 += MM_MEM[1]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 12
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 12
	NY1_mem0 += MAS_MEM[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 12
	NY1_mem1 += MAIN_MEM_r[1]

	k2_13_Z2 = S.Task('k2_13_Z2', length=8, delay_cost=1)
	S += k2_13_Z2 >= 12
	k2_13_Z2 += MM[0]

	NX1_ = S.Task('NX1_', length=2, delay_cost=1)
	S += NX1_ >= 13
	NX1_ += MAS[0]

	NY1 = S.Task('NY1', length=8, delay_cost=1)
	S += NY1 >= 13
	NY1 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 13
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 13
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 13
	k3_14_Z2_mem1 += MM_MEM[1]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 14
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 14
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 14
	k0_9_Z2_mem1 += MM_MEM[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=8, delay_cost=1)
	S += k3_14_Z2 >= 14
	k3_14_Z2 += MM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 15
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 15
	NX1_mem0 += MAS_MEM[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 15
	NX1_mem1 += MAIN_MEM_r[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=8, delay_cost=1)
	S += k0_9_Z2 >= 15
	k0_9_Z2 += MM[0]

	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	S += DX1__in >= 16
	DX1__in += MAS_in[0]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 16
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 16
	DX1__mem1 += MM_MEM[1]

	NX1 = S.Task('NX1', length=8, delay_cost=1)
	S += NX1 >= 16
	NX1 += MM[0]

	DX1_ = S.Task('DX1_', length=2, delay_cost=1)
	S += DX1_ >= 17
	DX1_ += MAS[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 17
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 17
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 17
	k1_8_Z3_mem1 += MM_MEM[1]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 18
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 18
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 18
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k1_8_Z3 = S.Task('k1_8_Z3', length=8, delay_cost=1)
	S += k1_8_Z3 >= 18
	k1_8_Z3 += MM[0]

	Z_exp4 = S.Task('Z_exp4', length=8, delay_cost=1)
	S += Z_exp4 >= 19
	Z_exp4 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 19
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 19
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 19
	k0_8_Z3_mem1 += MM_MEM[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=8, delay_cost=1)
	S += k0_8_Z3 >= 20
	k0_8_Z3 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 20
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 20
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 20
	k3_13_Z3_mem1 += MM_MEM[1]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 21
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 21
	DX1_mem0 += MAS_MEM[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 21
	DX1_mem1 += MAIN_MEM_r[1]

	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	S += DY1__in >= 21
	DY1__in += MAS_in[0]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 21
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 21
	DY1__mem1 += MM_MEM[1]

	k3_13_Z3 = S.Task('k3_13_Z3', length=8, delay_cost=1)
	S += k3_13_Z3 >= 21
	k3_13_Z3 += MM[0]

	DX1 = S.Task('DX1', length=8, delay_cost=1)
	S += DX1 >= 22
	DX1 += MM[0]

	DY1_ = S.Task('DY1_', length=2, delay_cost=1)
	S += DY1_ >= 22
	DY1_ += MAS[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 22
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 22
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 22
	k2_12_Z3_mem1 += MM_MEM[1]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 23
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 23
	DY1_mem0 += MAS_MEM[0]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 23
	DY1_mem1 += MAIN_MEM_r[1]

	NX2__in = S.Task('NX2__in', length=1, delay_cost=1)
	S += NX2__in >= 23
	NX2__in += MAS_in[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 23
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 23
	NX2__mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=8, delay_cost=1)
	S += k2_12_Z3 >= 23
	k2_12_Z3 += MM[0]

	DY1 = S.Task('DY1', length=8, delay_cost=1)
	S += DY1 >= 24
	DY1 += MM[0]

	NX2_ = S.Task('NX2_', length=2, delay_cost=1)
	S += NX2_ >= 24
	NX2_ += MAS[0]

	NY2__in = S.Task('NY2__in', length=1, delay_cost=1)
	S += NY2__in >= 24
	NY2__in += MAS_in[0]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 24
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 24
	NY2__mem1 += MM_MEM[1]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 25
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 25
	NX2_mem0 += MAS_MEM[0]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 25
	NX2_mem1 += MAIN_MEM_r[1]

	NY2_ = S.Task('NY2_', length=2, delay_cost=1)
	S += NY2_ >= 25
	NY2_ += MAS[0]

	NX2 = S.Task('NX2', length=8, delay_cost=1)
	S += NX2 >= 26
	NX2 += MM[0]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 26
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 26
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 26
	Z_exp5_mem1 += MAIN_MEM_r[1]

	Z_exp5 = S.Task('Z_exp5', length=8, delay_cost=1)
	S += Z_exp5 >= 27
	Z_exp5 += MM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 27
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 27
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 27
	k1_7_Z4_mem1 += MM_MEM[1]

	k1_7_Z4 = S.Task('k1_7_Z4', length=8, delay_cost=1)
	S += k1_7_Z4 >= 28
	k1_7_Z4 += MM[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 28
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 28
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 28
	k3_12_Z4_mem1 += MM_MEM[1]

	DX2__in = S.Task('DX2__in', length=1, delay_cost=1)
	S += DX2__in >= 29
	DX2__in += MAS_in[3]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 29
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 29
	DX2__mem1 += MM_MEM[1]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 29
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 29
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 29
	NY2_mem1 += MAIN_MEM_r[1]

	k3_12_Z4 = S.Task('k3_12_Z4', length=8, delay_cost=1)
	S += k3_12_Z4 >= 29
	k3_12_Z4 += MM[0]

	DX2_ = S.Task('DX2_', length=2, delay_cost=1)
	S += DX2_ >= 30
	DX2_ += MAS[3]

	NY2 = S.Task('NY2', length=8, delay_cost=1)
	S += NY2 >= 30
	NY2 += MM[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 30
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 30
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 30
	k2_11_Z4_mem1 += MM_MEM[1]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 31
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 31
	DX2_mem0 += MAS_MEM[6]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 31
	DX2_mem1 += MAIN_MEM_r[1]

	DY2__in = S.Task('DY2__in', length=1, delay_cost=1)
	S += DY2__in >= 31
	DY2__in += MAS_in[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 31
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 31
	DY2__mem1 += MM_MEM[1]

	k2_11_Z4 = S.Task('k2_11_Z4', length=8, delay_cost=1)
	S += k2_11_Z4 >= 31
	k2_11_Z4 += MM[0]

	DX2 = S.Task('DX2', length=8, delay_cost=1)
	S += DX2 >= 32
	DX2 += MM[0]

	DY2_ = S.Task('DY2_', length=2, delay_cost=1)
	S += DY2_ >= 32
	DY2_ += MAS[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 32
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 32
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 32
	k0_7_Z4_mem1 += MM_MEM[1]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 33
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 33
	DY2_mem0 += MAS_MEM[0]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 33
	DY2_mem1 += MAIN_MEM_r[1]

	NX3__in = S.Task('NX3__in', length=1, delay_cost=1)
	S += NX3__in >= 33
	NX3__in += MAS_in[0]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 33
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 33
	NX3__mem1 += MM_MEM[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=8, delay_cost=1)
	S += k0_7_Z4 >= 33
	k0_7_Z4 += MM[0]

	DY2 = S.Task('DY2', length=8, delay_cost=1)
	S += DY2 >= 34
	DY2 += MM[0]

	NX3_ = S.Task('NX3_', length=2, delay_cost=1)
	S += NX3_ >= 34
	NX3_ += MAS[0]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 34
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 34
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 34
	Z_exp6_mem1 += MAIN_MEM_r[1]

	Z_exp6 = S.Task('Z_exp6', length=8, delay_cost=1)
	S += Z_exp6 >= 35
	Z_exp6 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 35
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 35
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 35
	k2_10_Z5_mem1 += MM_MEM[1]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 36
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 36
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 36
	k0_6_Z5_mem1 += MM_MEM[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=8, delay_cost=1)
	S += k2_10_Z5 >= 36
	k2_10_Z5 += MM[0]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 37
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 37
	NX3_mem0 += MAS_MEM[0]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 37
	NX3_mem1 += MAIN_MEM_r[1]

	NY3__in = S.Task('NY3__in', length=1, delay_cost=1)
	S += NY3__in >= 37
	NY3__in += MAS_in[3]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 37
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 37
	NY3__mem1 += MM_MEM[1]

	k0_6_Z5 = S.Task('k0_6_Z5', length=8, delay_cost=1)
	S += k0_6_Z5 >= 37
	k0_6_Z5 += MM[0]

	NX3 = S.Task('NX3', length=8, delay_cost=1)
	S += NX3 >= 38
	NX3 += MM[0]

	NY3_ = S.Task('NY3_', length=2, delay_cost=1)
	S += NY3_ >= 38
	NY3_ += MAS[3]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 38
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 38
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 38
	k3_11_Z5_mem1 += MM_MEM[1]

	DX3__in = S.Task('DX3__in', length=1, delay_cost=1)
	S += DX3__in >= 39
	DX3__in += MAS_in[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 39
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 39
	DX3__mem1 += MM_MEM[1]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 39
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 39
	NY3_mem0 += MAS_MEM[6]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 39
	NY3_mem1 += MAIN_MEM_r[1]

	k3_11_Z5 = S.Task('k3_11_Z5', length=8, delay_cost=1)
	S += k3_11_Z5 >= 39
	k3_11_Z5 += MM[0]

	DX3_ = S.Task('DX3_', length=2, delay_cost=1)
	S += DX3_ >= 40
	DX3_ += MAS[0]

	NY3 = S.Task('NY3', length=8, delay_cost=1)
	S += NY3 >= 40
	NY3 += MM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 40
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 40
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 40
	k1_6_Z5_mem1 += MM_MEM[1]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 41
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 41
	DX3_mem0 += MAS_MEM[0]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 41
	DX3_mem1 += MAIN_MEM_r[1]

	DY3__in = S.Task('DY3__in', length=1, delay_cost=1)
	S += DY3__in >= 41
	DY3__in += MAS_in[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 41
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 41
	DY3__mem1 += MM_MEM[1]

	k1_6_Z5 = S.Task('k1_6_Z5', length=8, delay_cost=1)
	S += k1_6_Z5 >= 41
	k1_6_Z5 += MM[0]

	DX3 = S.Task('DX3', length=8, delay_cost=1)
	S += DX3 >= 42
	DX3 += MM[0]

	DY3_ = S.Task('DY3_', length=2, delay_cost=1)
	S += DY3_ >= 42
	DY3_ += MAS[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 42
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 42
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 42
	Z_exp7_mem1 += MAIN_MEM_r[1]

	Z_exp7 = S.Task('Z_exp7', length=8, delay_cost=1)
	S += Z_exp7 >= 43
	Z_exp7 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 43
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 43
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 43
	k0_5_Z6_mem1 += MM_MEM[1]

	k0_5_Z6 = S.Task('k0_5_Z6', length=8, delay_cost=1)
	S += k0_5_Z6 >= 44
	k0_5_Z6 += MM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 44
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 44
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 44
	k1_5_Z6_mem1 += MM_MEM[1]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 45
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 45
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 45
	DY3_mem1 += MAIN_MEM_r[1]

	NX4__in = S.Task('NX4__in', length=1, delay_cost=1)
	S += NX4__in >= 45
	NX4__in += MAS_in[0]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 45
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 45
	NX4__mem1 += MM_MEM[1]

	k1_5_Z6 = S.Task('k1_5_Z6', length=8, delay_cost=1)
	S += k1_5_Z6 >= 45
	k1_5_Z6 += MM[0]

	DY3 = S.Task('DY3', length=8, delay_cost=1)
	S += DY3 >= 46
	DY3 += MM[0]

	NX4_ = S.Task('NX4_', length=2, delay_cost=1)
	S += NX4_ >= 46
	NX4_ += MAS[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 46
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 46
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 46
	k2_9_Z6_mem1 += MM_MEM[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=8, delay_cost=1)
	S += k2_9_Z6 >= 47
	k2_9_Z6 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 47
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 47
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 47
	k3_10_Z6_mem1 += MM_MEM[1]

	NY4__in = S.Task('NY4__in', length=1, delay_cost=1)
	S += NY4__in >= 48
	NY4__in += MAS_in[3]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 48
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 48
	NY4__mem1 += MM_MEM[1]

	k3_10_Z6 = S.Task('k3_10_Z6', length=8, delay_cost=1)
	S += k3_10_Z6 >= 48
	k3_10_Z6 += MM[0]

	NY4_ = S.Task('NY4_', length=2, delay_cost=1)
	S += NY4_ >= 49
	NY4_ += MAS[3]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 50
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 50
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 50
	Z_exp8_mem1 += MAIN_MEM_r[1]

	Z_exp8 = S.Task('Z_exp8', length=8, delay_cost=1)
	S += Z_exp8 >= 51
	Z_exp8 += MM[0]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 51
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 51
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 51
	k0_4_Z7_mem1 += MM_MEM[1]

	k0_4_Z7 = S.Task('k0_4_Z7', length=8, delay_cost=1)
	S += k0_4_Z7 >= 52
	k0_4_Z7 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 52
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 52
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 52
	k2_8_Z7_mem1 += MM_MEM[1]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 53
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 53
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 53
	k1_4_Z7_mem1 += MM_MEM[1]

	k2_8_Z7 = S.Task('k2_8_Z7', length=8, delay_cost=1)
	S += k2_8_Z7 >= 53
	k2_8_Z7 += MM[0]

	k1_4_Z7 = S.Task('k1_4_Z7', length=8, delay_cost=1)
	S += k1_4_Z7 >= 54
	k1_4_Z7 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 54
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 54
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 54
	k3_9_Z7_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=8, delay_cost=1)
	S += k3_9_Z7 >= 55
	k3_9_Z7 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 58
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 58
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 58
	k3_8_Z8_mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 59
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 59
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 59
	k0_3_Z8_mem1 += MM_MEM[1]

	k3_8_Z8 = S.Task('k3_8_Z8', length=8, delay_cost=1)
	S += k3_8_Z8 >= 59
	k3_8_Z8 += MM[0]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 60
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 60
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 60
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k0_3_Z8 = S.Task('k0_3_Z8', length=8, delay_cost=1)
	S += k0_3_Z8 >= 60
	k0_3_Z8 += MM[0]

	Z_exp9 = S.Task('Z_exp9', length=8, delay_cost=1)
	S += Z_exp9 >= 61
	Z_exp9 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 61
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 61
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 61
	k2_7_Z8_mem1 += MM_MEM[1]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 62
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 62
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 62
	k1_3_Z8_mem1 += MM_MEM[1]

	k2_7_Z8 = S.Task('k2_7_Z8', length=8, delay_cost=1)
	S += k2_7_Z8 >= 62
	k2_7_Z8 += MM[0]

	k1_3_Z8 = S.Task('k1_3_Z8', length=8, delay_cost=1)
	S += k1_3_Z8 >= 63
	k1_3_Z8 += MM[0]


	# new tasks
	Z_exp10 = S.Task('Z_exp10', length=8, delay_cost=1)
	Z_exp10 += alt(MM)
	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	Z_exp10_in += alt(MM_in)
	S += Z_exp10_in*MM_in[0]<=Z_exp10*MM[0]
	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	Z_exp10_mem0 += MM_MEM[0]
	S += 68 < Z_exp10_mem0
	S += Z_exp10_mem0 <= Z_exp10

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	Z_exp10_mem1 += MAIN_MEM_r[1]
	S += Z_exp10_mem1 <= Z_exp10

	NX4 = S.Task('NX4', length=8, delay_cost=1)
	NX4 += alt(MM)
	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	NX4_in += alt(MM_in)
	S += NX4_in*MM_in[0]<=NX4*MM[0]
	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	NX4_mem0 += MAS_MEM[0]
	S += 47 < NX4_mem0
	S += NX4_mem0 <= NX4

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	NX4_mem1 += MAIN_MEM_r[1]
	S += NX4_mem1 <= NX4

	k0_2_Z9 = S.Task('k0_2_Z9', length=8, delay_cost=1)
	k0_2_Z9 += alt(MM)
	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	k0_2_Z9_in += alt(MM_in)
	S += k0_2_Z9_in*MM_in[0]<=k0_2_Z9*MM[0]
	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	k0_2_Z9_mem0 += MAIN_MEM_r[0]
	S += k0_2_Z9_mem0 <= k0_2_Z9

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	k0_2_Z9_mem1 += MM_MEM[1]
	S += 68 < k0_2_Z9_mem1
	S += k0_2_Z9_mem1 <= k0_2_Z9

	DX4_ = S.Task('DX4_', length=2, delay_cost=1)
	DX4_ += alt(MAS)
	DX4__in = S.Task('DX4__in', length=1, delay_cost=1)
	DX4__in += alt(MAS_in)
	S += DX4__in*MAS_in[0]<=DX4_*MAS[0]

	S += DX4__in*MAS_in[1]<=DX4_*MAS[1]

	S += DX4__in*MAS_in[2]<=DX4_*MAS[2]

	S += DX4__in*MAS_in[3]<=DX4_*MAS[3]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	DX4__mem0 += MM_MEM[0]
	S += 49 < DX4__mem0
	S += DX4__mem0 <= DX4_

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	DX4__mem1 += MM_MEM[1]
	S += 48 < DX4__mem1
	S += DX4__mem1 <= DX4_

	k1_2_Z9 = S.Task('k1_2_Z9', length=8, delay_cost=1)
	k1_2_Z9 += alt(MM)
	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	k1_2_Z9_in += alt(MM_in)
	S += k1_2_Z9_in*MM_in[0]<=k1_2_Z9*MM[0]
	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	k1_2_Z9_mem0 += MAIN_MEM_r[0]
	S += k1_2_Z9_mem0 <= k1_2_Z9

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	k1_2_Z9_mem1 += MM_MEM[1]
	S += 68 < k1_2_Z9_mem1
	S += k1_2_Z9_mem1 <= k1_2_Z9

	NY4 = S.Task('NY4', length=8, delay_cost=1)
	NY4 += alt(MM)
	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	NY4_in += alt(MM_in)
	S += NY4_in*MM_in[0]<=NY4*MM[0]
	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	NY4_mem0 += MAS_MEM[6]
	S += 50 < NY4_mem0
	S += NY4_mem0 <= NY4

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	NY4_mem1 += MAIN_MEM_r[1]
	S += NY4_mem1 <= NY4

	k2_6_Z9 = S.Task('k2_6_Z9', length=8, delay_cost=1)
	k2_6_Z9 += alt(MM)
	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	k2_6_Z9_in += alt(MM_in)
	S += k2_6_Z9_in*MM_in[0]<=k2_6_Z9*MM[0]
	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	k2_6_Z9_mem0 += MAIN_MEM_r[0]
	S += k2_6_Z9_mem0 <= k2_6_Z9

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	k2_6_Z9_mem1 += MM_MEM[1]
	S += 68 < k2_6_Z9_mem1
	S += k2_6_Z9_mem1 <= k2_6_Z9

	DY4_ = S.Task('DY4_', length=2, delay_cost=1)
	DY4_ += alt(MAS)
	DY4__in = S.Task('DY4__in', length=1, delay_cost=1)
	DY4__in += alt(MAS_in)
	S += DY4__in*MAS_in[0]<=DY4_*MAS[0]

	S += DY4__in*MAS_in[1]<=DY4_*MAS[1]

	S += DY4__in*MAS_in[2]<=DY4_*MAS[2]

	S += DY4__in*MAS_in[3]<=DY4_*MAS[3]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	DY4__mem0 += MM_MEM[0]
	S += 53 < DY4__mem0
	S += DY4__mem0 <= DY4_

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	DY4__mem1 += MM_MEM[1]
	S += 46 < DY4__mem1
	S += DY4__mem1 <= DY4_

	k3_7_Z9 = S.Task('k3_7_Z9', length=8, delay_cost=1)
	k3_7_Z9 += alt(MM)
	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	k3_7_Z9_in += alt(MM_in)
	S += k3_7_Z9_in*MM_in[0]<=k3_7_Z9*MM[0]
	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	k3_7_Z9_mem0 += MAIN_MEM_r[0]
	S += k3_7_Z9_mem0 <= k3_7_Z9

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	k3_7_Z9_mem1 += MM_MEM[1]
	S += 68 < k3_7_Z9_mem1
	S += k3_7_Z9_mem1 <= k3_7_Z9

	Z_exp11 = S.Task('Z_exp11', length=8, delay_cost=1)
	Z_exp11 += alt(MM)
	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	Z_exp11_in += alt(MM_in)
	S += Z_exp11_in*MM_in[0]<=Z_exp11*MM[0]
	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	Z_exp11_mem0 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < Z_exp11_mem0*MM_MEM[0]
	S += Z_exp11_mem0 <= Z_exp11

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	Z_exp11_mem1 += MAIN_MEM_r[1]
	S += Z_exp11_mem1 <= Z_exp11

	NX5_ = S.Task('NX5_', length=2, delay_cost=1)
	NX5_ += alt(MAS)
	NX5__in = S.Task('NX5__in', length=1, delay_cost=1)
	NX5__in += alt(MAS_in)
	S += NX5__in*MAS_in[0]<=NX5_*MAS[0]

	S += NX5__in*MAS_in[1]<=NX5_*MAS[1]

	S += NX5__in*MAS_in[2]<=NX5_*MAS[2]

	S += NX5__in*MAS_in[3]<=NX5_*MAS[3]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	NX5__mem0 += alt(MM_MEM)
	S += (NX4*MM[0])-1 < NX5__mem0*MM_MEM[0]
	S += NX5__mem0 <= NX5_

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	NX5__mem1 += MM_MEM[1]
	S += 44 < NX5__mem1
	S += NX5__mem1 <= NX5_

	k0_1_Z10 = S.Task('k0_1_Z10', length=8, delay_cost=1)
	k0_1_Z10 += alt(MM)
	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	k0_1_Z10_in += alt(MM_in)
	S += k0_1_Z10_in*MM_in[0]<=k0_1_Z10*MM[0]
	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	k0_1_Z10_mem0 += MAIN_MEM_r[0]
	S += k0_1_Z10_mem0 <= k0_1_Z10

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	k0_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k0_1_Z10_mem1*MM_MEM[1]
	S += k0_1_Z10_mem1 <= k0_1_Z10

	DX4 = S.Task('DX4', length=8, delay_cost=1)
	DX4 += alt(MM)
	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	DX4_in += alt(MM_in)
	S += DX4_in*MM_in[0]<=DX4*MM[0]
	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	DX4_mem0 += alt(MAS_MEM)
	S += (DX4_*MAS[0])-1 < DX4_mem0*MAS_MEM[0]
	S += (DX4_*MAS[1])-1 < DX4_mem0*MAS_MEM[2]
	S += (DX4_*MAS[2])-1 < DX4_mem0*MAS_MEM[4]
	S += (DX4_*MAS[3])-1 < DX4_mem0*MAS_MEM[6]
	S += DX4_mem0 <= DX4

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	DX4_mem1 += MAIN_MEM_r[1]
	S += DX4_mem1 <= DX4

	k1_1_Z10 = S.Task('k1_1_Z10', length=8, delay_cost=1)
	k1_1_Z10 += alt(MM)
	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	k1_1_Z10_in += alt(MM_in)
	S += k1_1_Z10_in*MM_in[0]<=k1_1_Z10*MM[0]
	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	k1_1_Z10_mem0 += MAIN_MEM_r[0]
	S += k1_1_Z10_mem0 <= k1_1_Z10

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	k1_1_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k1_1_Z10_mem1*MM_MEM[1]
	S += k1_1_Z10_mem1 <= k1_1_Z10

	NY5_ = S.Task('NY5_', length=2, delay_cost=1)
	NY5_ += alt(MAS)
	NY5__in = S.Task('NY5__in', length=1, delay_cost=1)
	NY5__in += alt(MAS_in)
	S += NY5__in*MAS_in[0]<=NY5_*MAS[0]

	S += NY5__in*MAS_in[1]<=NY5_*MAS[1]

	S += NY5__in*MAS_in[2]<=NY5_*MAS[2]

	S += NY5__in*MAS_in[3]<=NY5_*MAS[3]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	NY5__mem0 += alt(MM_MEM)
	S += (NY4*MM[0])-1 < NY5__mem0*MM_MEM[0]
	S += NY5__mem0 <= NY5_

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	NY5__mem1 += MM_MEM[1]
	S += 43 < NY5__mem1
	S += NY5__mem1 <= NY5_

	k2_5_Z10 = S.Task('k2_5_Z10', length=8, delay_cost=1)
	k2_5_Z10 += alt(MM)
	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	k2_5_Z10_in += alt(MM_in)
	S += k2_5_Z10_in*MM_in[0]<=k2_5_Z10*MM[0]
	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	k2_5_Z10_mem0 += MAIN_MEM_r[0]
	S += k2_5_Z10_mem0 <= k2_5_Z10

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	k2_5_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k2_5_Z10_mem1*MM_MEM[1]
	S += k2_5_Z10_mem1 <= k2_5_Z10

	DY4 = S.Task('DY4', length=8, delay_cost=1)
	DY4 += alt(MM)
	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	DY4_in += alt(MM_in)
	S += DY4_in*MM_in[0]<=DY4*MM[0]
	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	DY4_mem0 += alt(MAS_MEM)
	S += (DY4_*MAS[0])-1 < DY4_mem0*MAS_MEM[0]
	S += (DY4_*MAS[1])-1 < DY4_mem0*MAS_MEM[2]
	S += (DY4_*MAS[2])-1 < DY4_mem0*MAS_MEM[4]
	S += (DY4_*MAS[3])-1 < DY4_mem0*MAS_MEM[6]
	S += DY4_mem0 <= DY4

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	DY4_mem1 += MAIN_MEM_r[1]
	S += DY4_mem1 <= DY4

	k3_6_Z10 = S.Task('k3_6_Z10', length=8, delay_cost=1)
	k3_6_Z10 += alt(MM)
	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	k3_6_Z10_in += alt(MM_in)
	S += k3_6_Z10_in*MM_in[0]<=k3_6_Z10*MM[0]
	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	k3_6_Z10_mem0 += MAIN_MEM_r[0]
	S += k3_6_Z10_mem0 <= k3_6_Z10

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	k3_6_Z10_mem1 += alt(MM_MEM)
	S += (Z_exp10*MM[0])-1 < k3_6_Z10_mem1*MM_MEM[1]
	S += k3_6_Z10_mem1 <= k3_6_Z10

	Z_exp12 = S.Task('Z_exp12', length=8, delay_cost=1)
	Z_exp12 += alt(MM)
	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	Z_exp12_in += alt(MM_in)
	S += Z_exp12_in*MM_in[0]<=Z_exp12*MM[0]
	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	Z_exp12_mem0 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < Z_exp12_mem0*MM_MEM[0]
	S += Z_exp12_mem0 <= Z_exp12

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	Z_exp12_mem1 += MAIN_MEM_r[1]
	S += Z_exp12_mem1 <= Z_exp12

	NX5 = S.Task('NX5', length=8, delay_cost=1)
	NX5 += alt(MM)
	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	NX5_in += alt(MM_in)
	S += NX5_in*MM_in[0]<=NX5*MM[0]
	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	NX5_mem0 += alt(MAS_MEM)
	S += (NX5_*MAS[0])-1 < NX5_mem0*MAS_MEM[0]
	S += (NX5_*MAS[1])-1 < NX5_mem0*MAS_MEM[2]
	S += (NX5_*MAS[2])-1 < NX5_mem0*MAS_MEM[4]
	S += (NX5_*MAS[3])-1 < NX5_mem0*MAS_MEM[6]
	S += NX5_mem0 <= NX5

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	NX5_mem1 += MAIN_MEM_r[1]
	S += NX5_mem1 <= NX5

	k0_0_Z11 = S.Task('k0_0_Z11', length=8, delay_cost=1)
	k0_0_Z11 += alt(MM)
	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	k0_0_Z11_in += alt(MM_in)
	S += k0_0_Z11_in*MM_in[0]<=k0_0_Z11*MM[0]
	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	k0_0_Z11_mem0 += MAIN_MEM_r[0]
	S += k0_0_Z11_mem0 <= k0_0_Z11

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	k0_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k0_0_Z11_mem1*MM_MEM[1]
	S += k0_0_Z11_mem1 <= k0_0_Z11

	DX5_ = S.Task('DX5_', length=2, delay_cost=1)
	DX5_ += alt(MAS)
	DX5__in = S.Task('DX5__in', length=1, delay_cost=1)
	DX5__in += alt(MAS_in)
	S += DX5__in*MAS_in[0]<=DX5_*MAS[0]

	S += DX5__in*MAS_in[1]<=DX5_*MAS[1]

	S += DX5__in*MAS_in[2]<=DX5_*MAS[2]

	S += DX5__in*MAS_in[3]<=DX5_*MAS[3]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	DX5__mem0 += alt(MM_MEM)
	S += (DX4*MM[0])-1 < DX5__mem0*MM_MEM[0]
	S += DX5__mem0 <= DX5_

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	DX5__mem1 += MM_MEM[1]
	S += 52 < DX5__mem1
	S += DX5__mem1 <= DX5_

	k1_0_Z11 = S.Task('k1_0_Z11', length=8, delay_cost=1)
	k1_0_Z11 += alt(MM)
	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	k1_0_Z11_in += alt(MM_in)
	S += k1_0_Z11_in*MM_in[0]<=k1_0_Z11*MM[0]
	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	k1_0_Z11_mem0 += MAIN_MEM_r[0]
	S += k1_0_Z11_mem0 <= k1_0_Z11

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	k1_0_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k1_0_Z11_mem1*MM_MEM[1]
	S += k1_0_Z11_mem1 <= k1_0_Z11

	NY5 = S.Task('NY5', length=8, delay_cost=1)
	NY5 += alt(MM)
	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	NY5_in += alt(MM_in)
	S += NY5_in*MM_in[0]<=NY5*MM[0]
	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	NY5_mem0 += alt(MAS_MEM)
	S += (NY5_*MAS[0])-1 < NY5_mem0*MAS_MEM[0]
	S += (NY5_*MAS[1])-1 < NY5_mem0*MAS_MEM[2]
	S += (NY5_*MAS[2])-1 < NY5_mem0*MAS_MEM[4]
	S += (NY5_*MAS[3])-1 < NY5_mem0*MAS_MEM[6]
	S += NY5_mem0 <= NY5

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	NY5_mem1 += MAIN_MEM_r[1]
	S += NY5_mem1 <= NY5

	k2_4_Z11 = S.Task('k2_4_Z11', length=8, delay_cost=1)
	k2_4_Z11 += alt(MM)
	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	k2_4_Z11_in += alt(MM_in)
	S += k2_4_Z11_in*MM_in[0]<=k2_4_Z11*MM[0]
	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	k2_4_Z11_mem0 += MAIN_MEM_r[0]
	S += k2_4_Z11_mem0 <= k2_4_Z11

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	k2_4_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k2_4_Z11_mem1*MM_MEM[1]
	S += k2_4_Z11_mem1 <= k2_4_Z11

	DY5_ = S.Task('DY5_', length=2, delay_cost=1)
	DY5_ += alt(MAS)
	DY5__in = S.Task('DY5__in', length=1, delay_cost=1)
	DY5__in += alt(MAS_in)
	S += DY5__in*MAS_in[0]<=DY5_*MAS[0]

	S += DY5__in*MAS_in[1]<=DY5_*MAS[1]

	S += DY5__in*MAS_in[2]<=DY5_*MAS[2]

	S += DY5__in*MAS_in[3]<=DY5_*MAS[3]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	DY5__mem0 += alt(MM_MEM)
	S += (DY4*MM[0])-1 < DY5__mem0*MM_MEM[0]
	S += DY5__mem0 <= DY5_

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	DY5__mem1 += MM_MEM[1]
	S += 55 < DY5__mem1
	S += DY5__mem1 <= DY5_

	k3_5_Z11 = S.Task('k3_5_Z11', length=8, delay_cost=1)
	k3_5_Z11 += alt(MM)
	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	k3_5_Z11_in += alt(MM_in)
	S += k3_5_Z11_in*MM_in[0]<=k3_5_Z11*MM[0]
	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	k3_5_Z11_mem0 += MAIN_MEM_r[0]
	S += k3_5_Z11_mem0 <= k3_5_Z11

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	k3_5_Z11_mem1 += alt(MM_MEM)
	S += (Z_exp11*MM[0])-1 < k3_5_Z11_mem1*MM_MEM[1]
	S += k3_5_Z11_mem1 <= k3_5_Z11

	Z_exp13 = S.Task('Z_exp13', length=8, delay_cost=1)
	Z_exp13 += alt(MM)
	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	Z_exp13_in += alt(MM_in)
	S += Z_exp13_in*MM_in[0]<=Z_exp13*MM[0]
	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	Z_exp13_mem0 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < Z_exp13_mem0*MM_MEM[0]
	S += Z_exp13_mem0 <= Z_exp13

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	Z_exp13_mem1 += MAIN_MEM_r[1]
	S += Z_exp13_mem1 <= Z_exp13

	NX6_ = S.Task('NX6_', length=2, delay_cost=1)
	NX6_ += alt(MAS)
	NX6__in = S.Task('NX6__in', length=1, delay_cost=1)
	NX6__in += alt(MAS_in)
	S += NX6__in*MAS_in[0]<=NX6_*MAS[0]

	S += NX6__in*MAS_in[1]<=NX6_*MAS[1]

	S += NX6__in*MAS_in[2]<=NX6_*MAS[2]

	S += NX6__in*MAS_in[3]<=NX6_*MAS[3]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	NX6__mem0 += alt(MM_MEM)
	S += (NX5*MM[0])-1 < NX6__mem0*MM_MEM[0]
	S += NX6__mem0 <= NX6_

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	NX6__mem1 += MM_MEM[1]
	S += 51 < NX6__mem1
	S += NX6__mem1 <= NX6_

	DX5 = S.Task('DX5', length=8, delay_cost=1)
	DX5 += alt(MM)
	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	DX5_in += alt(MM_in)
	S += DX5_in*MM_in[0]<=DX5*MM[0]
	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	DX5_mem0 += alt(MAS_MEM)
	S += (DX5_*MAS[0])-1 < DX5_mem0*MAS_MEM[0]
	S += (DX5_*MAS[1])-1 < DX5_mem0*MAS_MEM[2]
	S += (DX5_*MAS[2])-1 < DX5_mem0*MAS_MEM[4]
	S += (DX5_*MAS[3])-1 < DX5_mem0*MAS_MEM[6]
	S += DX5_mem0 <= DX5

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	DX5_mem1 += MAIN_MEM_r[1]
	S += DX5_mem1 <= DX5

	NY6_ = S.Task('NY6_', length=2, delay_cost=1)
	NY6_ += alt(MAS)
	NY6__in = S.Task('NY6__in', length=1, delay_cost=1)
	NY6__in += alt(MAS_in)
	S += NY6__in*MAS_in[0]<=NY6_*MAS[0]

	S += NY6__in*MAS_in[1]<=NY6_*MAS[1]

	S += NY6__in*MAS_in[2]<=NY6_*MAS[2]

	S += NY6__in*MAS_in[3]<=NY6_*MAS[3]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	NY6__mem0 += alt(MM_MEM)
	S += (NY5*MM[0])-1 < NY6__mem0*MM_MEM[0]
	S += NY6__mem0 <= NY6_

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	NY6__mem1 += MM_MEM[1]
	S += 54 < NY6__mem1
	S += NY6__mem1 <= NY6_

	k2_3_Z12 = S.Task('k2_3_Z12', length=8, delay_cost=1)
	k2_3_Z12 += alt(MM)
	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	k2_3_Z12_in += alt(MM_in)
	S += k2_3_Z12_in*MM_in[0]<=k2_3_Z12*MM[0]
	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	k2_3_Z12_mem0 += MAIN_MEM_r[0]
	S += k2_3_Z12_mem0 <= k2_3_Z12

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	k2_3_Z12_mem1 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < k2_3_Z12_mem1*MM_MEM[1]
	S += k2_3_Z12_mem1 <= k2_3_Z12

	DY5 = S.Task('DY5', length=8, delay_cost=1)
	DY5 += alt(MM)
	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	DY5_in += alt(MM_in)
	S += DY5_in*MM_in[0]<=DY5*MM[0]
	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	DY5_mem0 += alt(MAS_MEM)
	S += (DY5_*MAS[0])-1 < DY5_mem0*MAS_MEM[0]
	S += (DY5_*MAS[1])-1 < DY5_mem0*MAS_MEM[2]
	S += (DY5_*MAS[2])-1 < DY5_mem0*MAS_MEM[4]
	S += (DY5_*MAS[3])-1 < DY5_mem0*MAS_MEM[6]
	S += DY5_mem0 <= DY5

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	DY5_mem1 += MAIN_MEM_r[1]
	S += DY5_mem1 <= DY5

	k3_4_Z12 = S.Task('k3_4_Z12', length=8, delay_cost=1)
	k3_4_Z12 += alt(MM)
	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	k3_4_Z12_in += alt(MM_in)
	S += k3_4_Z12_in*MM_in[0]<=k3_4_Z12*MM[0]
	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	k3_4_Z12_mem0 += MAIN_MEM_r[0]
	S += k3_4_Z12_mem0 <= k3_4_Z12

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	k3_4_Z12_mem1 += alt(MM_MEM)
	S += (Z_exp12*MM[0])-1 < k3_4_Z12_mem1*MM_MEM[1]
	S += k3_4_Z12_mem1 <= k3_4_Z12

	Z_exp14 = S.Task('Z_exp14', length=8, delay_cost=1)
	Z_exp14 += alt(MM)
	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	Z_exp14_in += alt(MM_in)
	S += Z_exp14_in*MM_in[0]<=Z_exp14*MM[0]
	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	Z_exp14_mem0 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < Z_exp14_mem0*MM_MEM[0]
	S += Z_exp14_mem0 <= Z_exp14

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	Z_exp14_mem1 += MAIN_MEM_r[1]
	S += Z_exp14_mem1 <= Z_exp14

	NX6 = S.Task('NX6', length=8, delay_cost=1)
	NX6 += alt(MM)
	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	NX6_in += alt(MM_in)
	S += NX6_in*MM_in[0]<=NX6*MM[0]
	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	NX6_mem0 += alt(MAS_MEM)
	S += (NX6_*MAS[0])-1 < NX6_mem0*MAS_MEM[0]
	S += (NX6_*MAS[1])-1 < NX6_mem0*MAS_MEM[2]
	S += (NX6_*MAS[2])-1 < NX6_mem0*MAS_MEM[4]
	S += (NX6_*MAS[3])-1 < NX6_mem0*MAS_MEM[6]
	S += NX6_mem0 <= NX6

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	NX6_mem1 += MAIN_MEM_r[1]
	S += NX6_mem1 <= NX6

	DX6_ = S.Task('DX6_', length=2, delay_cost=1)
	DX6_ += alt(MAS)
	DX6__in = S.Task('DX6__in', length=1, delay_cost=1)
	DX6__in += alt(MAS_in)
	S += DX6__in*MAS_in[0]<=DX6_*MAS[0]

	S += DX6__in*MAS_in[1]<=DX6_*MAS[1]

	S += DX6__in*MAS_in[2]<=DX6_*MAS[2]

	S += DX6__in*MAS_in[3]<=DX6_*MAS[3]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	DX6__mem0 += alt(MM_MEM)
	S += (DX5*MM[0])-1 < DX6__mem0*MM_MEM[0]
	S += DX6__mem0 <= DX6_

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	DX6__mem1 += MM_MEM[1]
	S += 61 < DX6__mem1
	S += DX6__mem1 <= DX6_

	NY6 = S.Task('NY6', length=8, delay_cost=1)
	NY6 += alt(MM)
	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	NY6_in += alt(MM_in)
	S += NY6_in*MM_in[0]<=NY6*MM[0]
	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	NY6_mem0 += alt(MAS_MEM)
	S += (NY6_*MAS[0])-1 < NY6_mem0*MAS_MEM[0]
	S += (NY6_*MAS[1])-1 < NY6_mem0*MAS_MEM[2]
	S += (NY6_*MAS[2])-1 < NY6_mem0*MAS_MEM[4]
	S += (NY6_*MAS[3])-1 < NY6_mem0*MAS_MEM[6]
	S += NY6_mem0 <= NY6

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	NY6_mem1 += MAIN_MEM_r[1]
	S += NY6_mem1 <= NY6

	k2_2_Z13 = S.Task('k2_2_Z13', length=8, delay_cost=1)
	k2_2_Z13 += alt(MM)
	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	k2_2_Z13_in += alt(MM_in)
	S += k2_2_Z13_in*MM_in[0]<=k2_2_Z13*MM[0]
	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	k2_2_Z13_mem0 += MAIN_MEM_r[0]
	S += k2_2_Z13_mem0 <= k2_2_Z13

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	k2_2_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k2_2_Z13_mem1*MM_MEM[1]
	S += k2_2_Z13_mem1 <= k2_2_Z13

	DY6_ = S.Task('DY6_', length=2, delay_cost=1)
	DY6_ += alt(MAS)
	DY6__in = S.Task('DY6__in', length=1, delay_cost=1)
	DY6__in += alt(MAS_in)
	S += DY6__in*MAS_in[0]<=DY6_*MAS[0]

	S += DY6__in*MAS_in[1]<=DY6_*MAS[1]

	S += DY6__in*MAS_in[2]<=DY6_*MAS[2]

	S += DY6__in*MAS_in[3]<=DY6_*MAS[3]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	DY6__mem0 += alt(MM_MEM)
	S += (DY5*MM[0])-1 < DY6__mem0*MM_MEM[0]
	S += DY6__mem0 <= DY6_

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	DY6__mem1 += MM_MEM[1]
	S += 62 < DY6__mem1
	S += DY6__mem1 <= DY6_

	k3_3_Z13 = S.Task('k3_3_Z13', length=8, delay_cost=1)
	k3_3_Z13 += alt(MM)
	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	k3_3_Z13_in += alt(MM_in)
	S += k3_3_Z13_in*MM_in[0]<=k3_3_Z13*MM[0]
	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	k3_3_Z13_mem0 += MAIN_MEM_r[0]
	S += k3_3_Z13_mem0 <= k3_3_Z13

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	k3_3_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k3_3_Z13_mem1*MM_MEM[1]
	S += k3_3_Z13_mem1 <= k3_3_Z13

	Z_exp15 = S.Task('Z_exp15', length=8, delay_cost=1)
	Z_exp15 += alt(MM)
	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	Z_exp15_in += alt(MM_in)
	S += Z_exp15_in*MM_in[0]<=Z_exp15*MM[0]
	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	Z_exp15_mem0 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < Z_exp15_mem0*MM_MEM[0]
	S += Z_exp15_mem0 <= Z_exp15

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	Z_exp15_mem1 += MAIN_MEM_r[1]
	S += Z_exp15_mem1 <= Z_exp15

	NX7_ = S.Task('NX7_', length=2, delay_cost=1)
	NX7_ += alt(MAS)
	NX7__in = S.Task('NX7__in', length=1, delay_cost=1)
	NX7__in += alt(MAS_in)
	S += NX7__in*MAS_in[0]<=NX7_*MAS[0]

	S += NX7__in*MAS_in[1]<=NX7_*MAS[1]

	S += NX7__in*MAS_in[2]<=NX7_*MAS[2]

	S += NX7__in*MAS_in[3]<=NX7_*MAS[3]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	NX7__mem0 += alt(MM_MEM)
	S += (NX6*MM[0])-1 < NX7__mem0*MM_MEM[0]
	S += NX7__mem0 <= NX7_

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	NX7__mem1 += MM_MEM[1]
	S += 59 < NX7__mem1
	S += NX7__mem1 <= NX7_

	DX6 = S.Task('DX6', length=8, delay_cost=1)
	DX6 += alt(MM)
	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	DX6_in += alt(MM_in)
	S += DX6_in*MM_in[0]<=DX6*MM[0]
	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	DX6_mem0 += alt(MAS_MEM)
	S += (DX6_*MAS[0])-1 < DX6_mem0*MAS_MEM[0]
	S += (DX6_*MAS[1])-1 < DX6_mem0*MAS_MEM[2]
	S += (DX6_*MAS[2])-1 < DX6_mem0*MAS_MEM[4]
	S += (DX6_*MAS[3])-1 < DX6_mem0*MAS_MEM[6]
	S += DX6_mem0 <= DX6

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	DX6_mem1 += MAIN_MEM_r[1]
	S += DX6_mem1 <= DX6

	NY7_ = S.Task('NY7_', length=2, delay_cost=1)
	NY7_ += alt(MAS)
	NY7__in = S.Task('NY7__in', length=1, delay_cost=1)
	NY7__in += alt(MAS_in)
	S += NY7__in*MAS_in[0]<=NY7_*MAS[0]

	S += NY7__in*MAS_in[1]<=NY7_*MAS[1]

	S += NY7__in*MAS_in[2]<=NY7_*MAS[2]

	S += NY7__in*MAS_in[3]<=NY7_*MAS[3]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	NY7__mem0 += alt(MM_MEM)
	S += (NY6*MM[0])-1 < NY7__mem0*MM_MEM[0]
	S += NY7__mem0 <= NY7_

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	NY7__mem1 += MM_MEM[1]
	S += 60 < NY7__mem1
	S += NY7__mem1 <= NY7_

	k2_1_Z14 = S.Task('k2_1_Z14', length=8, delay_cost=1)
	k2_1_Z14 += alt(MM)
	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	k2_1_Z14_in += alt(MM_in)
	S += k2_1_Z14_in*MM_in[0]<=k2_1_Z14*MM[0]
	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	k2_1_Z14_mem0 += MAIN_MEM_r[0]
	S += k2_1_Z14_mem0 <= k2_1_Z14

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	k2_1_Z14_mem1 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < k2_1_Z14_mem1*MM_MEM[1]
	S += k2_1_Z14_mem1 <= k2_1_Z14

	DY6 = S.Task('DY6', length=8, delay_cost=1)
	DY6 += alt(MM)
	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	DY6_in += alt(MM_in)
	S += DY6_in*MM_in[0]<=DY6*MM[0]
	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	DY6_mem0 += alt(MAS_MEM)
	S += (DY6_*MAS[0])-1 < DY6_mem0*MAS_MEM[0]
	S += (DY6_*MAS[1])-1 < DY6_mem0*MAS_MEM[2]
	S += (DY6_*MAS[2])-1 < DY6_mem0*MAS_MEM[4]
	S += (DY6_*MAS[3])-1 < DY6_mem0*MAS_MEM[6]
	S += DY6_mem0 <= DY6

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	DY6_mem1 += MAIN_MEM_r[1]
	S += DY6_mem1 <= DY6

	k3_2_Z14 = S.Task('k3_2_Z14', length=8, delay_cost=1)
	k3_2_Z14 += alt(MM)
	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	k3_2_Z14_in += alt(MM_in)
	S += k3_2_Z14_in*MM_in[0]<=k3_2_Z14*MM[0]
	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	k3_2_Z14_mem0 += MAIN_MEM_r[0]
	S += k3_2_Z14_mem0 <= k3_2_Z14

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

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS4/ISOGENY/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

