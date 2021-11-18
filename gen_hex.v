module gen_hex(
	input switch, rst_n,
	output reg [3:0] hex_number
);


always@(posedge switch) begin
	if(~rst_n) 
		hex_number <= 4'b0000;
	else
		hex_number <= hex_number+1'b0001;
end

endmodule