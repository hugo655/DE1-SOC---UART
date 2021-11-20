//Module Byte Shift Register (BSR) w/ individual byte viewer

module BSR (
	input clk, rst_n, en,
	input [7:0] byte_in,
	output wire [7:0] byte_probe0,
	output wire [7:0] byte_probe1,
	output wire [7:0] byte_probe2,
	output wire [7:0] byte_out
);

// Inner registers
reg [7:0] byte_reg[0:2] ;

// Assignments
assign byte_probe0 = byte_reg[0];
assign byte_probe1 = byte_reg[1];
assign byte_probe2 = byte_reg[2];
assign byte_out = byte_reg[2];

always @(posedge clk) begin
	if(~rst_n)begin
		byte_reg[0] <= 8'b0;
		byte_reg[1] <= 8'b0;
		byte_reg[2] <= 8'b0;
	end
	else if(en) begin
		byte_reg[0] <= byte_in;
		byte_reg[1] <= byte_reg[0];
		byte_reg[2] <= byte_reg[1];
	end
		
end
endmodule

///////////////////////////////////////////