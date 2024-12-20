from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t0 = S.Task('t0', length=6, delay_cost=1)
	t0 += alt(MM)
	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	t0_in += alt(MM_in)
	S += t0_in*MM_in[0]<=t0*MM[0]
	S += t0_in*MM_in[1]<=t0*MM[1]
	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	t0_mem0 += MAIN_MEM_r[0]
	S += t0_mem0 <= t0

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	t0_mem1 += MAIN_MEM_r[1]
	S += t0_mem1 <= t0

	t1 = S.Task('t1', length=6, delay_cost=1)
	t1 += alt(MM)
	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	S += t1_in*MM_in[0]<=t1*MM[0]
	S += t1_in*MM_in[1]<=t1*MM[1]
	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r[0]
	S += t1_mem0 <= t1

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	t1_mem1 += MAIN_MEM_r[1]
	S += t1_mem1 <= t1

	t2 = S.Task('t2', length=6, delay_cost=1)
	t2 += alt(MM)
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	S += t2_in*MM_in[0]<=t2*MM[0]
	S += t2_in*MM_in[1]<=t2*MM[1]
	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r[0]
	S += t2_mem0 <= t2

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	t2_mem1 += MAIN_MEM_r[1]
	S += t2_mem1 <= t2

	t3 = S.Task('t3', length=1, delay_cost=1)
	t3 += alt(MAS)
	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	t3_mem0 += MAIN_MEM_r[0]
	S += t3_mem0 <= t3

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	t3_mem1 += MAIN_MEM_r[1]
	S += t3_mem1 <= t3

	t4 = S.Task('t4', length=1, delay_cost=1)
	t4 += alt(MAS)
	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	t4_mem0 += MAIN_MEM_r[0]
	S += t4_mem0 <= t4

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	t4_mem1 += MAIN_MEM_r[1]
	S += t4_mem1 <= t4

	t8 = S.Task('t8', length=1, delay_cost=1)
	t8 += alt(MAS)
	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	t8_mem0 += MAIN_MEM_r[0]
	S += t8_mem0 <= t8

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	t8_mem1 += MAIN_MEM_r[1]
	S += t8_mem1 <= t8

	t9 = S.Task('t9', length=1, delay_cost=1)
	t9 += alt(MAS)
	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	t9_mem0 += MAIN_MEM_r[0]
	S += t9_mem0 <= t9

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	t9_mem1 += MAIN_MEM_r[1]
	S += t9_mem1 <= t9

	t13 = S.Task('t13', length=1, delay_cost=1)
	t13 += alt(MAS)
	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += MAIN_MEM_r[0]
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += MAIN_MEM_r[1]
	S += t13_mem1 <= t13

	t14 = S.Task('t14', length=1, delay_cost=1)
	t14 += alt(MAS)
	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += MAIN_MEM_r[0]
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += MAIN_MEM_r[1]
	S += t14_mem1 <= t14

	t5 = S.Task('t5', length=6, delay_cost=1)
	t5 += alt(MM)
	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	t5_in += alt(MM_in)
	S += t5_in*MM_in[0]<=t5*MM[0]
	S += t5_in*MM_in[1]<=t5*MM[1]
	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	t5_mem0 += alt(MAS_MEM)
	S += (t3*MAS[0])-1 < t5_mem0*MAS_MEM[0]
	S += (t3*MAS[1])-1 < t5_mem0*MAS_MEM[2]
	S += (t3*MAS[2])-1 < t5_mem0*MAS_MEM[4]
	S += (t3*MAS[3])-1 < t5_mem0*MAS_MEM[6]
	S += t5_mem0 <= t5

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	t5_mem1 += alt(MAS_MEM)
	S += (t4*MAS[0])-1 < t5_mem1*MAS_MEM[1]
	S += (t4*MAS[1])-1 < t5_mem1*MAS_MEM[3]
	S += (t4*MAS[2])-1 < t5_mem1*MAS_MEM[5]
	S += (t4*MAS[3])-1 < t5_mem1*MAS_MEM[7]
	S += t5_mem1 <= t5

	t6 = S.Task('t6', length=1, delay_cost=1)
	t6 += alt(MAS)
	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	t6_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t6_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t6_mem0*MM_MEM[2]
	S += t6_mem0 <= t6

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	t6_mem1 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t6_mem1*MM_MEM[1]
	S += (t1*MM[1])-1 < t6_mem1*MM_MEM[3]
	S += t6_mem1 <= t6

	t10 = S.Task('t10', length=6, delay_cost=1)
	t10 += alt(MM)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MM_in)
	S += t10_in*MM_in[0]<=t10*MM[0]
	S += t10_in*MM_in[1]<=t10*MM[1]
	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MAS_MEM)
	S += (t8*MAS[0])-1 < t10_mem0*MAS_MEM[0]
	S += (t8*MAS[1])-1 < t10_mem0*MAS_MEM[2]
	S += (t8*MAS[2])-1 < t10_mem0*MAS_MEM[4]
	S += (t8*MAS[3])-1 < t10_mem0*MAS_MEM[6]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MAS_MEM)
	S += (t9*MAS[0])-1 < t10_mem1*MAS_MEM[1]
	S += (t9*MAS[1])-1 < t10_mem1*MAS_MEM[3]
	S += (t9*MAS[2])-1 < t10_mem1*MAS_MEM[5]
	S += (t9*MAS[3])-1 < t10_mem1*MAS_MEM[7]
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(MAS)
	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t11_mem0*MM_MEM[0]
	S += (t1*MM[1])-1 < t11_mem0*MM_MEM[2]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t11_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t11_mem1*MM_MEM[3]
	S += t11_mem1 <= t11

	t15 = S.Task('t15', length=6, delay_cost=1)
	t15 += alt(MM)
	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	t15_in += alt(MM_in)
	S += t15_in*MM_in[0]<=t15*MM[0]
	S += t15_in*MM_in[1]<=t15*MM[1]
	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	t15_mem0 += alt(MAS_MEM)
	S += (t13*MAS[0])-1 < t15_mem0*MAS_MEM[0]
	S += (t13*MAS[1])-1 < t15_mem0*MAS_MEM[2]
	S += (t13*MAS[2])-1 < t15_mem0*MAS_MEM[4]
	S += (t13*MAS[3])-1 < t15_mem0*MAS_MEM[6]
	S += t15_mem0 <= t15

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	t15_mem1 += alt(MAS_MEM)
	S += (t14*MAS[0])-1 < t15_mem1*MAS_MEM[1]
	S += (t14*MAS[1])-1 < t15_mem1*MAS_MEM[3]
	S += (t14*MAS[2])-1 < t15_mem1*MAS_MEM[5]
	S += (t14*MAS[3])-1 < t15_mem1*MAS_MEM[7]
	S += t15_mem1 <= t15

	t16 = S.Task('t16', length=1, delay_cost=1)
	t16 += alt(MAS)
	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	t16_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t16_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t16_mem0*MM_MEM[2]
	S += t16_mem0 <= t16

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	t16_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t16_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t16_mem1*MM_MEM[3]
	S += t16_mem1 <= t16

	t19 = S.Task('t19', length=6, delay_cost=1)
	t19 += alt(MM)
	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	t19_in += alt(MM_in)
	S += t19_in*MM_in[0]<=t19*MM[0]
	S += t19_in*MM_in[1]<=t19*MM[1]
	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	t19_mem0 += MAIN_MEM_r[0]
	S += t19_mem0 <= t19

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	t19_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t19_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t19_mem1*MM_MEM[3]
	S += t19_mem1 <= t19

	t24 = S.Task('t24', length=1, delay_cost=1)
	t24 += alt(MAS)
	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	t24_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t24_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t24_mem0*MM_MEM[2]
	S += t24_mem0 <= t24

	t24_mem1 = S.Task('t24_mem1', length=1, delay_cost=1)
	t24_mem1 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t24_mem1*MM_MEM[1]
	S += (t0*MM[1])-1 < t24_mem1*MM_MEM[3]
	S += t24_mem1 <= t24

	t26 = S.Task('t26', length=6, delay_cost=1)
	t26 += alt(MM)
	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	t26_in += alt(MM_in)
	S += t26_in*MM_in[0]<=t26*MM[0]
	S += t26_in*MM_in[1]<=t26*MM[1]
	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	t26_mem0 += MAIN_MEM_r[0]
	S += t26_mem0 <= t26

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	t26_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t26_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t26_mem1*MM_MEM[3]
	S += t26_mem1 <= t26

	t7 = S.Task('t7', length=1, delay_cost=1)
	t7 += alt(MAS)
	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	t7_mem0 += alt(MM_MEM)
	S += (t5*MM[0])-1 < t7_mem0*MM_MEM[0]
	S += (t5*MM[1])-1 < t7_mem0*MM_MEM[2]
	S += t7_mem0 <= t7

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	t7_mem1 += alt(MAS_MEM)
	S += (t6*MAS[0])-1 < t7_mem1*MAS_MEM[1]
	S += (t6*MAS[1])-1 < t7_mem1*MAS_MEM[3]
	S += (t6*MAS[2])-1 < t7_mem1*MAS_MEM[5]
	S += (t6*MAS[3])-1 < t7_mem1*MAS_MEM[7]
	S += t7_mem1 <= t7

	t12 = S.Task('t12', length=1, delay_cost=1)
	t12 += alt(MAS)
	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MM_MEM)
	S += (t10*MM[0])-1 < t12_mem0*MM_MEM[0]
	S += (t10*MM[1])-1 < t12_mem0*MM_MEM[2]
	S += t12_mem0 <= t12

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	t12_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t12_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t12_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t12_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t12_mem1*MAS_MEM[7]
	S += t12_mem1 <= t12

	t17 = S.Task('t17', length=1, delay_cost=1)
	t17 += alt(MAS)
	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	t17_mem0 += alt(MM_MEM)
	S += (t15*MM[0])-1 < t17_mem0*MM_MEM[0]
	S += (t15*MM[1])-1 < t17_mem0*MM_MEM[2]
	S += t17_mem0 <= t17

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	t17_mem1 += alt(MAS_MEM)
	S += (t16*MAS[0])-1 < t17_mem1*MAS_MEM[1]
	S += (t16*MAS[1])-1 < t17_mem1*MAS_MEM[3]
	S += (t16*MAS[2])-1 < t17_mem1*MAS_MEM[5]
	S += (t16*MAS[3])-1 < t17_mem1*MAS_MEM[7]
	S += t17_mem1 <= t17

	t25 = S.Task('t25', length=1, delay_cost=1)
	t25 += alt(MAS)
	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	t25_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t25_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t25_mem0*MM_MEM[2]
	S += t25_mem0 <= t25

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	t25_mem1 += alt(MAS_MEM)
	S += (t24*MAS[0])-1 < t25_mem1*MAS_MEM[1]
	S += (t24*MAS[1])-1 < t25_mem1*MAS_MEM[3]
	S += (t24*MAS[2])-1 < t25_mem1*MAS_MEM[5]
	S += (t24*MAS[3])-1 < t25_mem1*MAS_MEM[7]
	S += t25_mem1 <= t25

	t29 = S.Task('t29', length=1, delay_cost=1)
	t29 += alt(MAS)
	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	t29_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t29_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t29_mem0*MM_MEM[2]
	S += t29_mem0 <= t29

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	t29_mem1 += alt(MM_MEM)
	S += (t26*MM[0])-1 < t29_mem1*MM_MEM[1]
	S += (t26*MM[1])-1 < t29_mem1*MM_MEM[3]
	S += t29_mem1 <= t29

	t18 = S.Task('t18', length=6, delay_cost=1)
	t18 += alt(MM)
	t18_in = S.Task('t18_in', length=1, delay_cost=1)
	t18_in += alt(MM_in)
	S += t18_in*MM_in[0]<=t18*MM[0]
	S += t18_in*MM_in[1]<=t18*MM[1]
	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	t18_mem0 += MAIN_MEM_r[0]
	S += t18_mem0 <= t18

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	t18_mem1 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t18_mem1*MAS_MEM[1]
	S += (t12*MAS[1])-1 < t18_mem1*MAS_MEM[3]
	S += (t12*MAS[2])-1 < t18_mem1*MAS_MEM[5]
	S += (t12*MAS[3])-1 < t18_mem1*MAS_MEM[7]
	S += t18_mem1 <= t18

	t27 = S.Task('t27', length=6, delay_cost=1)
	t27 += alt(MM)
	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	t27_in += alt(MM_in)
	S += t27_in*MM_in[0]<=t27*MM[0]
	S += t27_in*MM_in[1]<=t27*MM[1]
	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	t27_mem0 += MAIN_MEM_r[0]
	S += t27_mem0 <= t27

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	t27_mem1 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t27_mem1*MAS_MEM[1]
	S += (t12*MAS[1])-1 < t27_mem1*MAS_MEM[3]
	S += (t12*MAS[2])-1 < t27_mem1*MAS_MEM[5]
	S += (t12*MAS[3])-1 < t27_mem1*MAS_MEM[7]
	S += t27_mem1 <= t27

	t28 = S.Task('t28', length=1, delay_cost=1)
	t28 += alt(MAS)
	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	t28_mem0 += alt(MAS_MEM)
	S += (t25*MAS[0])-1 < t28_mem0*MAS_MEM[0]
	S += (t25*MAS[1])-1 < t28_mem0*MAS_MEM[2]
	S += (t25*MAS[2])-1 < t28_mem0*MAS_MEM[4]
	S += (t25*MAS[3])-1 < t28_mem0*MAS_MEM[6]
	S += t28_mem0 <= t28

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	t28_mem1 += alt(MM_MEM)
	S += (t26*MM[0])-1 < t28_mem1*MM_MEM[1]
	S += (t26*MM[1])-1 < t28_mem1*MM_MEM[3]
	S += t28_mem1 <= t28

	t30 = S.Task('t30', length=6, delay_cost=1)
	t30 += alt(MM)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MM_in)
	S += t30_in*MM_in[0]<=t30*MM[0]
	S += t30_in*MM_in[1]<=t30*MM[1]
	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAIN_MEM_r[0]
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(MAS_MEM)
	S += (t29*MAS[0])-1 < t30_mem1*MAS_MEM[1]
	S += (t29*MAS[1])-1 < t30_mem1*MAS_MEM[3]
	S += (t29*MAS[2])-1 < t30_mem1*MAS_MEM[5]
	S += (t29*MAS[3])-1 < t30_mem1*MAS_MEM[7]
	S += t30_mem1 <= t30

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(MAS)
	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += alt(MM_MEM)
	S += (t19*MM[0])-1 < t20_mem0*MM_MEM[0]
	S += (t19*MM[1])-1 < t20_mem0*MM_MEM[2]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += alt(MM_MEM)
	S += (t18*MM[0])-1 < t20_mem1*MM_MEM[1]
	S += (t18*MM[1])-1 < t20_mem1*MM_MEM[3]
	S += t20_mem1 <= t20

	t31 = S.Task('t31', length=6, delay_cost=1)
	t31 += alt(MM)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MM_in)
	S += t31_in*MM_in[0]<=t31*MM[0]
	S += t31_in*MM_in[1]<=t31*MM[1]
	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MM_MEM)
	S += (t27*MM[0])-1 < t31_mem0*MM_MEM[0]
	S += (t27*MM[1])-1 < t31_mem0*MM_MEM[2]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(MM_MEM)
	S += (t30*MM[0])-1 < t31_mem1*MM_MEM[1]
	S += (t30*MM[1])-1 < t31_mem1*MM_MEM[3]
	S += t31_mem1 <= t31

	t35 = S.Task('t35', length=6, delay_cost=1)
	t35 += alt(MM)
	t35_in = S.Task('t35_in', length=1, delay_cost=1)
	t35_in += alt(MM_in)
	S += t35_in*MM_in[0]<=t35*MM[0]
	S += t35_in*MM_in[1]<=t35*MM[1]
	t35_mem0 = S.Task('t35_mem0', length=1, delay_cost=1)
	t35_mem0 += alt(MAS_MEM)
	S += (t7*MAS[0])-1 < t35_mem0*MAS_MEM[0]
	S += (t7*MAS[1])-1 < t35_mem0*MAS_MEM[2]
	S += (t7*MAS[2])-1 < t35_mem0*MAS_MEM[4]
	S += (t7*MAS[3])-1 < t35_mem0*MAS_MEM[6]
	S += t35_mem0 <= t35

	t35_mem1 = S.Task('t35_mem1', length=1, delay_cost=1)
	t35_mem1 += alt(MAS_MEM)
	S += (t28*MAS[0])-1 < t35_mem1*MAS_MEM[1]
	S += (t28*MAS[1])-1 < t35_mem1*MAS_MEM[3]
	S += (t28*MAS[2])-1 < t35_mem1*MAS_MEM[5]
	S += (t28*MAS[3])-1 < t35_mem1*MAS_MEM[7]
	S += t35_mem1 <= t35

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS4/EP_ADD_A_ANY/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

