`default_nettype none
`timescale 1ns/1ps

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test.py
    input clk,
    input rst,
    input enable,
    input [4:0] delay,
    output [7:0] channel 
   );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    // wire up the inputs and outputs
    wire [7:0] inputs = {delay[4:0], enable, rst, clk};
    wire [7:0] outputs;
    assign channel = outputs[6:0];

    // instantiate the DUT
    loxodes_sequencer loxodes_sequencer(
        .io_in  (inputs),
        .io_out (outputs)
        );

endmodule
