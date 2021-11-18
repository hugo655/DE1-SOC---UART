module byte_reg(
	input [7:0] byte_in,
	input clk, rst_n, en,
	output reg [7:0] byte_out
);

always @(posedge clk) begin
	if(~rst_n)
	byte_out <= 8'b0;
	 else
	if(en)byte_out <= byte_in;
			
end

endmodule