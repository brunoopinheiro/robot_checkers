from movebank.movebank import MoveBank


def main():
    mb = MoveBank()
    pose = mb.get_cartesian('a1')
    print(pose)
    joint = mb.get_joints('a1')
    print(joint)


if __name__ == '__main__':
    main()
