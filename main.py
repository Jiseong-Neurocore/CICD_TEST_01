import script2print
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset_id', type=str, default=None, help="Dataset ID is required")
    parser.add_argument('--mp_version_id', type=str, default=None)
    parser.add_argument('--yyyymmdd', type=str, default=datetime.now().strftime("%Y%m%d"), help="PLAN_START_TIME에서 -값을 지워 8자리로 만든 값")
    parser.add_argument('--plan_start_time', type=str, default=datetime.now().strftime("%Y%m%d%H%M"), help="PLAN_START_TIME에서 -값을 지워 12자리로 만든 값")
    parser.add_argument('--site_id', type=str, default='MAEIL')
    parser.add_argument('--plan_type', type=str, default='WEEKLY')
    parser.add_argument('--fp_instance_type', type=str, default=None)
    parser.add_argument('--plan_horizon', type=str, default='42')
    parser.add_argument('--plan_horizon_uom', type=str, default="DAY")
    parser.add_argument('--user_id', type=str, default="FP_ENGINE")
    parser.add_argument('--eng_run_user_id', type=str, default="UNKNOWN_USER_(RUN_BY_ENGINE)")

    return parser.parse_args()


def print_dataset_id(args):
    print(args.dataset_id)

  

if __name__ == '__main__':
  args = parse_args()
  print_dataset_id(args)
  script2print.print_text()
