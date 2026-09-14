import type { ComponentProps } from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cn } from '../../lib/utils';

type Props = ComponentProps<'button'> & {
  variant?: 'primary' | 'outline' | 'ghost';
  size?: 'default' | 'icon';
  asChild?: boolean;
};

export function Button({ className, variant = 'outline', size = 'default', asChild, ...props }: Props) {
  const Component = asChild ? Slot : 'button';
  return <Component data-slot="button" className={cn(
    'inline-flex min-h-9 shrink-0 items-center justify-center gap-2 rounded-[5px] border px-3 py-2 text-[13px] font-medium leading-5 tracking-normal transition-colors outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent disabled:pointer-events-none disabled:opacity-50 [&_svg]:shrink-0',
    variant === 'primary' && 'border-accent bg-accent text-white hover:bg-accent-hover',
    variant === 'outline' && 'border-line bg-surface text-ink hover:bg-soft',
    variant === 'ghost' && 'border-transparent bg-transparent text-ink hover:bg-soft',
    size === 'icon' && 'size-9 min-w-9 p-0', className,
  )} {...props}/>;
}
