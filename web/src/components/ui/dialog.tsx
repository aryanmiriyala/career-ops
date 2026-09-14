import type { ReactNode } from 'react';
import * as DialogPrimitive from '@radix-ui/react-dialog';
import { X } from 'lucide-react';
import { Button } from './button';
import { cn } from '../../lib/utils';

export const DialogTitle = DialogPrimitive.Title;

export function Dialog({ children, onClose, sheet = false }: {
  children: ReactNode;
  onClose: () => void;
  sheet?: boolean;
}) {
  return <DialogPrimitive.Root open onOpenChange={open => { if (!open) onClose(); }}>
    <DialogPrimitive.Portal>
      <DialogPrimitive.Overlay className="fixed inset-0 z-40 bg-black/30"/>
      <DialogPrimitive.Content aria-describedby={undefined} className={cn(
        'fixed z-50 box-border overflow-y-auto overscroll-contain bg-surface p-5 text-ink shadow-xl outline-none sm:p-6',
        sheet
          ? 'inset-y-0 right-0 w-full max-w-[440px]'
          : 'left-1/2 top-4 max-h-[calc(100dvh-2rem)] w-[calc(100%-2rem)] max-w-[620px] -translate-x-1/2 rounded-lg sm:top-1/2 sm:-translate-y-1/2',
      )}>
        <DialogPrimitive.Close asChild>
          <Button variant="ghost" size="icon" className="absolute right-3 top-3" aria-label="Close" title="Close"><X size={18}/></Button>
        </DialogPrimitive.Close>
        {children}
      </DialogPrimitive.Content>
    </DialogPrimitive.Portal>
  </DialogPrimitive.Root>;
}
