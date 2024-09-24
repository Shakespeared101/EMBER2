
import argparse
from pathlib import Path

def create_arg_parser():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description=('t5_embedder.py creates T5 embeddings for a given text file containing sequence(s) in FASTA-format.') )

    parser.add_argument('-i', '--input_string', type=str, help='A string containing protein sequence(s) in FASTA-format.')
    parser.add_argument('--split_char', type=str, default=' ', help="The character for splitting the FASTA header in order to retrieve the protein identifier. Should be used in conjunction with --id. Default: ' '")
    parser.add_argument('--id', type=int, default=0, help="The index for the uniprot identifier field after splitting the FASTA header after each symbole in ['|', '#', ':', ' ']. Default: 0")
    parser.add_argument('-o', '--output', required=True, type=str, help="A path where predictions are stored")

    parser.add_argument('--t5_model', type=str, default="./ProtT5-XL-U50/", help='A path to a directory holding the checkpoint for the pre-trained ProtT5 model (model will be downloaded if not already present)' )
    parser.add_argument('--dst_model', type=str, default="./EMBER2_model/model", help='A path to the checkpoint file for the EMBER2 model')
    parser.add_argument('--stride', type=int, default=16, help="Cropping stride to use for predictions. Smaller values need exponentially more computation time, but might be more accurate. Default: 16")
    parser.add_argument('--batch_size', type=int, default=200, help="Batch size used for inference. Set lower values if you run out of memory. Default: 200")
    parser.add_argument('--workers', type=int, default=0, help="Number of threads used for data loading. Default: 0")

    return parser


def main():
    parser     = create_arg_parser()
    args       = parser.parse_args()
    sequence_input = args.input_string
    op = args.output
    print(sequence_input, op)



if __name__ == '__main__':
    main()

