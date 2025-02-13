// ALU MM Memory
`define ALU_MM_MEM_SIZE		128
`define ALU_MM_MEM_ADDR_BITS	7

// ALU MAS Memory
`define ALU_MAS_MEM_SIZE		32
`define ALU_MAS_MEM_ADDR_BITS	5

// ALU MAIN Memory
`define ALU_MAIN_MEM_SIZE		256
`define ALU_MAIN_MEM_ADDR_BITS	8

// ===================================================================================
`define INST_CAL_MUX_BIT		4
`define INST_MAIN_MEM_MUX_BIT	3
`define INST_ADDR_MASK_BIT		1
`define INST_MM_MAS_VAL_BIT		1
`define INST_MAS_ISSUB_BIT		1
`define INST_WRITE_EN_BIT		1
`define INST_CONDKEY_BIT		2

// ALU Instructions Index
`define INDEX_MM0_READA		0
`define INDEX_MM0_MUXA		7
`define INDEX_MM0_READB		11
`define INDEX_MM0_MUXB		18
`define INDEX_MM0_VAL		22
`define INDEX_MM0_WRITE		23
`define INDEX_MM0_WE		30
`define INDEX_MAS0_READA		31
`define INDEX_MAS0_MUXA		36
`define INDEX_MAS0_READB		40
`define INDEX_MAS0_MUXB		45
`define INDEX_MAS0_ISSUB		49
`define INDEX_MAS0_VAL		50
`define INDEX_MAS0_WRITE		51
`define INDEX_MAS0_WE		56
`define INDEX_MAS1_READA		57
`define INDEX_MAS1_MUXA		62
`define INDEX_MAS1_READB		66
`define INDEX_MAS1_MUXB		71
`define INDEX_MAS1_ISSUB		75
`define INDEX_MAS1_VAL		76
`define INDEX_MAS1_WRITE		77
`define INDEX_MAS1_WE		82
`define INDEX_MAS2_READA		83
`define INDEX_MAS2_MUXA		88
`define INDEX_MAS2_READB		92
`define INDEX_MAS2_MUXB		97
`define INDEX_MAS2_ISSUB		101
`define INDEX_MAS2_VAL		102
`define INDEX_MAS2_WRITE		103
`define INDEX_MAS2_WE		108
`define INDEX_MAS3_READA		109
`define INDEX_MAS3_MUXA		114
`define INDEX_MAS3_READB		118
`define INDEX_MAS3_MUXB		123
`define INDEX_MAS3_ISSUB		127
`define INDEX_MAS3_VAL		128
`define INDEX_MAS3_WRITE		129
`define INDEX_MAS3_WE		134
`define INDEX_INV		135
`define INDEX_CSL_MODE		136
`define INDEX_CSL_START		137
`define INDEX_RAND_INIT		138
`define INDEX_MAIN_READA		139
`define INDEX_MAIN_READB		147
`define INDEX_MAIN_WRITE		155
`define INDEX_MAIN_WE		163
`define INDEX_MAIN_WRITE_MUX		164
`define INDEX_MAIN_READ_MASKA		167
`define INDEX_MAIN_READ_MASKB		168
`define INDEX_MAIN_WRITE_MASK		169
`define INDEX_INST_CONT		172
`define INDEX_INST_END		173

`define INDEX_CONDKEY			170

`define ALU_INST_BITS			167
`define INST_BITS				174
